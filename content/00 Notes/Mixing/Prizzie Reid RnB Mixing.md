# Prizzie Reid — RnB Mixing Study

> Estudo de mix de Prizzie Reid em uma produção de RnB. Foco em cadeia de vocais, tratamento de bus vocal, sends e processamento de 808/graves.
> Vídeo: https://www.youtube.com/watch?v=roZxck7CC1w

---

## 🧠 Resumo — Principais Sacadas

### Vocal Bus — Uma Lição de Organização
- **Bus de sends dedicado:** todos os sends (room, plate, verb, widener, slap) são roteados para um **bus de sends** antes de chegar ao master. Isso dá um controle extra: ele pode subir e abaixar todos os efeitos de uma vez, e coloca o **Inflator** nesse bus (15–20% / curve ~28) para adicionar vibe e saturação nos sends coletivamente.
- **Soothe no vocal bus com preset de "harshness":** Soothe 2 no vocal bus com preset "Clean up a little vocal harshness" — depth bem baixo (0.4), mix em 85%, focado em 2k–8k. Não processa demais, só limpa as asperezas que o ouvido cansa.
- **Pro-Q no vocal bus com "808 cleanup":** corte dinâmico em ~7kHz no vocal bus com o preset "PR 808 CLEANUP" — tira as frequências que conflitam com o 808 de forma dinâmica. Inteligente: mantém o brilho da voz mas cede espaço para o 808 quando necessário.

### Lead Vocal — Chain Minimalista
- **De esser primeiro:** antes de qualquer compressão ou EQ.
- **Soothe na chain individual** (não só no bus).
- **Pultec na chain sem fazer nada** — só pela coloração/colocação no sinal. Muita gente ignora que plugins passivos colorem o som mesmo bypass/flat.
- **MC DSP 404 como failsafe:** não está comprimindo ativamente — está lá como seguro caso o vocal extrapole em algum momento.
- **RVox só 2–3dB:** compressão muito leve. Ele não amassa a voz.
- **Spec Craft e Fresh Air bem de leve** no final.

### Backing Vocals — Separação Inteligente
- Mesma chain da lead, mas com dois acréscimos:
  - **Blackbox EQ cortando o high end de leve** — separa timbre dos backings vs. lead
  - **P22 Spread** — abre o stereo dos backings para criar separação espacial

### Sends — Estrutura Completa
| Send | Plugin | Uso |
|---|---|---|
| Room | Seventh Heaven | Curto e de leve — só para colocar no espaço |
| Plate | UAD Lexicon 480L + EQ | Plate verb com EQ depois para tirar mud |
| Throws | TrueVerb "Millenial" | Preset longo para lançamentos de frases |
| Widener | Doubler | De leve |
| Slap | — | Muito de leve |

---

## 📋 Anotações Detalhadas

### 🎤 BACKING VOCALS

Uma lição importante: mixers profissionais têm uma **vocal chain específica para os backings no bus**, não apenas processam individualmente.

Chain: igual à lead, mas com dois acréscimos:
- **Blackbox EQ** cortando o high end muito de leve (para separar timbre dos backings da lead)
- **P22 Spread** para abrir o stereo dos backings

---

### 🎤 LEAD VOCAL

Chain: `De-esser → Pro-Q (leve) → Soothe 2 → Pultec (flat — só colocação) → MC DSP 404 (failsafe) → RVox (2–3dB) → Spec Craft (leve) → Fresh Air (leve)`

Pontos importantes:
- Pultec sem fazer nada — só pela coloração passiva
- MC404 como failsafe, não como compressor ativo
- RVox muito leve (2–3dB apenas)

---

### 📤 SENDS — Roteamento e Bus de Sends

Todos os sends são roteados para um **bus de sends** antes do master. Nesse bus:
- **Inflator:** 15–20% / curve ~28 — adiciona vibe e saturação coletiva nos sends

| Send | Plugin |
|---|---|
| Room | Seventh Heaven (curto e de leve) |
| Plate | UAD Lexicon 480L + EQ (para tirar mud) |
| Millenial/Throw | TrueVerb (preset longo) |
| Widener | Doubler (leve) |
| Slap | Slap delay (muito leve) |

---

### 🎛️ VOCAL BUS — Processamento

**Pro-Q 3 — preset "PR 808 CLEANUP":** corte dinâmico steep em ~7kHz no vocal bus. Remove frequências que conflitam com o 808 de forma dinâmica — mantém o brilho da voz sem entrar em conflito:

![[Assets/Prizzie Reid RnB Mixing/image_01.png]]

**Soothe 2 — preset "Clean up a little vocal harshness":** depth bem baixo (0.4), mix 85%, attack 1.5, selectivity 5.7. Foco em 2k–8kHz. Limpa as asperezas sem processar demais:

![[Assets/Prizzie Reid RnB Mixing/image_02.png]]
