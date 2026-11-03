#!/usr/bin/env bash
# ==============================================================================
# h470skills Installer
# Installs and links the master skill collection for Google Antigravity (agy)
# and Claude Code. Works on Termux, Linux and macOS.
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$SCRIPT_DIR/skills"

AGY_GLOBAL="${HOME}/.gemini/config/skills"
AGY_LOCAL="${PWD}/.agents/skills"
CLAUDE_GLOBAL="${HOME}/.claude/skills"
CLAUDE_LOCAL="${PWD}/.claude/skills"

MODE="symlink"
TARGET_DIR="$AGY_GLOBAL"
DRY_RUN=0
VALIDATE=1
ONLY=()

usage() {
  cat <<EOF
Usage: $(basename "$0") [OPTIONS] [SKILL ...]

Targets (pick one):
  -g, --global         Antigravity, all workspaces: ~/.gemini/config/skills (default)
  -l, --local          Antigravity, current project: ./.agents/skills
  -C, --claude         Claude Code, all projects:    ~/.claude/skills
  -L, --claude-local   Claude Code, current project: ./.claude/skills
  -t, --target DIR     Any other skills directory

Mode:
  -s, --symlink        Symlink each skill (default; 'git pull' updates them in place)
  -c, --copy           Copy skills instead (use for sandboxes that don't follow symlinks)

Other:
  -n, --dry-run        Show what would be installed without touching anything
      --no-validate    Skip running scripts/validate_skills.py first
  -h, --help           Show this help message

Pass skill names to install only those (default: all).

Examples:
  ./install.sh                         # Symlink all skills for Antigravity (global)
  ./install.sh --claude                # Symlink all skills for Claude Code (global)
  ./install.sh --claude --copy         # Copy all skills into ~/.claude/skills
  ./install.sh -L neon postgresql      # Two skills into this project's .claude/skills
EOF
  exit 0
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -g|--global)       TARGET_DIR="$AGY_GLOBAL"; shift ;;
    -l|--local)        TARGET_DIR="$AGY_LOCAL"; shift ;;
    -C|--claude)       TARGET_DIR="$CLAUDE_GLOBAL"; shift ;;
    -L|--claude-local) TARGET_DIR="$CLAUDE_LOCAL"; shift ;;
    -t|--target)       [[ $# -ge 2 ]] || { echo "--target needs a directory" >&2; exit 2; }
                       TARGET_DIR="$2"; shift 2 ;;
    -c|--copy)         MODE="copy"; shift ;;
    -s|--symlink)      MODE="symlink"; shift ;;
    -n|--dry-run)      DRY_RUN=1; shift ;;
    --no-validate)     VALIDATE=0; shift ;;
    -h|--help)         usage ;;
    -*)                echo "Unknown option: $1" >&2; usage ;;
    *)                 ONLY+=("$1"); shift ;;
  esac
done

echo "=================================================="
echo "  h470skills Installer"
echo "  Source : $SKILLS_SRC"
echo "  Target : $TARGET_DIR"
echo "  Mode   : $MODE$([[ $DRY_RUN -eq 1 ]] && echo ' (dry run)')"
echo "=================================================="

if [[ $VALIDATE -eq 1 ]] && command -v python3 >/dev/null 2>&1 \
   && python3 -c 'import yaml' >/dev/null 2>&1; then
  if ! python3 "$SCRIPT_DIR/scripts/validate_skills.py" >/dev/null; then
    echo " Validation failed. Run: python3 scripts/validate_skills.py" >&2
    echo " (or pass --no-validate to install anyway)" >&2
    exit 1
  fi
  echo " Validation passed."
fi

[[ $DRY_RUN -eq 1 ]] || mkdir -p "$TARGET_DIR"

count=0
skipped=0
for skill_dir in "$SKILLS_SRC"/*/; do
  skill_dir="${skill_dir%/}"
  skill_name="$(basename "$skill_dir")"
  # Skip alias symlinks inside the repo and anything that isn't a skill.
  [[ -L "$skill_dir" || ! -f "$skill_dir/SKILL.md" ]] && continue
  if [[ ${#ONLY[@]} -gt 0 ]] && [[ ! " ${ONLY[*]} " =~ " ${skill_name} " ]]; then
    continue
  fi
  target_path="$TARGET_DIR/$skill_name"

  # Never clobber a real (non-symlink) directory that we didn't create in copy mode.
  if [[ -d "$target_path" && ! -L "$target_path" && "$MODE" = "symlink" ]]; then
    echo " ! $skill_name: $target_path is a real directory; leaving it (use --copy to replace)"
    skipped=$((skipped + 1))
    continue
  fi

  if [[ $DRY_RUN -eq 1 ]]; then
    echo " would $MODE: $skill_name"
  elif [[ "$MODE" = "symlink" ]]; then
    ln -sfn "$skill_dir" "$target_path"
  else
    rm -rf "$target_path"
    cp -R "$skill_dir" "$target_path"
  fi
  count=$((count + 1))
done

echo " $([[ $DRY_RUN -eq 1 ]] && echo "Would install" || echo "Installed") $count skills to $TARGET_DIR ($MODE mode)$([[ $skipped -gt 0 ]] && echo ", skipped $skipped")."
case "$TARGET_DIR" in
  *"/.claude/skills") echo " Restart Claude Code (or start a new session), then type /<skill-name> or just ask." ;;
  *) echo " Launch 'agy' and type /<skill-name> or trigger skills via prompts!" ;;
esac
