#!/usr/bin/env python3
"""
Daily Journal Rollover — RAFA AI BRAIN
Runs every morning via macOS launchd (and also via ~/.zshrc on terminal open).

What it does:
  1. Reads Today.md
  2. If already dated today → exits silently (nothing to do)
  3. If dated before today → archives the note to 01 Journals/[year]/[month]/[date].md
  4. Extracts any incomplete tasks (- [ ] with text)
  5. Writes a fresh Today.md with today's date + carried-over tasks (if any)
"""

import os
import re
from datetime import datetime

# ── Config ──────────────────────────────────────────────────────────────────

VAULT       = "/Users/rafa/Desktop/RAFA AI BRAIN"
TODAY_MD    = os.path.join(VAULT, "Today.md")

MONTHS = {
    1: "January",  2: "February", 3: "March",    4: "April",
    5: "May",      6: "June",     7: "July",      8: "August",
    9: "September",10: "October", 11: "November", 12: "December",
}
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# ── Helpers ──────────────────────────────────────────────────────────────────

def parse_note_date(content: str):
    """
    Extract date from first line — handles both:
      'Friday, April 17, 2026'      (no heading marker)
      '# Friday, April 17, 2026'   (with # heading marker)
    Returns a date object or None.
    """
    m = re.search(r'^#?\s*\w+,\s+(\w+)\s+(\d+),\s+(\d+)', content, re.MULTILINE)
    if not m:
        return None
    month_name, day, year = m.group(1), int(m.group(2)), int(m.group(3))
    month_num = {v: k for k, v in MONTHS.items()}.get(month_name)
    if not month_num:
        return None
    try:
        return datetime(year, month_num, day).date()
    except ValueError:
        return None

def format_date(d) -> str:
    """Returns e.g. 'Friday, April 17, 2026'"""
    return f"{WEEKDAYS[d.weekday()]}, {MONTHS[d.month]} {d.day}, {d.year}"

def archive_path(d) -> str:
    year_folder  = f"{d.year} Journals"
    month_folder = f"{d.month:02d} {MONTHS[d.month]}"
    filename     = f"{d.strftime('%Y-%m-%d')}.md"
    return os.path.join(VAULT, "01 Journals", year_folder, month_folder, filename)

def get_incomplete_tasks(content: str) -> list:
    """Return non-empty incomplete task lines (- [ ] with actual text after)."""
    return [
        line.strip()
        for line in content.splitlines()
        if re.search(r'-\s\[\s\]\s+\S', line)
    ]

def build_fresh_note(today_str: str, carried: list, prev_weekday: str) -> str:
    """
    Build a fresh Today.md matching the vault template exactly.
    No # heading — just the date string on the first line.
    """
    lines = [today_str, "", "---", ""]

    # Carried-over tasks block (only if there are any)
    if carried:
        lines += [f"## 🔁 Carried over from {prev_weekday}", ""]
        lines += carried
        lines += ["", "---", ""]

    lines += [
        "## 🙏 Gratidão",
        "",
        "- ",
        "",
        "---",
        "",
        "## 💭 Pensamentos do dia",
        "",
        "",
        "",
        "---",
        "",
        "## ✅ To-do",
        "",
        "- [ ]",
        "- [ ]",
        "- [ ]",
        "- [ ]",
        "- [ ]",
        "",
        "---",
        "",
        "## 📝 Random thoughts",
        "",
        "",
        "",
        "---",
        "",
        "## 🍽️ Food Log",
        "",
        "",
        "",
        "---",
        "",
        "📝 LOG",
        "",
        "",
        "",
        "---",
        "",
        "👨‍🦳 Identidade",
        "",
        "",
    ]

    return "\n".join(lines)

# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    today = datetime.now().date()

    # ── Read existing note ──
    if os.path.exists(TODAY_MD):
        with open(TODAY_MD, "r", encoding="utf-8") as f:
            content = f.read()

        note_date = parse_note_date(content)

        if note_date == today:
            return  # Already fresh — nothing to do

        # ── Archive previous day ──
        carried   = []
        prev_wday = ""
        if note_date:
            carried   = get_incomplete_tasks(content)
            prev_wday = WEEKDAYS[note_date.weekday()]
            dest      = archive_path(note_date)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            if not os.path.exists(dest):   # never overwrite an existing archive
                with open(dest, "w", encoding="utf-8") as f:
                    f.write(content)
        # If note_date is None (unreadable date), we still write a fresh note
        # but we don't try to archive (to avoid data loss on malformed files).

    else:
        carried   = []
        prev_wday = ""

    # ── Write fresh Today.md ──
    fresh = build_fresh_note(format_date(today), carried, prev_wday)
    with open(TODAY_MD, "w", encoding="utf-8") as f:
        f.write(fresh)

    print(f"[daily-rollover] Today.md rolled over → {format_date(today)}")


if __name__ == "__main__":
    main()
