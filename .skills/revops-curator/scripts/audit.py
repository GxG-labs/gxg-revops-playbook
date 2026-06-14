#!/usr/bin/env python3
"""
GxG RevOps Playbook — Audit Script
Scans all SKILL.md files, scores against G1–G7 gates, outputs report.

Config is read from .skills/config.yaml (relative to --root). Falls back to
built-in defaults if the file is not present.

Usage:
    python audit.py [--root PATH] [--domain DOMAIN] [--json]

Examples:
    python audit.py
    python audit.py --domain pipeline
    python audit.py --json > audit.json
"""

import os
import re
import sys
import json
import argparse
from datetime import datetime, date
from pathlib import Path

# ─── Config (defaults — overridden by .skills/config.yaml) ────────────────────

_DEFAULT_COVERAGE_TARGETS = {
    "pipeline": 6,
    "demand-gen": 5,
    "sales-enablement": 7,
    "crm-ops": 6,
    "rev-analytics": 5,
    "cs-ops": 5,
    "rev-tech": 4,
    "pricing-packaging": 4,
    "territory-quota": 4,
    "mktg-ops": 5,
}

_DEFAULT_SETTINGS = {
    "stale_threshold_days": 90,
    "max_skill_lines": 500,
    "max_description_chars": 1024,
    "staging_ready_warning_days": 30,
    "staging_parked_warning_days": 90,
    "staging_raw_warning_days": 14,
    "staging_max_total": 20,
    "staging_max_ready": 5,
}


def load_config(root: Path) -> tuple[dict, dict]:
    """
    Load domain targets and settings from .skills/config.yaml.
    Returns (coverage_targets, settings). Falls back to defaults if YAML
    is unavailable or the file doesn't exist.
    """
    config_path = root / ".skills" / "config.yaml"
    if not config_path.exists():
        return _DEFAULT_COVERAGE_TARGETS.copy(), _DEFAULT_SETTINGS.copy()

    try:
        import yaml  # type: ignore
        raw = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    except ImportError:
        # PyYAML not installed — parse manually (simple key: value only)
        raw = _parse_simple_yaml(config_path)
    except Exception:
        return _DEFAULT_COVERAGE_TARGETS.copy(), _DEFAULT_SETTINGS.copy()

    coverage_targets = {}
    for domain_key, domain_data in raw.get("domains", {}).items():
        if isinstance(domain_data, dict):
            target = domain_data.get("target_skills") or domain_data.get("target") or 0
            coverage_targets[domain_key] = int(target)

    settings = _DEFAULT_SETTINGS.copy()
    for k, v in raw.get("settings", {}).items():
        if k in settings:
            settings[k] = int(v)

    return coverage_targets or _DEFAULT_COVERAGE_TARGETS.copy(), settings


def _parse_simple_yaml(path: Path) -> dict:
    """Minimal YAML parser for the config file when PyYAML is unavailable."""
    result: dict = {}
    stack: list = [result]
    indent_stack: list = [-1]
    current_key: list[str] = []

    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        stripped = line.lstrip()
        indent = len(line) - len(stripped)
        if ":" in stripped:
            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            while indent_stack and indent <= indent_stack[-1]:
                indent_stack.pop()
                stack.pop()
                current_key.pop() if current_key else None
            if val:
                stack[-1][key] = val
            else:
                new_dict: dict = {}
                stack[-1][key] = new_dict
                stack.append(new_dict)
                indent_stack.append(indent)
                current_key.append(key)
    return result


# ─── Runtime config (populated in main) ───────────────────────────────────────

COVERAGE_TARGETS: dict[str, int] = _DEFAULT_COVERAGE_TARGETS.copy()
SETTINGS: dict = _DEFAULT_SETTINGS.copy()

STALE_THRESHOLD_DAYS = SETTINGS["stale_threshold_days"]
MAX_SKILL_LINES = SETTINGS["max_skill_lines"]
MAX_DESCRIPTION_CHARS = SETTINGS["max_description_chars"]
MIN_TRIGGER_KEYWORDS = 5
MIN_EXAMPLES = 2

REQUIRED_FRONTMATTER = {"name", "description", "status", "domain", "tags", "version", "updated", "author"}
VALID_STATUSES = {"draft", "review", "needs-work", "active", "deprecated", "archived"}

SKILL_SCORE_LABELS = {
    7: "✅ Exemplary",
    6: "⚠️  Good",
    5: "⚠️  Good",
    4: "🔧 Needs Work",
    3: "🔧 Needs Work",
    2: "🚫 Critical",
    1: "🚫 Critical",
    0: "🚫 Critical",
}

# ─── Parser ───────────────────────────────────────────────────────────────────

def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from a SKILL.md file."""
    fm = {}
    if not content.startswith("---"):
        return fm
    end = content.find("\n---", 3)
    if end == -1:
        return fm
    block = content[4:end]
    for line in block.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def count_examples(content: str) -> int:
    return len(re.findall(r"^### Example", content, re.MULTILINE))


def has_out_of_scope(content: str) -> bool:
    return bool(re.search(r"out of scope", content, re.IGNORECASE))


def count_trigger_keywords(description: str) -> int:
    return len(re.findall(r'"[^"]{2,}"', description))


def is_third_person(description: str) -> bool:
    return not bool(re.search(r"\b(I |you |we |our )\b", description, re.IGNORECASE))


def days_since_update(updated_str: str) -> int | None:
    try:
        updated = datetime.strptime(updated_str, "%Y-%m-%d").date()
        return (date.today() - updated).days
    except Exception:
        return None

# ─── Gate Checks ──────────────────────────────────────────────────────────────

def check_gates(skill_path: Path, content: str, fm: dict) -> dict:
    name = fm.get("name", "")
    description = fm.get("description", "")
    lines = content.splitlines()

    gates = {}

    g1 = bool(re.match(r"^[a-z][a-z0-9-]{1,62}[a-z0-9]$", name)) and len(name) <= 64
    gates["G1"] = {"pass": g1, "detail": f"name='{name}' {'OK' if g1 else 'FAIL: not kebab-case or too long'}"}

    has_use_when = "use when" in description.lower()
    kw_count = count_trigger_keywords(description)
    third_person = is_third_person(description)
    desc_len = len(description)
    g2 = has_use_when and kw_count >= MIN_TRIGGER_KEYWORDS and third_person and desc_len <= MAX_DESCRIPTION_CHARS
    gates["G2"] = {
        "pass": g2,
        "detail": f"USE WHEN={'✓' if has_use_when else '✗'} | keywords={kw_count}/{MIN_TRIGGER_KEYWORDS} | "
                  f"third-person={'✓' if third_person else '✗'} | chars={desc_len}/{MAX_DESCRIPTION_CHARS}"
    }

    g3 = len(lines) <= MAX_SKILL_LINES
    gates["G3"] = {"pass": g3, "detail": f"{len(lines)} lines (max {MAX_SKILL_LINES})"}

    example_count = count_examples(content)
    g4 = example_count >= MIN_EXAMPLES
    gates["G4"] = {"pass": g4, "detail": f"{example_count} examples found (min {MIN_EXAMPLES})"}

    g5 = has_out_of_scope(content)
    gates["G5"] = {"pass": g5, "detail": "'Out of scope' section " + ("found" if g5 else "MISSING")}

    has_domain = "domain" in fm and fm["domain"] in COVERAGE_TARGETS
    has_tags = "tags" in fm and len(fm["tags"]) > 2
    g6 = has_domain and has_tags
    gates["G6"] = {"pass": g6, "detail": f"domain={'✓' if has_domain else '✗'} | tags={'✓' if has_tags else '✗'}"}

    missing = REQUIRED_FRONTMATTER - set(fm.keys())
    g7 = len(missing) == 0
    gates["G7"] = {"pass": g7, "detail": f"missing fields: {missing if missing else 'none'}"}

    return gates


# ─── Scanner ──────────────────────────────────────────────────────────────────

def scan_playbook(root: Path, domain_filter: str | None = None) -> list[dict]:
    results = []

    for skill_md in sorted(root.rglob("SKILL.md")):
        # Skip curator adapter and shared skill content
        if ".claude" in skill_md.parts or ".skills" in skill_md.parts:
            continue
        parts = skill_md.relative_to(root).parts
        if not parts:
            continue
        skill_domain = parts[0]
        if domain_filter and skill_domain != domain_filter:
            continue

        content = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        gates = check_gates(skill_md, content, fm)
        score = sum(1 for g in gates.values() if g["pass"])
        days_stale = days_since_update(fm.get("updated", ""))

        results.append({
            "path": str(skill_md.relative_to(root)),
            "name": fm.get("name", skill_md.parent.name),
            "domain": fm.get("domain", skill_domain),
            "status": fm.get("status", "unknown"),
            "score": score,
            "score_label": SKILL_SCORE_LABELS.get(score, "unknown"),
            "gates": gates,
            "days_stale": days_stale,
            "stale": (days_stale or 0) > STALE_THRESHOLD_DAYS and fm.get("status") == "active",
            "version": fm.get("version", "?"),
            "updated": fm.get("updated", "?"),
            "tags": fm.get("tags", ""),
        })

    return results


# ─── Report ───────────────────────────────────────────────────────────────────

def print_report(results: list[dict], root: Path):
    total = len(results)
    by_status: dict = {}
    for r in results:
        by_status.setdefault(r["status"], []).append(r)

    by_domain: dict = {}
    for r in results:
        by_domain.setdefault(r["domain"], []).append(r)

    active_count = len(by_status.get("active", []))
    avg_score = sum(r["score"] for r in results) / total if total else 0
    stale = [r for r in results if r["stale"]]

    print(f"\n{'='*60}")
    print(f"GxG RevOps Playbook — Audit Report")
    print(f"Date: {date.today()}  |  Skills audited: {total}")
    print(f"{'='*60}\n")

    print("SUMMARY")
    print(f"  Total skills:    {total}")
    for s in ["active", "draft", "review", "needs-work", "deprecated"]:
        n = len(by_status.get(s, []))
        if n:
            print(f"  {s:16} {n}")
    print(f"  Avg gate score:  {avg_score:.1f}/7")
    print(f"  Stale skills:    {len(stale)}")
    total_target = sum(COVERAGE_TARGETS.values())
    print(f"  Coverage:        {active_count}/{total_target} ({100*active_count/total_target:.0f}%)\n")

    print("DOMAIN COVERAGE")
    print(f"  {'Domain':<22} {'Active':>6} {'Draft':>6} {'Target':>6} {'Coverage':>9}")
    print(f"  {'-'*52}")
    for domain, target in COVERAGE_TARGETS.items():
        skills = by_domain.get(domain, [])
        n_active = sum(1 for s in skills if s["status"] == "active")
        n_draft = sum(1 for s in skills if s["status"] == "draft")
        cov = f"{100*n_active//target}%" if target else "n/a"
        flag = "✅" if n_active >= target else ("⚠️ " if n_active >= target * 0.5 else "🔧")
        print(f"  {domain:<22} {n_active:>6} {n_draft:>6} {target:>6}  {cov:>6} {flag}")

    print("\nQUALITY BREAKDOWN")
    exemplary  = [r for r in results if r["score"] == 7]
    good       = [r for r in results if r["score"] in (5, 6)]
    needs_work = [r for r in results if r["score"] in (3, 4)]
    critical   = [r for r in results if r["score"] <= 2]

    for label, group in [("✅ Exemplary (7/7)", exemplary), ("⚠️  Good (5-6/7)", good),
                          ("🔧 Needs Work (3-4/7)", needs_work), ("🚫 Critical (≤2/7)", critical)]:
        if group:
            print(f"\n  {label}")
            for r in sorted(group, key=lambda x: x["score"], reverse=True):
                failing = [k for k, v in r["gates"].items() if not v["pass"]]
                fail_str = f"  failing: {', '.join(failing)}" if failing else ""
                print(f"    [{r['score']}/7] {r['name']} ({r['domain']}){fail_str}")

    if stale:
        print(f"\n⏰ STALE SKILLS ({len(stale)})")
        for r in stale:
            print(f"  {r['name']} ({r['domain']}) — last updated {r['updated']} ({r['days_stale']} days ago)")

    print("\n" + "="*60)


# ─── Main ─────────────────────────────────────────────────────────────────────

def _init_config(root: Path):
    """Load config from .skills/config.yaml and update module-level variables."""
    global COVERAGE_TARGETS, SETTINGS, STALE_THRESHOLD_DAYS, MAX_SKILL_LINES, MAX_DESCRIPTION_CHARS
    COVERAGE_TARGETS, SETTINGS = load_config(root)
    STALE_THRESHOLD_DAYS = SETTINGS["stale_threshold_days"]
    MAX_SKILL_LINES = SETTINGS["max_skill_lines"]
    MAX_DESCRIPTION_CHARS = SETTINGS["max_description_chars"]


# ─── README Freshness ─────────────────────────────────────────────────────────

def check_readme_freshness(root: Path) -> dict:
    readme = root / "README.md"
    if not readme.exists():
        return {"stale": False, "message": "README.md not found"}

    content = readme.read_text(encoding="utf-8")

    skill_match = re.search(r"skills-(\d+)%20active", content)
    cov_match   = re.search(r"coverage-(\d+)%25", content)
    badge_count = int(skill_match.group(1)) if skill_match else None
    badge_pct   = int(cov_match.group(1))   if cov_match  else None

    actual_active = 0
    for sm in root.rglob("SKILL.md"):
        if ".claude" in sm.parts or ".skills" in sm.parts:
            continue
        fm = parse_frontmatter(sm.read_text(encoding="utf-8"))
        if fm.get("status") == "active":
            actual_active += 1

    total_target = sum(COVERAGE_TARGETS.values())
    actual_pct = round(actual_active / total_target * 100) if total_target else 0

    stale = (badge_count != actual_active) or (badge_pct != actual_pct)

    msg = ""
    if stale:
        parts_changed = []
        if badge_count != actual_active:
            parts_changed.append(f"skills {badge_count}→{actual_active}")
        if badge_pct != actual_pct:
            parts_changed.append(f"coverage {badge_pct}%→{actual_pct}%")
        msg = f"📋 README is stale ({', '.join(parts_changed)}). Update?"

    return {
        "stale": stale,
        "badge_count": badge_count,
        "actual_count": actual_active,
        "badge_pct": badge_pct,
        "actual_pct": actual_pct,
        "message": msg,
    }


def update_readme_badges(root: Path) -> bool:
    readme = root / "README.md"
    if not readme.exists():
        return False

    content = readme.read_text(encoding="utf-8")
    original = content

    domain_counts: dict[str, int] = {}
    for sm in root.rglob("SKILL.md"):
        if ".claude" in sm.parts or ".skills" in sm.parts:
            continue
        parts = sm.relative_to(root).parts
        domain = parts[0]
        fm = parse_frontmatter(sm.read_text(encoding="utf-8"))
        if fm.get("status") == "active":
            domain_counts[domain] = domain_counts.get(domain, 0) + 1

    total_active = sum(domain_counts.values())
    total_target = sum(COVERAGE_TARGETS.values())
    actual_pct   = round(total_active / total_target * 100) if total_target else 0

    color = "red" if actual_pct < 40 else "orange" if actual_pct < 60 else "yellow" if actual_pct < 80 else "brightgreen"

    from datetime import datetime as _dt
    month_year = _dt.today().strftime("%B %Y").replace(" ", "%20")

    content = re.sub(r"skills-\d+%20active-\w+", f"skills-{total_active}%20active-{color}", content)
    content = re.sub(r"coverage-\d+%25-\w+", f"coverage-{actual_pct}%25-{color}", content)
    content = re.sub(r"updated-[^)]+", f"updated-{month_year}-lightgrey", content)

    def replace_domain_row(m):
        domain_link = m.group(0)
        domain_key = re.search(r"\./(\S+)/", domain_link)
        if not domain_key:
            return m.group(0)
        dk = domain_key.group(1)
        target = COVERAGE_TARGETS.get(dk)
        if not target:
            return m.group(0)
        active = domain_counts.get(dk, 0)
        pct = round(active / target * 100)
        result = re.sub(r"\d+/\d+", f"{active}/{target}", domain_link, count=1)
        result = re.sub(r"\d+%", f"{pct}%", result, count=1)
        return result

    content = re.sub(r"\| \[.*?\]\(\.\/\w[\w-]*\/\).*?\|.*?\|.*?\|", replace_domain_row, content)

    content = re.sub(
        r"(\*\*Итого\*\*.*?\| \*\*)\d+/51(\*\*.*?\| \*\*)\d+%(\*\*)",
        lambda m: f"{m.group(1)}{total_active}/51{m.group(2)}{actual_pct}%{m.group(3)}",
        content
    )

    if content != original:
        readme.write_text(content, encoding="utf-8")
        return True
    return False


# ─── Staging Scanner ──────────────────────────────────────────────────────────

def _staging_thresholds() -> dict:
    return {
        "raw": SETTINGS.get("staging_raw_warning_days", 14),
        "refining": SETTINGS.get("staging_ready_warning_days", 30),
        "ready": SETTINGS.get("staging_ready_warning_days", 30),
        "parked": SETTINGS.get("staging_parked_warning_days", 90),
    }


def scan_staging(root: Path) -> list[dict]:
    staging_dir = root / "_staging"
    if not staging_dir.exists():
        return []

    thresholds = _staging_thresholds()
    results = []

    for note in sorted(staging_dir.glob("*.md")):
        if note.name in ("README.md", "_template.md"):
            continue

        content = note.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        if not fm:
            continue

        status = fm.get("status", "raw")
        days = days_since_update(fm.get("added", "")) or 0
        threshold = thresholds.get(status, 30)
        stale = days > threshold

        readiness = 0
        if fm.get("skill_candidate") == "yes":
            readiness += 1
        body = content[content.find("\n---", 3) + 4:] if "---" in content else content
        if len(body.split()) > 100:
            readiness += 1
        if "Вопросы без ответа" not in content or re.search(r"Вопросы без ответа\s*\n+\s*\{", content):
            readiness += 1

        results.append({
            "slug": note.stem,
            "title": fm.get("title", note.stem),
            "domain": fm.get("domain", "?"),
            "status": status,
            "skill_candidate": fm.get("skill_candidate", "?"),
            "days_in_staging": days,
            "stale": stale,
            "readiness": readiness,
            "added": fm.get("added", "?"),
            "source": fm.get("source", "?"),
        })

    return results


def print_staging_report(notes: list[dict]):
    if not notes:
        print("\n📥 STAGING: empty\n")
        return

    print(f"\n📥 STAGING ({len(notes)} notes)")

    stars = {3: "★★★ ready", 2: "★★☆ almost", 1: "★☆☆ partial", 0: "☆☆☆ raw"}

    print(f"\n  {'Note':<30} {'Domain':<18} {'Status':<10} {'Days':>5} {'Readiness':<15} {'Action'}")
    print(f"  {'-'*90}")
    for n in sorted(notes, key=lambda x: (-x["readiness"], x["days_in_staging"])):
        stale_flag = " ⏰" if n["stale"] else ""
        action = ""
        if n["status"] == "ready" and n["stale"]:
            action = "→ promote now"
        elif n["readiness"] == 3:
            action = "→ ready to promote"
        elif n["status"] == "parked" and n["stale"]:
            action = "→ delete or reconsider"
        elif n["status"] == "raw" and n["stale"]:
            action = "→ refine or park"
        elif n["readiness"] >= 2:
            action = "→ refine"
        print(f"  {n['title'][:29]:<30} {n['domain']:<18} {n['status']:<10} {n['days_in_staging']:>5}{stale_flag:<3} {stars[n['readiness']]:<15} {action}")

    alerts = []
    ready_notes = [n for n in notes if n["readiness"] == 3 or n["status"] == "ready"]
    max_ready = SETTINGS.get("staging_max_ready", 5)
    max_total = SETTINGS.get("staging_max_total", 20)
    if len(ready_notes) > max_ready:
        alerts.append(f"⚠️  {len(ready_notes)} ready notes — backlog building up")
    if len(notes) > max_total:
        alerts.append(f"⚠️  {len(notes)} notes in staging — inbox overflowing")
    stale = [n for n in notes if n["stale"]]
    if stale:
        alerts.append(f"⏰  {len(stale)} stale notes need attention")

    if alerts:
        print()
        for a in alerts:
            print(f"  {a}")


# ─── Entry point ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Audit GxG RevOps Playbook skills + staging")
    parser.add_argument("--root", default=".", help="Playbook root directory")
    parser.add_argument("--domain", help="Filter skills to a specific domain")
    parser.add_argument("--staging-only", action="store_true", help="Show only staging report")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"ERROR: root path not found: {root}", file=sys.stderr)
        sys.exit(1)

    _init_config(root)

    staging_notes = scan_staging(root)

    if args.staging_only:
        if args.json:
            print(json.dumps(staging_notes, indent=2, default=str))
        else:
            print_staging_report(staging_notes)
        return

    skill_results = scan_playbook(root, domain_filter=args.domain)

    if not skill_results and not staging_notes:
        print("No skills or staging notes found. Is --root correct?")
        sys.exit(0)

    if args.json:
        print(json.dumps({"skills": skill_results, "staging": staging_notes}, indent=2, default=str))
    else:
        if skill_results:
            print_report(skill_results, root)
        print_staging_report(staging_notes)


if __name__ == "__main__":
    main()
