# Skill: Quick Scan

Adiciona um resumo ultracompacto no topo de notas densas — para que Rafa bata o olho e lembre do conteúdo sem precisar ler o documento inteiro.

## When to Use

- Rafa pede pra adicionar um quick scan em uma nota existente
- Rafa pede pra simplificar ou "fazer um resumo rápido" de uma nota
- Rafa cria uma nota nova que é densa e vale ter resumo no topo
- Trigger phrases: "adiciona quick scan", "faz o resumo rápido", "quero bater o olho", "simplifica o topo"

---

## Positioning

O Quick Scan vai **sempre logo após o título e subtítulo/quote da nota**, antes do primeiro `---` e antes de qualquer seção de conteúdo.

```
# Título da Nota

> Subtítulo ou quote (se existir)

---

> [!abstract] Quick Scan     ← AQUI
> ...

---

## Primeira seção real
(conteúdo completo...)
```

---

## Format Rules

- Usar callout `[!abstract]` com título **Quick Scan** — fica visualmente destacado no Obsidian
- Máximo de 8 linhas visíveis no callout
- Sem frases longas — bullets secos, direto ao ponto
- Sem repetir o título da nota — o Quick Scan complementa, não descreve
- **Adaptar os labels ao tipo de conteúdo** da nota (ver exemplos abaixo)

---

## Templates por Tipo de Conteúdo

### Padrão psicológico / comportamental
```markdown
> [!abstract] Quick Scan
> **O padrão em uma frase:** [descrição seca do padrão]
>
> **Como aparece:**
> - bullet
> - bullet
>
> **Por que:** [mecanismo em uma frase]
>
> **Custo:** [consequência concreta]
>
> **O que ajuda:** [alavanca principal]
```

### Conceito / framework / mental model
```markdown
> [!abstract] Quick Scan
> **O que é:** [definição em uma frase]
>
> **Quando usar:** [contexto de aplicação]
>
> **Os pontos-chave:**
> - bullet
> - bullet
> - bullet
>
> **Para lembrar:** [a ideia central, a takeaway que não pode esquecer]
```

### Nota de sistema / processo / workflow
```markdown
> [!abstract] Quick Scan
> **O que faz:** [função do sistema em uma frase]
>
> **Passos:**
> 1. passo
> 2. passo
>
> **Gatilho:** [quando ativar]
>
> **Não esquecer:** [o detalhe crítico que costuma ser esquecido]
```

### Nota de estudo / aprendizado / referência
```markdown
> [!abstract] Quick Scan
> **O assunto:** [tópico em uma frase]
>
> **Os 3 pontos que mais importam:**
> - bullet
> - bullet
> - bullet
>
> **A aplicação direta:** [como isso entra no trabalho real de Rafa]
```

---

## Quality Rules

- **Não resumir o óbvio** — o Quick Scan captura o que é fácil de esquecer, não o que está no título
- **Priorizar o acionável** — terminar sempre com algo que Rafa pode *fazer* ou *lembrar* na hora certa
- **Ser honesto sobre incertezas** — se a nota tem hipóteses não confirmadas, o Quick Scan também deve sinalizá-las como tal
- **Não inventar** — o Quick Scan é uma destilação do que está na nota, não uma interpretação nova

---

## Multiple Notes at Once

Se Rafa pedir para adicionar Quick Scan em várias notas de uma pasta:
1. Ler todas as notas em paralelo primeiro
2. Identificar o tipo de conteúdo de cada uma
3. Fazer todas as edições em paralelo
4. Confirmar quantas notas foram atualizadas
