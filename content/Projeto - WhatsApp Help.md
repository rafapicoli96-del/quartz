# Projeto — WhatsApp Help

> Sistema para sugerir respostas de WhatsApp no estilo do Rafa, com contexto de quem é cada pessoa.

---

## Como usar

1. Tira um print da conversa (ou descreve o que foi dito)
2. Fala pra mim: "me ajuda a responder o [nome]" ou "o que respondo aqui?"
3. Eu leio o contexto e te dou 2–3 sugestões prontas

---

## Arquivos do Sistema

| Arquivo | Função |
|---------|--------|
| `00 Notes/(C) Meu Estilo de Comunicação.md` | Perfil completo do estilo de comunicação do Rafa — gerado a partir de 11 chats reais |
| `05 Skills/whatsapp-responder.md` | Instruções de execução para o Claude |
| `06 People/[nome].md` | Perfil de cada pessoa (histórico, contexto, pendências) |

---

## Chats Analisados (Mai 2026)

- Daniel McLaughlin — cliente Pickup (EN)
- Karl Kerfoot — cliente Pickup (EN)
- Nick Cisneros — cliente Pickup (EN)
- Julio Mendoza — cliente BR
- Gabriel Guper — amigo próximo
- Rodrigo Deltoro — amigo próximo
- Peu — amigo próximo
- Hell_P — amigo próximo
- Lucas Vaz — amigo/colega
- Mari Sena — namorada
- Graziela — mãe

---

## Para Adicionar Mais Contexto

- Exportar novas conversas → colocar em `/Users/rafa/Documents/Whatsapp Responder/`
- Pedir: "atualiza meu perfil de comunicação com esses novos chats"
- Para atualizar o perfil de uma pessoa específica: "atualiza o perfil do [nome] com o histórico do WhatsApp"
