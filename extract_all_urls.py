#!/usr/bin/env python3
"""
EXTRAÇÃO DE 174 URLs - TAREFA URGENTE
Para cada bunker: listar TODAS as páginas e extrair URLs
"""

import json
import re
from typing import Dict, List, Optional
from datetime import datetime

BUNKER_IDS = {
    "Bunker 1": {
        "database_id": "057169a11eaa8317a11481f6e41d59bc",
        "collection_id": "e19169a1-1eaa-82b4-9a51-07ba8bfc68ef",
        "roteiros": "15-200",
        "expected_total": 44
    },
    "Bunker 2": {
        "database_id": "3a5169a11eaa83339475010f06c27836",
        "collection_id": "d30169a1-1eaa-83b2-8b38-07a371dc3aae",
        "roteiros": "201-251",
        "expected_total": 29
    },
    "Bunker 3": {
        "database_id": "63a169a11eaa827f8901819c562db674",
        "collection_id": "fbd169a1-1eaa-8374-a3e4-878a6c3535f2",
        "roteiros": "252-302",
        "expected_total": 51
    },
    "Bunker 5": {
        "database_id": "5e2169a11eaa82038bac0171e2479cc4",
        "collection_id": "716169a1-1eaa-8346-bff4-87e4cc1c1ad0",
        "roteiros": "401-450",
        "expected_total": 50
    }
}

class URLExtractor:
    """Extrai URLs de todas as páginas dos bunkers."""

    def __init__(self):
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "bunkers": {},
            "stats": {
                "total_found": 0,
                "total_expected": 174
            }
        }
        self.bunker_summaries = []

    def extract_urls_from_page_title(self, title_html: str) -> Optional[str]:
        """Extrai URL mention-page do título HTML."""
        if not title_html:
            return None

        # Padrão: <mention-page url="https://..."/>
        match = re.search(r'<mention-page url="(https://[^"]+)"', title_html)
        if match:
            return match.group(1)

        # Padrão alternativo: link direto
        match = re.search(r'(https://www\.notion\.so/[a-f0-9]+)', title_html)
        if match:
            return match.group(1)

        return None

    def extract_roteiro_number(self, title: str) -> Optional[str]:
        """Extrai número do roteiro do título."""
        # Padrão: ROTEIRO-123
        match = re.search(r'ROTEIRO-(\d+)', title)
        if match:
            return f"ROTEIRO-{match.group(1)}"
        return None

    def format_roteiro_entry(self, title: str, url: Optional[str]) -> Dict:
        """Formata entrada de roteiro."""
        roteiro_num = self.extract_roteiro_number(title) or "UNKNOWN"

        return {
            "roteiro": roteiro_num,
            "titulo": title.replace("@Não encontrado ", "").strip(),
            "url": url or "[URL não encontrada]",
            "tem_url": url is not None
        }

    def process_bunker(self, bunker_name: str, bundle_data: Dict) -> List[Dict]:
        """Processa um bunker e extrai URLs."""
        print(f"\n🔍 Processando {bunker_name}...")

        # Instruções para buscar as páginas
        print(f"   Collection ID: {bundle_data['collection_id']}")
        print(f"   Expected: {bundle_data['expected_total']} roteiros")
        print(f"   Roteiros esperados: {bundle_data['roteiros']}")

        # Resultado esperado da busca (será preenchido via notion-search)
        return []

    def print_instructions(self):
        """Imprime instruções para executar com notion-search."""
        print("\n" + "="*80)
        print("EXTRAÇÃO DE 174 URLs - INSTRUÇÕES DE EXECUÇÃO")
        print("="*80)

        print("\n📋 TAREFA: Executar notion-search para cada bunker")
        print("\nCada bunker precisa de:")
        print("  1. notion-search com query='ROTEIRO' para listar todas as páginas")
        print("  2. Para cada página: extrair mention-page URL do título")
        print("  3. Compilar lista final")

        print("\n🔧 FERRAMENTAS NECESSÁRIAS:")
        print("  ✓ notion-search: para buscar páginas")
        print("  ✓ Regex extraction: para URLs do título")
        print("  ✓ JSON compilation: para resultado final")

        print("\n📌 BUNKERS A PROCESSAR:")
        for bunker_name, bundle_data in BUNKER_IDS.items():
            print(f"  {bunker_name}: {bundle_data['expected_total']} roteiros ({bundle_data['roteiros']})")
            print(f"    Collection: {bundle_data['collection_id']}")

    def save_instructions(self):
        """Salva instruções em arquivo."""
        instructions = {
            "timestamp": datetime.now().isoformat(),
            "task": "Extract 174 URLs from 4 bunkers",
            "bunkers": BUNKER_IDS,
            "steps": [
                "1. Para cada bunker: fazer notion-search(data_source_url=collection://..., query='ROTEIRO')",
                "2. Coletar TODAS as páginas (pode ter múltiplas páginas de resultados)",
                "3. Para cada página: extrair URL do campo 'Nome' (mention-page link)",
                "4. Compilar em JSON final com todas as 174 URLs",
                "5. Gerar arquivo urls_todas_174_roteiros.json"
            ],
            "expected_output": {
                "Bunker 1": {"total": 44},
                "Bunker 2": {"total": 29},
                "Bunker 3": {"total": 51},
                "Bunker 5": {"total": 50}
            }
        }

        with open("/home/user/opensquad/url_extraction_instructions.json", 'w') as f:
            json.dump(instructions, f, indent=2, ensure_ascii=False)

        print("\n✅ Instruções salvas em: url_extraction_instructions.json")

def main():
    extractor = URLExtractor()

    print("\n" + "="*80)
    print("EXTRAÇÃO DE 174 URLs - PREPARAÇÃO")
    print("="*80)

    # Processar cada bunker
    for bunker_name, bundle_data in BUNKER_IDS.items():
        extractor.process_bunker(bunker_name, bundle_data)

    # Imprimir instruções
    extractor.print_instructions()

    # Salvar instruções
    extractor.save_instructions()

    print("\n" + "="*80)
    print("✅ PREPARAÇÃO COMPLETA")
    print("="*80)
    print("\n📝 Arquivo criado: url_extraction_instructions.json")
    print("\n⏭️  PRÓXIMO PASSO:")
    print("   Executar script de busca com notion-search para cada bunker")


if __name__ == "__main__":
    main()
