# 📚 Skill: Summarize Book (Smart PDF Summarizer)

**Invoque esta skill quando precisar resumir um livro em PDF.**

---

## 🎯 O que faz

Você envia um PDF (ou indica o caminho) e a skill:

1. **Detecta tamanho** do livro
2. **Escolhe estratégia automática:**
   - <100 pgs → Processa direto (Sonnet, melhor qualidade)
   - 100-250 pgs → Divide em chunks (Haiku barato + Sonnet consolidação)
   - >250 pgs → Pergunta se quer completo ou seletivo
3. **Otimiza tokens** (~40-60% mais barato que direto)
4. **Retorna 6 seções estruturadas:**
   - 📌 SINOPSE (resumo executivo)
   - 🎯 INSIGHTS PRINCIPAIS (8-10 conceitos)
   - 📝 RESUMO (narrativa enxuta)
   - 📖 TABELA (capítulos)
   - 🧠 QUIZ (12-15 perguntas com respostas ocultas)
   - 📚 RESUMO COMPLETO (análise detalhada)
5. **Salva tudo** em `00 Notes/Books/[Livro] - Resumo Completo.md`

---

## 🔧 Como usar

### **Invocação simples:**

```
/summarize-book seu_livro.pdf
```

Ou:

```
/summarize-book livro.pdf --model haiku
```

Ou:

```
/summarize-book livro.pdf --selective
```

---

## 📋 Fluxo automático da skill

```
1. Você invoca: /summarize-book livro.pdf
   ↓
2. Skill detecta tamanho do PDF
   ↓
3. Escolhe estratégia (direto / chunked / ask)
   ↓
4. Processa automaticamente com os modelos otimizados
   ↓
5. Consolidada em 6 seções estruturadas
   ↓
6. Salva em 00 Notes/Books/
   ↓
7. Retorna: "✅ Pronto! Resumo em [caminho]"
```

---

## 💾 Saída

Após executar, um arquivo é criado em:

```
00 Notes/Books/[Seu Livro] - Resumo Completo.md
```

Com todas as 6 seções prontas pra usar no Obsidian.

---

## 📊 Estratégias e custos

| Tamanho | Método | Modelos | Tokens | Tempo |
|---------|--------|---------|--------|-------|
| <100 pgs | DIRETO | Sonnet | 1-2k | 2-3 min |
| 100-250 pgs | CHUNKED | Haiku + Sonnet | 40-80k | 5-10 min |
| >250 pgs | ASK | Você escolhe | 100k+ | 10-20 min |

**Chunking economiza 40-60% vs. processamento direto.**

---

## 🎛️ Opções

```bash
# Forçar Haiku (mais barato, menos detalhe)
/summarize-book livro.pdf --model haiku

# Forçar Sonnet (melhor qualidade, mais caro)
/summarize-book livro.pdf --model sonnet

# Modo seletivo (pergunta se quer completo ou partes)
/summarize-book livro.pdf --selective
```

---

## 🌟 Features

- ✅ **Totalmente automático** — detecta e processa sozinho
- ✅ **Inteligente** — otimiza tokens automaticamente
- ✅ **Contexto rico** — divide bem, consolida bem
- ✅ **6 seções sempre** — estrutura consistente
- ✅ **Quiz incluído** — 12-15 perguntas geradas automaticamente
- ✅ **Salva pronto** — direto no Obsidian format
- ✅ **Reutilizável** — funciona com qualquer PDF

---

## 📝 Exemplo real

```
User: /summarize-book The_Art_of_Learning.pdf

System:
============================================================
📚 LIVRO: The_Art_of_Learning
📄 Páginas: 285
🧠 Tokens estimados: 78,540
============================================================
📊 Médio (285 pgs) — 6 chunks (Haiku) + consolidação (Sonnet)
============================================================

🔄 Processando 6 chunks com Haiku...
  📄 Chunk 1/6... ✅
  📄 Chunk 2/6... ✅
  📄 Chunk 3/6... ✅
  📄 Chunk 4/6... ✅
  📄 Chunk 5/6... ✅
  📄 Chunk 6/6... ✅

🔄 Consolidando com Sonnet...

✅ PRONTO! Resumo salvo em:
00 Notes/Books/The_Art_of_Learning - Resumo Completo.md

[Arquivo contém as 6 seções estruturadas]
```

---

## 🚀 Próximos passos

1. **Envie um PDF** (qualquer tamanho)
2. **Invoque:** `/summarize-book seu_livro.pdf`
3. **Aguarde:** Skill processa automaticamente
4. **Abra em Obsidian:** Tudo estruturado e pronto!

---

**Skill criada em:** `/05 Skills/book-summarizer-skill.md`

**Invoke com:** `/summarize-book`
