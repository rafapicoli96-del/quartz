# Smart Book Summarizer

**Sistema inteligente que transforma qualquer PDF em um resumo estruturado de 6 seções, automaticamente.**

---

## 📋 O que faz

Você manda um PDF de qualquer tamanho. O script:

1. **Detecta o tamanho** do livro
2. **Escolhe a estratégia automaticamente:**
   - **Pequeno** (<100 pgs) → Processa direto com Sonnet
   - **Médio** (100-250 pgs) → Divide em chunks (Haiku) + consolida (Sonnet)
   - **Grande** (>250 pgs) → Pergunta se quer completo ou seletivo

3. **Otimiza tokens:**
   - Usa Haiku (10x mais barato) para dividir livros grandes
   - Usa Sonnet (melhor qualidade) apenas para consolidação final
   - Economiza ~40-60% de tokens

4. **Retorna as 6 seções:**
   - SINOPSE
   - INSIGHTS PRINCIPAIS
   - RESUMO (narrativo)
   - TABELA DE CAPÍTULOS
   - QUIZ (com respostas ocultas)
   - RESUMO COMPLETO

---

## 🚀 Como usar

### **Setup (primeira vez)**

```bash
# 1. Instalar dependências
pip install anthropic pypdf

# 2. Verificar que ANTHROPIC_API_KEY está no ambiente
echo $ANTHROPIC_API_KEY  # deve retornar sua chave
```

### **Uso básico**

```bash
# Resumir um livro
python3 smart-book-summarizer.py seu_livro.pdf
```

O script:
- Mostra a estratégia escolhida
- Processa automaticamente
- Salva em `00 Notes/Books/seu_livro - Resumo Completo.md`

### **Opções avançadas**

```bash
# Forçar modelo específico (padrão é automático)
python3 smart-book-summarizer.py livro.pdf --model sonnet

# Usar Haiku (mais barato, menos detalhes)
python3 smart-book-summarizer.py livro.pdf --model haiku

# Modo seletivo (para livros muito grandes)
python3 smart-book-summarizer.py livro.pdf --selective
```

---

## 📊 Estratégias e custos

### Livro <100 páginas
```
✅ Método: DIRETO
🧠 Modelo: Sonnet (melhor qualidade)
💰 Custo: ~1-2k tokens
⏱️ Tempo: 2-3 minutos
```

### Livro 100-250 páginas
```
✅ Método: CHUNKED (Haiku + Sonnet)
🧠 Modelos: Haiku (chunks) + Sonnet (consolidação)
💰 Custo: ~40-80k tokens (40-60% menos que direto)
⏱️ Tempo: 5-10 minutos
```

### Livro >250 páginas
```
⚠️ Método: ASKS (você escolhe)
💰 Custo: ~100k+ tokens (se completo)
💡 Sugestão: fazer só capítulos relevantes
```

---

## 📁 Saída

Após rodar, o arquivo é salvo em:
```
00 Notes/Books/[Seu Livro] - Resumo Completo.md
```

Com a estrutura pronta para usar:

```markdown
# 📌 SINOPSE
...

# 🎯 INSIGHTS PRINCIPAIS
...

# 📝 RESUMO DO LIVRO
...

# 📖 RESUMO ENXUTO POR CAPÍTULO
...

# 🧠 QUIZ
<details>
<summary>Pergunta 1?</summary>
Resposta aqui
</details>
...

# 📚 RESUMO COMPLETO
...
```

---

## 🔧 Troubleshooting

**Erro: "pypdf não instalado"**
```bash
pip install pypdf
```

**Erro: "ANTHROPIC_API_KEY não definida"**
```bash
export ANTHROPIC_API_KEY="sk-..."
```

**Script está lento**
- Livros grandes levam tempo mesmo
- Chunking com Haiku é mais rápido que Sonnet direto
- Paciência: o script está processando, não travou

**Tokens gastos demais?**
- Use `--model haiku` para versão mais rápida e barata
- Para livros >200 pgs, considere fazer capítulos específicos

---

## 💡 Dicas

1. **Primeiro teste:** comece com um livro pequeno (<100 pgs) pra ver como funciona
2. **Otimização:** se tiver livros muito grandes, divida em 2-3 PDFs antes
3. **Reutilização:** o script é genérico, funciona com qualquer PDF
4. **Qualidade:** quanto maior o livro, melhor faça em chunks (mais consistente)

---

## 📝 Exemplo de execução

```
$ python3 smart-book-summarizer.py The_Art_of_Learning.pdf

============================================================
📚 LIVRO: The_Art_of_Learning
📄 Páginas: 285
🧠 Tokens estimados: 78,540
============================================================

📊 Médio (285 pgs) — 6 chunks (Haiku) + consolidação (Sonnet)
Método: CHUNKED
Chunks: 6
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
   /Users/rafa/Desktop/RAFA AI BRAIN/00 Notes/Books/The_Art_of_Learning - Resumo Completo.md
```

---

**Salvo em:** `/05 Skills/smart-book-summarizer.py`

**Próximos passos:** Manda um PDF pra testar! 🚀
