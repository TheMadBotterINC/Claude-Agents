#!/usr/bin/env python3
"""Sync portable architecture resources from their canonical skill tree."""

import argparse
from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills/thought-thru-architecture"
DESTINATION = ROOT / "codex/skills/thought-thru-architecture"


def resources(directory: Path) -> dict[Path, Path]:
    if (
        directory.is_symlink()
        or directory.parent.resolve() != directory.parent
    ):
        raise ValueError(f"Linked ancestors in resource root: {directory}")
    found = {}
    for path in directory.rglob("*"):
        relative = path.relative_to(directory)
        if relative.parts[0] == "agents" or "__pycache__" in relative.parts:
            continue
        if path.is_symlink():
            raise ValueError(f"Refusing linked skill resource: {path}")
        if path.is_file() and path.name != ".DS_Store":
            found[relative] = path
    return found


def synchronize(check: bool = False) -> list[str]:
    if not (SOURCE / "SKILL.md").is_file():
        raise ValueError("Canonical architecture SKILL.md is missing")
    source, destination = resources(SOURCE), resources(DESTINATION)
    differences = []
    for relative in sorted(source.keys() | destination.keys()):
        original, copy = source.get(relative), destination.get(relative)
        if original and copy and original.read_bytes() == copy.read_bytes():
            continue
        differences.append(str(relative))
        if check:
            continue
        output = DESTINATION / relative
        if original:
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(original, output)
        else:
            # Only this explicitly generated tree is pruned; metadata stays.
            output.unlink()
    return differences


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="Report drift without writing.",
    )
    args = parser.parse_args()
    differences = synchronize(check=args.check)
    if differences:
        print(
            ("Architecture drift: " if args.check else "Synchronized: ")
            + ", ".join(differences),
        )
    else:
        print("Architecture resources are synchronized.")
    return 1 if args.check and differences else 0


if __name__ == "__main__":
    raise SystemExit(main())
