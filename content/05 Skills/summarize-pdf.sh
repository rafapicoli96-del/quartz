#!/bin/bash
# Wrapper para smart-book-summarizer.py
# Uso: ./summarize-pdf.sh livro.pdf

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/smart-book-summarizer.py" "$@"
