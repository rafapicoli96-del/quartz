# Jaycen Joshua — "Playa" (Mix Study)

> Estudo de mix do Jaycen Joshua na faixa "Playa" do projeto MWTM. Foco em processamento de percussões, gestão de stereo, movimento/automação, e técnicas de synth.

---

## 🧠 Resumo — Principais Sacadas

### Percussões — O Core Desta Mix
- **Stereo das percs é regra, não exceção:** ele usa o Izotope Insight (visualizador Lissajous) em todas as percussões para checar se estão muito no meio. Se estiver, usa o P22 Spread para abrir — e o critério visual de "perfeito" é quando a informação ocupa bem o campo stereo sem extravasar.
- **Movimento é diferencial:** não basta colocar a perc no lugar — ele adiciona **automação de pan no P22** (o parâmetro "rotation") e **tremolo com Tremolator** nos bongos para criar vida e groove sutil. Movimento pra frente e pra trás na mix também.
- **TrueVerb com distance automatizado:** para percussões que precisam ir de perto para longe na mix, ele cria um preset específico do TrueVerb (sala maior + distance mais afastado do que o padrão de hihat) e **automa o distance** — cria um efeito de movimento de profundidade que vai de frente para trás na room.
- **Soothe no mid range das percs agudas:** quando o mid range das percs high entra em conflito com kick e 808, ele faz sidechain do Soothe nas percs com o kick+808 como sinal de trigger — tira o mid quando o grave entra, sem precisar cortar estático.

### Bells e Synths — Técnicas Específicas
- **Bell com sidechain no Soothe (kick+808 como trigger):** ao invés de cortar o low end do bell (o que muita gente faria), ele mantém o low end e usa sidechain para que o Soothe retire as frequências problemáticas dinamicamente quando o kick e o 808 estiverem tocando. O beat fica mais pesado.
- **Vitamin em synths/teclas:** preset favorito dele — usado duas vezes nessa música. Dá uma "vida a mais" e engorda o synth. Vale ter esse preset na mão.
- **ShredSpread em synth teclas** para abrir o stereo.
- **Air EQ em voz tipo bell:** boost em 7–8k (ao invés do Pultec que seria a escolha óbvia). Diferença de timbre entre os dois — vale explorar.
- **Pro-Q slope variado no bell:** trocar o slope do corte tipo bell no Pro-Q — frequentemente esquecido, mas muda bastante o resultado.

### Vocals
- **Spectre modo "Warm":** boost de 200hz para trazer calorzinho à voz. Modo "Rectify" no 1k — basicamente tira a frequência e coloca de volta do jeito dele (é ao mesmo tempo um boost e cut na mesma frequência — precisa testar).
- **Compressão paralela no bus de synths:** CLA Mixdown com um pouco de glue + drive — deu gordura nos pads sem comprimir direto.
- **TrueVerb no Snap:** colocou o TrueVerb no send de snap porque a voz estava muito na frente. Early reflections pequenas para recuar o elemento.

---

## 🔌 Ferramentas Usadas

| Ferramenta | Uso |
|---|---|
| **Izotope Insight** | Checar stereo das percussões (Lissajous) — critério visual para P22 |
| **P22 Spread** | Abrir stereo das percs + automação do pan (rotation) |
| **Tremolator (Soundtoys)** | Tremolo nos bongos — groove sutil, preset "Dynamical", 1/8th, 87bpm |
| **TrueVerb** | Percussões atrás do kick/snare (sala maior + distance automatizado) |
| **Soothe 2** | Sidechain nas percs agudas (kick+808 como trigger) + sidechain no bell |
| **Vitamin (Waves)** | Vida + gordura em synths e teclas (preset favorito dele) |
| **CLA Mixdown** | Compressão paralela no bus de synths (glue + drive) |
| **Spectre** | Voz: modo Warm (boost 200hz) + modo Rectify (1k) |
| **Air EQ** | Boost 7–8k em voz tipo bell |
| **ShredSpread** | Stereo em synth teclas |

---

## 📋 Anotações Detalhadas

### Synths Bus — Compressão Paralela

Primeira coisa importante: compressão paralela no bus de synths. Usou o CLA Mixdown com um pouco de glue e drive — deu uma gordura bem legal para os pads.

---

### 🥁 PERCUSSÃO — Processamento Completo

**Sidechain do Soothe nas percs agudas:**
O mid range das percussões agudas estava atrapalhando um pouco e não casava bem com o kick e 808. Ao invés de EQ estático, ele fez sidechain do Soothe nas percs com o sinal do kick+808 como trigger. Soothe só age quando o grave está presente.

**TrueVerb — preset diferente para percussões:**
Ele queria colocar as percussões atrás do kick e snare. Aumentou o tamanho da sala e colocou o distance mais atrás da room (diferente do preset padrão que usa para hihats). Depois automatizou o distance para ir de frente para trás na room:

![[Assets/JAYCEN - Mixing Playa MWTM/image_01.png]]

**Tremolator nos bongos** — GEM sutil para adicionar groove. Preset "Dynamical", shape "Premier", 1/8th, sincronizado no BPM da sessão (87 BPM):

![[Assets/JAYCEN - Mixing Playa MWTM/image_02.png]]

> Junto com isso, no P22, também tem automação do parâmetro "rotation" (pan do plugin) para dar movimento às percussões.

**Pro-Q slope variado:** uma coisa que ele usou que é fácil esquecer — trocar o slope do corte tipo bell no Pro-Q. Muda bastante o resultado.

---

### 📊 PERCUSSÃO — Checagem de Stereo (Izotope Insight)

Ele usa o Izotope Insight (Lissajous) para checar a informação stereo de cada percussão. Quando estão muito no meio, usa o P22 Spread para abrir. O critério é visual:

**Este ele considerou "ainda um pouco no meio":**

![[Assets/JAYCEN - Mixing Playa MWTM/image_03.png]]

**Este também ainda muito no meio:**

![[Assets/JAYCEN - Mixing Playa MWTM/image_04.png]]

**Este ele achou perfeito** — a informação stereo ocupa bem o campo sem extravasar. Basicamente: precisa estar assim para não entrar no lugar da voz:

![[Assets/JAYCEN - Mixing Playa MWTM/image_05.png]]

---

### 🔔 BELL — Sidechain com Soothe

Tinha um bell na track que muita gente teria cortado bastante no grave. Mas ele fez sidechain no Soothe com o sinal do kick+baixo como trigger — consegue manter o low end do bell (mantém o beat pesado) enquanto o Soothe remove as frequências problemáticas dinamicamente quando o grave entra.

---

### 🎹 SYNTHS E TECLAS

**Vitamin** — usado duas vezes nessa música em synths/teclas diferentes. Preset favorito dele: traz uma vida extra, engorda e "acorda" o synth:

![[Assets/JAYCEN - Mixing Playa MWTM/image_06.png]]

- Xover: LO 90 / LM 500 / HM 2594 / HI 9310
- Hi-Mid band subindo para brilho e presença

**ShredSpread** em um synth de teclas para abrir o stereo.

---

### 🎤 VOCALS

**Spectre na voz:**
- Modo **Warm** → boost de 200hz para trazer calorzinho
- Modo **Rectify** em 1k → tira a frequência e coloca de volta do jeito dele. É simultaneamente um boost e cut na mesma frequência. Explorar depois.

**Air EQ:** boost em 7 ou 8k em uma voz tipo bell. (Nota: eu usaria Pultec ou algo similar, mas ele usou o Air EQ — vale explorar a diferença de timbre entre os dois nessa situação.)

**TrueVerb no Snap:** voz estava muito na frente, então colocou o TrueVerb no send de snap com early reflections para recuá-la na mix.
