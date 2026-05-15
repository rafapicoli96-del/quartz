#!/bin/bash
# vault-backup.sh
# Cria um backup .zip do vault (sem plugins) e salva no iCloud Drive.
# Mantém os últimos 30 backups. Roda automaticamente via launchd todo dia às 02:00.

VAULT_PARENT="/Users/rafa/Desktop"
VAULT_NAME="RAFA AI BRAIN"
BACKUP_DIR="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Vault Backups"
LOG_FILE="$HOME/Library/Logs/vault-backup.log"
MAX_BACKUPS=30

DATE=$(date +"%Y-%m-%d_%H-%M")
BACKUP_FILE="$BACKUP_DIR/RAFA-AI-BRAIN_${DATE}.zip"

# Garante que a pasta de backup existe
mkdir -p "$BACKUP_DIR"

# Cria o zip excluindo plugins (são reinstalaveis e pesados)
cd "$VAULT_PARENT" || exit 1

zip -r "$BACKUP_FILE" "$VAULT_NAME" \
  --exclude "$VAULT_NAME/.obsidian/plugins/*" \
  -q

if [ $? -eq 0 ]; then
  SIZE=$(du -sh "$BACKUP_FILE" | cut -f1)
  echo "$(date '+%Y-%m-%d %H:%M') ✅ Backup criado: $(basename "$BACKUP_FILE") ($SIZE)" >> "$LOG_FILE"
else
  echo "$(date '+%Y-%m-%d %H:%M') ❌ Falha ao criar backup" >> "$LOG_FILE"
  exit 1
fi

# Mantém apenas os últimos MAX_BACKUPS backups
BACKUP_LIST=$(ls -t "$BACKUP_DIR"/*.zip 2>/dev/null)
BACKUP_COUNT=$(echo "$BACKUP_LIST" | grep -c ".zip" 2>/dev/null || echo 0)

if [ "$BACKUP_COUNT" -gt "$MAX_BACKUPS" ]; then
  echo "$BACKUP_LIST" | tail -n +$((MAX_BACKUPS + 1)) | xargs rm -f
  echo "$(date '+%Y-%m-%d %H:%M') 🗑️  Backups antigos removidos (mantendo últimos $MAX_BACKUPS)" >> "$LOG_FILE"
fi
