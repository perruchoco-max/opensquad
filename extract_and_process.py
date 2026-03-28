#!/usr/bin/env python3
"""
Script para extrair URLs de páginas do Notion e processar migração.
Usa a estrutura dos Laboratórios para encontrar as páginas.
"""

import re
import json
from typing import List, Dict, Optional

# UUIDs dos Laboratórios
LABORATORIES = {
    "Bunker 1": "70c169a1-1eaa-822c-889c-01e8a17ae067",
    "Bunker 2": "c10169a1-1eaa-82d0-b639-81ae945e809f",
    "Bunker 3": "4b4169a1-1eaa-82fb-aa6f-81e5386617a8",
    "Bunker 5": "fd0169a1-1eaa-83e5-b265-81ef32f37bee",
}

class PageExtractor:
    """Extrai URLs de páginas do conteúdo Notion."""

    @staticmethod
    def extract_page_urls(content: str) -> List[str]:
        """Extrai URLs de mention-page do conteúdo."""
        pattern = r'<mention-page url="(https://www\.notion\.so/[a-f0-9]+)"\s*/?>'
        return re.findall(pattern, content)

    @staticmethod
    def convert_notion_url_to_id(url: str) -> str:
        """Converte URL notion para ID."""
        # URL format: https://www.notion.so/0983e471869a4f36976f502b10259402
        match = re.search(r'notion\.so/([a-f0-9]+)', url)
        if match:
            uuid = match.group(1)
            # Converte para formato com hífens
            if len(uuid) == 32:
                return f"{uuid[0:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:32]}"
        return url

    @staticmethod
    def format_page_id(page_url: str) -> str:
        """Formata ID da página para uso na API Notion."""
        # Extrai o hash e converte para UUID format
        match = re.search(r'notion\.so/([a-f0-9]+)(\?|$)', page_url)
        if match:
            hex_id = match.group(1)
            if len(hex_id) == 32:
                return f"{hex_id[0:8]}{hex_id[8:12]}{hex_id[12:16]}{hex_id[16:20]}{hex_id[20:32]}"
        return page_url


# Conteúdo do Laboratório Bunker 1 (extraído acima)
BUNKER_1_CONTENT = """<mention-page url="https://www.notion.so/0983e471869a4f36976f502b10259402"/>
<mention-page url="https://www.notion.so/68e940bc71f74ab2a107695ede7a46ea"/>
<mention-page url="https://www.notion.so/8d21832dfcf64ce6854c45364300697e"/>
<mention-page url="https://www.notion.so/a54707473b6143cab2b7890b83d9595d"/>
<mention-page url="https://www.notion.so/d53426058b0a4d1b89b45b8c4f9b194e"/>
<mention-page url="https://www.notion.so/7b4a032fc64e4c3fac9da8380d3f778d"/>
<mention-page url="https://www.notion.so/0c1a6b8c2e6c44269b5053af90868252"/>
<mention-page url="https://www.notion.so/c3fcb9ee61a7475fbd5902d33f941d10"/>
<mention-page url="https://www.notion.so/e065116b00eb4332b5cccb7138c51efc"/>
<mention-page url="https://www.notion.so/f214b7c8b00a4cd988c5497d6c15e0ab"/>
<mention-page url="https://www.notion.so/d4f485ae5f86420fb37185cb79fde05a"/>
<mention-page url="https://www.notion.so/e06a9f84d4674d238e6b6e936ffff730"/>
<mention-page url="https://www.notion.so/cd502abc100a4cf7a6fb119c4214b9f2"/>
<mention-page url="https://www.notion.so/dd443eb33307499a988bdde66481b376"/>
<mention-page url="https://www.notion.so/10b2f64495ea47e2b8e1b2306fa49781"/>
<mention-page url="https://www.notion.so/63eb1a9686a7407fb1879b386590ee26"/>
<mention-page url="https://www.notion.so/3ba90ebe4287433f8491f4899ce99463"/>
<mention-page url="https://www.notion.so/3c3968dae2024afcbc9afc3304d6429f"/>
<mention-page url="https://www.notion.so/0f34e8a00faf4f6795c4b667932e748e"/>
<mention-page url="https://www.notion.so/4f3b0fb05615415bbdfbbde89af34656"/>"""


def main():
    print("="*70)
    print("EXTRATOR DE PÁGINA DO NOTION")
    print("="*70)

    extractor = PageExtractor()

    # Extrai URLs do Bunker 1
    urls = extractor.extract_page_urls(BUNKER_1_CONTENT)

    print(f"\n[INFO] Páginas encontradas no Bunker 1: {len(urls)}")
    print(f"\nPrimeiras 5 páginas (para teste):")

    for i, url in enumerate(urls[:5], 1):
        page_id = extractor.convert_notion_url_to_id(url)
        print(f"  [{i}] URL: {url}")
        print(f"      ID:  {page_id}")

    # Salva em JSON para processamento
    data = {
        "bunker": "Bunker 1",
        "lab_id": LABORATORIES["Bunker 1"],
        "total_pages": len(urls),
        "pages": [
            {
                "order": i,
                "url": url,
                "id": extractor.convert_notion_url_to_id(url)
            }
            for i, url in enumerate(urls, 1)
        ]
    }

    output_file = "/home/user/opensquad/bunker1_pages.json"
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"\n[✓] Dados salvos em: {output_file}")
    print(f"[INFO] Total de páginas no Bunker 1: {len(urls)}")
    print(f"[PRÓXIMO] Usar notion-fetch para processar cada página")

    print("\n" + "="*70)


if __name__ == "__main__":
    main()
