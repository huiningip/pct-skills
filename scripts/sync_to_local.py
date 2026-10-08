#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync the skills in this repository into a local WorkBuddy skills directory.

One-way sync: repo -> local runtime.
  * new / changed files are copied over
  * stale files are removed
  * protected local metadata (_user_meta.json, _icon.png, ...) is never touched

Usage:
  py -3 scripts/sync_to_local.py                     # sync to ~/.workbuddy/skills
  py -3 scripts/sync_to_local.py --dry-run           # preview, do not write
  py -3 scripts/sync_to_local.py --target <dir>      # custom skills directory
"""
import argparse
import filecmp
import os
import shutil
import sys
from pathlib import Path

PROTECTED = {
    "_user_meta.json", "_skillhub_meta.json", "_meta.json", "_icon.png",
    ".DS_Store", "Thumbs.db", "desktop.ini",
}
SKIP_DIRS = {"__pycache__", ".git"}

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_SKILLS = REPO_ROOT / "skills"


def default_target():
    return Path.home() / ".workbuddy" / "skills"


def main():
    parser = argparse.ArgumentParser(
        description="Sync repo skills into a local skills directory (repo -> local).")
    parser.add_argument("--target", default=None,
                        help="target skills directory (default: ~/.workbuddy/skills)")
    parser.add_argument("--dry-run", action="store_true",
                        help="show changes without writing")
    args = parser.parse_args()

    if not SRC_SKILLS.is_dir():
        sys.exit("skills/ directory not found: %s" % SRC_SKILLS)

    target = Path(args.target).expanduser() if args.target else default_target()
    if not target.is_dir():
        sys.exit("target directory not found: %s (create it or pass --target)" % target)

    copied = removed = 0
    skills = sorted(p for p in SRC_SKILLS.iterdir() if p.is_dir())
    print("repo   : %s" % REPO_ROOT)
    print("target : %s%s" % (target, "  (dry-run)" if args.dry_run else ""))
    print("skills : %d" % len(skills))
    print("")

    for skill in skills:
        dst = target / skill.name
        n_copy = n_rm = 0

        for root, dirs, files in os.walk(skill):
            dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
            rel = Path(root).relative_to(skill)
            for fn in sorted(files):
                if fn in PROTECTED:
                    continue
                src = Path(root) / fn
                df = dst / rel / fn
                if df.exists() and filecmp.cmp(src, df, shallow=False):
                    continue
                n_copy += 1
                print("  [copy]   %s/%s" % (skill.name, rel / fn))
                if not args.dry_run:
                    df.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, df)

        if dst.is_dir():
            for root, dirs, files in os.walk(dst):
                dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
                rel = Path(root).relative_to(dst)
                for fn in sorted(files):
                    if fn in PROTECTED:
                        continue
                    df = Path(root) / fn
                    if not (skill / rel / fn).exists():
                        n_rm += 1
                        print("  [remove] %s/%s" % (skill.name, rel / fn))
                        if not args.dry_run:
                            try:
                                df.unlink()
                            except OSError as exc:
                                print("    ! could not remove: %s" % exc)

        copied += n_copy
        removed += n_rm
        print("%s: %d copied, %d removed" % (skill.name, n_copy, n_rm))

    print("")
    print("Done. copied=%d removed=%d%s" % (copied, removed, " (dry-run)" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
