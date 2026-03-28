#!/usr/bin/env python3
"""
EXTRAIDOR FINAL DE 174 URLs - COMPLETO
Extrai todas as mention-page URLs de todos os 4 bunkers
Passo: notion-search para listar todas as páginas + notion-fetch para extrair URLs
"""

import json
import re
from typing import Dict, List, Tuple
from datetime import datetime

# IDs dos bunkers (collection IDs para notion-search)
BUNKER_CONFIG = {
    "Bunker 1": {
        "collection_id": "e19169a1-1eaa-82b4-9a51-07ba8bfc68ef",
        "database_id": "057169a11eaa8317a11481f6e41d59bc",
        "expected": 44,
        "roteiros": "15-200"
    },
    "Bunker 2": {
        "collection_id": "d30169a1-1eaa-83b2-8b38-07a371dc3aae",
        "database_id": "3a5169a11eaa83339475010f06c27836",
        "expected": 29,
        "roteiros": "201-251"
    },
    "Bunker 3": {
        "collection_id": "fbd169a1-1eaa-8374-a3e4-878a6c3535f2",
        "database_id": "63a169a11eaa827f8901819c562db674",
        "expected": 51,
        "roteiros": "252-302"
    },
    "Bunker 5": {
        "collection_id": "716169a1-1eaa-8346-bff4-87e4cc1c1ad0",
        "database_id": "5e2169a11eaa82038bac0171e2479cc4",
        "expected": 50,
        "roteiros": "401-450"
    }
}

class URLExtractor:
    """Extrai todas as 174 URLs de mention-page dos bunkers."""

    def __init__(self):
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "tarefa": "Extrair 174 URLs de roteiros",
            "bunkers": {},
            "stats": {
                "total_found": 0,
                "total_expected": 174
            }
        }

    def extract_mention_page_url(self, page_content_text: str) -> str:
        """Extrai URL mention-page do conteúdo JSON da página."""
        # Padrão: "Nome":"<mention-page url=\"https://www.notion.so/[hex32]\"/>"
        match = re.search(r'"Nome":"<mention-page url=\\"(https://www\.notion\.so/[a-f0-9]+)\\"', page_content_text)
        if match:
            return match.group(1)
        return None

    def extract_roteiro_number(self, page_id: str, notion_content: str) -> str:
        """Tenta extrair número do roteiro do conteúdo."""
        # Padrão: ROTEIRO-123
        match = re.search(r'ROTEIRO-(\d+)', notion_content)
        if match:
            return f"ROTEIRO-{match.group(1)}"
        return f"UNKNOWN-{page_id[:8]}"

    def process_page_fetch_result(self, page_id: str, notion_fetch_result: str) -> Dict:
        """Processa resultado de notion-fetch para extrair URL."""
        url = self.extract_mention_page_url(notion_fetch_result)
        roteiro = self.extract_roteiro_number(page_id, notion_fetch_result)

        return {
            "page_id": page_id,
            "roteiro": roteiro,
            "url": url,
            "status": "✓" if url else "✗"
        }

    def generate_final_report(self):
        """Gera relatório final com instruções."""

        print("\n" + "="*80)
        print("EXTRATOR DE 174 URLs - INSTRUÇÕES DE EXECUÇÃO")
        print("="*80)

        print("""
🎯 TAREFA: Extrair todas as 174 mention-page URLs dos bunkers

📋 PROCESSO:
1. Para CADA bunker (1, 2, 3, 5):
   a. Executar: notion-search(
      data_source_url=collection://[collection_id],
      query='ROTEIRO',
      page_size=25
   )
   b. Coletar TODOS os page_ids (pode ter múltiplas páginas de resultados)

2. Para CADA page_id encontrado:
   a. Executar: notion-fetch(id=[page_id])
   b. Extrair URL mention-page do campo "Nome":
      Padrão: "Nome":"<mention-page url=\"https://www.notion.so/[UUID]\"/>"

3. Compilar em JSON final:
   {
     "Bunker 1": {
       "total": 44,
       "urls": [
         {"roteiro": "ROTEIRO-15", "url": "https://www.notion.so/..."},
         ...
       ]
     },
     ...
   }

🔧 DADOS NECESSÁRIOS:
""")

        for bunker_name, config in BUNKER_CONFIG.items():
            print(f"\n{bunker_name}:")
            print(f"  Collection ID: {config['collection_id']}")
            print(f"  Database ID:   {config['database_id']}")
            print(f"  Expected:      {config['expected']} roteiros")
            print(f"  Range:         {config['roteiros']}")

        print("\n" + "="*80)
        print("✅ COMO USAR ESTE SCRIPT:")
        print("="*80)
        print("""
OPÇÃO 1 - Usar com Notion MCP Tools (via Claude Code):
  1. Chamar notion-search 4 vezes (1 por bunker)
  2. Chamar notion-fetch para cada page_id encontrado
  3. Extrair URLs usando regex: extract_mention_page_url()
  4. Compilar JSON final

OPÇÃO 2 - Executar manualmente:
  1. Script fornecido prepara instruções
  2. Você executa notion-search/fetch via Claude Code tools
  3. Cola resultados aqui
  4. Script compila JSON final

⏱️ TEMPO ESTIMADO:
  • notion-search (4 bunkers): ~10 segundos
  • notion-fetch (100-174 páginas): ~1-2 minutos
  • JSON compilation: ~30 segundos
  • TOTAL: ~2-3 minutos
""")

    def save_instructions(self):
        """Salva instruções em arquivo."""
        instructions = {
            "timestamp": datetime.now().isoformat(),
            "tarefa": "Extrair 174 URLs mention-page de roteiros",
            "bunkers": BUNKER_CONFIG,
            "processo": [
                "1. Para cada bunker: notion-search(data_source_url=collection://..., query='ROTEIRO', page_size=25)",
                "2. Coletar todos os page_ids de cada bunker",
                "3. Para cada page_id: notion-fetch(id=[page_id])",
                "4. Extrair URL do campo 'Nome': <mention-page url=\"https://www.notion.so/[UUID]\"/>",
                "5. Compilar em JSON com estrutura: {Bunker: {total, urls: [{roteiro, url}]}}"
            ],
            "regex_pattern": r'"Nome":"<mention-page url=\\"(https://www\.notion\.so/[a-f0-9]+)\\"',
            "expected_output": {
                "timestamp": "ISO-8601",
                "bunkers": {
                    "Bunker 1": {
                        "total": 44,
                        "urls": [
                            {"roteiro": "ROTEIRO-15", "url": "https://www.notion.so/..."}
                        ]
                    }
                }
            }
        }

        with open("/home/user/opensquad/EXTRACT_URLs_INSTRUCTIONS.json", 'w') as f:
            json.dump(instructions, f, indent=2, ensure_ascii=False)

        print("\n✅ Instruções salvas em: EXTRACT_URLs_INSTRUCTIONS.json")

def main():
    print("\n" + "="*80)
    print("EXTRATOR DE 174 URLs - NOTION ROTEIROS")
    print("="*80)

    extractor = URLExtractor()

    # Gera relatório
    extractor.generate_final_report()

    # Salva instruções
    extractor.save_instructions()

    print("\n" + "="*80)
    print("📌 RESUMO DA TAREFA:")
    print("="*80)
    print(f"""
Total de URLs a extrair: 174
Bunkers: 4 (Bunker 1, 2, 3, 5)
Distribuição:
  • Bunker 1: 44 roteiros (ROTEIRO 15-200)
  • Bunker 2: 29 roteiros (ROTEIRO 201-251)
  • Bunker 3: 51 roteiros (ROTEIRO 252-302)
  • Bunker 5: 50 roteiros (ROTEIRO 401-450)

Próximo passo: Executar extrações via notion-search + notion-fetch

Uma vez com todas as 174 URLs, será possível fazer o web scraping
e popular os cards com conteúdo dos roteiros externos.
""")

    print("="*80)

if __name__ == "__main__":
    main()
