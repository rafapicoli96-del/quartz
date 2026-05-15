# 06 People

Perfis das pessoas importantes da minha vida — clientes, amigos, parceiros de música, networking.

Cada nota é gerada a partir do export de conversa do WhatsApp + análise do Claude.

---

## Como adicionar uma pessoa

1. No WhatsApp: abra a conversa → `...` → **Exportar conversa** → sem mídia
2. Manda o `.txt` pro Claude no chat do Obsidian
3. Claude analisa e cria a nota aqui

---

## Pessoas

```dataview
TABLE role AS "Papel", last-contact AS "Último contato"
FROM "06 People"
WHERE file.name != "README"
SORT last-contact DESC
```
