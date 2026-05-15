# Habit Bot — Telegram + IA

**Status:** Experimento pessoal | Prioridade: baixa (não compete com música/networking)

---

## O que é

Um bot no Telegram que recebe áudios e registra hábitos automaticamente.

Exemplo de uso: você manda um áudio no celular — *"Tomei todos os suplementos, meditei 20 min, não treinei hoje"* — e o bot transcreve, interpreta e atualiza uma planilha. Sem abrir app, sem preencher nada manualmente.

---

## Regra do projeto

**Fase 1 (única que importa agora): construir para uso próprio.**

Só passa pra monetização se estiver usando o bot todo dia por 30 dias seguidos. Sem exceção.

---

## Tech Stack (MVP)

| Componente | Ferramenta |
|---|---|
| Interface | Telegram Bot (via BotFather) |
| Automação | Make.com (plano gratuito suficiente pra testar) |
| Transcrição de áudio | OpenAI API — Whisper |
| Processamento de texto | OpenAI API — gpt-4o-mini |
| Banco de dados | Google Sheets |

**Custo inicial:** ~$5 de créditos na OpenAI. Nada mais.

---

## O que o bot precisa fazer (MVP)

1. Receber áudio no Telegram
2. Transcrever o áudio (Whisper)
3. Extrair dados do texto (GPT-4o-mini → JSON)
4. Inserir numa linha do Google Sheets
5. Responder com confirmação do que foi registrado

Nada além disso por enquanto.

---

## Colunas do Google Sheets (definir antes de codar)

> Preencher aqui quais hábitos você quer rastrear. Sugestão inicial:

- Data
- Meditação (✅ / ❌)
- Treino (✅ / ❌ / tipo)
- Suplementos (✅ / ❌)
- Proteína do dia (g)
- Observação livre

---

## Próximo passo único

Definir as colunas do Sheets acima. Só depois disso faz sentido criar o bot.

---

## Se chegar a monetizar (só depois do uso pessoal)

- Preço: R$14,90/mês
- Break-even: 6 usuários pagantes (~R$60-80/mês de custo de API + Make.com)
- Canal: vídeo de demonstração curto no Instagram/TikTok mostrando o bot em ação

---

## Referências da conversa de origem

- Conversa com Gemini: [[Possível Side Project com AI]]
- Ideia original: "Life RPG / Rastreador de Hábitos via Áudio/Telegram" (Ideia 2)
