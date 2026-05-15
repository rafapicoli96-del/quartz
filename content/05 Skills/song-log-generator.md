# Skill: Song Log Generator

Generate a structured, formatted vault log from Rafa's freeform analysis notes written in Logic Pro's notes block.

## When to Use

- After any music study/analysis session in Logic Pro
- Rafa pastes his raw notes from Logic and asks Claude to generate the log
- Trigger phrase: "generate song log", "cria o song log", or similar

---

## How It Works

1. Rafa provides his raw notes from Logic Pro (or pastes them directly)
2. **Buscar o link do Spotify:** usar o script em `05 Skills/Spotify/spotify_playlist.py` para obter o link exato da faixa. **Double check obrigatório:** conferir que o nome do artista E o título retornados pela API batem exatamente com a música do song log — músicas com nomes parecidos podem retornar um resultado errado. Se o resultado não bater, tentar queries alternativas até confirmar:
   ```bash
   cd "/Users/rafa/Desktop/RAFA AI BRAIN/05 Skills/Spotify" && python3 - <<'EOF'
   import sys; sys.path.insert(0, ".")
   from spotify_playlist import load_creds, get_access_token, search_track
   creds = load_creds(); token = get_access_token(creds)
   result = search_track(token, "Artist - Song Title")
   if result: print(f"https://open.spotify.com/track/{result['id']}")
   EOF
   ```
3. Claude generates the **3-layer song log** (see template below):
   - **📝 Rascunho Original** — raw notes preserved as-is
   - **⚡ Song Log Enxuto** — quick reference (TLDR for scanning before production)
   - **📋 Song Log Completo** — full structured log with all sections
3. Save to `03 Projects/Music Mastery/01 Song Logs/` with filename: `[YYYY-MM-DD] — [Artist] — [Song].md`
4. Update the Artist Study List to track progress
5. Remind Rafa to scan the last 3-5 logs before his next production session and mark "Applied?" when he uses the insight

---

## Claude's Additional Insights (Song Log Completo Only)

In the **📋 Song Log Completo** section, add a **"🧠 Claude's Notes"** section with relevant insights from your own knowledge about the song, artist, or production. This enriches the log beyond what Rafa observed in the session.

Include anything genuinely useful — skip anything generic or obvious. Examples of what to add:

- **Production context:** Who produced it, what gear/plugins/techniques they're known for using, what made this track innovative at the time
- **Technical details:** Specific production techniques used that Rafa may not have caught
- **Creative decisions:** Behind-the-scenes info about why certain choices were made, what the artist/producer said about the track
- **Connections:** How this track connects to other music, what it influenced or was influenced by, genre context
- **What to listen for on a second pass:** Things Rafa might have missed that are worth going back for

**Rule:** Only add what you're confident about. If uncertain, flag it with *"(not 100% sure — worth verifying)"*. Never fabricate production details.

---

## Estudo Ativo — Regras de Preenchimento

Ao gerar o checklist de Estudo Ativo:

1. **Se o rascunho já tiver perguntas/tarefas explícitas** (ex: "como eu faria essa bateria?", "samplear isso") → extrair e transformar em checklist
2. **Se o rascunho não tiver tarefas, ou elas forem vagas** → Claude sugere itens baseado nas observações. Para cada elemento que chamou atenção (um som específico, uma decisão de mix, um acorde, um processamento), propor: *"Replicar [elemento] no DAW"* ou *"Criar preset de [elemento]"*. Focar em coisas concretas e replicáveis, não abstrações.
3. **Sinalizar itens sugeridos:** adicionar `← sugestão` ao lado dos itens que Claude criou (não vieram do rascunho) para Rafa saber quais são seus e quais são sugestões
4. **Não exagerar:** máximo de 6-8 itens. Priorizar o que tem maior ROI de aprendizado (sons únicos, decisões contraintuitivas, técnicas reutilizáveis)

---

## What to Do With Thin Notes

If the raw notes are short or vague (low-inspiration day), still follow the 3-layer structure:
- **📝 Rascunho Original** — paste what's there, even if short
- **⚡ Song Log Enxuto** — distill to absolute essentials; it's OK if this is brief
- **📋 Song Log Completo** — Claude's Notes can be fuller even when Rafa's observations are thin (that's fine — this section can carry the load)
- Never fabricate observations in the Completo section that weren't in Rafa's notes, but Claude's independent insights are welcome
- Add a gentle note: *"Sessão mais curta — revisitar essa música num dia mais inspirado?"*

---

## Song Log Template (3-Layer Structure)

```markdown
# [Artist] — [Song Title]

**Date:** [YYYY-MM-DD] | **Genre:** [Genre] | **Listen count:** 1
**Spotify:** [Ouvir no Spotify](https://open.spotify.com/track/TRACK_ID)

---

## 📝 Rascunho Original

```
[Paste Rafa's raw notes from Logic exactly as written — preserve the stream of consciousness]
```

---

## 🎯 Estudo Ativo

> Coisas para replicar ou investigar no DAW durante essa sessão. Marque conforme for fazendo.

- [ ] [Elemento 1 para replicar — ex: "Replicar groove da bateria (menos de 2 min)"]
- [ ] [Elemento 2 — ex: "Criar preset de vocal pad rápido"]
- [ ] [Elemento 3]

---

## ⚡ Song Log Enxuto

[Quick reference version — 1-2 sentences per section. What Rafa needs to see at a glance before the next production session]

**Vibe:** [1-2 lines]
**Production Stars:**
- [Standout element 1]
- [Standout element 2]
- [Standout element 3]
**Mix Decision:** [1-2 lines — any smart arrangement choice]
**The Steal:** 
1. [Actionable takeaway 1]
2. [Actionable takeaway 2]

---

## 📋 Song Log Completo

### Vibe & Feeling
[What emotion/vibe the track creates and what specifically produces it]

### Structure & Arrangement
[Section map, transitions, arrangement arc]

### Production & Sound Design
[Standout sounds, unexpected choices, textures worth noting]

### Mix & Space
[Frequency, dynamics, stereo field, depth observations]

### Patterns & References
[Recurring patterns, influences, comparisons to other artists/tracks]

---

### 🧠 Claude's Notes
[Insights Claude adds from its own knowledge: production context, technical details, behind-the-scenes info, connections to other music, what to listen for on a second pass]

---

### ⭐ The Steal (2 insights)

> **#1 — [Short title]:**
> **[The concrete thing to apply — in one clear sentence]**

Aplicação prática: [How Rafa will implement this in his own work]

> **#2 — [Short title]:**
> **[The concrete thing to apply — in one clear sentence]**

Aplicação prática: [How Rafa will implement this in his own work]

---

**Applied in a production?** Not yet
<!-- When applied, update to: Yes → [Project name] on [date] -->
```

---

## After Creating the Log

### 1. Update the Artist Study List
At `03 Projects/Music Mastery/00 Queue/(C) Artist Study List.md`:
- Find the artist in the list and increment the song count
- If the artist isn't on the list yet, add them to the appropriate genre section
- Update status: `[ ]` → `[~]` if first song, keep `[~]` until 3+ songs, then `[x]`

### 2. Update BOTH Song Logs Indexes (Automatic — ALWAYS do both)

**Index #1 — Tabela (Compact)** at `03 Projects/Music Mastery/(C) Song Logs Index.md`:
- Add a new row at the TOP of the table (most recent first)
- Format: Date | Artist | [Song](spotify_url) | Genre | Key Insight (2-3 lines describing what stood out)
- The song title must be a clickable Spotify link

**Index #2 — Bullets (Detailed)** at `03 Projects/Music Mastery/(C) Song Logs Index — Bullets Version.md`:
- Add a new section at the TOP with format:
  ```
  ## YYYY-MM-DD — Artist — **Song**
  **Gênero:** [Genre] | **Spotify:** [Ouvir](spotify_url)
  
  **O que me chamou atenção:**
  - [Bullet 1: key insight]
  - [Bullet 2: production detail]
  - [Bullet 3: mix decision or arrangement choice]
  - [Bullet 4: specific technique to steal]
  
  **Roubei:** [1-2 lines on what Rafa will apply]
  ```

**Important:** Keep BOTH lists in sync — they must always have the same songs, just different formats.

### 3. Remind Rafa
- Before his next production session, scan the Song Logs Index (either format) to activate insights
- Mark "Applied?" in the individual log when he uses the insight in actual production
