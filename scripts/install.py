#!/usr/bin/env python3
"""Install Claude and Codex resources without clobbering local files."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
from uuid import uuid4


ROOT = Path(__file__).resolve().parents[1]


def inventory(home: Path, codex_home: Path) -> list[tuple[Path, Path]]:
    items = []
    for directory in sorted(ROOT.iterdir()):
        source = directory / f"{directory.name}.md"
        if directory.is_dir() and source.is_file():
            items.append((source, home / ".claude/agents" / source.name))
    items += [
        (source, home / ".claude" / source.name)
        for source in sorted((ROOT / "shared").glob("*.md"))
    ]
    for base, destination in (
        (ROOT / "skills", home / ".claude/skills"),
        (ROOT / "codex/skills", codex_home / "skills"),
    ):
        items += [
            (source, destination / source.name)
            for source in sorted(base.iterdir())
            if (source / "SKILL.md").is_file()
        ]
    return items


def signature(path: Path) -> str:
    """Hash copies without following links to unrelated targets."""
    if path.is_symlink():
        return "link:" + os.readlink(path)
    digest = hashlib.sha256()
    if path.is_file():
        digest.update(b"file\0" + path.read_bytes())
    elif path.is_dir():
        digest.update(b"directory\0")
        for child in sorted(path.iterdir()):
            relative = child.relative_to(path).as_posix().encode()
            digest.update(relative + b"\0" + signature(child).encode() + b"\0")
    else:
        return "missing" if not path.exists() else "unsupported"
    return digest.hexdigest()


def load_receipt(path: Path) -> dict:
    if not path.exists():
        return {"version": 1, "entries": {}}
    receipt = json.loads(path.read_text())
    if (
        not isinstance(receipt, dict) or receipt.get("version") != 1
        or not isinstance(receipt.get("entries"), dict)
    ):
        raise ValueError("Invalid installation receipt")
    return receipt


def managed(source: Path, dest: Path, receipt: dict) -> bool:
    if dest.is_symlink():
        # Legacy links to this exact source can be safely adopted.
        return dest.resolve() == source.resolve()
    entry = receipt["entries"].get(str(dest))
    return bool(
        entry and entry.get("source") == str(source)
        and entry.get("signature") == signature(dest)
    )


def save_receipt(path: Path, receipt: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(receipt, indent=2) + "\n")
    temporary.replace(path)


def remove_owned(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    else:
        shutil.rmtree(path)


def install_item(source: Path, dest: Path, copy: bool) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    # Stage on the same filesystem, then move the old owned entry aside.
    with tempfile.TemporaryDirectory(
        prefix=".skill-stage-", dir=dest.parent,
    ) as temp:
        staged = Path(temp) / dest.name
        if not copy:
            staged.symlink_to(source, target_is_directory=source.is_dir())
        elif source.is_dir():
            shutil.copytree(
                source, staged, symlinks=True,
                ignore=shutil.ignore_patterns(
                    "__pycache__", "*.pyc", ".DS_Store",
                ),
            )
        else:
            shutil.copy2(source, staged)
        backup = dest.with_name(f".{dest.name}.previous-{uuid4().hex}")
        existed = dest.exists() or dest.is_symlink()
        if existed:
            dest.rename(backup)
        try:
            staged.rename(dest)
        except OSError:
            if existed:
                backup.rename(dest)
            raise
        if existed:
            remove_owned(backup)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--copy", action="store_true", help="Copy, not symlink.")
    mode.add_argument("--list", action="store_true", help="Inspect read-only.")
    args = parser.parse_args()
    home = Path.home()
    codex_home = Path(
        os.environ.get("CODEX_HOME", home / ".codex"),
    ).expanduser()
    if not codex_home.is_absolute():
        raise ValueError("CODEX_HOME must be an absolute path")
    receipt_path = home / ".claude/.claude-agents-install.json"
    receipt = load_receipt(receipt_path)
    items = inventory(home, codex_home)
    destinations = [dest for _, dest in items]
    if len(set(destinations)) != len(destinations):
        raise ValueError("Claude and Codex installation destinations overlap")
    if any(dest.absolute() == source for source, dest in items):
        raise ValueError("Installation destination cannot be its own source")
    conflicts = []
    for source, dest in items:
        exists = dest.exists() or dest.is_symlink()
        owned = managed(source, dest, receipt) if exists else False
        if args.list:
            state = (
                "not installed" if not exists else
                "managed link" if owned and dest.is_symlink() else
                "managed copy" if owned else "unmanaged or locally modified"
            )
            print(f"{dest}: {state}")
        elif exists and not owned:
            conflicts.append(str(dest))
    if args.list:
        return 0
    if conflicts:
        raise ValueError(
            "Refusing to replace unmanaged or locally modified destinations. "
            "Move them aside explicitly, then reinstall:\n"
            + "\n".join(conflicts)
        )
    for source, dest in items:
        install_item(source, dest, args.copy)
        receipt["entries"][str(dest)] = {
            "source": str(source), "signature": signature(dest),
        }
        save_receipt(receipt_path, receipt)
        print(f"{'copied' if args.copy else 'linked'} {dest}")
    print(f"Installed {len(items)} entries.")
    print(f"Codex skills: {codex_home / 'skills'}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        sys.exit(1)
