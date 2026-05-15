#!/usr/bin/env python3
"""
Auto-process food photos from vault root to journal food logs.
Runs on session start to catch any loose images.
"""

import os
import glob
import json
import re
from datetime import datetime
from pathlib import Path

VAULT_ROOT = "/Users/rafa/Desktop/RAFA AI BRAIN"
IMAGE_EXTENSIONS = ("*.jpg", "*.jpeg", "*.png", "*.webp")

def find_loose_images():
    """Find any image files in vault root (not in subdirectories)."""
    os.chdir(VAULT_ROOT)
    images = []
    for ext in IMAGE_EXTENSIONS:
        images.extend(glob.glob(ext))
    return [img for img in images if os.path.isfile(img)]

def get_today_journal_path():
    """Get path to today's journal note."""
    today = datetime.now()
    year = today.strftime("%Y")
    month_num = today.strftime("%m")
    month_name = today.strftime("%B")
    day = today.strftime("%Y-%m-%d")

    journal_path = f"01 Journals/{year} Journals/{month_num} {month_name}/{day}.md"
    return journal_path

def add_image_to_foodlog(image_filename, journal_path):
    """Add image embed to the food log section of journal note."""

    if not os.path.exists(journal_path):
        return {"success": False, "reason": "journal_not_found"}

    with open(journal_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if Food Log section exists
    if "## 🍽️ Food Log" not in content:
        return {"success": False, "reason": "no_foodlog_section"}

    # Find where to insert (right after Food Log header, before first ### or other section)
    lines = content.split('\n')
    insert_idx = None
    for i, line in enumerate(lines):
        if "## 🍽️ Food Log" in line:
            insert_idx = i + 2  # Skip header and blank line
            break

    if insert_idx is None:
        return {"success": False, "reason": "foodlog_parse_failed"}

    # Create embed markdown
    embed_line = f"![{image_filename}]({image_filename})"

    # Insert at the found position
    lines.insert(insert_idx, embed_line)
    lines.insert(insert_idx + 1, "")  # Add blank line after

    # Write back
    new_content = '\n'.join(lines)
    with open(journal_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return {"success": True}

def process_images():
    """Main: find, analyze, and process all loose images."""
    images = find_loose_images()

    if not images:
        return {
            "found": 0,
            "processed": 0,
            "failed": []
        }

    journal_path = get_today_journal_path()
    processed = 0
    failed = []

    for image in images:
        # Add to food log
        result = add_image_to_foodlog(image, journal_path)

        if result["success"]:
            # Delete the image from root
            try:
                os.remove(image)
                processed += 1
            except Exception as e:
                failed.append({"image": image, "reason": f"delete_failed: {str(e)}"})
        else:
            failed.append({"image": image, "reason": result.get("reason", "unknown")})

    return {
        "found": len(images),
        "processed": processed,
        "failed": failed
    }

if __name__ == "__main__":
    result = process_images()

    # Output for Claude to parse
    if result["processed"] > 0:
        print(json.dumps({
            "systemMessage": f"✅ Food photo automation: {result['processed']} image(s) processed and added to today's food log."
        }))
    elif result["failed"]:
        print(json.dumps({
            "systemMessage": f"⚠️ Food photos found but not fully processed. Check manually: {', '.join([f['image'] for f in result['failed']])}"
        }))
