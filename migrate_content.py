#!/usr/bin/env python3
"""
Script para migrar conteúdo de roteiros entre workspaces do Notion.
Usa Notion API via requests e web scraping.
"""

import os
import sys
import json
import time
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import re

# Token do Notion
NOTION_TOKEN = "ntn_c60671341229r0PxmmdICq6Uiq4WZSNLDo0KDsFSABv9ds"

# IDs dos bunkers
BUNKERS = {
    "Bunker 1": "e19169a1-1eaa-82b4-9a51-07ba8bfc68ef",
    "Bunker 2": "d30169a1-1eaa-83b2-8b38-07a371dc3aae",
    "Bunker 3": "fbd169a1-1eaa-8374-a3e4-878a6c3535f2",
    "Bunker 5": "716169a1-1eaa-8346-bff4-87e4cc1c1ad0",
}

class NotionMigrator:
    def __init__(self):
        self.stats = {
            "total_processed": 0,
            "successful": 0,
            "failed": 0,
            "errors": []
        }

        self.notion_headers = {
            "Authorization": f"Bearer {NOTION_TOKEN}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

        self.scrape_session = requests.Session()
        self.scrape_session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })

    def query_database(self, database_id: str) -> List[Dict]:
        """Busca todas as páginas de uma database/coleção."""
        url = "https://api.notion.com/v1/databases/{}/query".format(database_id)
        pages = []
        start_cursor = None

        try:
            while True:
                payload = {}
                if start_cursor:
                    payload["start_cursor"] = start_cursor

                response = requests.post(
                    url,
                    headers=self.notion_headers,
                    json=payload,
                    timeout=30
                )

                if response.status_code != 200:
                    error = f"Erro na query: {response.status_code} - {response.text}"
                    print(f"[ERRO] {error}")
                    self.stats["errors"].append(error)
                    break

                data = response.json()
                pages.extend(data.get("results", []))

                if not data.get("has_more"):
                    break

                start_cursor = data.get("next_cursor")
                time.sleep(0.5)  # Rate limiting

            return pages
        except Exception as e:
            error = f"Erro ao query database {database_id}: {str(e)}"
            print(f"[ERRO] {error}")
            self.stats["errors"].append(error)
            return []

    def get_page_details(self, page_id: str) -> Optional[Dict]:
        """Obtém detalhes de uma página."""
        url = f"https://api.notion.com/v1/pages/{page_id}"

        try:
            response = requests.get(
                url,
                headers=self.notion_headers,
                timeout=30
            )

            if response.status_code == 200:
                return response.json()
            else:
                print(f"[ERRO] Falha ao obter página {page_id}: {response.status_code}")
                return None
        except Exception as e:
            print(f"[ERRO] Erro ao obter página {page_id}: {str(e)}")
            return None

    def get_page_content(self, page_id: str) -> str:
        """Obtém o conteúdo de texto de uma página."""
        url = f"https://api.notion.com/v1/blocks/{page_id}/children"
        blocks = []

        try:
            while True:
                response = requests.get(
                    url,
                    headers=self.notion_headers,
                    timeout=30
                )

                if response.status_code != 200:
                    break

                data = response.json()
                blocks.extend(data.get("results", []))

                if not data.get("has_more"):
                    break

                url = f"https://api.notion.com/v1/blocks/{page_id}/children?start_cursor={data.get('next_cursor')}"
                time.sleep(0.3)

            # Extrai texto dos blocos
            text_content = []
            for block in blocks:
                block_type = block.get("type")
                block_data = block.get(block_type, {})

                if block_type == "paragraph":
                    text_content.append(self._extract_rich_text(block_data.get("rich_text", [])))
                elif block_type == "heading_1":
                    text_content.append("# " + self._extract_rich_text(block_data.get("rich_text", [])))
                elif block_type == "heading_2":
                    text_content.append("## " + self._extract_rich_text(block_data.get("rich_text", [])))
                elif block_type == "heading_3":
                    text_content.append("### " + self._extract_rich_text(block_data.get("rich_text", [])))
                elif block_type == "bulleted_list_item":
                    text_content.append("- " + self._extract_rich_text(block_data.get("rich_text", [])))
                elif block_type == "numbered_list_item":
                    text_content.append("1. " + self._extract_rich_text(block_data.get("rich_text", [])))

            return "\n".join(text_content)
        except Exception as e:
            print(f"[ERRO] Erro ao obter conteúdo da página {page_id}: {str(e)}")
            return ""

    def _extract_rich_text(self, rich_text_array: List) -> str:
        """Extrai texto de um array de rich_text."""
        text_parts = []
        for rt in rich_text_array:
            if rt.get("type") == "text":
                text_parts.append(rt["text"]["content"])
            elif rt.get("type") == "mention":
                text_parts.append(rt.get("plain_text", ""))
            elif rt.get("type") == "equation":
                text_parts.append(rt.get("plain_text", ""))
        return "".join(text_parts)

    def extract_external_url_from_title(self, page_id: str) -> Optional[str]:
        """Extrai URL externa do link no título."""
        page = self.get_page_details(page_id)
        if not page:
            return None

        properties = page.get("properties", {})
        title_prop = properties.get("Nome", {})

        if title_prop.get("type") == "title":
            rich_text = title_prop.get("title", [])
            for rt in rich_text:
                if rt.get("type") == "text":
                    text_obj = rt.get("text", {})
                    link = text_obj.get("link")
                    if link and "notion.site" in link.get("url", ""):
                        return link["url"]

        return None

    def scrape_external_page(self, external_url: str) -> Optional[str]:
        """Faz web scraping do conteúdo da página externa."""
        try:
            print(f"    [WEB] Fazendo scraping de {external_url}...")
            response = self.scrape_session.get(external_url, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            # Remove scripts e styles
            for script in soup(["script", "style"]):
                script.decompose()

            # Encontra o conteúdo principal
            content = ""

            # Tenta encontrar elemento principal
            main = soup.find(['main', 'article'])
            if not main:
                main = soup.find('div', class_=re.compile('main|content|body', re.I))
            if not main:
                main = soup.find('div', {'role': 'main'})

            if main:
                content = main.get_text(separator='\n', strip=True)
            else:
                content = soup.get_text(separator='\n', strip=True)

            # Limpa espaços em branco
            lines = [line.strip() for line in content.split('\n') if line.strip()]
            content = '\n'.join(lines)

            # Limita tamanho
            if len(content) > 10000:
                content = content[:10000] + "\n[Conteúdo truncado...]"

            return content if content else None
        except Exception as e:
            print(f"    [ERRO] Falha ao scraping {external_url}: {str(e)}")
            return None

    def update_page_content(self, page_id: str, content: str) -> bool:
        """Atualiza conteúdo da página no Notion."""
        try:
            # Cria um bloco de parágrafo com o conteúdo
            url = f"https://api.notion.com/v1/blocks/{page_id}/children"

            # Divide o conteúdo em parágrafos
            paragraphs = content.split('\n\n')
            children = []

            for para in paragraphs[:50]:  # Limita a 50 parágrafos
                if para.strip():
                    children.append({
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": para.strip()[:2000]  # Notion tem limite de 2000 chars
                                    }
                                }
                            ]
                        }
                    })

            if not children:
                return False

            payload = {"children": children}

            response = requests.patch(
                url,
                headers=self.notion_headers,
                json=payload,
                timeout=30
            )

            if response.status_code != 200:
                print(f"    [ERRO] Falha ao atualizar: {response.status_code} - {response.text}")
                return False

            return True
        except Exception as e:
            print(f"    [ERRO] Erro ao atualizar página: {str(e)}")
            return False

    def migrate_bunker(self, bunker_name: str, bunker_id: str):
        """Migra conteúdo de um bunker completo."""
        print(f"\n{'='*70}")
        print(f"Iniciando migração: {bunker_name}")
        print(f"ID: {bunker_id}")
        print(f"{'='*70}")

        # Query database
        pages = self.query_database(bunker_id)
        print(f"\n[INFO] {len(pages)} páginas encontradas")

        for i, page in enumerate(pages, 1):
            page_id = page.get('id', '')
            title = "Sem título"

            # Extrai título
            props = page.get('properties', {})
            if 'Nome' in props:
                nome_prop = props['Nome'].get('title', [])
                if nome_prop:
                    title = nome_prop[0].get('plain_text', 'Sem título')

            print(f"\n[{i}/{len(pages)}] {title}")

            self.stats["total_processed"] += 1

            # Extrai URL externa
            external_url = self.extract_external_url_from_title(page_id)
            if not external_url:
                print("    [AVISO] Nenhuma URL externa encontrada no título")
                continue

            print(f"    [URL] {external_url}")

            # Faz scraping
            content = self.scrape_external_page(external_url)
            if not content:
                print("    [ERRO] Falha ao fazer scraping")
                self.stats["failed"] += 1
                continue

            print(f"    [SCRAP] Extraído: {len(content)} caracteres")

            # Atualiza página
            if self.update_page_content(page_id, content):
                print("    [✓] Página atualizada com sucesso")
                self.stats["successful"] += 1
            else:
                self.stats["failed"] += 1

            # Rate limiting
            time.sleep(1)

    def print_report(self):
        """Imprime relatório de progresso."""
        print(f"\n\n{'='*70}")
        print(f"RELATÓRIO FINAL")
        print(f"{'='*70}")
        print(f"Total processado:  {self.stats['total_processed']}")
        print(f"Sucesso:           {self.stats['successful']}")
        print(f"Falhas:            {self.stats['failed']}")
        print(f"Taxa de sucesso:   {(self.stats['successful'] / max(1, self.stats['total_processed']) * 100):.1f}%")

        if self.stats['errors']:
            print(f"\nPrimeiros erros:")
            for error in self.stats['errors'][:5]:
                print(f"  - {error}")

        print(f"{'='*70}\n")

def main():
    print("Iniciando migração de conteúdo do Notion...")
    print(f"Token: {NOTION_TOKEN[:20]}...")
    print(f"Bunkers: {len(BUNKERS)}")

    migrator = NotionMigrator()

    for bunker_name, bunker_id in BUNKERS.items():
        migrator.migrate_bunker(bunker_name, bunker_id)

    migrator.print_report()

if __name__ == "__main__":
    main()
