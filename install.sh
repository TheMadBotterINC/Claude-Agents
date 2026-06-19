#!/usr/bin/env bash
#
# Install agents from this repo into ~/.claude/agents/ (user-global), so they are
# available in every project. Each agent lives in its own folder as
# <agent>/<agent>.md; this script links (or copies) that file to
# ~/.claude/agents/<agent>.md.
#
# Usage:
#   ./install.sh            # symlink each agent (edits in the repo update live)
#   ./install.sh --copy     # copy instead of symlink
#   ./install.sh --list     # show what is currently installed from this repo
#
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_DIR="${HOME}/.claude/agents"
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

if [ "${MODE}" != "list" ]; then
  echo
  echo "Installed ${installed} agent(s) into ${DEST_DIR}"
  echo "Note: ux_tester needs the Playwright MCP wherever you run it (see README)."
fi
