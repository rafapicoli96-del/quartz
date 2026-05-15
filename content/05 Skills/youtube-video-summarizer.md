# Skill: YouTube Video Summarizer

Summarize any YouTube video into a structured Obsidian note with quiz, quick summary, complete deep-dive, and personal connection. **The complete summary must be thorough, accurate, and follow the video's narrative structure — not fabricated.**

## When to Use

- Rafa posts a YouTube link and asks for a summary, note, or resumo
- Trigger: qualquer link do YouTube com pedido de resumo, nota, ou "cria uma note"

---

## Critical Requirements

⚠️ **ANTES DE COMEÇAR, LEIA ISSO:**

1. **Completude = Não-Fabricação**
   - Não invente conteúdo, exemplos ou seções que não estejam no vídeo
   - Se uma seção é mencionada mas rápida, capture a essência sem expandir
   - Se há um conceito complexo, explique com detalhe BASEADO no que foi dito
   - Dúvida? Transcreva mais literal, não sintetize demais

2. **Ordem do Vídeo = Estrutura do Resumo**
   - O resumo completo DEVE seguir a ordem exata do vídeo
   - Não reorganize seções por "lógica" ou "clareza" — respeite o fluxo narrativo do criador
   - Isso permite que o usuário leia junto com o vídeo rodando (referência paralela)
   - Se o vídeo tem digressões ou exemplos fora de ordem, capture na ordem que aparecem

3. **Estrutura = Acompanhável**
   - Use headers (### ou ####) para cada seção PRINCIPAL do vídeo
   - Se uma seção tem múltiplos tópicos ou exemplos, use subheaders
   - O objetivo é permitir "seguir" o vídeo pelo resumo sem se perder

4. **Detalhamento = Proporcional ao Vídeo**
   - Se o vídeo dedica 2 minutos a um exemplo, não escreva 5 parágrafos sobre ele
   - Se o vídeo dedica 10 minutos a um conceito, detalhe adequadamente
   - Balance entre completude e proporcionalidade

5. **Linguagem = Fidelidade**
   - Use citações diretas quando o criador faz declarações-chave
   - Traduza o significado com suas palavras APENAS para clareza, não reinterpretação
   - Se há uma metáfora ou framework importante (ex: "3 níveis", "1% vs 99%"), preserve exatamente como foi apresentado

---

## Step-by-Step Process

### 1. Extract transcript + metadata

Run these two commands in parallel:

**Get channel name (CRITICAL — never skip this):**
```bash
/Users/rafa/Library/Python/3.9/bin/yt-dlp --print "%(channel)s" --skip-download "URL"
```
> ⚠️ If `%(channel)s` returns `NA`, fall back to `%(uploader)s`. If still NA, use `%(uploader_id)s`. Never infer or guess the channel name from the content style.

**Get transcript:**
```bash
/Users/rafa/Library/Python/3.9/bin/yt-dlp --write-auto-sub --skip-download --sub-lang pt,en --cookies-from-browser chrome -o "/tmp/yt_summary_%(id)s" "URL"
```

Then clean the VTT **preserving timestamps** — needed for section mapping later:
```python
import re

with open("/tmp/yt_summary_[VIDEO_ID].pt.vtt", "r") as f:  # try .en.vtt if pt not available
    content = f.read()

# Build list of (timestamp, text) entries
lines = content.split('\n')
current_timestamp = "00:00:00"
entries = []
current_text = []

for line in lines:
    stripped = line.strip()
    if re.match(r'^\d{2}:\d{2}:\d{2}\.\d{3}', stripped):
        m = re.match(r'^(\d{2}:\d{2}:\d{2})', stripped)
        if m:
            if current_text:
                entries.append((current_timestamp, ' '.join(current_text)))
                current_text = []
            current_timestamp = m.group(1)
        continue
    if stripped.startswith(('WEBVTT', 'Kind:', 'Language:')) or not stripped: continue
    clean = re.sub(r'<[^>]+>', '', stripped).strip()
    if clean:
        current_text.append(clean)

if current_text:
    entries.append((current_timestamp, ' '.join(current_text)))

# Full transcript (for summarization)
full_text = ' '.join(text for _, text in entries)
print(full_text)

# entries list is also used in step 1b below for timestamp mapping
```

**1b. Map timestamps to sections (run after drafting the Resumo Completo):**

Once the section titles are defined, search for each section's opening phrase in `entries` to get its timestamp:

```python
# For each section, define a keyword that appears near its start
sections = {
    "Section Title": ["keyword phrase", "alternative phrase"],
    # ...
}

for section, keywords in sections.items():
    for ts, text in entries:
        if any(kw.lower() in text.lower() for kw in keywords):
            print(f"{section}: {ts}")
            break
```

Use the found timestamp as `[MM:SS]` appended to the section header (see template below).

---

### 2. Determine subfolder

Based on video topic, place the note in the most relevant subfolder of `00 Notes/Vídeos/`. Create the subfolder if it doesn't exist. Existing subfolders for reference:
- `ADHD/`
- `Espiritualidade & Consciência/`
- `Neurociência & Performance/`
- (create new if needed — e.g., `Produtividade/`, `Música/`, `Finanças/`, etc.)

---

### 3. Generate the note

Filename: `[Topic — Short Descriptive Title].md`

---

## Note Template

```markdown
# [Video Title]

**Fonte:** [full YouTube URL]
**Canal:** [channel name from yt-dlp — NEVER guess]
**Tags:** #[topic1] #[topic2] #[topic3]

---

## 🎯 Estudo Ativo

> Coisas concretas para implementar o que foi ensinado neste vídeo no dia a dia.

**1. [Ação concreta]**
[Descrição de como implementar — específica, acionável, contextualizada para o Rafa]

**2. [Ação concreta]**
[...]

[Quantos itens forem necessários: 2 para vídeos simples, até 10–15 para vídeos densos com muitos conceitos aplicáveis. Cada item deve ser uma ação real, não um resumo do conceito.]

---

## 🧠 Quiz

> Tente responder antes de revelar. Respostas colapsadas.

---

**1. [Pergunta]**

> [!NOTE]- Resposta
> [Resposta completa]

---

**2. [Pergunta]**

> [!NOTE]- Resposta
> [Resposta completa]

---

[... 10 perguntas mínimo. Se o vídeo for denso, adicionar até 15.]

---

---

## ⚡ Resumo Rápido

> Bater o olho e lembrar do que se trata.

**Em uma linha:** [O que o vídeo diz em 1 frase]

**Main takeaways:**
- [Takeaway 1 — claro e direto]
- [Takeaway 2]
- [Takeaway 3]
- [Takeaway 4]
- [Takeaway 5 se houver]

---

## 📋 Resumo Completo

### ⚠️ INSTRUÇÕES CRÍTICAS PARA ESTA SEÇÃO:

1. **ESTRUTURA: CRONOLÓGICA ou TEMÁTICA — detectar o formato primeiro**

   **Vídeos lineares** (tutoriais, aulas, documentários, apresentações): seguir ordem cronológica estrita. Cada seção = uma parte do vídeo. O usuário consegue ler junto com o vídeo rodando sem se perder.

   **Vídeos conversacionais** (podcasts, entrevistas, sessões de coaching, debates): organizar tematicamente. Nesses formatos o mesmo tema aparece, some e volta várias vezes — forçar cronologia resulta num resumo fragmentado e difícil de usar. Agrupe por tema/conceito, mesmo que o vídeo volte ao assunto em momentos diferentes.

   > **Regra prática:** se os timestamps das seções ficam fora de ordem crescente, é sinal de que o vídeo é conversacional e a organização temática é a certa. Os timestamps indicam *onde o tema aparece pela primeira vez*, não que todo o conteúdo da seção está naquele ponto.

   Independente do formato: não reorganize por "lógica" ou "clareza" artificiais — respeite o fluxo real do conteúdo.

2. **SEJA COMPLETÍSSIMO — NÃO FABRIQUE**
   - Cubra TUDO: contexto, exemplos, histórias, nuances, citações, dados
   - Se não está no vídeo, não escreva (mesmo que "melhoraria" a explicação)
   - Dúvida sobre algo? Releia a transcrição 2x antes de expandir
   - Proporção importa: 2 min no vídeo ≈ 2 parágrafos; 10 min ≈ detalhado

3. **USE ESTRUTURA CLARA = ACOMPANHÁVEL**
   - Headers ### para cada seção PRINCIPAL do vídeo
   - Subheaders #### para tópicos dentro de uma seção
   - Objetivo: usuário consegue "acompanhar" junto com vídeo rodando, sem se perder

4. **CITAÇÕES DIRETAS quando relevante**
   - Use quotes para afirmações importantes do criador
   - Especialmente para definições, conceitos-chave, ou frameworks
   - Preserve exatamente como foi dito (não reinterprete)

5. **FIDELIDADE AO CONTEÚDO**
   - Se há uma metáfora (ex: "foguete"), preserve exatamente
   - Se há um framework (ex: "3 níveis"), use exatamente como apresentado
   - Traduza APENAS para clareza, nunca para "melhorar"

[Resumão aprofundado, seguindo exatamente a ordem do vídeo. Usar headers ### e #### para organizar. Ser completo = não fabricado. Objetivo: entendimento real do conteúdo, permitindo leitura paralela com o vídeo.]

> **💡 Dica:** Clique no timestamp `[MM:SS]` ao lado de cada tópico para pular direto para aquela parte do vídeo no YouTube.

### Nome da Seção `[MM:SS]`

---

## 🔗 Como se Conecta a Mim

[NOTA: Esta seção é SEPARADA do Resumo Completo. Aqui SIM você analisa pessoalmente como o conteúdo se conecta aos objetivos, padrões e vida do Rafa. Use contexto completo: carreira musical, meta de renda (R$20k/mês), ADHD, sistemas de produtividade, padrões psicológicos, relacionamento, saúde. Não só ADHD — use o que for mais relevante. Ser específico e honesto. Evitar conexões forçadas.]
```

---

## Rules

- **NUNCA adicionar conteúdo ao Today.md.** O output desta skill é sempre e exclusivamente uma nova note em `00 Notes/Vídeos/[subfolder]/`. Nenhum resumo, extrato ou bloco vai para o Today.md.
- **Canal:** sempre usar o valor retornado pelo yt-dlp (`%(channel)s` → `%(uploader)s` → `%(uploader_id)s`). Nunca inventar.
- **Estudo Ativo:** lista de ações concretas e implementáveis derivadas do vídeo. Quantidade proporcional à densidade do vídeo (mínimo 2, sem limite máximo). Cada item deve ser uma ação real — não um resumo de conceito. Contextualizar para a vida do Rafa quando relevante (música, ADHD, rotina, metas de renda).
- **Quiz:** mínimo 10 perguntas. Se o vídeo for denso (muitos conceitos, estudo científico, framework complexo), ir até 15.
- **Resumo Rápido:** máximo 5-6 bullets. Só o essencial. Quem lê em 30 segundos precisa entender o core.
- **Resumo Completo:** sem limite de tamanho — o objetivo é profundidade real E fidelidade à ordem. SEMPRE verificar: ordem segue vídeo? Nada foi fabricado? Está acompanhável?
- **Timestamps:** OBRIGATÓRIO em todos os headers `###` do Resumo Completo. Formato: `### Nome da Seção \`[MM:SS]\``. Usar o script de mapeamento do step 1b. Nenhuma seção pode ficar sem timestamp.
- **Como se Conecta a Mim:** específico e honesto. Evitar conexões forçadas — se o conteúdo não se conecta muito, dizer isso claramente em vez de inventar relevância.
- **Subfolder:** sempre categorizar por tema. Organizar por criador/canal como subpasta se houver múltiplos vídeos do mesmo criador. Ex: `00 Notes/Vídeos/Leon Hendrix/` ou `00 Notes/Vídeos/Produtividade/`
- **Tags:** 2-4 tags temáticas relevantes (sem tag de canal ou autor).

---

## ✅ Quality Checklist (ANTES de entregar a nota)

Antes de finalizar a note, verificar:

- [ ] **Estudo Ativo:** seção presente antes do Quiz? Itens são ações reais (não resumos de conceito)? Quantidade proporcional ao vídeo?
- [ ] **Ordem:** Resumo Completo segue EXATAMENTE a ordem do vídeo (verificar contra transcrição)
- [ ] **Completude:** Nenhuma seção/exemplo/história importante está faltando
- [ ] **Não-Fabricação:** Nenhum parágrafo foi adicionado sem estar no vídeo original
- [ ] **Acompanhável:** Headers estão claros? Usuário consegue ler junto com vídeo rodando?
- [ ] **Timestamps:** Todos os headers `###` do Resumo Completo têm timestamp `[MM:SS]`? Nenhum ficou sem?
- [ ] **Citações:** Conceitos-chave têm citações diretas onde relevante
- [ ] **Proporção:** Tempo dedicado a cada seção corresponde ao vídeo
- [ ] **Quiz:** Mínimo 10 perguntas? Baseadas em conceitos reais do vídeo?
- [ ] **Takeaways:** Os 5 main takeaways são realmente os principais?
- [ ] **Conexão Pessoal:** Está separada do resumo completo? É específica ao Rafa, não genérica?
- [ ] **Pasta/Tags:** Subfolder correto? Tags apropriadas?

Se algo falhar nesse checklist, corrigir ANTES de entregar a nota ao usuário.
