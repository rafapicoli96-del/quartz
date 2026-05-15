#!/usr/bin/env python3
"""
Pickup Track Renamer — Shareable Version

Usage:
  python3 rename_pickup_shareable.py /path/to/folder [--course LP-24-Interm_v2]

Or:
  python3 rename_pickup_shareable.py /path/to/folder --auto
  (Uses LP-24-Interm_v2 by default)

This script renames audio files according to the Pickup Music naming convention:
  (course_prefix)-(Grade#)-(Day#)-(Track_Description)-(BPM)-(Key)-(exercise_optional)

Example output: LP-24-Interm_v2-G4-D5-Good_Times-85-Emi-Ex1.wav
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class PickupTrackRenamer:
    """Renames Pickup Music course tracks to a standard naming convention."""

    # Known course prefixes
    COURSE_PREFIXES = {
        "lp-24-interm": "LP-24-Interm_v2",
        "lp-24-intermediate": "LP-24-Interm_v2",
        "lp 24 intermediate": "LP-24-Interm_v2",
    }

    DEFAULT_COURSE = "LP-24-Interm_v2"

    def __init__(self, folder_path: str, course_prefix: Optional[str] = None):
        """Initialize with folder path and optional course prefix."""
        self.folder_path = Path(folder_path)
        if not self.folder_path.exists():
            raise FileNotFoundError(f"Folder not found: {folder_path}")
        if not self.folder_path.is_dir():
            raise NotADirectoryError(f"Not a directory: {folder_path}")

        self.course_prefix = course_prefix or self.DEFAULT_COURSE
        self.audio_extensions = {'.wav', '.mp3', '.aiff', '.aif', '.m4a', '.flac'}

    def parse_filename(self, filename: str) -> Dict[str, Optional[str]]:
        """
        Extract components from filename: Grade, Day, Description, BPM, Key, Exercise.
        Returns a dict with keys: grade, day, description, bpm, key, exercise
        """
        # Remove extension
        name, ext = os.path.splitext(filename)

        # Initialize result
        result = {
            'grade': None,
            'day': None,
            'description': None,
            'bpm': None,
            'key': None,
            'exercise': None,
            'extension': ext,
        }

        # Find grade pattern: G followed by digit(s)
        grade_match = re.search(r'[Gg]rade\s*(\d+)|[Gg](\d+)', name)
        if grade_match:
            grade_num = grade_match.group(1) or grade_match.group(2)
            result['grade'] = f"G{grade_num}"
            name = re.sub(r'[Gg]rade\s*\d+|[Gg]\d+', '', name, flags=re.IGNORECASE).strip()

        # Find day pattern: D followed by digit(s)
        day_match = re.search(r'[Dd]ay\s*(\d+)|[Dd](\d+)', name)
        if day_match:
            day_num = day_match.group(1) or day_match.group(2)
            result['day'] = f"D{day_num}"
            name = re.sub(r'[Dd]ay\s*\d+|[Dd]\d+', '', name, flags=re.IGNORECASE).strip()

        # Find exercise pattern at the end: ex1, ex2, jam, etc.
        exercise_match = re.search(r'([Ee]x\d+|[Jj]am)\s*$', name)
        if exercise_match:
            ex_text = exercise_match.group(1).lower()
            result['exercise'] = ex_text.capitalize() if ex_text.startswith('ex') else "Jam"
            name = name[:exercise_match.start()].strip()

        # Find BPM: a number typically between 40-240, preferably isolated
        bpm_match = re.search(r'\b([5-9]\d|1\d{2}|2[0-3]\d)\b', name)
        if bpm_match:
            result['bpm'] = bpm_match.group(1)
            name = name[:bpm_match.start()] + name[bpm_match.end():]

        # Find key: typically a note name with optional quality
        # Pattern: A-G, optionally followed by b/# and/or maj/min/m/dim, etc.
        key_pattern = r'(?:^|\s)([A-Ga-g][b#]?(?:maj|min|m|dim|aug|sus)?)\s*$'
        key_match = re.search(key_pattern, name)
        if key_match:
            result['key'] = key_match.group(1)
            name = name[:key_match.start()].strip()
        else:
            # If key not at end, try to find it anywhere (less strict)
            key_pattern_loose = r'([A-Ga-g][b#]?(?:maj|min|m|dim|aug)?)'
            key_match = re.search(key_pattern_loose, name)
            if key_match:
                result['key'] = key_match.group(1)
                name = name[:key_match.start()] + name[key_match.end():]

        # What's left is description
        description = name.strip()
        if description:
            # Clean up: replace multiple spaces, hyphens, underscores with single underscore
            description = re.sub(r'[\s\-_]+', '_', description)
            result['description'] = description

        return result

    def build_new_name(self, parsed: Dict[str, Optional[str]]) -> Optional[str]:
        """Build new filename from parsed components."""
        components = [self.course_prefix]

        required = ['grade', 'day', 'description', 'bpm', 'key']
        for key in required:
            if not parsed.get(key):
                return None  # Missing required component

        components.append(parsed['grade'])
        components.append(parsed['day'])
        components.append(parsed['description'])
        components.append(parsed['bpm'])
        components.append(parsed['key'])

        if parsed.get('exercise'):
            components.append(parsed['exercise'])

        return '-'.join(components) + parsed['extension']

    def process_folder(self) -> List[Tuple[str, Optional[str], bool]]:
        """
        Process all audio files in the folder.
        Returns list of (original_name, new_name_or_error, success)
        """
        results = []

        for filename in sorted(os.listdir(self.folder_path)):
            if not any(filename.lower().endswith(ext) for ext in self.audio_extensions):
                continue

            parsed = self.parse_filename(filename)
            new_name = self.build_new_name(parsed)

            if new_name and new_name != filename:
                results.append((filename, new_name, True))
            elif new_name:
                results.append((filename, new_name, True))
            else:
                # Missing required components
                missing = [k for k in ['grade', 'day', 'description', 'bpm', 'key']
                          if not parsed.get(k)]
                error_msg = f"Missing: {', '.join(missing)}"
                results.append((filename, error_msg, False))

        return results

    def show_preview(self, results: List[Tuple[str, str, bool]]):
        """Display a preview table before renaming."""
        print("\n" + "="*80)
        print(f"📋 PREVIEW — {len(results)} files found")
        print("="*80)
        print(f"Course prefix: {self.course_prefix}\n")

        # Print table header
        print(f"{'#':<3} | {'ORIGINAL NAME':<40} | {'NEW NAME':<40}")
        print("-"*80)

        for i, (original, new, success) in enumerate(results, 1):
            status = "✅" if success else "⚠️"
            print(f"{status} {i:<1} | {original:<40} | {new:<40}")

        failed = [r for r in results if not r[2]]
        if failed:
            print(f"\n⚠️  {len(failed)} file(s) flagged for review (missing components)")

        print("\n" + "="*80)

    def execute_renames(self, results: List[Tuple[str, str, bool]]) -> int:
        """Rename files. Returns count of successful renames."""
        count = 0
        for original, new, success in results:
            if not success:
                print(f"⏭️  Skipping: {original}")
                continue

            old_path = self.folder_path / original
            new_path = self.folder_path / new

            try:
                os.rename(old_path, new_path)
                print(f"✅ {original} → {new}")
                count += 1
            except Exception as e:
                print(f"❌ Error renaming {original}: {e}")

        return count


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 rename_pickup_shareable.py <folder_path> [--course PREFIX] [--auto]")
        print("\nExamples:")
        print("  python3 rename_pickup_shareable.py /path/to/tracks")
        print("  python3 rename_pickup_shareable.py /path/to/tracks --course LP-24-Interm_v2")
        print("  python3 rename_pickup_shareable.py /path/to/tracks --auto")
        sys.exit(1)

    folder_path = sys.argv[1]
    course_prefix = None
    auto_confirm = False

    # Parse arguments
    for arg in sys.argv[2:]:
        if arg == "--auto":
            auto_confirm = True
        elif arg.startswith("--course"):
            if "=" in arg:
                course_prefix = arg.split("=", 1)[1]
            elif len(sys.argv) > sys.argv.index(arg) + 1:
                course_prefix = sys.argv[sys.argv.index(arg) + 1]

    try:
        renamer = PickupTrackRenamer(folder_path, course_prefix)
        results = renamer.process_folder()

        if not results:
            print(f"❌ No audio files found in {folder_path}")
            sys.exit(1)

        # Show preview
        renamer.show_preview(results)

        # Ask for confirmation
        if not auto_confirm:
            response = input("\n✋ Proceed with renames? (yes/no): ").strip().lower()
            if response not in ['yes', 'y']:
                print("Cancelled.")
                sys.exit(0)

        # Execute renames
        print("\n🚀 Executing renames...\n")
        count = renamer.execute_renames(results)

        print(f"\n{'='*80}")
        print(f"✅ {count} files renamed successfully!")
        print(f"{'='*80}\n")

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
