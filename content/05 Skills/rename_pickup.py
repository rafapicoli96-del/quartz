#!/usr/bin/env python3
"""
Pickup Music Track Renamer
Renomeia tracks dos cursos FUNK BASS e ROCK BASS para o formato padrão.

Uso:
    python3 rename_pickup.py /path/to/folder

Formato de saída:
    Bass-LP-08-Funk-G#-D#-Track_Description-BPM-Key[-Ex#][-v2].wav
    Bass-LP-09-Rock-G#-D#-Track_Description-BPM-Key[-Ex#][-v2].wav

Padrões suportados:
    - ROCK BASS: Bass-LP-09-Rock_Description_Key_BPM_G#D#.wav
    - FUNK BASS: FUNK_BASS_G#_D#_Description_Key_BPM.wav
    - Exercícios: Ex1, Ex2, Ex3, Jam, track_1, track_2, track_3, Exercise 1, etc
    - Versões: v2, V2
"""

import os
import re
import sys

def parse_rock_bass(filename):
    """Parse ROCK BASS files: Bass-LP-09-Rock_..._G#D#"""
    base = os.path.splitext(filename)[0]

    if 'Dont' in base or 'dont' in base:
        return None

    # Remove prefix
    clean = re.sub(r'^Bass[-_]LP[-_]\d+[-_](?:Funk|Rock)[-_]', '', base)

    # Extract G#D#
    gd = re.search(r'G(\d)D(\d)', clean)
    if not gd:
        return None

    G, D = int(gd.group(1)), int(gd.group(2))

    # Extract BPM and KEY
    match = re.search(r'_([A-G]#?m?(?:aj)?)_(\d{2,3})(?:_|$)', clean)
    if not match:
        match = re.search(r'_(\d{2,3})_([A-G]#?m?(?:aj)?)(?:_|$)', clean)
        if match:
            bpm, key = match.group(1), match.group(2)
        else:
            return None
    else:
        key, bpm = match.group(1), match.group(2)

    # Extract exercise
    ex = None
    for pattern, label in [(r'Ex1', 'Ex1'), (r'Ex2', 'Ex2'), (r'Ex3', 'Ex3'),
                           (r'[Jj]am', 'Jam'), (r'track[_\s]?1', 'Ex1'),
                           (r'track[_\s]?2', 'Ex2'), (r'track[_\s]?3', 'Ex3')]:
        if re.search(pattern, clean, re.I):
            ex = label
            break

    v2 = bool(re.search(r'\bv2\b', clean, re.I))

    # Extract description
    bpm_key_pattern = f'_{key}_{bpm}|_{bpm}_{key}'
    match_pos = re.search(bpm_key_pattern, clean)
    if not match_pos:
        return None

    desc = clean[:match_pos.start()].strip('_\- ')

    return {'G': G, 'D': D, 'desc': desc, 'bpm': bpm, 'key': key, 'ex': ex, 'v2': v2} if desc else None

def parse_funk_bass(filename):
    """Parse FUNK BASS files: FUNK_BASS_G#_D#_Description_Key_BPM"""
    base = os.path.splitext(filename)[0]

    if 'Dont' in base or 'dont' in base:
        return None

    # Extract G#_D#
    gd = re.search(r'G(\d)_D(\d)', base)
    if not gd:
        return None

    G, D = int(gd.group(1)), int(gd.group(2))

    # Find BPM
    bpm_match = re.search(r'_(\d{2,3})(?:_|$)', base)
    if not bpm_match:
        return None

    bpm = bpm_match.group(1)

    # Everything between G#_D# and BPM
    after_gd = re.sub(r'^.*?G\d_D\d_', '', base)
    before_bpm = re.sub(f'_{bpm}.*$', '', after_gd)

    # Extract key (support mi, m, maj)
    key_match = re.search(r'_([A-G](?:-[A-G])?#?(?:mi|m)?(?:aj)?)(?:_|$)', before_bpm)
    if not key_match:
        return None

    key = key_match.group(1)

    # Description
    desc_match = re.search(rf'^(.+?)_{re.escape(key)}$', before_bpm)
    if not desc_match:
        return None

    desc = desc_match.group(1).strip('_')

    # Extract exercise
    ex = None
    for pattern, label in [(r'Ex1', 'Ex1'), (r'Ex2', 'Ex2'), (r'Ex3', 'Ex3'),
                           (r'[Jj]am', 'Jam'), (r'track[_\s]?1', 'Ex1'),
                           (r'track[_\s]?2', 'Ex2'), (r'track[_\s]?3', 'Ex3'),
                           (r'[Ee]xercise\s+1', 'Ex1'), (r'[Ee]xercise\s+2', 'Ex2'),
                           (r'[Ee]xercise\s+3', 'Ex3')]:
        if re.search(pattern, base, re.I):
            ex = label
            break

    v2 = bool(re.search(r'\bv2\b', base, re.I))

    return {'G': G, 'D': D, 'desc': desc, 'bpm': bpm, 'key': key, 'ex': ex, 'v2': v2} if desc else None

def generate_new_name(filename, parsed, prefix):
    """Generate new filename from parsed data"""
    parts = [f"G{parsed['G']}", f"D{parsed['D']}", parsed['desc'],
             parsed['bpm'], parsed['key']]

    if parsed.get('ex'):
        parts.append(parsed['ex'])

    if parsed.get('v2'):
        parts.append('v2')

    ext = os.path.splitext(filename)[1]
    return f"{prefix}-{'-'.join(parts)}{ext}"

def process_folder(folder_path):
    """Process all audio files in folder"""
    audio_files = []

    # Determine course and prefix
    if 'FUNK BASS' in folder_path:
        course, prefix = 'FUNK', 'Bass-LP-08-Funk'
        parser = parse_funk_bass
    elif 'ROCK BASS' in folder_path:
        course, prefix = 'ROCK', 'Bass-LP-09-Rock'
        parser = parse_rock_bass
    else:
        print("❌ Pasta deve conter 'FUNK BASS' ou 'ROCK BASS'")
        return

    # Collect files
    for root, dirs, files in os.walk(folder_path):
        for filename in sorted(files):
            if filename.endswith(('.wav', '.mp3')) and not filename.startswith('.'):
                audio_files.append({
                    'path': os.path.join(root, filename),
                    'filename': filename
                })

    # Parse and rename
    renames = []
    skipped = 0
    errors = 0

    for file_info in audio_files:
        parsed = parser(file_info['filename'])

        if parsed is None:
            if 'Dont' in file_info['filename'] or 'dont' in file_info['filename']:
                skipped += 1
            else:
                errors += 1
            continue

        new_name = generate_new_name(file_info['filename'], parsed, prefix)
        renames.append({
            'old_path': file_info['path'],
            'old_name': file_info['filename'],
            'new_name': new_name
        })

    # Execute renames
    print(f"\n{'='*100}")
    print(f"Renomeando {course} BASS")
    print(f"{'='*100}\n")
    print(f"📋 Prontos: {len(renames)} | ⏭️ Pulados: {skipped} | ❌ Erros: {errors}\n")

    success = failed = 0
    for r in renames:
        try:
            new_path = os.path.join(os.path.dirname(r['old_path']), r['new_name'])
            os.rename(r['old_path'], new_path)
            success += 1
        except Exception as e:
            failed += 1
            print(f"❌ {r['old_name']}: {e}")

    print(f"\n{'='*100}")
    print(f"✅ Renomeados: {success} | ❌ Falhados: {failed} | ⏭️ Pulados: {skipped}")
    print(f"{'='*100}\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3 rename_pickup.py /path/to/FUNK_BASS_or_ROCK_BASS")
        sys.exit(1)

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print(f"❌ Pasta não encontrada: {folder}")
        sys.exit(1)

    process_folder(folder)
