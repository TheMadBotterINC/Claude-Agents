#!/usr/bin/env bash
#
# Install agents and skills from this repo user-globally, so they are available
# in every project. Claude agents and skills install under ~/.claude; Codex
# skills under codex/skills install to ${CODEX_HOME:-~/.codex}/skills.
#
# Usage:
#   ./install.sh            # symlink each agent (edits in the repo update live)
#   ./install.sh --copy     # copy instead of symlink
#   ./install.sh --list     # show what is currently installed from this repo
#
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_DIR="${HOME}/.claude/agents"
SKILLS_DEST_DIR="${HOME}/.claude/skills"
CODEX_HOME_DIR="${CODEX_HOME:-${HOME}/.codex}"
CODEX_SKILLS_DEST_DIR="${CODEX_HOME_DIR}/skills"
MODE="link"

case "${1:-}" in
  --copy) MODE="copy" ;;
  --list) MODE="list" ;;
  --help|-h)
    grep '^#' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
    exit 0
    ;;
  "") ;;
  *) echo "Unknown option: $1" >&2; exit 1 ;;
esac

mkdir -p "${DEST_DIR}"

installed=0
for dir in "${REPO_DIR}"/*/; do
  name="$(basename "${dir}")"
  src="${dir}${name}.md"
  [ -f "${src}" ] || continue            # skip folders without a matching <name>.md
  dest="${DEST_DIR}/${name}.md"

  case "${MODE}" in
    list)
      if [ -L "${dest}" ]; then
        echo "${name}  ->  $(readlink "${dest}")"
      elif [ -f "${dest}" ]; then
        echo "${name}  (copied)"
      else
        echo "${name}  (not installed)"
      fi
      ;;
    copy)
      cp "${src}" "${dest}"
      echo "copied  ${name}  ->  ${dest}"
      installed=$((installed + 1))
      ;;
    link)
      ln -sf "${src}" "${dest}"
      echo "linked  ${name}  ->  ${dest}"
      installed=$((installed + 1))
      ;;
  esac
done

skills_installed=0
if [ -d "${REPO_DIR}/skills" ]; then
  mkdir -p "${SKILLS_DEST_DIR}"
  for dir in "${REPO_DIR}"/skills/*/; do
    name="$(basename "${dir}")"
    [ -f "${dir}SKILL.md" ] || continue  # skip folders without a SKILL.md
    dest="${SKILLS_DEST_DIR}/${name}"

    case "${MODE}" in
      list)
        if [ -L "${dest}" ]; then
          echo "${name}  ->  $(readlink "${dest}")"
        elif [ -d "${dest}" ]; then
          echo "${name}  (copied)"
        else
          echo "${name}  (not installed)"
        fi
        ;;
      copy)
        rm -rf "${dest}"
        cp -R "${dir%/}" "${dest}"
        echo "copied  ${name}  ->  ${dest}"
        skills_installed=$((skills_installed + 1))
        ;;
      link)
        [ -L "${dest}" ] || rm -rf "${dest}"
        ln -sfn "${dir%/}" "${dest}"
        echo "linked  ${name}  ->  ${dest}"
        skills_installed=$((skills_installed + 1))
        ;;
    esac
  done
fi

codex_skills_installed=0
if [ -d "${REPO_DIR}/codex/skills" ]; then
  mkdir -p "${CODEX_SKILLS_DEST_DIR}"
  for dir in "${REPO_DIR}"/codex/skills/*/; do
    name="$(basename "${dir}")"
    [ -f "${dir}SKILL.md" ] || continue
    dest="${CODEX_SKILLS_DEST_DIR}/${name}"

    case "${MODE}" in
      list)
        if [ -L "${dest}" ]; then
          echo "codex:${name}  ->  $(readlink "${dest}")"
        elif [ -d "${dest}" ]; then
          echo "codex:${name}  (copied)"
        else
          echo "codex:${name}  (not installed)"
        fi
        ;;
      copy)
        rm -rf "${dest}"
        cp -R "${dir%/}" "${dest}"
        echo "copied  codex:${name}  ->  ${dest}"
        codex_skills_installed=$((codex_skills_installed + 1))
        ;;
      link)
        [ -L "${dest}" ] || rm -rf "${dest}"
        ln -sfn "${dir%/}" "${dest}"
        echo "linked  codex:${name}  ->  ${dest}"
        codex_skills_installed=$((codex_skills_installed + 1))
        ;;
    esac
  done
fi

if [ "${MODE}" != "list" ]; then
  echo
  echo "Installed ${installed} Claude agent(s), ${skills_installed} Claude skill(s), and ${codex_skills_installed} Codex skill(s)"
  echo "Codex skills destination: ${CODEX_SKILLS_DEST_DIR}"
  echo "Note: ux_tester needs the Playwright MCP wherever you run it (see README)."
fi
