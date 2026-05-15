# Jaycen Joshua — "Drunk" (Mix Study)

> Estudo de mix do Jaycen Joshua na faixa "Drunk" do projeto MWTM. Análise track by track do fluxo de trabalho, gain staging, escolhas de processamento e filosofia.

---

## 🧠 Resumo — Principais Sacadas

### Filosofia Geral
- **Top-down mixing:** quando ele processa tracks individuais, elas já estão passando por todo o processamento dos buses. Nunca mistura fora de contexto.
- **Começa do zero em cada track:** sola o kick, faz o melhor kick possível, e assim por diante. Foco total em cada elemento antes de juntar.
- **Gain staging é a base de tudo:** ele trabalha sempre para acertar os níveis antes de processar. Clip gain > faders. Faders travados em 0.
- **Release = peso vs. controle:** release baixo no compressor = mais peso/sustain. Release alto = mais controle/tight. Ele usa essa lógica conscientemente em cada decisão de compressão.

### Drums
- **Kick duplicado para thump sem transiente:** quando quer mais low end sem adicionar punch, duplica o kick e usa MV2 squashando + Pultec dando 60hz com corte no agudo. Resultado: sub body sem click.
- **Hihat vs. Snare:** sempre EQ'a o hihat primeiro, acha a fundamental, e corta ela no snare. Resolve o problema de snare "piercing" que muita gente ignora.
- **Rim engrossado com Torque:** quando o rim soa muito fino/piercing, usa o Torque da Waves para adicionar corpo.
- **TrueVerb só com early reflections:** usa decay em 0.5, room size pequeno, apenas para empurrar elementos pra trás na mix — sem adicionar reverb perceptível. Alternativa a só abaixar o volume.
- **Hihat com Lo-Fi:** baixa minimamente o sample rate + um tique de saturação + anti-aliasing reduzido para trazer um pouco de high end de volta. Deixa o hihat mais "thick".

### Bass
- **Kick recebe Neutron Transient Designer** (preset "K - Transient") para moldar ataque/sustain por banda de frequência.
- **Bass instável → duplicar e separar:** quando o bass é muito instável (synth bass com muita variação de harmônicos), duplica a track e separa high/low com corte em 100hz. Low end com Soothe 2 preset "Bass Chill" ou RComp dedicado. High com Pro-Q preset "Bass Growl" (corte em 220, boost em 1100).
- **Bass Soothe sidechain:** coloca o Soothe no fim da chain do bass e faz sidechain com o próprio bass para controle dinâmico de resonâncias.
- **Bass stereo → mono no grave:** fecha o pan do low end duplicado no DAW para manter o grave centrado, mesmo que o synth seja stereo.
- **Micro-ajustes no Spectre no final:** dá uns 1db aqui e ali em frequências específicas (40hz, 400hz) no fim da mix para pequenos ajustes de tonalidade.

### Vocals
- **Muta o hihat antes de mixar os vocais:** quer que o high end venha principalmente da voz. Volta o hihat depois de terminar os vocais, ajustando de acordo.
- **Muta também o bass e a music:** mixa a voz com bateria só (sem hihat, sem bass, sem music). Contexto mínimo para focar no que importa.
- **MC404 release por banda:** peso no grave = release baixo. Controle no agudo = release alto. Numa voz alterboy/aguda: release alto no grave (para não engordar demais), release alto no médio-agudo (para não apertar os "s").
- **Corte em 20kHz na voz:** tira o hiss digital que alguns microfones e gravações têm ali no topo. Limpa o espaço para hihat e outros elementos de high end.
- **Separação lead vs. backing:** não copia o EQ da lead nos backings. Acha a fundamental da lead (ex: 2k) e corta essa frequência pesado no backing, compensando em outra frequência (ex: 4k). Isso cria separação real.
- **MV2 no lugar do El Rey** para vocal mais "in your face": troca um plugin de coloração por um compressor mais agressivo quando quer a voz mais presente.

### Sample
- **ShredSpread para abrir o stereo** + mono maker em 80hz.
- **Duplicar para controlar mid-range:** quando o Spectre não dá a consistência que ele precisa em uma frequência específica (ex: 450hz), duplica a track, isola aquela range com Pro-Q + MV2, e controla o volume da duplicata separadamente. Método mais preciso que saturação.

### EQ Philosophy
- **EQ preferido por banda de frequência:** ele tem EQs favoritos para frequências específicas. 10k: Pultec ou Air EQ. 7k: Trident. Não usa um EQ genérico pra tudo.
- **Soothe 2 para resonâncias instáveis:** não usa EQ estático para resonâncias de instrumentos instáveis — usa Soothe 2 dinâmico, que só atua quando a resonância aparece.
- **Pro-Q dinâmico no sub do kick:** usa um preset de contorno dinâmico bem lá embaixo (~20hz) para controle do sub absoluto do kick.

---

## 🔌 Chain Reference

### Bass Bus (padrão)
`RBass → Shadowhills → RComp → Blackbox → Gate/Exp → Pro-Q`
(+ El Rey, Spectre, Soothe 2 ready to go)

### Vocal Chain (padrão)
`Spectre → El Rey → Pro-Q → MC404 → Pro-Q → Air EQ → MC404 → CLA Vocals → C6 → Soothe 2`

### Gain Staging Reference
- Drums: bate **-1** no Shadow Hills (visor direito)
- Kick + Bass juntos: bate **-4** no God Particle
- Bass individual: bate **-1 a -2** no RComp

---

## 📋 Anotações Track by Track

### EQ — Filosofia de Bandas

He loves different bands in different eqs — for example, 10k his favorite is Pultec, and possibly 8k as well. Trident — 7k. Air EQ 10k is also great. No Pensado EQ, ele moldou seus EQs favoritos para cada banda.

---

### Buses — Configuração Geral

Eu vi no bus dele — All Music e All Drums — o Spectre com todas as bandas já ativo.

Standard clip no drums and bass.

---

### 🥁 KICK

**Neutron Transient Designer** (preset "K - Transient") — moldando ataque e sustain por banda de frequência:

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 10.32.41 PM.png]]

Kick — para fazer o kick sair mais no celular, usou o Transformer 2 para dar mais punch nos médios. Passou um pouco do tanto de corpo que queria, então colocou um EQ extra no aux do Transformer 2 e tirou um pouco de 300hz. Quando adicionou esses, aumentou o volume, então teve que abaixar no clip gain — ele trabalha mais com faders em 0 no geral.

Achou que estava "inflated", então ajustou o Spectre — desmarcou os pontos de cima e mudou o mix para 30%. Depois desativou o Spectre completamente e gostou mais. Tirou o segundo e o sexto NLS (que ele costuma tirar) para reduzir o engordamento harmônico que estava excessivo.

**Kick duplicado para thump no low end sem transiente** — duplicou o kick, colocou MV2 squashing forte + Pultec dando muito 60hz + atenuação pesada no agudo:

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 10.48.18 PM.png]]

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 10.48.44 PM.png]]

Pro-Q — usa o preset de contorno dinâmico no low-low (~20hz). Ele corta o kick no sub absoluto frequentemente.

---

### 🥁 RIM

Achou o rim piercing demais — usou o **Torque** (Waves) para deixar mais encorpado.

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 10.37.31 PM.png]]

OBS: nessa mix o snare é um rim bem fininho, então não há muito para aprender sobre snare. Mas o método de engrossar rim = Torque.

---

### 🥁 HIHAT

Checou com o Insight para ver se era muito stereo. Usou o PS22-X Split para automatizar um pan desenhado manualmente — bem diferente de um pan normal:

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 11.27.31 PM.png]]

***Hat — insight importante sobre profundidade:** estava achando o hihat muito na frente da mix, com vontade de abaixar. Mas ele diz que abaixar não faz quase nada — é aí que ele usa o **TrueVerb** para empurrar pra trás na mix. Room size e distance ajustados. Early reflections only, decay 0.5.

> A distância do reverb também pode ser automatizada — cria movimento interessante.

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 11.31.22 PM.png]]

**Lo-Fi para engrosar o hat** — baixou o sample rate minimamente + um tique de saturação + anti-aliasing reduzido para trazer um pouco de high end de volta:

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 11.34.49 PM.png]]

---

### 🎸 BASS (Reese Bass — instável)

Bass All e Boom bus chain: `RBass → Shadowhills → RComp → Blackbox → Gate/Exp → Pro-Q` (todos ativados, + El Rey, Spectre e Soothe 2 prontos).

Começou diminuindo o clip gain do bass para bater entre -1 e -2 no RComp.

**Bass instável → solução: duplicar e separar em high/low:**
- Low: Pro-Q corte em ~100hz (slope 30) → Soothe 2 "Bass Chill" preset (depth ~14)
- High: Pro-Q preset "Bass Growl" (corte em 220, boost em 1100hz)

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 10.57.21 PM.png]]

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 10.57.39 PM.png]]

No fim das contas tirou o Soothe "Bass Chill" do low end e colocou um **RComp dedicado só no low:**
- Release super alto (quer controle, não peso)
- Ratio 1.25
- Reduzindo ~6db
- Make-up gain de acordo com a redução

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 11.02.18 PM.png]]

Agora que o low end está controlado, fez o **sidechain do Soothe 2 com o próprio bass** — no fim da chain:

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 11.06.50 PM.png]]

**Bass stereo → mono:** fechou o pan da duplicata grave no DAW (o synth era stereo). Abaixou o clip gain porque ficou mais alto.

Bass high com Pro-Q "Bass Growl":

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 11.11.18 PM.png]]

> A lot of times he would spatialize the high part of the bass to get it out of the lead vocal. Nessa não foi necessário pois já estava spatializado.

---

### 🎸 BASS 2 (Synth bass plucky)

Checou gain staging no Bass All bus — já estava certo.

Achou crazy demais → aumentou o release do RComp para 150 no Bass All.

Ainda não gostou → colocou Soothe 2 "Bass Chill" direto na track. Ajustou o notch mais alto para controlar o low-low (~30hz):

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 11.23.29 PM.png]]

---

### 🎹 SAMPLE

Checou stereo com Insight → usou **ShredSpread** para abrir os lados + mono maker em 80hz:

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 11.37.04 PM.png]]

Achou resonâncias indesejadas → Pro-Q hover no espectro para identificar picos → abaixa ~10db com EQ dinâmico:

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 11.39.41 PM.png]]

***Método para controlar uma faixa de frequência específica de forma consistente:**
Tentou Spectre (+1db em 450hz para mais corpo) — mas sentiu que não daria a consistência necessária. Então **duplicou a track, isolou o low-midrange com Pro-Q + MV2** — agora tem controle total daquele range com o fader da duplicata:

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 11.43.03 PM.png]]

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-03 at 11.43.48 PM.png]]

---

### 🎤 VOCALS

**Workflow de referência:**
- Muta o hihat antes de começar os vocais (não quer interferência no high end enquanto toma decisões)
- Muta bass e music também — mixa a voz com a bateria (sem hihat, sem bass, sem music)
- Só volta o hihat depois que a voz está pronta, para ajustar de acordo

Chain: `Spectre → El Rey → Pro-Q → MC404 → Pro-Q → Air EQ → MC404 → CLA Vocals → C6 → Soothe 2`

---

#### Lead Vocal 1 (Alterboy — voz aguda)

**MC404 — release por banda pensando em weight vs. control:**
- Grave: quer peso → release baixo
- Médio-agudo: não quer mais agudo (já é agudo) → release alto

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-04 at 12.00.11 AM.png]]

Pro-Q tirando resonâncias + low shelf grande para tirar peso no grave:

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-04 at 12.00.59 AM.png]]

Slate Fresh Air (no lugar do Air EQ):

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-04 at 12.02.17 AM.png]]

---

#### Lead Vocal 2 (voz feminina — mais in your face)

Tirou o El Rey e colocou MV2 no lugar para uma presença mais agressiva:

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-04 at 12.06.16 AM.png]]

MC404 — padrão dele. Pro-Q nas resonâncias. Air EQ: tirou ~1.5db em 260hz, +0.5db em 5k, +0.5db de air.

**MC404 — ajuste no over-compression:** mais pra frente, o vocal estava over compressed e os "s" ficaram muito apertados. Abriu o ataque no high-mid e na última banda → trouxe um pouco dos "s" de volta.

CLA Vocals — só um tique de Spank.

**Corte em 20kHz na voz** — tira o hiss digital que alguns microfones têm ali no topo. Limpa espaço para hihat e outros elementos:

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-04 at 12.13.20 AM.png]]

CLA Vocals para body no upper + um pouco de spread:

![[Assets/Jaycen - Drunk MWTM/Screenshot 2026-03-04 at 12.14.57 AM.png]]

---

### 🎤 Backing Vocals — Separação de Lead

> Perguntaram sobre separação dos backings e lead: EQ. Não dá para copiar o EQ da voz lead nos backings se você quer separação.
>
> Truque: achar onde está a fundamental da voz lead (ex: 2k) → cortar bastante de 2k no backing → adicionar de outra frequência (ex: 4k). Isso cria separação real entre as camadas.

---

### 🔧 Ajustes Finais

Bass — no final mexeu no Spectre do bass: +1db em 40hz e +1db em 400hz. Mini-ajustes de tonalidade no fim da mix.

---

## 📌 Hihat × Snare — O Erro Que Todo Mundo Comete

> Ele menciona isso duas vezes ao longo da sessão: ver direto as pessoas EQ'ing um snare certinho, soando bem, mas quando coloca no beat o snare soa muito piercing. É porque o hihat está dobrando uma frequência dele.
>
> **Solução:** abre o Pro-Q no hat, localiza a fundamental, tira uns dB — e passa esse corte para o snare também.
