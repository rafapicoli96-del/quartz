# Skill: Pickup Track Renamer

Rename exported Pickup Music course tracks from whatever format they came out of to the standard naming convention.

## When to Use

- Rafa exported tracks for a Pickup course and needs to rename the batch
- Trigger phrases: "rename my pickup tracks", "renomear as tracks da pickup", "formatar nomes das tracks", or similar
- Rafa provides a folder path containing the audio files

## 📤 Shareable Version for Friends

If you want to share this system with your friends who also use Pickup:
- **Prompt for ChatGPT:** `PICKUP-RENAMER-PROMPT.txt`
- **Python script:** `rename_pickup_shareable.py`
- **Full guide:** `PICKUP-RENAMER-README.md`

See [PICKUP-RENAMER-README.md](PICKUP-RENAMER-README.md) for 3 ways to use (ChatGPT, Script, or Manual).

## Quick Start (2 formas)

### Opção A: Chamar Claude (rápido — 1-2 min)
```
"Rename my pickup tracks in /Users/rafa/Downloads/PICKUP rename/FUNK BASS"
```
Claude executa tudo automaticamente.

### Opção B: Usar o script direto (super rápido — 30s)
```bash
python3 ~/Desktop/RAFA\ AI\ BRAIN/05\ Skills/rename_pickup.py /path/to/folder
```
Exemplo:
```bash
python3 ~/Desktop/RAFA\ AI\ BRAIN/05\ Skills/rename_pickup.py /Users/rafa/Downloads/PICKUP\ rename/FUNK\ BASS
```

---

## Naming Convention

**Format:** `(course_prefix)-(Grade#)-(Day#)-(Track_Description)-(BPM)-(Key)-(exercise_optional)`

**Full example:** `LP-24-Interm_v2-G4-D5-Good_Times-85-Emi-Ex1`

### Component Rules

| Component | Rule | Example |
|-----------|------|---------|
| **Course prefix** | Fixed code for the course — ask if unknown | `LP-24-Interm_v2` |
| **Grade** | `G` + number | `G1`, `G3`, `G4` |
| **Day** | `D` + number | `D1`, `D5` |
| **Track description** | Words joined by `_` (not `-` or spaces) | `Good_Times`, `Expression`, `Slow_Blues` |
| **BPM** | Numeric only | `85`, `120` |
| **Key** | Tonal center, as written | `C`, `Emi`, `Bbmaj`, `Am` |
| **Exercise** | Optional — only include if present | `Ex1`, `Ex2`, `Jam` — omit entirely if absent |

**File extension:** Preserved exactly as-is (`.wav`, `.mp3`, `.aiff`, etc.)

---

## Known Course Prefixes

Update this list as new courses are encountered:

| Course | Prefix |
|--------|--------|
| LP 24 Intermediate v2 | `LP-24-Interm_v2` |
| Bass LP 09 Rock | `Bass-LP-09-Rock` |

> When Rafa mentions a course not listed here, ask for the prefix code and add it to this table.

---

## Workflow

### Step 1 — Get the folder path
Ask Rafa for the folder path if not already provided. Confirm you can see files in it.

```bash
ls "/path/to/folder"
```

### Step 2 — Identify the course prefix
- Check if Rafa mentioned the course name or prefix in his message
- Look at the filenames — if they hint at a course (e.g., "Intermed", "Beginner", "Adv"), try to match to the Known Course Prefixes table
- **If unclear or not in the table → ask before proceeding.** Never guess the prefix.

### Step 3 — Parse each filename

For every audio file in the folder, extract these components:

| Component | What to look for |
|-----------|-----------------|
| **Grade** | Patterns like `G4`, `G4D5`, `Grade 4`, `grade4` |
| **Day** | Patterns like `D5`, `G4D5`, `Day 5`, `day5` |
| **Description** | The text between the day info and BPM — strip "grade/day" markers, clean up spaces → `_` |
| **BPM** | A standalone number (typically 60–200) that isn't a grade or day number |
| **Key** | Text after BPM — typically a note name with optional quality (Am, Emi, G, Bb, Cmaj) |
| **Exercise** | `ex1`, `ex2`, `jam`, or similar at the end — capitalize to `Ex1`, `Ex2`, `Jam` |

**Edge cases:**
- If BPM is ambiguous (e.g., could be a grade number), look at position in the filename and value range
- If a component is completely missing and can't be inferred → flag that file, don't guess
- Description words get `_` between them — strip existing hyphens/spaces between description words and rejoin with `_`

### Step 4 — Show preview table

Before touching any file, display a full preview:

```
📋 Preview — 12 files found in /path/to/folder

  # | ORIGINAL NAME                          | NEW NAME
  --|----------------------------------------|------------------------------------------
  1 | Intermed G4D5 Good Times 85 Emi ex1.wav | LP-24-Interm_v2-G4-D5-Good_Times-85-Emi-Ex1.wav
  2 | Intermed G4D5 Good Times 85 Emi ex2.wav | LP-24-Interm_v2-G4-D5-Good_Times-85-Emi-Ex2.wav
  3 | G3D2 Slow Blues 120 Am.wav             | LP-24-Interm_v2-G3-D2-Slow_Blues-120-Am.wav
  ⚠️ | G2D1 ??? 95.wav                        | Could not parse description — flagged for review

Course prefix used: LP-24-Interm_v2
Files flagged for manual review: 1
```

Then ask: **"Tudo certo? Posso renomear? (s/n)"**

### Step 5 — Execute renames (only after confirmation)

For each confirmed file, run:

```bash
mv "/path/to/folder/ORIGINAL NAME.wav" "/path/to/folder/NEW NAME.wav"
```

Run all renames, then confirm:
```
✅ 11 arquivos renomeados com sucesso.
⚠️ 1 arquivo pulado (review manual): G2D1 ??? 95.wav
```

### Step 6 — Handle flagged files

For any files flagged during preview, show what was parsed and what's missing, and ask Rafa to provide the missing component(s) manually so you can complete the rename.

---

## Important Rules

- **NEVER rename without showing the full preview first and getting explicit confirmation**
- **NEVER guess the course prefix** — always ask if not known or not in the table
- If a filename can't be parsed confidently → flag it, don't skip silently and don't guess
- Preserve the file extension exactly (`.wav` stays `.wav`, `.aiff` stays `.aiff`)
- After adding a new course prefix, update the Known Course Prefixes table in this file
- If Rafa corrects a rename in the preview, apply the correction before executing

---

## Quick Reference — Input Format Examples

These are all valid inputs that should map to the same output:

| Input filename | Output |
|----------------|--------|
| `Intermed G4D5 Good Times 85 Emi ex1.wav` | `LP-24-Interm_v2-G4-D5-Good_Times-85-Emi-Ex1.wav` |
| `G4-D5 Good Times 85 Emi.wav` | `LP-24-Interm_v2-G4-D5-Good_Times-85-Emi.wav` |
| `grade4 day5 good times 85 emi jam.wav` | `LP-24-Interm_v2-G4-D5-Good_Times-85-Emi-Jam.wav` |
| `G1D3 Expression 100 C.wav` | `LP-24-Interm_v2-G1-D3-Expression-100-C.wav` |
