#!/data/data/com.termux/files/usr/bin/env bash
# ==============================================================================
# h470skills Installer
# Installs and links the master Antigravity skill collection
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$SCRIPT_DIR/skills"

GLOBAL_TARGET="${HOME}/.gemini/config/skills"
LOCAL_TARGET="${PWD}/.agents/skills"

MODE="symlink"
TARGET_DIR="$GLOBAL_TARGET"

usage() {
  cat <<EOF
Usage: $(basename "$0") [OPTIONS]

Options:
  -g, --global     Install globally to ~/.gemini/config/skills (Default)
  -l, --local      Install locally to current project's .agents/skills
  -c, --copy       Copy skills instead of creating symlinks
  -s, --symlink    Create symlinks to skills (Default)
  -h, --help       Show this help message

Examples:
  ./install.sh                # Symlinks all skills globally
  ./install.sh --local        # Symlinks all skills to current project
  ./install.sh --global --copy # Copies all skill directories globally
EOF
  exit 0
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -g|--global)
      TARGET_DIR="$GLOBAL_TARGET"
      shift
      ;;
    -l|--local)
      TARGET_DIR="$LOCAL_TARGET"
      shift
      ;;
    -c|--copy)
      MODE="copy"
      shift
      ;;
    -s|--symlink)
      MODE="symlink"
      shift
      ;;
    -h|--help)
      usage
      ;;
    *)
      echo "Unknown option: $1"
      usage
      ;;
  esac
done

echo "=================================================="
echo "  h470skills Installer"
echo "  Source : $SKILLS_SRC"
echo "  Target : $TARGET_DIR"
echo "  Mode   : $MODE"
echo "=================================================="

mkdir -p "$TARGET_DIR"

count=0
for skill_dir in "$SKILLS_SRC"/*; do
  [ -e "$skill_dir" ] || continue
  skill_name="$(basename "$skill_dir")"
  target_path="$TARGET_DIR/$skill_name"

  if [ "$MODE" = "symlink" ]; then
    ln -sfn "$skill_dir" "$target_path"
  else
    rm -rf "$target_path"
    cp -r "$skill_dir" "$target_path"
  fi
  count=$((count + 1))
done

echo " Successfully installed $count skills to $TARGET_DIR ($MODE mode)."
echo " Launch 'agy' and type /<skill-name> or trigger skills via prompts!"
