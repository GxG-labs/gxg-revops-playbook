#!/usr/bin/env python3
"""Summarize a user-provided LinkedIn data export for profile optimization."""

from __future__ import annotations

import argparse
import csv
import io
import os
import sys
import tempfile
import zipfile
from pathlib import Path


FILES = [
    "Profile.csv",
    "Positions.csv",
    "Education.csv",
    "Skills.csv",
    "Certifications.csv",
    "Languages.csv",
    "Projects.csv",
    "Volunteering.csv",
    "Recommendations_Received.csv",
    "Connections.csv",
    "Invitations.csv",
    "Ad_Targeting.csv",
    "Inferences_about_you.csv",
]


def extract_if_zip(path: Path) -> tuple[Path, tempfile.TemporaryDirectory[str] | None]:
    if path.is_file() and path.suffix.lower() == ".zip":
        tmp = tempfile.TemporaryDirectory()
        with zipfile.ZipFile(path) as zf:
            zf.extractall(tmp.name)
        return Path(tmp.name), tmp
    return path, None


def find_file(root: Path, name: str) -> Path | None:
    direct = root / name
    if direct.exists():
        return direct
    matches = list(root.rglob(name))
    return matches[0] if matches else None


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def cell(row: dict[str, str], *names: str) -> str:
    for name in names:
        if name in row and row[name]:
            return row[name].strip()
    return ""


def truncate(text: str, limit: int = 280) -> str:
    text = " ".join((text or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- None found"


def summarize(root: Path) -> str:
    found: dict[str, Path] = {}
    rows: dict[str, list[dict[str, str]]] = {}
    for name in FILES:
        file_path = find_file(root, name)
        if file_path:
            found[name] = file_path
            try:
                rows[name] = read_csv(file_path)
            except csv.Error as exc:
                rows[name] = []
                print(f"Warning: failed to parse {name}: {exc}", file=sys.stderr)

    out = io.StringIO()
    out.write("# LinkedIn Export Summary\n\n")
    out.write(f"Source: `{root}`\n\n")

    out.write("## Files Found\n\n")
    for name in FILES:
        marker = "found" if name in found else "missing"
        count = len(rows.get(name, []))
        out.write(f"- {name}: {marker} ({count} rows)\n")
    out.write("\n")

    profile = rows.get("Profile.csv", [])
    if profile:
        p = profile[0]
        full_name = " ".join(x for x in [cell(p, "First Name"), cell(p, "Last Name")] if x)
        out.write("## Profile\n\n")
        out.write(f"- Name: {full_name or '(missing)'}\n")
        out.write(f"- Headline: {cell(p, 'Headline') or '(missing)'}\n")
        out.write(f"- Industry: {cell(p, 'Industry') or '(missing)'}\n")
        out.write(f"- Location: {cell(p, 'Geo Location', 'Location') or '(missing)'}\n")
        out.write(f"- Websites: {cell(p, 'Websites') or '(missing)'}\n")
        out.write(f"- About preview: {truncate(cell(p, 'Summary'), 500) or '(missing)'}\n\n")

    positions = rows.get("Positions.csv", [])
    out.write("## Positions\n\n")
    if positions:
        for row in positions[:12]:
            title = cell(row, "Title")
            company = cell(row, "Company Name")
            start = cell(row, "Started On", "Start Date")
            end = cell(row, "Finished On", "End Date") or "Present"
            description = cell(row, "Description")
            desc_flag = "description present" if description else "NO DESCRIPTION"
            out.write(f"### {title or '(missing title)'} @ {company or '(missing company)'}\n\n")
            out.write(f"- Dates: {start or '?'} - {end}\n")
            out.write(f"- Location: {cell(row, 'Location') or '(missing)'}\n")
            out.write(f"- Description: {desc_flag}\n")
            if description:
                out.write(f"- Preview: {truncate(description)}\n")
            out.write("\n")
    else:
        out.write("- No positions found\n\n")

    out.write("## Skills\n\n")
    skills = [cell(row, "Name") for row in rows.get("Skills.csv", []) if cell(row, "Name")]
    out.write(bullets(skills[:100]))
    out.write("\n\n")

    for fname, title, fields in [
        ("Education.csv", "Education", ("School Name", "Degree Name")),
        ("Certifications.csv", "Certifications", ("Name", "Authority")),
        ("Languages.csv", "Languages", ("Name", "Proficiency")),
        ("Projects.csv", "Projects", ("Title", "Description")),
        ("Volunteering.csv", "Volunteering", ("Company Name", "Role")),
    ]:
        out.write(f"## {title}\n\n")
        items = []
        for row in rows.get(fname, [])[:20]:
            primary = cell(row, fields[0])
            secondary = cell(row, fields[1]) if len(fields) > 1 else ""
            items.append(" - ".join(x for x in [primary, truncate(secondary, 120)] if x))
        out.write(bullets(items))
        out.write("\n\n")

    out.write("## Optimization Flags\n\n")
    flags = []
    if not profile or not cell(profile[0], "Headline"):
        flags.append("Profile headline missing.")
    if not profile or not cell(profile[0], "Summary"):
        flags.append("About/Summary missing.")
    missing_desc = sum(1 for row in positions if not cell(row, "Description"))
    if missing_desc:
        flags.append(f"{missing_desc} position entries have no description.")
    if len(skills) < 20:
        flags.append(f"Only {len(skills)} skills found; likely under-optimized for recruiter search.")
    if "Certifications.csv" not in found:
        flags.append("Certifications.csv missing; certifications cannot be audited from export.")
    if "Projects.csv" not in found:
        flags.append("Projects.csv missing; project proof cannot be audited from export.")
    out.write(bullets(flags))
    out.write("\n")

    return out.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize LinkedIn export CSVs.")
    parser.add_argument("path", help="Path to LinkedIn export directory or zip")
    args = parser.parse_args()

    path = Path(os.path.expanduser(args.path)).resolve()
    if not path.exists():
        print(f"Path not found: {path}", file=sys.stderr)
        return 1

    root, tmp = extract_if_zip(path)
    try:
        print(summarize(root))
    finally:
        if tmp:
            tmp.cleanup()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
