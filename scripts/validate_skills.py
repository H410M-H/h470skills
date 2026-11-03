#!/usr/bin/env python3
"""Validate every skill in ./skills against the Agent Skills spec.

Checks (errors fail the run, warnings are advisory):
  * SKILL.md exists and starts with a parseable YAML frontmatter block
  * `name` is lowercase-hyphenated, <= 64 chars, and matches the directory
  * `description` exists, is a plain string, <= 1024 chars, has no XML tags,
    and says *when* to use the skill (trigger phrase)
  * every relative Markdown link and every referenced bundled file resolves
  * bundled scripts parse (python -m py_compile, bash -n) and JSON assets load
  * SKILL.md body stays under the 500-line progressive-disclosure budget

Usage: python3 scripts/validate_skills.py [--strict] [skill ...]
  --strict  treat warnings as errors
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TRIGGER_RE = re.compile(
    r"\b(use (this skill )?(when|for|to|proactively|whenever)|activate (this skill )?when|trigger)",
    re.I,
)
# Keys understood by Claude Code / the Agent Skills spec. Others are kept but flagged.
KNOWN_KEYS = {
    "name", "description", "license", "allowed-tools", "metadata", "compatibility",
    "argument-hint", "disable-model-invocation", "user-invocable", "model",
    "context", "agent", "hooks", "when_to_use", "paths", "version",
}
# Antigravity-specific keys: intentional, ignored by other hosts.
PLATFORM_KEYS = {"aliases", "disable-slash-command"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
# Bare references like `references/foo.md` or scripts/bar.sh inside the body.
BUNDLED_RE = re.compile(
    r"(?<![\w./-])((?:references|resources|assets|scripts|templates|docs)/[\w./-]+\.\w+)"
)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def err(self, skill: str, msg: str) -> None:
        self.errors.append(f"[ERROR] {skill}: {msg}")

    def warn(self, skill: str, msg: str) -> None:
        self.warnings.append(f"[WARN]  {skill}: {msg}")


def split_frontmatter(text: str) -> tuple[str | None, str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)(.*)$", text, re.S)
    return (m.group(1), m.group(2)) if m else (None, text)


def strip_code(body: str) -> str:
    """Drop fenced code blocks and inline code so example links are not checked."""
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", body)


def check_skill(skill_dir: Path, rep: Report) -> None:
    sid = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        rep.err(sid, "missing SKILL.md")
        return
    text = skill_md.read_text(encoding="utf-8")
    raw, body = split_frontmatter(text)
    if raw is None:
        rep.err(sid, "SKILL.md has no YAML frontmatter")
        return
    try:
        fm = yaml.safe_load(raw) or {}
    except yaml.YAMLError as e:
        rep.err(sid, f"frontmatter is not valid YAML: {e}")
        return
    if not isinstance(fm, dict):
        rep.err(sid, "frontmatter is not a mapping")
        return

    name = fm.get("name")
    if not isinstance(name, str) or not name:
        rep.err(sid, "missing `name`")
    else:
        if not NAME_RE.match(name) or len(name) > 64:
            rep.err(sid, f"name {name!r} must be lowercase letters/digits/hyphens, <= 64 chars")
        if name != sid:
            rep.err(sid, f"name {name!r} does not match directory {sid!r}")

    desc = fm.get("description")
    if not isinstance(desc, str) or not desc.strip():
        rep.err(sid, "missing `description`")
    else:
        d = " ".join(desc.split())
        if len(d) > 1024:
            rep.err(sid, f"description is {len(d)} chars (max 1024)")
        if re.search(r"<[A-Za-z/][^>]*>", d):
            rep.err(sid, "description contains XML/HTML tags")
        if d.startswith(">"):
            rep.err(sid, "description starts with '>' (broken folded scalar)")
        if re.search(r"[a-z]- [a-z]", d):
            rep.warn(sid, "description has 'word- word': a hyphenated word was split across folded lines")
        if not TRIGGER_RE.search(d):
            rep.warn(sid, "description does not say when to use the skill ('Use when ...')")
        if len(d) < 60:
            rep.warn(sid, f"description is very short ({len(d)} chars)")

    unknown = sorted(set(fm) - KNOWN_KEYS - PLATFORM_KEYS)
    if unknown:
        rep.warn(sid, f"non-standard frontmatter keys: {', '.join(unknown)}")

    n_lines = body.count("\n") + 1
    if n_lines > 500:
        rep.warn(sid, f"SKILL.md body is {n_lines} lines (> 500); move detail to references/")

    # Links and bundled-file references, resolved relative to the skill dir.
    prose = strip_code(body)
    targets = set()
    for t in LINK_RE.findall(prose):
        # Skip URLs / URI schemes (https:, file:, sidecar:, ...), anchors, and placeholders.
        if re.match(r"^([a-z][a-z0-9+.-]*:|#|/)", t) or "{" in t or "<" in t:
            continue
        targets.add(t.split("#")[0])
    # Bare paths like `references/x.md` only count when that bundle dir exists;
    # otherwise they usually describe files in the *user's* project.
    targets.update(t for t in BUNDLED_RE.findall(body)
                   if (skill_dir / t.split("/")[0]).is_dir())
    for t in sorted(x for x in targets if x):
        if not (skill_dir / t).resolve().exists():
            rep.err(sid, f"referenced file does not exist: {t}")

    # Bundled file sanity.
    for f in skill_dir.rglob("*"):
        if not f.is_file():
            continue
        rel = f.relative_to(skill_dir)
        if f.suffix == ".py":
            r = subprocess.run([sys.executable, "-m", "py_compile", str(f)],
                               capture_output=True, text=True)
            if r.returncode:
                rep.err(sid, f"{rel} does not compile: {r.stderr.strip().splitlines()[-1]}")
        elif f.suffix == ".sh":
            r = subprocess.run(["bash", "-n", str(f)], capture_output=True, text=True)
            if r.returncode:
                rep.err(sid, f"{rel} has bash syntax errors: {r.stderr.strip()}")
        elif f.suffix == ".json":
            try:
                json.loads(f.read_text(encoding="utf-8"))
            except ValueError as e:
                rep.err(sid, f"{rel} is not valid JSON: {e}")


def main(argv: list[str]) -> int:
    strict = "--strict" in argv
    wanted = [a for a in argv if not a.startswith("--")]
    rep = Report()
    dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir() and not p.is_symlink())
    if wanted:
        dirs = [d for d in dirs if d.name in wanted]
    for d in dirs:
        check_skill(d, rep)
    for p in SKILLS.iterdir():
        if p.is_symlink() and not p.resolve().exists():
            rep.err(p.name, "dangling symlink")
    for line in rep.errors + rep.warnings:
        print(line)
    print(f"\nChecked {len(dirs)} skills: {len(rep.errors)} errors, {len(rep.warnings)} warnings")
    return 1 if rep.errors or (strict and rep.warnings) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
