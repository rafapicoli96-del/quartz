# 🎮 RPG Character Generator — Guia de Uso

## Resumo

Seu personagem é atualizado **automaticamente todo dia às 7h da manhã** ou você pode rodar manualmente quando quiser.

---

## ⚙️ AUTOMÁTICO (Daily Update)

**Status:** ✅ Ativado  
**Horário:** 7h da manhã  
**Logs:** `🎮-character.log` e `🎮-character-error.log`

### Como funciona:
1. Todo dia às 7h, o job executa automaticamente
2. Lê seus dados (Today.md, Work, Journals)
3. Gera imagem nova
4. Atualiza `🎮-character.png`
5. Você abre a nota `🎮 Character Status.md` e vê a imagem novo

### Gerenciar o job:

**Desativar (pausar):**
```bash
launchctl unload /Users/rafa/Library/LaunchAgents/com.rafa.rpg-character.plist
```

**Ativar novamente:**
```bash
launchctl load /Users/rafa/Library/LaunchAgents/com.rafa.rpg-character.plist
```

**Ver status:**
```bash
launchctl list | grep rpg
```

**Ver logs:**
```bash
tail -50 "/Users/rafa/Desktop/RAFA AI BRAIN/🎮-character.log"
tail -50 "/Users/rafa/Desktop/RAFA AI BRAIN/🎮-character-error.log"
```

**Mudar o horário:** Editar `/Users/rafa/Library/LaunchAgents/com.rafa.rpg-character.plist` e mudar `<key>Hour</key>` para outro número (0-23).

---

## 🖱️ MANUAL (On-Demand)

Roda quando você quer, instantaneamente:

```bash
cd "/Users/rafa/Desktop/RAFA AI BRAIN"
python3 "05 Skills/rpg-character-sd.py"
```

**Quando usar:**
- Depois de um dia importante (para ver update imediato)
- Para testar/debug
- Quando quiser ver a imagem novo sem esperar pelas 7h

---

## 📊 O que a imagem reflete

Seu personagem muda baseado em:

- **HP (Vida):** Tarefas pendentes, padrões de sono, exercício
- **Energy (Vigor):** Rotina matinal + meditação vs. busywork/álcool/lactose
- **Focus (Mana):** Trabalho real vs. avoidance/gaming

**Cores:**
- 🟡 **Ouro** = Legendary (HP 80+) — armadura brilha, divina
- 🟡 **Prata** = Strong (HP 60-80) — armadura nítida, celestial
- 🟣 **Roxo** = Balanced (HP 40-60) — neutro, focado
- 🔴 **Ferrugem** = Weakened (HP 20-40) — armadura deteriorada
- 💀 **Roxo escuro** = Cursed (HP < 20) — corrompido

---

## 🔄 Fluxo Diário

1. **Você vive sua vida** — faz tarefas, rotina, meditação, etc.
2. **Registra nos journals/Today.md** — como de costume
3. **Acorda às 7h** → script roda automaticamente
4. **Abre a nota Character Status** → vê seu personagem atualizado
5. **Reflection:** "Como estava meu dia pra merecer essa imagem?"

---

## 🛠️ Troubleshooting

**A imagem não mudou:**
- Verifique se você atualizou Today.md ou journals
- Verifique os logs: `tail -50 🎮-character.log`
- Rode manual pra testar: `python3 05 Skills/rpg-character-sd.py`

**Geração muito lenta:**
- Normal no Mac (2-3 minutos por imagem)
- Primeira rodada é mais lenta (modelo carrega na memória)

**Erro na geração:**
- Verifique `🎮-character-error.log`
- Certifique que tem internet (pra baixar modelo)
- Certifique que tem 8GB+ livres em disco

---

## 📝 Próximas Melhorias

- [ ] Adicionar mais detalhes visuais (acessórios baseados em habilidades)
- [ ] Sistema de "conquistas" visual (badges no personagem)
- [ ] Diferentes "classes" baseado em focus (Warrior, Mage, Rogue, etc)
- [ ] Animações simples (postura mudando baseado em status)

---

**Script criado:** 15 Abr 2026  
**Última atualização:** 15 Abr 2026
