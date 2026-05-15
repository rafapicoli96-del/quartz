# How I Recreated Over 1000 Sounds

**Fonte:** https://www.youtube.com/watch?v=MZpZaucYI4E
**Canal:** Eric Bowman
**Tags:** #sound-design #synthesis #vital #production-process

---

## 🧠 Quiz

> Tente responder antes de revelar. Respostas colapsadas.

---

**1. Qual é o primeiro passo essencial para recriar um som sintetizado?**

> [!NOTE]- Resposta
> Isolar o som que você quer recriar — encontrar uma parte da gravação onde nenhum outro som está tocando. Se isso não existir, você pode usar ferramentas de IA para separar os stems da música.

---

**2. Quais são as duas principais ferramentas recomendadas para separar stems usando IA?**

> [!NOTE]- Resposta
> GAO (aplicativo online gratuito, mas às vezes com espera) e Dieser Spliter (também está disponível como plugin Max for Live).

---

**3. No segundo passo, o que você precisa fazer além de sincronizar o tempo?**

> [!NOTE]- Resposta
> Transcrever as notas — identificar exatamente quais notas estão sendo tocadas no som que você está recriando.

---

**4. Qual é o propósito de fazer uma comparação AB rápida no terceiro passo?**

> [!NOTE]- Resposta
> Permitir que você alterne rapidamente entre o som original e sua recriação usando um atalho de teclado, o que é fundamental para reconhecer como realmente está a reprodução em comparação com o original.

---

**5. O que é "dinâmica" no contexto do quarto passo?**

> [!NOTE]- Resposta
> A evolução do volume ao longo do som — se o ataque é imediato ou aumenta gradualmente, quanto tempo leva para decair e qual a inclinação desse decaimento. É controlado pelo envelope.

---

**6. Qual é a diferença entre um padrão de frequência e um padrão harmônico?**

> [!NOTE]- Resposta
> Um padrão de frequência é uma característica que permanece na mesma frequência independentemente da nota tocada, enquanto um padrão harmônico é relativo à série harmônica da nota específica sendo tocada.

---

**7. Como você pode determinar qual é a série harmônica de uma nota sem saber de memória?**

> [!NOTE]- Resposta
> Criar uma nova faixa, adicionar um oscilador Vital com uma onda dente de serra padrão, tocar a nota e analisar seu espectro com o Span — assim você vê os harmônicos reais daquela nota.

---

**8. Por que uma onda dente de serra é frequentemente a melhor escolha como fonte sonora para recriar um som sintetizado?**

> [!NOTE]- Resposta
> Porque ela contém todos os harmônicos, permitindo que você remova ou reduza os que não fazem parte do som original usando filtros e equalizações.

---

**9. Qual é a diferença entre usar rastreamento de tecla (key tracking) a 100% versus 0% em um filtro?**

> [!NOTE]- Resposta
> Com key tracking a 100%, o filtro acompanha a frequência da nota tocada (útil quando o corte muda proporcionalmente com a nota). Com 0%, o filtro corta a mesma frequência absoluta independentemente da nota.

---

**10. O que é vibrato/LFO no contexto do oitavo passo?**

> [!NOTE]- Resposta
> Uma modulação lenta da afinação (pitch) usando um LFO (Low Frequency Oscillator) com forma de onda senoidal — cria aquele efeito de ondulação subtil que sobe e desce a afinação.

---

**11. Como você determina se o som original tem componentes estéreo?**

> [!NOTE]- Resposta
> Usar o plugin MS Voxengo para silenciar o canal central e ouvir apenas as laterais — se o som for mono puro, você não ouvirá nada.

---

**12. Quais são as técnicas mais comuns para adicionar largura estéreo a um som?**

> [!NOTE]- Resposta
> Unison, Dune, chorus, phaser, flanger ou um delay curto — cada uma adiciona uma quantidade de diferença entre os canais esquerdo e direito.

---

**13. Qual é a diferença entre o décimo passo (profundidade com reverb/delay) e os efeitos estéreo do nono passo?**

> [!NOTE]- Resposta
> O nono passo adiciona largura estéreo (diferenças esquerda-direita), enquanto o décimo passo adiciona profundidade temporal — fazendo o som parecer que está ecoando ou refletindo em um espaço.

---

**14. Por que Eric Bowman menciona voltar aos passos anteriores mesmo quando está perto do final?**

> [!NOTE]- Resposta
> Porque adicionar efeitos como reverb e delay muda a percepção da duração da nota e de outras características, exigindo ajustes finos dos parâmetros anteriores (como envelope, dinâmica, etc.).

---

**15. O que é "modelagem física" e como ela difere da abordagem de síntese subtrativa usada para sons sintetizados?**

> [!NOTE]- Resposta
> Modelagem física tenta replicar as leis da física que governam a produção sonora real (útil para sons acústicos). Síntese subtrativa começa com uma forma de onda rica e remove/modifica características — é mais fácil para sons sintetizados.

---

---

## ⚡ Resumo Rápido

**Em uma linha:** Um framework sistemático de 10 passos para recriar qualquer som sintetizado, desde isolamento até profundidade, usando análise espectral e síntese subtrativa no Vital.

**Main takeaways:**
- Isolamento + sincronização temporal + transcrição de notas é o fundamento (passos 1-2)
- Comparação AB é crítica — você não saberá se está perto do original sem ela
- Análise espectral (série harmônica) revela padrões de frequência vs. harmônicos que definem o timbre
- Dinâmica (envelope) é frequentemente negligenciada mas é fundamental
- O processo é iterativo — você volta a passos anteriores conforme adiciona efeitos

---

## 📋 Resumo Completo

### Contexto e Motivação

Eric Bowman, produtor no YouTube, recriou mais de 1000 presets de som no sintetizador gratuito Vital. Após parar de aceitar encomendas, decidiu documentar seu processo. Este vídeo é o primeiro de uma série — o segundo abordará técnicas de modelagem física para sons acústicos.

### Os 10 Passos para Recriar um Som

#### **Passo 1: Isolamento do Som**
Encontre uma parte da gravação onde apenas o som que você quer recriar está tocando. Se isso for impossível:
- Use IA para separar stems: **GAO** (online gratuito) ou **Dieser Spliter** (plugin Max for Live)
- Cuidado: se vários sintetizadores compartilham a faixa de frequência, a IA pode agrupá-los
- Você pode ter que ignorar parcialmente elementos que interferem

#### **Passo 2: Tempo e Transcrição de Notas**
- Sincronize o BPM: reproduza um trecho da referência e ajuste o tempo em sua DAW (Ableton) até que a grade visual coincida
- Transcreva as notas: identifique exatamente quais notas a melodia toca
- Não precisa ser perfeito na sincronização inicial

#### **Passo 3: Comparação AB (Crítica)**
- Configure um atalho de teclado para alternar entre o original e sua versão
- No Ableton: clique direito em um botão → "Editar mapeamento de teclas" → atribua uma tecla (ex: R)
- Iguale os volumes das duas faixas para comparação justa
- **Insight:** Muitas pessoas subestimam o quão diferente seu som é porque nunca fazem essa comparação

#### **Passo 4: Dinâmica (Envelope)**
Adapte o envelope (ADSR) para combinar a evolução do volume:
- O ataque é imediato ou aumenta gradualmente?
- Qual é a duração do decay e sua inclinação?
- Onde o som estabiliza (sustain)?
- Ative o envelope 1 e ignore o timbre por enquanto

#### **Passo 5: Análise Espectral do Timbre**
Use um analisador de espectro como **Span** (gratuito da Voxengo):
- Procure padrões consistentes em diferentes notas
- Pergunta-chave: É uma característica da frequência absoluta ou da série harmônica da nota?

**Exemplo prático:**
- Para uma nota B3, os cinco primeiros harmônicos são: B3, B4, F5, B5, D6
- Se você vê B3 e F5 particularmente altos em todas as notas, é um padrão harmônico (sempre o 1º e 3º harmônicos)
- Se você vê a mesma frequência absoluta alta em notas diferentes, é um padrão de frequência (use equalização sem key tracking)

#### **Passo 6: Escolher a Fonte Sonora**
Se o som contém muitos harmônicos (não está filtrado agressivamente):
- Use uma **onda dente de serra** — ela possui todos os harmônicos, permitindo remover os indesejados
- Se o som é muito harmônico-pobre, considere uma onda mais simples

#### **Passo 7: Adicionar/Subtrair Amplitude de Frequências**
Duas abordagens baseadas no que você encontrou:

1. **Padrão de frequência absoluta** → Use filtro sem key tracking ou equalização em banda fixa
2. **Padrão harmônico** → Ajuste no editor de tabela de ondas (wavetable) ou use key tracking 100% no filtro

No exemplo: os harmônicos diminuem na região aguda, então:
- Use um filtro passa-baixa de 24dB com key tracking 100%
- Ajuste o ponto de corte para corresponder ao 8º harmônico aproximadamente

#### **Passo 8: Modulações de Frequência (Vibrato/LFO)**
Se você perceber uma variação subtil na afinação:
- Adicione um LFO com forma de onda senoidal
- Configure-o para modular a afinação fina do oscilador
- Ajuste a quantidade (depth) e a taxa (speed/frequency)

#### **Passo 9: Efeitos Estéreo**
Determine se o original tem diferenças entre canais esquerdo e direito usando **MS Voxengo**:
- Silencie o canal central — se ouve algo, há componente estéreo
- Técnicas para adicionar largura: unison, detuning, chorus, phaser, flanger, delay curto
- Pode ser útil testar várias para ver qual combina melhor

#### **Passo 10: Profundidade (Reverb/Delay)**
Adicione profundidade temporal:
- Detect a presença de delay curto e reverb
- **Aviso:** Reverb e delay mudam a percepção da duração da nota — você pode precisar voltar ao passo 4 para ajustar o envelope

### O Processo é Iterativo

Conforme você progride, frequentemente volta a passos anteriores:
- Adicionar reverb muda como você percebe o sustain
- Mudanças no timbre podem exigir reajustes de dinâmica
- O processo é de refinamento progressivo, não linear

### Síntese Subtrativa vs. Modelagem Física

- **Síntese subtrativa** (usada aqui): começa com uma forma de onda rica e remove características
  - Funciona bem para sons sintetizados
  
- **Modelagem física**: replica as leis da física que criam o som
  - Mais intuitiva para sons acústicos
  - Próximo vídeo abordará isso usando Vital e compressor Spect

---

## 🔗 Como se Conecta a Mim

Este vídeo é **extremamente relevante** para seu objetivo de música mastery e deve virar prática regular:

### 1. **Aplicação Direta ao Music Mastery System**
Você já tem o Song Analysis Framework e está gerando song logs. Este vídeo documenta exatamente o processo que você deveria estar aplicando: análise espectral, identificação de padrões (harmônicos vs. frequência), e reconstrução consciente do som. Isso eleva o song log de "o que observei" para "o que aprendi aplicável no meu workflow".

### 2. **Sound Design Como Vantagem Competitiva**
Você fatura R$3-3.5k por faixa de produção completa. Presets de qualidade superior = produção mais rápida e resultados melhores = potencial para elevar o preço e escalar para 3-4 faixas/mês (o único bottleneck pro R$20k/mês). Este framework economiza horas na procura por sounds — você *recria* o que precisa.

### 3. **Iteração e Refinamento vs. Procrastinação**
O vídeo reforça algo que você já sabe: o processo é iterativo (passos 1-10, depois volta). Mas a estrutura clara de feedback (comparação AB, análise espectral) **remove a ambiguidade que costuma paralysar**. Você sabe exatamente quando está perto do original. Isso combate o padrão de avoidance onde você toca levemente em algo, não tem certeza do progresso, e abandona.

### 4. **Aplicação Imediata em Seus Recalls**
Você tem recalls em produção (Eterno Amor, Te Falaria, Te Amo ponto, etc.). Quando chega a "aproveitar um sound/preset existente", este framework te dá o caminho: ao invés de gastar 3 horas experimentando, você:
1. Isola o som original (se disponível)
2. Analisa o espectro
3. Reconstrói com propósito

### 5. **O Que Fazer Agora**
- **Esta semana**: assista novamente com Logic aberto, pause em cada passo e adapte para seu workflow
- **Próxima faixa que produzir**: tente o processo completo (ou pelo menos passos 1-7) em um sound que você quer replicar
- **Song log futuro**: quando analisar uma faixa, note se consegue descrever a técnica de som design — isso vira aplicável

### ⚠️ Armadilha a Evitar
Este vídeo é **muito detalhado** — há um risco de cair no "estudo sem aplicação". A síntese subtrativa é profunda e você pode perder semanas estudando harmônicos sem gravar nada. Mantenha o foco: use como ferramenta para sounds específicos que você *precisa* recriar, não como currículo de sound design genérico.

---

