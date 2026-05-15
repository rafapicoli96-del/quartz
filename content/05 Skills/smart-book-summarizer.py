#!/usr/bin/env python3
"""
Smart Book Summarizer
Processa PDFs de qualquer tamanho e cria resumos em 6 seções (SINOPSE, INSIGHTS, RESUMO, TABELA, QUIZ, RESUMO COMPLETO)

Uso:
    python3 smart-book-summarizer.py livro.pdf
    python3 smart-book-summarizer.py livro.pdf --selective [cap_inicio-cap_fim]
    python3 smart-book-summarizer.py livro.pdf --model haiku

Requer:
    - pip install anthropic pypdf
    - ANTHROPIC_API_KEY configurada no ambiente
"""

import sys
import os
import json
from pathlib import Path
from anthropic import Anthropic

try:
    from pypdf import PdfReader
except ImportError:
    print("❌ pypdf não instalado. Execute:")
    print("   pip install pypdf")
    sys.exit(1)

# ==================== CONFIG ====================
HAIKU_TOKENS_PER_1K = 0.80  # Preço relativo
SONNET_TOKENS_PER_1K = 3.00
CHUNK_PAGES = 50
TOKEN_LIMIT_SAFE = 180000  # Limite seguro de tokens por sessão

# ==================== CLASSES ====================

class BookSummarizer:
    def __init__(self, pdf_path: str, selective: str = None, model: str = "auto"):
        self.pdf_path = Path(pdf_path)
        self.model = model
        self.selective = selective

        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF não encontrado: {pdf_path}")

        self.client = Anthropic()
        self.pdf_reader = PdfReader(self.pdf_path)
        self.total_pages = len(self.pdf_reader.pages)
        self.book_title = self.pdf_path.stem

        # Extrair texto
        self.full_text = self._extract_text()
        self.token_estimate = len(self.full_text) // 4  # ~4 caracteres por token

    def _extract_text(self) -> str:
        """Extrai todo o texto do PDF"""
        text = ""
        for page_num, page in enumerate(self.pdf_reader.pages):
            text += f"\n\n--- Página {page_num + 1} ---\n"
            text += page.extract_text()
        return text

    def _get_strategy(self) -> dict:
        """Determina a estratégia baseado no tamanho"""
        strategy = {
            "total_pages": self.total_pages,
            "estimated_tokens": self.token_estimate,
            "is_large": self.total_pages > 150,
            "chunks": 1,
            "haiku_model": "claude-3-5-haiku-20241022",
            "sonnet_model": "claude-3-5-sonnet-20241022",
        }

        if self.total_pages < 100:
            strategy["method"] = "direct"
            strategy["description"] = f"✅ Pequeno ({self.total_pages} pgs) — processamento direto"
            strategy["model_choice"] = "sonnet"

        elif self.total_pages < 250:
            strategy["method"] = "chunked"
            strategy["chunks"] = (self.total_pages // CHUNK_PAGES) + 1
            strategy["description"] = f"📊 Médio ({self.total_pages} pgs) — {strategy['chunks']} chunks (Haiku) + consolidação (Sonnet)"
            strategy["model_choice"] = "hybrid"

        else:
            strategy["method"] = "selective"
            strategy["description"] = f"⚠️ Grande ({self.total_pages} pgs) — necessário escolher seções ou aceitar custo alto"
            strategy["model_choice"] = "ask"

        return strategy

    def show_strategy(self):
        """Mostra a estratégia escolhida"""
        strategy = self._get_strategy()
        print("\n" + "="*60)
        print(f"📚 LIVRO: {self.book_title}")
        print(f"📄 Páginas: {strategy['total_pages']}")
        print(f"🧠 Tokens estimados: {strategy['estimated_tokens']:,}")
        print("="*60)
        print(f"\n{strategy['description']}")
        print(f"Método: {strategy['method'].upper()}")
        print(f"Chunks: {strategy['chunks']}")
        print("="*60 + "\n")

        return strategy

    def _summarize_chunk(self, text: str, chunk_num: int = None) -> str:
        """Resumo de um chunk usando Haiku"""
        prompt = f"""Você é um assistente expert em resumo de livros.

Leia o seguinte texto (pode ser um capítulo ou seção de um livro) e faça um resumo estruturado com:
1. **Conceitos principais** (3-5 bullet points)
2. **Exemplos ou histórias**
3. **Aplicação prática**
4. **Conexões com outros conceitos** (se aplicável)

Seja conciso mas completo. Use markdown.

---

{text}

---

RESUMO ESTRUTURADO:"""

        message = self.client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        )

        return message.content[0].text

    def _consolidate_chunks(self, chunk_summaries: list) -> dict:
        """Consolida chunks em 6 seções usando Sonnet"""
        summaries_text = "\n\n---\n\n".join(chunk_summaries)

        prompt = f"""Você é um expert em estruturar resumos de livros.

Você recebeu vários resumos parciais de um livro chamado "{self.book_title}".
Sua tarefa é consolidar tudo em uma estrutura padrão de 6 seções:

1. **📌 SINOPSE** — resumo executivo (autor, tema, relevância, frase-chave) — máximo 150 palavras
2. **🎯 INSIGHTS PRINCIPAIS** — 8-10 conceitos transformadores do livro com 1-2 parágrafos cada
3. **📝 RESUMO DO LIVRO** — narrativa enxuta (arco da história + pilares principais) — ~300-400 palavras
4. **📖 RESUMO ENXUTO POR CAPÍTULO** — tabela com capítulos + ideia-chave (1 linha cada)
5. **🧠 QUIZ** — 12-15 perguntas sobre o livro com respostas ocultas em <details> HTML (quantas forem necessárias)
6. **📚 RESUMO COMPLETO** — o original preservado intacto

Aqui estão os resumos parciais:

{summaries_text}

---

Estruture em Markdown com as 6 seções completas. Seja prático, direto e rico em detalhes."""

        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "consolidated": message.content[0].text,
            "tokens_used": message.usage.output_tokens
        }

    def _direct_summarize(self) -> dict:
        """Resumo direto para livros pequenos"""
        prompt = f"""Você é um expert em estruturar resumos de livros.

Leia o seguinte livro e crie uma estrutura padrão de 6 seções:

1. **📌 SINOPSE** — resumo executivo (autor, tema, relevância, frase-chave) — máximo 150 palavras
2. **🎯 INSIGHTS PRINCIPAIS** — 8-10 conceitos transformadores com 1-2 parágrafos cada
3. **📝 RESUMO DO LIVRO** — narrativa enxuta (arco + pilares principais) — ~300-400 palavras
4. **📖 RESUMO ENXUTO POR CAPÍTULO** — tabela com capítulos + ideia-chave (1 linha cada)
5. **🧠 QUIZ** — 12-15 perguntas sobre o livro com respostas ocultas em <details> HTML
6. **📚 RESUMO COMPLETO** — análise detalhada preservada

LIVRO COMPLETO:

{self.full_text}

---

Estruture em Markdown. Seja prático, direto e rico em detalhes."""

        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "consolidated": message.content[0].text,
            "tokens_used": message.usage.output_tokens
        }

    def summarize(self) -> str:
        """Executa o resumo com a estratégia apropriada"""
        strategy = self.show_strategy()

        if strategy["method"] == "direct":
            print("🔄 Processando com Sonnet (direto)...\n")
            result = self._direct_summarize()

        elif strategy["method"] == "chunked":
            print(f"🔄 Processando {strategy['chunks']} chunks com Haiku...\n")
            chunk_summaries = []

            # Dividir em chunks
            chars_per_chunk = len(self.full_text) // strategy["chunks"]
            for i in range(strategy["chunks"]):
                start = i * chars_per_chunk
                end = (i + 1) * chars_per_chunk if i < strategy["chunks"] - 1 else len(self.full_text)
                chunk_text = self.full_text[start:end]

                print(f"  📄 Chunk {i+1}/{strategy['chunks']}...", end=" ", flush=True)
                summary = self._summarize_chunk(chunk_text, i+1)
                chunk_summaries.append(summary)
                print("✅")

            print(f"\n🔄 Consolidando com Sonnet...\n")
            result = self._consolidate_chunks(chunk_summaries)

        else:  # selective
            print("⚠️  Livro muito grande. Escolha uma opção:")
            print("1. Processar completo (pode gastar muitos tokens)")
            print("2. Especificar capítulos/páginas")
            choice = input("\nOpção (1 ou 2): ").strip()

            if choice == "1":
                print("\n🔄 Processando completo...\n")
                result = self._direct_summarize()
            else:
                print("\n⏭️  Operação cancelada.")
                return None

        return result["consolidated"]

    def save_result(self, content: str):
        """Salva o resultado em arquivo"""
        output_dir = Path("00 Notes/Books")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / f"{self.book_title} - Resumo Completo.md"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"\n✅ PRONTO! Resumo salvo em:")
        print(f"   {output_file.absolute()}\n")


# ==================== MAIN ====================

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 smart-book-summarizer.py livro.pdf [--selective] [--model haiku|sonnet]")
        print("\nExemplo:")
        print("  python3 smart-book-summarizer.py meu_livro.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]
    selective = "--selective" in sys.argv
    model = "auto"

    if "--model" in sys.argv:
        idx = sys.argv.index("--model")
        if idx + 1 < len(sys.argv):
            model = sys.argv[idx + 1]

    try:
        summarizer = BookSummarizer(pdf_path, selective=selective, model=model)
        result = summarizer.summarize()

        if result:
            summarizer.save_result(result)

    except FileNotFoundError as e:
        print(f"❌ Erro: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro ao processar: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
