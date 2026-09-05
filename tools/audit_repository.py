#!/usr/bin/env python3
"""Read-only integrity audit for the Lovejoy research repository."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_FROZEN_ROOT = ROOT / "research_notes" / "_frozen"
ARCHIVE_FROZEN_ROOT = ROOT / "archive_index" / "_frozen"
FROZEN_ROOTS = (RESEARCH_FROZEN_ROOT, ARCHIVE_FROZEN_ROOT)
SOURCE_ROOT = ROOT / "source"

REQUIRED = (
    "README.md",
    "CONSOLIDATED_RESEARCH_ENTRYPOINT.md",
    "CURRENT_STATE.md",
    "TRANSCRIPTION_COMPLETION_QUEUE.md",
    "CANONICAL_INDEX.md",
    "ARCHIVE_TRANSCRIPTION_PROGRESS.md",
    "QUELLENFORSCHUNG_CURRENT_GATE.md",
    "WORKING_RULES.md",
    "root_payload_index.md",
    "source/README.md",
    "source/SOURCE_INDEX.md",
    "archive_index/README.md",
    "archive_index/ARCHIVE_ROUTER.md",
    "archive_transcriptions/README.md",
    "research_notes/README.md",
    "research_notes/FROZEN_INDEX.md",
    "research_notes/FROZEN_PROVENANCE_REGISTER.md",
    "research_notes/LOVEJOY_004_TERMINAL_SYNTHESIS.md",
    "research_notes/LOVEJOY_005_TERMINAL_SYNTHESIS.md",
    "research_notes/LOVEJOY_1897_1898_PUBLICATION_GENESIS_TERMINAL.md",
    "research_notes/LOVEJOY_FORMATION_1895_1899_TERMINAL.md",
    "research_notes/LOVEJOY_1902_1906_EXIT_TERMINAL.md",
    "research_notes/JHI_blog_full_draft_v3_7_clean_submission_2026-09-03.md",
    "research_notes/JHI_blog_v3_7_notebook_guide_quellenkritik_calibration_2026-09-03.md",
    "archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md",
)

RAW_ROOT_SUFFIXES = {
    ".pdf",
    ".txt",
    ".json",
    ".xml",
    ".csv",
    ".tsv",
    ".zip",
    ".epub",
    ".html",
}

CANONICAL_BATCHES = (
    ("archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json", 1, 18),
    ("archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json", 19, 36),
    ("archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json", 37, 54),
    ("archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json", 55, 71),
    ("archive_transcriptions/MS38_004_001_061_005_p001-015_clean.json", 1, 15),
    ("archive_transcriptions/MS38_004_001_061_005_p016-030_clean.json", 16, 30),
    ("archive_transcriptions/MS38_004_001_061_005_p031-045_clean.json", 31, 45),
    ("archive_transcriptions/MS38_004_001_061_005_p046-060_clean.json", 46, 60),
    ("archive_transcriptions/MS38_004_001_061_005_p061-075_clean.json", 61, 75),
    ("archive_transcriptions/MS38_004_001_061_005_p076-090_clean.json", 76, 90),
    ("archive_transcriptions/MS38_004_001_061_005_p091-105_clean.json", 91, 105),
    ("archive_transcriptions/MS38_004_001_061_005_p106-120_clean.json", 106, 120),
)

LINK_RE = re.compile(r"(?<!!)\[[^]]*\]\(([^)]+)\)")
BACKTICK_PATH_RE = re.compile(
    r"`((?:research_notes|archive_transcriptions|archive_index|source|tools)/[^`]+\.(?:md|json|csv|tsv|txt|xml|html|py))`"
)


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [
        path
        for item in result.stdout.split(b"\0")
        if item and (path := ROOT / item.decode()).is_file()
    ]


def under(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def is_frozen(path: Path) -> bool:
    return any(under(path, frozen_root) for frozen_root in FROZEN_ROOTS)


def is_raw_source(path: Path) -> bool:
    return under(path, SOURCE_ROOT)


def legacy_frozen_fallback(target: Path) -> Path | None:
    """Resolve a pre-freeze active path into a preserved snapshot when possible."""
    candidates = (
        (ROOT / "research_notes", RESEARCH_FROZEN_ROOT / "snapshot_2026-09-05"),
        (ROOT / "archive_index", ARCHIVE_FROZEN_ROOT / "snapshot_2026-09-05"),
    )
    for active_root, snapshot_root in candidates:
        try:
            relative = target.resolve().relative_to(active_root.resolve())
        except ValueError:
            continue
        if relative.parts and relative.parts[0] == "_frozen":
            return None
        candidate = snapshot_root / relative
        return candidate if candidate.exists() else None
    return None


def local_link_target(markdown: Path, raw_target: str) -> Path | None:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    target = target.split("#", 1)[0]
    if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
        return None
    target = unquote(target)
    if " " in target and not target.startswith("/"):
        target = target.split(" ", 1)[0]
    candidate = Path(target)
    return candidate if candidate.is_absolute() else markdown.parent / candidate


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    files = tracked_files()

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    for path in files:
        if path.parent == ROOT and path.suffix.lower() in RAW_ROOT_SUFFIXES:
            errors.append(
                f"raw payload in repository root: {path.name} (move under source/ and register in source/SOURCE_INDEX.md)"
            )

    # Validate active/curated JSON, but do not repeatedly parse raw OCR payloads or frozen rounds.
    parsed_json = 0
    for path in files:
        if path.suffix.lower() != ".json" or is_frozen(path) or is_raw_source(path):
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
            parsed_json += 1
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"invalid JSON: {path.relative_to(ROOT)} ({exc})")

    covered: dict[str, list[int]] = defaultdict(list)
    for relative, start, end in CANONICAL_BATCHES:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing canonical batch: {relative}")
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            pages = [int(page["pdf_page"]) for page in payload["pages"]]
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"malformed canonical batch: {relative} ({exc})")
            continue
        expected = list(range(start, end + 1))
        if pages != expected:
            errors.append(f"page-range mismatch: {relative} expected {start}-{end}, got {pages}")
        notebook = "004" if "_004_p" in relative else "005"
        covered[notebook].extend(pages)

    if covered.get("004") != list(range(1, 72)):
        errors.append("canonical 004 coverage is not exactly pages 1-71")
    if covered.get("005") != list(range(1, 121)):
        errors.append("canonical 005 coverage is not exactly pages 1-120")

    integrated_check = subprocess.run(
        [sys.executable, "tools/build_integrated_transcription.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if integrated_check.returncode != 0:
        detail = integrated_check.stderr.strip() or integrated_check.stdout.strip()
        errors.append(f"integrated transcription check failed: {detail}")

    broken_links: list[str] = []
    for path in files:
        if path.suffix.lower() != ".md" or is_frozen(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"non-UTF-8 Markdown: {path.relative_to(ROOT)} ({exc})")
            continue
        for match in LINK_RE.finditer(text):
            target = local_link_target(path, match.group(1))
            if target is None or target.exists():
                continue
            fallback = legacy_frozen_fallback(target)
            if fallback is not None:
                warnings.append(
                    f"legacy active-path link resolves through frozen snapshot: {path.relative_to(ROOT)} -> {fallback.relative_to(ROOT)}"
                )
                continue
            line = text.count("\n", 0, match.start()) + 1
            broken_links.append(f"{path.relative_to(ROOT)}:{line} -> {match.group(1)}")
    if broken_links:
        errors.extend(f"broken local Markdown link: {item}" for item in broken_links)

    living_docs = (
        "README.md",
        "CONSOLIDATED_RESEARCH_ENTRYPOINT.md",
        "CURRENT_STATE.md",
        "TRANSCRIPTION_COMPLETION_QUEUE.md",
        "CANONICAL_INDEX.md",
        "ARCHIVE_TRANSCRIPTION_PROGRESS.md",
        "QUELLENFORSCHUNG_CURRENT_GATE.md",
        "WORKING_RULES.md",
        "root_payload_index.md",
        "source/README.md",
        "source/SOURCE_INDEX.md",
        "archive_index/README.md",
        "archive_index/ARCHIVE_ROUTER.md",
        "archive_transcriptions/README.md",
        "research_notes/README.md",
        "research_notes/FROZEN_INDEX.md",
        "research_notes/FROZEN_PROVENANCE_REGISTER.md",
        "research_notes/LOVEJOY_004_TERMINAL_SYNTHESIS.md",
        "research_notes/LOVEJOY_005_TERMINAL_SYNTHESIS.md",
        "research_notes/LOVEJOY_1897_1898_PUBLICATION_GENESIS_TERMINAL.md",
        "research_notes/LOVEJOY_FORMATION_1895_1899_TERMINAL.md",
        "research_notes/LOVEJOY_1902_1906_EXIT_TERMINAL.md",
    )
    for relative in living_docs:
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for match in BACKTICK_PATH_RE.finditer(text):
            target = ROOT / match.group(1)
            if any(character in str(target) for character in "*{}") or target.exists():
                continue
            fallback = legacy_frozen_fallback(target)
            if fallback is not None:
                warnings.append(
                    f"living navigation uses legacy path resolved in frozen snapshot: {relative} -> {fallback.relative_to(ROOT)}"
                )
                continue
            line = text.count("\n", 0, match.start()) + 1
            errors.append(f"missing path in living navigation: {relative}:{line} -> {match.group(1)}")

    # Duplicate hashing is limited to active curated files; raw source payloads and frozen snapshots are intentionally excluded.
    digests: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        if is_frozen(path) or is_raw_source(path):
            continue
        digests[hashlib.sha256(path.read_bytes()).hexdigest()].append(path)
    duplicate_sets = [group for group in digests.values() if len(group) > 1]
    for group in duplicate_sets:
        warnings.append("exact duplicate active content: " + ", ".join(str(path.relative_to(ROOT)) for path in group))

    print(f"Tracked files: {len(files)}")
    print(f"Parsed active/curated JSON files: {parsed_json}")
    print("Canonical page coverage: 004=71/71, 005=120/120")
    print("Raw source routing: source/SOURCE_INDEX.md")
    print("Frozen research history: research_notes/FROZEN_INDEX.md")
    print("Frozen archive-search history: archive_index/_frozen/snapshot_2026-09-05/")
    print("Audit skips source/, research_notes/_frozen/, and archive_index/_frozen/ for expensive parse/hash/link passes")
    print("Diplomatic transcription completion is governed separately by TRANSCRIPTION_COMPLETION_QUEUE.md")
    if warnings:
        print(f"Warnings: {len(warnings)}")
        for warning in warnings:
            print(f"  WARN {warning}")
    if errors:
        print(f"Errors: {len(errors)}")
        for error in errors:
            print(f"  ERROR {error}")
        return 1
    print("Repository structural audit: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
