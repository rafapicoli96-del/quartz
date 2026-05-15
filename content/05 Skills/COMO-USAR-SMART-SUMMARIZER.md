# 📚 Como Usar o Smart Book Summarizer

**Sistema completo para transformar qualquer PDF em um resumo estruturado automaticamente.**

---

## ⚡ Quick Start (30 segundos)

```bash
# 1. Coloque seu PDF em qualquer lugar
# 2. Rode:
python3 ~/Desktop/RAFA\ AI\ BRAIN/05\ Skills/smart-book-summarizer.py seu_livro.pdf

# 3. Pronto! Resumo salvo em: 00 Notes/Books/seu_livro - Resumo Completo.md
```

---

## 🎯 O que esperar

### ✅ O sistema faz automaticamente:

1. **Detecta tamanho do PDF**
2. **Escolhe estratégia otimizada:**
   - Livro pequeno? → Processa direto
   - Livro médio? → Divide em chunks baratos, consolida bem
   - Livro grande? → Pergunta o que você quer fazer
3. **Cria 6 seções:**
   - SINOPSE (resumo executivo)
   - INSIGHTS (conceitos principais)
   - RESUMO (narrativa)
   - TABELA (capítulos)
   - QUIZ (perguntas com respostas ocultas)
   - RESUMO COMPLETO (análise detalhada)
4. **Salva pronto pra usar** em `00 Notes/Books/`

---

## 📖 Exemplos de uso

### Exemplo 1: Livro pequeno (80 páginas)

```bash
$ python3 smart-book-summarizer.py pequeno_livro.pdf

✅ Pequeno (80 pgs) — processamento direto
Método: DIRECT
🔄 Processando com Sonnet...
✅ PRONTO! Resumo salvo em: 00 Notes/Books/pequeno_livro - Resumo Completo.md
```

**Resultado:** Resumo completo em 2-3 minutos, super detalhado.

---

### Exemplo 2: Livro médio (180 páginas)

```bash
$ python3 smart-book-summarizer.py livro_medio.pdf

✅ Médio (180 pgs) — 4 chunks (Haiku) + consolidação (Sonnet)
Método: CHUNKED
🔄 Processando 4 chunks com Haiku...
  📄 Chunk 1/4... ✅
  📄 Chunk 2/4... ✅
  📄 Chunk 3/4... ✅
  📄 Chunk 4/4... ✅
🔄 Consolidando com Sonnet...
✅ PRONTO! Resumo salvo em: 00 Notes/Books/livro_medio - Resumo Completo.md
```

**Resultado:** Resumo bem balanceado, 40% mais barato que direto, em 5-10 minutos.

---

### Exemplo 3: Livro grande (320 páginas)

```bash
$ python3 smart-book-summarizer.py livro_grande.pdf

⚠️ Grande (320 pgs) — necessário escolher seções ou aceitar custo alto
Método: SELECTIVE

Escolha uma opção:
1. Processar completo (pode gastar muitos tokens)
2. Especificar capítulos/páginas

Opção (1 ou 2): 1

🔄 Processando completo...
✅ PRONTO! Resumo salvo em: 00 Notes/Books/livro_grande - Resumo Completo.md
```

**Resultado:** Resumo completo, mas com custo maior (~150-200k tokens).

---

## 🔧 Opções avançadas

### Forçar modelo (padrão é automático)

```bash
# Usar apenas Sonnet (mais detalhado, mais caro)
python3 smart-book-summarizer.py livro.pdf --model sonnet

# Usar Haiku (mais rápido, mais barato, menos detalhes)
python3 smart-book-summarizer.py livro.pdf --model haiku
```

### Modo seletivo

```bash
# Pergunta se quer completo ou seletivo (útil para livros muito grandes)
python3 smart-book-summarizer.py livro.pdf --selective
```

---

## 💾 Onde fica o resultado

Após rodar, o arquivo é salvo em:

```
~/Desktop/RAFA AI BRAIN/00 Notes/Books/[Seu Livro] - Resumo Completo.md
```

Abra no Obsidian e pronto! Tem tudo formatado em 6 seções prontas pra usar.

---

## 💰 Custos estimados (tokens)

| Tamanho | Páginas | Método | Tokens | Tempo | Custo Relativo |
|---------|---------|--------|--------|-------|--------|
| 🟢 Pequeno | <100 | Direto (Sonnet) | 1-2k | 2-3 min | $0.01-0.02 |
| 🟡 Médio | 100-250 | Chunked (Haiku+Sonnet) | 40-80k | 5-10 min | $0.20-0.40 |
| 🔴 Grande | >250 | Ask user | 100k+ | 10-20 min | $0.50+ |

**Nota:** Preços são aproximados. Chunking (Haiku) economiza 40-60% vs. Sonnet direto.

---

## ✨ Features

- ✅ **Automático:** Detecta tamanho, escolhe estratégia, processa
- ✅ **Inteligente:** Usa Haiku (barato) + Sonnet (bom) = otimização
- ✅ **Estruturado:** 6 seções sempre, mesmo formato
- ✅ **Reutilizável:** Funciona com qualquer PDF
- ✅ **Pronto pra usar:** Salva direto no Obsidian format
- ✅ **Com Quiz:** Cria 12-15 perguntas automaticamente

---

## 🐛 Troubleshooting

**"pypdf não instalado"**
```bash
pip install pypdf
```

**"ANTHROPIC_API_KEY não definida"**
```bash
export ANTHROPIC_API_KEY="sk-..."
```

**"Erro ao processar PDF"**
- Verifique se o PDF não está corrompido
- Tente outro PDF primeiro pra descartar problema do script

**Script está lento**
- Normal! Chunking leva tempo mesmo
- Um livro de 200 pgs leva 5-10 minutos
- Não cancele (Ctrl+C), deixa rodar

**Quero fazer só partes do livro**
- Use `--selective` e escolha opção 2
- Ou divida o PDF em 2-3 arquivos menores antes

---

## 📝 Fluxo completo

```
1. Você: "Tenho um PDF, preciso de resumo"
   ↓
2. Smart Summarizer: "Deixa eu ver o tamanho..."
   ↓
3. Script detecta: "200 páginas = divido em chunks com Haiku"
   ↓
4. Processa: Chunk 1, Chunk 2, Chunk 3, Chunk 4 (Haiku — rápido e barato)
   ↓
5. Consolida: Usa Sonnet pra juntar tudo em 6 seções (qualidade alta)
   ↓
6. Salva: 00 Notes/Books/seu_livro - Resumo Completo.md
   ↓
7. Você abre no Obsidian: PRONTO! 📚
```

---

## 🚀 Próximos passos

1. **Primeiro teste:** comece com um livro pequeno (<100 pgs)
2. **Veja o resultado:** abra em Obsidian, cheque as 6 seções
3. **Ajuste conforme necessário:** quer mais quiz? mais resumo? fácil ajustar o script
4. **Use sempre:** qualquer PDF novo, rode o script!

---

## 📞 Dúvidas?

Ver o arquivo completo: `/05 Skills/SMART-BOOK-SUMMARIZER-README.md`

Arquivo do script: `/05 Skills/smart-book-summarizer.py`
