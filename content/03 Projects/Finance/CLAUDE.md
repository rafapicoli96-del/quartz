# Finance — Sistema de Análise Financeira

Rulebook conciso para análise de extratos. Suba CSVs (não PDFs) um mês de cada vez.
**Relatórios salvos em:** `03 Projects/Finance/Relatorios/YYYY-MM.md`

---

## Contas Conhecidas

| Conta | Banco | Moeda |
|-------|-------|-------|
| NuConta | Nubank | BRL |
| Cartão Nubank | Nubank | BRL |
| Conta C6 | C6 Bank | BRL |
| PayPal | PayPal | USD |

---

## Deduplicação — 3 Regras

**Regra 1 — Pagamento de Fatura do Cartão**
- Se encontrar em conta corrente: "Pagamento", "Fatura", "Nu Pagamentos" → EXCLUIR
- As compras já estão no extrato do cartão

**Regra 2 — Transferências PayPal → Brasil**
- Procurar par: PayPal "Withdrawal" + Nubank depósito compatível (mesmo valor, mesma semana)
- EXCLUIR ambas as pontas (são internas, não receita/despesa)

**Regra 3 — Transferências entre Contas Brasileiras (TED/PIX)**
- Procurar: "TED", "PIX" com mesmo valor, datas próximas
- Beneficiário = Rafa → EXCLUIR ambas as pontas

---

## Conversão USD → BRL

- **Cotação padrão: R$ 5,00 por USD** (padrão adotado para relatórios financeiros — aproxima-se do real atual, sem volatilidade extrema)
- Usar cotação média do mês (BCB PTAX via WebSearch) SOMENTE se desviar significativamente de 5,00
- Fallback: cotação no próprio extrato (ex: CC Nubank mostra o rate)
- Documentar cotação usada no topo de cada relatório

---

## Categorias de Despesa

| Categoria | Exemplos |
|-----------|----------|
| 🏠 Moradia | Aluguel, internet, energia, empregada doméstica, condomínio |
| 🍔 Alimentação | Supermercado, restaurante, delivery, iFood |
| 🎵 Música & Produção | Plugins, samples (Splice), cursos, equipamento, estúdio |
| 📱 Assinaturas | Netflix, Spotify, Adobe, iCloud, serviços mensais |
| 🚗 Transporte | Uber, 99, metrô, gasolina, estacionamento |
| 🏋️ Saúde & Bem-estar | Academia, suplementos, farmácia, veterinário, consultas |
| 🎮 Lazer | Jogos, bares, eventos, passeios, PlayStation |
| 👔 Pessoal | Roupas, cuidados pessoais, compras diversas |
| 🔧 Ferramentas & Serviços | Hosting, domínios, contadores, ferramentas profissionais |
| ❓ Não identificado | Listar explicitamente — perguntar ao Rafa |

---

## Categorias de Receita

| Categoria | Descrição |
|-----------|-----------|
| 🎼 Pickup Music | Backing tracks (plataforma online) |
| 🎛️ Produção Completa | Faixas produzidas para artistas (maior valor) |
| 💵 Internacional (PayPal) | Receitas em USD convertidas para BRL |
| 💰 Outras | Qualquer outra entrada |

---

## Estrutura do Relatório

```
# Relatório Financeiro — [Mês Ano]

> Gerado em [data]. Extratos processados: [lista].
> Cotação USD/BRL: R$ X,XX (fonte: [BCB/extrato/outro])

## 📊 Resumo
[Tabela: Receita Total | Despesas Totais | Saldo | Meta (R$20k) | % atingido]

## 💰 Receitas
[Tabela: Fonte | Valor | %]

## 💸 Despesas por Categoria
[Tabela: Categoria | Valor | %]

## 🔍 Detalhamento por Categoria
[Seção para cada categoria com transações detalhadas]

## 🔄 Transferências Internas
[Tabela: De | Para | Valor | Nota]

## 🤖 Análise do Advisor
### Saúde Financeira Geral
### Progresso para R$20k/mês
### Padrões Identificados
### Alertas & Pontos de Atenção
### Recomendações

## ✅ Classificações Confirmadas
[Se houver transações que precisarem confirmação]
```

---

## Checklist — O Que Sempre Avaliar

1. **Progresso para R$20k/mês** — onde está, gap, qual alavanca resolve
2. **Concentração de receita** — se >70% de uma fonte só, alertar
3. **Receita de Produção Completa** — se não apareceu no mês, sinalizar (maior lever)
4. **Subscription creep** — novas assinaturas que apareceram sem aviso
5. **Lazer vs. investimento** — proporção de gastos que "drenam" vs. que "crescem"
6. **Receita PayPal** — rastrear tendência (clientes internacionais = sinal de crescimento)
7. **Gastos com Música & Produção** — positivo, indica investimento na carreira
8. **Transações grandes não recorrentes** — identificar e contextualizar
9. **Comparação com mês anterior** — principais métricas vs. mês passado

---

## 🔄 Workflow: Atualizar Saúde Financeira Geral

**Trigger:** Quando Rafa faz upload de novos extratos e um novo relatório mensal é gerado

**Ação automática:** Após gerar o relatório `YYYY-MM.md`, SEMPRE atualizar `(C) Saúde Financeira Geral.md`

**O que atualizar:**
1. **Saldos Atuais por Conta** — pedir ao Rafa os valores atualizados (NuConta, C6, PayPal, fatura cartão)
2. **Análise por Período** — adicionar nova linha com dados do mês que foi gerado
3. **Alertas & Padrões** — revisar se há novos padrões (Uber mudou? Pickup estabilizou? Full Production cresceu?)
4. **Score de Saúde** — recalcular as 5 dimensões baseado nos novos dados
5. **Próxima Revisão** — atualizar data para o mês seguinte

**Formato da entrada no histórico:**
```
### **[Mês] [Ano]**
- Receita: R$ X.XXX
- Despesas: R$ X.XXX
- **Saldo: R$ X.XXX** [✅/❌]
- Padrão: [uma frase sobre o destaque do mês]
```

**Resultado final:** Documento sempre atualizado, mostrando tendências de 3+ meses de forma consolidada.
