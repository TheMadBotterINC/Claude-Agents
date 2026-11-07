#!/usr/bin/env bash
#
# Install agents and skills from this repo user-globally, so they are available
# in every project. Claude agents and skills install under ~/.claude; Codex
# skills under codex/skills install to ${CODEX_HOME:-~/.codex}/skills.
#
# Usage: ./install.sh [--copy | --list]
# Requires Python 3.10+. Refuses unmanaged or locally modified destinations.
set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "${REPO_DIR}/scripts/install.py" "$@"
