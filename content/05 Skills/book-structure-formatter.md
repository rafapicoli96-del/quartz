# Book Structure Formatter

**Propósito:** Transformar um resumo completo de livro em uma estrutura de 5 seções organizada.

## Como Usar

Passe um resumo completo de um livro (ou copie o conteúdo) e peça:

```
/book-structure <nome do livro> [conteúdo ou arquivo]
```

Ou simplesmente:

```
@book-structure
Sinopse: [dados do livro]
Resumo: [conteúdo completo]
```

## O que Sai

A skill retorna uma nota estruturada em **6 seções**:

1. **📌 SINOPSE** — resumo executivo (quem é o autor, do que trata, por que importa, frase-chave)
2. **🎯 INSIGHTS PRINCIPAIS** — 8-10 conceitos transformadores do livro
3. **📝 RESUMO DO LIVRO** — narrativa enxuta sem separação por capítulos (arco da história + pilares principais)
4. **📖 RESUMO ENXUTO POR CAPÍTULO** — tabela com capítulos + ideia-chave (1 linha cada)
5. **🧠 QUIZ** — 10 perguntas sobre o livro com respostas ocultas (clique para revelar)
6. **📚 RESUMO COMPLETO** — o original preservado intacto

## Exemplos de Saída

```markdown
---

# 📌 SINOPSE
[sinopse curtinha]

---

# 🎯 INSIGHTS PRINCIPAIS
[insights com explicação]

---

# 📝 RESUMO DO LIVRO (SEM SEPARAÇÃO POR CAPÍTULOS)
[narrativa enxuta: arco da história + pilares principais + por que importa]

---

# 📖 RESUMO ENXUTO POR CAPÍTULO
[tabela dos capítulos]

---

# 🧠 QUIZ — Teste Seu Conhecimento

<details>
<summary><strong>1. Pergunta sobre o livro?</strong></summary>

Resposta aqui.
</details>

<details>
<summary><strong>2. Próxima pergunta?</strong></summary>

Próxima resposta.
</details>

[... quantas perguntas forem necessárias]

---

# 📚 RESUMO COMPLETO
[seu resumo original aqui]
```

## Instruções para Claude

Quando o usuário pedir uma transformação:

1. **Extrair sinopse:** Autor, tema principal, relevância, frase-chave (4-5 linhas max)
2. **Identificar insights:** 8-10 conceitos principais com 1-2 parágrafos cada (não just bullet points)
3. **Criar resumo narrativo:** Conectar o arco narrativo do livro (início → virada → conclusão), destacar 3-4 pilares principais, explicar por que isso importa. ~300-400 palavras, leitura rápida de 3-4 minutos. SEM separar por capítulos—é uma narrativa fluida.
4. **Criar tabela de capítulos:** Todos os capítulos/seções em 1 linha com a ideia-chave
5. **Criar quiz:** Perguntas sobre os conceitos principais do livro (quantas forem necessárias para cobertura completa — não se prender a um número fixo). **Formato:** Use `<details><summary>Pergunta</summary>Resposta</details>` para ocultar respostas (clique para revelar). Perguntas devem cobrir insights principais, definições, exemplos e aplicações práticas. Se o livro é denso, pode ser 15-20 perguntas. Se é mais focado, 8-10 é suficiente.
6. **Preservar resumo original:** Colocar no final intacto

**Tom:** Direto, prático, sem fluff. Cada seção deve ser acionável. O resumo narrativo (seção 3) é a "versão média"—mais que insights isolados, menos que resumo completo. O quiz deve testar compreensão ativa, não memorização trivial.

---

---

## Dica: Como Funciona o Quiz com Details/Summary

O HTML `<details>` e `<summary>` cria uma seção **clicável e expansível** nativa do Obsidian:

```html
<details>
<summary><strong>Pergunta?</strong></summary>

Resposta aqui (só aparece ao clicar)
</details>
```

- **Clique no `<summary>`** → expande e mostra a resposta
- **Clique de novo** → fecha
- Sem plugins, sem JavaScript, funciona em qualquer lugar que renderize HTML

Perfeito para estudo ativo: você testa seu conhecimento antes de revelar.

---

**Salvo em:** `/05 Skills/book-structure-formatter.md`

**Próximos livros:** Cola aqui + pede a transformação!
