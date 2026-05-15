# Music Mastery

Um sistema completo de estudo de produções musicais. O objetivo é desenvolver a habilidade de ouvir e replicar as decisões de produção dos artistas de referência — analisando músicas com profundidade, registrando os insights em song logs, e aplicando o que foi aprendido diretamente no workflow de produção. O estudo não é uma tarefa separada: é parte do processo criativo.

---

## Claude's Role

Nesse projeto, o Claude é o sistema de conversão: recebe as notas brutas tiradas no Logic e gera o song log formatado via `song-log-generator`. Também acompanha o progresso semanal, identifica padrões recorrentes entre os logs, e garante que o estudo esteja sendo aplicado — não só registrado.

**Prime Directive:** Se uma sessão estiver passando sem gerar um log ou sem avançar na fila, nudge: *"Você estudou algo hoje — isso virou um log ou ficou nas notas do Logic?"*

---

## Process

1. **Escolher a música** — consultar o [[00 Queue/(C) Artist Study List]] e pegar a próxima sugestão da Study Queue, ou escolher livremente
2. **Escutar e anotar no Logic** — markers + bloco de notas interno, guiado pelo [[03 System/(C) Song Analysis Framework]]
3. **Gerar o song log** — colar as notas brutas e rodar o skill `song-log-generator`
4. **Salvar o log** — arquivo vai em `01 Song Logs/` com nome no formato `YYYY-MM-DD — Artista — Música.md`
5. **Atualizar o Artist Study List** — marcar o artista com `[~]` ou `[x]` e incrementar o contador de logs
6. **Atualizar os dois índices** — OBRIGATÓRIO após cada log gerado:
   - `(C) Song Logs Index.md` — adicionar linha na tabela (mais recente primeiro) com date, artista, música, gênero e key insight
   - `(C) Song Logs Index — Bullets Version.md` — adicionar seção em bullets (mais recente primeiro) com gênero, BPM, observações e "Roubei"
7. **Atualizar o Current Status** neste CLAUDE.md (contador de logs e data)
8. **Scan pré-sessão de produção** — revisar os últimos 3-5 logs antes de produzir para ativar os insights

---

## Folder Structure

```
Music Mastery/
├── CLAUDE.md              ← Você está aqui
├── COMMANDS.md            ← Skills e comandos disponíveis
├── 00 Queue/              ← Curriculum de artistas e Study Queue
│   └── (C) Artist Study List.md  ← Lista completa por gênero + sugestões de início
├── 01 Song Logs/          ← Logs completos de cada música analisada
├── 02 Insights & Patterns/← Padrões recorrentes identificados ao longo do tempo
├── 03 System/             ← Frameworks e referências reutilizáveis
│   └── (C) Song Analysis Framework.md
├── 04 Skills/             ← Skill markdown files
│   └── song-log-generator.md
└── 05 Attachments/        ← Imagens, prints, referências visuais
```

---

## Rules & Conventions

- **`(C)` prefix** — Arquivos criados pelo Claude levam prefixo `(C)`.
- **Editing rule** — Antes de editar qualquer arquivo sem prefixo `(C)`, pedir permissão.
- **Formato de nome dos logs** — `YYYY-MM-DD — Artista — Música.md` sem exceção.
- **Tracking semanal** — No review semanal do brain principal, incluir: quantas músicas estudei essa semana + qual foi o melhor insight aplicado em produção.

---

## Current Status

> **Last updated:** 2026-04-25
> **Status:** Ativo — 6 song logs gerados (Mac Miller — Self Care, 25/04 · Wizkid — Essence, 23/04 · Tyler the Creator — Sugar on My Tongue, 23/04 · Frank Ocean — Pink & White, 23/04 · Kanye West — Father, 22/04 · Lana Del Rey — Westcoast, 16/04). Sistema rodando.
