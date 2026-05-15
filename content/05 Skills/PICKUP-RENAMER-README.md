# Pickup Track Renamer — Shared with Friends

Este é um sistema completo para renomear tracks de Pickup Music automaticamente. Você pode compartilhar isso com seus amigos que também trabalham com o mesmo sistema de nomeação.

---

## 3 Formas de Usar

### **Opção 1: ChatGPT/Claude (Recomendado — Nenhuma instalação)**

1. Abra [ChatGPT](https://chat.openai.com) ou [Claude](https://claude.ai)
2. Copie o conteúdo de `PICKUP-RENAMER-PROMPT.txt`
3. Cole no chat
4. Copie e cole a lista de arquivos que você quer renomear
5. Copie a lista de renames gerada

**Vantagem:** Funciona em qualquer máquina, nenhuma instalação, interface familiar.
**Tempo:** 2-3 minutos.

---

### **Opção 2: Script Python (Mais Rápido — Python 3 necessário)**

Requer: Python 3.6+ (já vem instalado em Mac/Linux, Windows precisa instalar)

#### No Mac ou Linux:

```bash
# 1. Copiar o script ou fazer download
curl -o rename_pickup.py "https://[seu-link-aqui]"

# 2. Rodar o script (com confirmação visual)
python3 rename_pickup.py /Users/seu_user/Downloads/PICKUP_rename/FUNK_BASS

# 3. Revisar o preview, digitar "yes" ou "y" para confirmar
```

#### No Windows (cmd ou PowerShell):

```powershell
# 1. Copiar o arquivo rename_pickup_shareable.py para o computador

# 2. Abrir CMD/PowerShell no folder com os arquivos de áudio

# 3. Rodar o script
python rename_pickup_shareable.py .
```

**Vantagem:** Muito mais rápido, executa localmente, sem depender de serviços online.
**Tempo:** 30 segundos.

---

### **Opção 3: Google Sheets + Script (Para Colaboração em Equipe)**

Se você e seus amigos querem compartilhar um sheet e validar nomes juntos:

1. Criar uma Google Sheet com colunas: `Original Name | Parsed Grade | Parsed Day | ... | New Name`
2. Usar a função `=REGEXMATCH()` ou fórmulas customizadas para validar componentes
3. Todos veem as mudanças em tempo real e podem sugerir correções

**Vantagem:** Colaborativo, todos veem em tempo real.
**Complexidade:** Alta — requer configuração.

---

## Convenção de Nomeação

Todos os 3 métodos seguem a mesma convenção:

```
(course_prefix)-(Grade#)-(Day#)-(Track_Description)-(BPM)-(Key)-(exercise_optional)
```

### Componentes

| Component | Format | Example |
|-----------|--------|---------|
| Course prefix | Fixed code | `LP-24-Interm_v2` |
| Grade | `G` + number | `G4` |
| Day | `D` + number | `D5` |
| Description | Words with `_` | `Good_Times` |
| BPM | Number | `85` |
| Key | Note + quality | `Emi`, `Am`, `C` |
| Exercise | Optional `ExN` or `Jam` | `Ex1`, omit if absent |

### Exemplos de Conversão

```
INPUT:  Intermed G4D5 Good Times 85 Emi ex1.wav
OUTPUT: LP-24-Interm_v2-G4-D5-Good_Times-85-Emi-Ex1.wav

INPUT:  G3D2 Slow Blues 120 Am.wav
OUTPUT: LP-24-Interm_v2-G3-D2-Slow_Blues-120-Am.wav

INPUT:  grade1 day3 expression 100 c.wav
OUTPUT: LP-24-Interm_v2-G1-D3-Expression-100-C.wav
```

---

## Cursos Conhecidos

O sistema conhece estes prefixos:

| Course | Prefix |
|--------|--------|
| LP 24 Intermediate v2 | `LP-24-Interm_v2` |

Se você tem outro curso, você pode especificar manualmente:

**ChatGPT:** Diga ao Claude qual é o prefix no chat.
**Script:** `python3 rename_pickup.py /path --course MY-CUSTOM-PREFIX`

---

## Dicas para Uso

### ✅ Formatos que funcionam bem
- `Intermed G4D5 Good Times 85 Emi ex1.wav`
- `G4-D5-Good-Times-85-Emi.wav` (hyphens são OK)
- `grade4 day5 good times 85 emi jam.wav` (case-insensitive)
- `G1D3 Expression 100 C` (sem extensão é detectada automaticamente)

### ⚠️ Formatos problemáticos
- `G4D5 ??? 85 Emi` ← descrição vazia (será sinalizado)
- `Intermed G4D5 85` ← sem key (será sinalizado)
- `G4D5 Good Times Emi` ← sem BPM (será sinalizado)

Se um arquivo não puder ser parseado, o sistema vai **sinalizar para revisão manual** — você pode então fornecer os componentes faltantes.

---

## Suporte & Customização

Se você quer adicionar mais cursos ou mudar a lógica:

1. **Script Python:** Edite `COURSE_PREFIXES` no início do arquivo
2. **ChatGPT:** Diga ao Claude qual é o novo curso na primeira mensagem
3. **Lógica:** Quer mudar como o parsing funciona? Você pode refinar o script ou avisar ao Rafa para atualizar a versão compartilhada

---

## Quick Links

- **Prompt para ChatGPT:** `PICKUP-RENAMER-PROMPT.txt`
- **Script Python:** `rename_pickup_shareable.py`
- **Este README:** `PICKUP-RENAMER-README.md`

---

## Troubleshooting

### Python não encontrado (Mac/Linux)
```bash
# Instalar Python via Homebrew
brew install python3

# Checar versão
python3 --version
```

### Python não encontrado (Windows)
1. Fazer download do [Python.org](https://www.python.org/downloads/)
2. Instalar, certificando-se de marcar "Add Python to PATH"
3. Reiniciar o CMD/PowerShell
4. Rodar `python --version` para confirmar

### Script roda mas não vê nenhum arquivo
- Certifique-se que os arquivos têm extensão `.wav`, `.mp3`, `.aiff`, `.m4a`, ou `.flac`
- Copie o caminho exato (pode ter espaços — use aspas): `python3 rename_pickup.py "/path/with spaces"`

### Alguns arquivos são sinalizados como "Missing components"
- Abra o script e edite os nomes manualmente no prompt do ChatGPT
- Ou revise o arquivo original e certifique-se que tem Grade, Day, Description, BPM, e Key

---

**Versão:** 1.0 (Abril 2026)
**Mantido por:** Rafa & amigos de Pickup
