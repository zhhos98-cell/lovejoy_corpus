#!/usr/bin/env python3
"""Build the human-readable 004+005 page-by-page transcription edition."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "archive_transcriptions/MS38_004_005_integrated_page_by_page_final_2026-09-01.md"

BATCHES = (
    ("004", "archive_transcriptions/MS38_004_001_061_004_p001-018_clean.json", 1, 18),
    ("004", "archive_transcriptions/MS38_004_001_061_004_p019-036_clean.json", 19, 36),
    ("004", "archive_transcriptions/MS38_004_001_061_004_p037-054_clean.json", 37, 54),
    ("004", "archive_transcriptions/MS38_004_001_061_004_p055-071_clean.json", 55, 71),
    ("005", "archive_transcriptions/MS38_004_001_061_005_p001-015_clean.json", 1, 15),
    ("005", "archive_transcriptions/MS38_004_001_061_005_p016-030_clean.json", 16, 30),
    ("005", "archive_transcriptions/MS38_004_001_061_005_p031-045_clean.json", 31, 45),
    ("005", "archive_transcriptions/MS38_004_001_061_005_p046-060_clean.json", 46, 60),
    ("005", "archive_transcriptions/MS38_004_001_061_005_p061-075_clean.json", 61, 75),
    ("005", "archive_transcriptions/MS38_004_001_061_005_p076-090_clean.json", 76, 90),
    ("005", "archive_transcriptions/MS38_004_001_061_005_p091-105_clean.json", 91, 105),
    ("005", "archive_transcriptions/MS38_004_001_061_005_p106-120_clean.json", 106, 120),
)


def blockquote(text: str) -> list[str]:
    return [">" if not line else f"> {line}" for line in text.strip().splitlines()]


def display(value: object) -> str:
    if value is None or value == "":
        return "not visibly numbered"
    return str(value)


def load_batches() -> tuple[dict[str, list[dict]], list[dict]]:
    notebooks: dict[str, list[dict]] = {"004": [], "005": []}
    provenance: list[dict] = []
    for notebook, relative, start, end in BATCHES:
        path = ROOT / relative
        payload = json.loads(path.read_text(encoding="utf-8"))
        pages = payload["pages"]
        actual = [int(page["pdf_page"]) for page in pages]
        expected = list(range(start, end + 1))
        if actual != expected:
            raise ValueError(f"{relative}: expected pages {start}-{end}, got {actual}")
        expected_source = f"MS38_004_001_061_{notebook}"
        if payload.get("source_id") != expected_source:
            raise ValueError(
                f"{relative}: source_id {payload.get('source_id')!r} != {expected_source!r}"
            )
        notebooks[notebook].extend(pages)
        provenance.append(
            {
                "notebook": notebook,
                "path": relative,
                "range": f"{start:03d}–{end:03d}",
                "status": payload.get("batch", {}).get("status", "status not recorded"),
            }
        )
    if [page["pdf_page"] for page in notebooks["004"]] != list(range(1, 72)):
        raise ValueError("004 coverage is not exactly 1-71")
    if [page["pdf_page"] for page in notebooks["005"]] != list(range(1, 121)):
        raise ValueError("005 coverage is not exactly 1-120")
    return notebooks, provenance


def render_page(notebook: str, page: dict) -> list[str]:
    pdf_page = int(page["pdf_page"])
    manuscript_label = page.get("manuscript_page_label")
    manuscript = (
        f"manuscript p.{display(manuscript_label)}"
        if manuscript_label not in (None, "")
        else "manuscript leaf not visibly numbered"
    )
    lines = [
        f"<!-- page:{notebook}:{pdf_page:03d} -->",
        f"## {notebook} · PDF p.{pdf_page:03d} · {manuscript}",
        "",
        f"**Page type:** `{page['page_type']}`  ",
        f"**Transcription confidence:** {page['transcription_confidence']}",
    ]
    if page.get("text_layer"):
        lines.extend(["  ", f"**Text layer:** `{page['text_layer']}`"])
    if page.get("witness_status"):
        lines.extend(["  ", f"**Witness status:** {page['witness_status']}"])

    lines.extend(["", "### Integrated corrected text", ""])
    lines.extend(blockquote(page["corrected_text"]))

    supplemental = (
        ("Diplomatic visible text", "diplomatic_visible_text"),
        ("Editorial argument summary", "editorial_argument_summary"),
        ("External source collation", "external_source_collation"),
        ("Material/layout observation", "material_layout_observation"),
        ("Second-pass note", "second_pass_note"),
    )
    normalized_main = page["corrected_text"].strip()
    for title, key in supplemental:
        value = page.get(key)
        if not value or str(value).strip() == normalized_main:
            continue
        lines.extend(["", f"### {title}", ""])
        lines.extend(blockquote(str(value)))

    uncertain = page.get("uncertain_readings") or []
    lines.extend(["", "### Uncertain readings", ""])
    if uncertain:
        lines.extend(f"- {item}" for item in uncertain)
    else:
        lines.append("- None separately recorded in the canonical page entry.")
    lines.extend(["", "[Back to notebook contents](#contents)", ""])
    return lines


def render() -> str:
    notebooks, provenance = load_batches()
    lines = [
        "# Lovejoy notebooks 004 + 005 — integrated page-by-page transcription",
        "",
        "Edition date: 2026-09-01",
        "",
        "This is the single human-readable edition generated from the twelve canonical paginated `*_clean.json` batches. It contains every PDF page in notebook 004 (71/71) and notebook 005 (120/120), in order. The canonical JSON remains the machine-readable authority; this Markdown file is its integrated reading surface.",
        "",
        "## Evidentiary status",
        "",
        "- **004:** first-pass coverage complete; targeted original-image second pass conceptually closed for the present argument; remaining residue is micro-paleographic, compressed foreign-language, or bibliographic. This is not advertised as a fully diplomatic edition.",
        "- **005:** first-pass coverage complete; targeted original-image corrections through Round 20 are merged into the canonical batches; a complete page-by-page diplomatic second pass has not been claimed.",
        "- `Integrated corrected text` reproduces the canonical page-level `corrected_text`. Depending on the recorded `text_layer`, this may be diplomatic visible wording, image-secure key wording plus conservative summary, or an editorial argument summary.",
        "- Separate diplomatic text, editorial summary, source collation, material observation, witness grade, and uncertainty fields are retained whenever present. They must not be collapsed into one evidence type.",
        "- The digitization component `061` does not establish archival Box 61.",
        "",
        "## Contents",
        "",
        "- [Notebook 004 — PDF pp.001–071](#notebook-004)",
        "- [Notebook 005 — PDF pp.001–120](#notebook-005)",
        "- [Batch provenance](#batch-provenance)",
        "",
    ]

    for notebook, title in (
        ("004", "Notebook 004"),
        ("005", "Notebook 005"),
    ):
        lines.extend(
            [
                f"# {title}",
                "",
                f"PDF coverage: {len(notebooks[notebook])}/{len(notebooks[notebook])} pages.",
                "",
            ]
        )
        for page in notebooks[notebook]:
            lines.extend(render_page(notebook, page))

    lines.extend(
        [
            "# Batch provenance",
            "",
            "| Notebook | PDF range | Canonical batch | Recorded batch status |",
            "|---|---:|---|---|",
        ]
    )
    for item in provenance:
        status = str(item["status"]).replace("|", "\\|").replace("\n", " ")
        lines.append(
            f"| {item['notebook']} | {item['range']} | `{item['path']}` | {status} |"
        )
    lines.extend(
        [
            "",
            "## Regeneration and verification",
            "",
            "Regenerate from the canonical JSON batches:",
            "",
            "```bash",
            "python tools/build_integrated_transcription.py",
            "```",
            "",
            "Verify that the committed edition exactly matches the generator output:",
            "",
            "```bash",
            "python tools/build_integrated_transcription.py --check",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify that the committed output exactly matches canonical JSON",
    )
    args = parser.parse_args()
    generated = render()
    if args.check:
        if not OUTPUT.is_file():
            print(f"missing integrated edition: {OUTPUT.relative_to(ROOT)}", file=sys.stderr)
            return 1
        current = OUTPUT.read_text(encoding="utf-8")
        if current != generated:
            print("integrated edition is stale; regenerate it", file=sys.stderr)
            return 1
        print("Integrated transcription: PASS (004=71/71, 005=120/120)")
        return 0
    OUTPUT.write_text(generated, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
