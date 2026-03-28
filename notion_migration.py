#!/usr/bin/env python3
"""
Script de migração de conteúdo Notion com suporte a retry e tratamento de rede.
"""

import json
import time
import requests
from typing import List, Dict, Optional
from bs4 import BeautifulSoup
import re
import sys
from pathlib import Path

# Token Notion (fornecido no enunciado)
NOTION_TOKEN = "ntn_c60671341229r0PxmmdICq6Uiq4WZSNLDo0KDsFSABv9ds"

# IDs dos bunkers
BUNKERS = {
    "Bunker 1": "e19169a1-1eaa-82b4-9a51-07ba8bfc68ef",
    "Bunker 2": "d30169a1-1eaa-83b2-8b38-07a371dc3aae",
    "Bunker 3": "fbd169a1-1eaa-8374-a3e4-878a6c3535f2",
    "Bunker 5": "716169a1-1eaa-8346-bff4-87e4cc1c1ad0",
}

class NotionAPI:
    """API wrapper para Notion com retry logic."""

    def __init__(self, token: str, max_retries: int = 4):
        self.token = token
        self.max_retries = max_retries
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def _request_with_retry(self, method: str, url: str, **kwargs) -> Optional[dict]:
        """Faz requisição com retry em caso de erro de rede."""
        retries = [2, 4, 8, 16]  # delays em segundos

        for attempt in range(self.max_retries):
            try:
                response = requests.request(
                    method,
                    url,
                    headers=self.headers,
                    timeout=30,
                    **kwargs
                )

                # Success
                if response.status_code == 200:
                    return response.json()
                # Rate limit - retry
                elif response.status_code == 429:
                    if attempt < self.max_retries - 1:
                        wait = retries[attempt]
                        print(f"    [RATE LIMIT] Aguardando {wait}s...")
                        time.sleep(wait)
                        continue
                # Other error
                else:
                    print(f"    [HTTP {response.status_code}] {response.text[:100]}")
                    return None

            except requests.exceptions.Timeout:
                print(f"    [TIMEOUT] Tentativa {attempt + 1}/{self.max_retries}")
                if attempt < self.max_retries - 1:
                    wait = retries[attempt]
                    time.sleep(wait)
                    continue
            except requests.exceptions.ConnectionError as e:
                print(f"    [CONEXÃO] Erro de rede: {str(e)[:50]}")
                if attempt < self.max_retries - 1:
                    wait = retries[attempt]
                    time.sleep(wait)
                    continue
            except Exception as e:
                print(f"    [ERRO] {str(e)[:100]}")
                return None

        return None

    def query_database(self, database_id: str, start_cursor: str = None) -> Optional[dict]:
        """Query de uma database."""
        url = f"{self.base_url}/databases/{database_id}/query"
        payload = {}
        if start_cursor:
            payload["start_cursor"] = start_cursor

        return self._request_with_retry("POST", url, json=payload)

    def get_page(self, page_id: str) -> Optional[dict]:
        """Obtem detalhes de uma página."""
        url = f"{self.base_url}/pages/{page_id}"
        return self._request_with_retry("GET", url)

    def get_page_children(self, page_id: str) -> Optional[dict]:
        """Obtem blocos filhos de uma página."""
        url = f"{self.base_url}/blocks/{page_id}/children"
        return self._request_with_retry("GET", url)

    def append_block_children(self, page_id: str, children: list) -> Optional[dict]:
        """Adiciona blocos como filhos de uma página."""
        url = f"{self.base_url}/blocks/{page_id}/children"
        return self._request_with_retry("PATCH", url, json={"children": children})


class ContentMigrator:
    """Migrador de conteúdo Notion."""

    def __init__(self):
        self.notion = NotionAPI(NOTION_TOKEN)
        self.scraper = ContentScraper()

        self.stats = {
            "total": 0,
            "success": 0,
            "failed": 0,
            "errors": []
        }

    def migrate_bunker(self, bunker_name: str, bunker_id: str):
        """Migra conteúdo de um bunker."""
        print(f"\n{'='*70}")
        print(f"MIGRANDO: {bunker_name}")
        print(f"{'='*70}")

        # Query database
        pages = []
        start_cursor = None

        while True:
            result = self.notion.query_database(bunker_id, start_cursor)

            if not result:
                print("[ERRO] Falha ao query database")
                break

            pages.extend(result.get("results", []))

            if not result.get("has_more"):
                break

            start_cursor = result.get("next_cursor")
            time.sleep(1)

        print(f"[INFO] {len(pages)} páginas encontradas")

        # Processa cada página
        for i, page in enumerate(pages[:10], 1):  # Limite a 10 para teste
            self._process_page(page, i, len(pages[:10]))

    def _process_page(self, page: dict, idx: int, total: int):
        """Processa uma página individual."""
        page_id = page.get("id", "")
        title = self._extract_title(page)

        print(f"\n[{idx}/{total}] {title[:60]}")

        self.stats["total"] += 1

        if not page_id:
            print("    [ERRO] Sem ID")
            self.stats["failed"] += 1
            return

        # Extrai URL externa
        external_url = self._extract_external_url(page)

        if not external_url:
            print("    [AVISO] Sem URL externa")
            self.stats["failed"] += 1
            return

        print(f"    [URL] {external_url[:60]}...")

        # Scraping
        content = self.scraper.scrape(external_url)

        if not content:
            print("    [ERRO] Falha no scraping")
            self.stats["failed"] += 1
            return

        print(f"    [SCRAPE] {len(content)} caracteres")

        # Atualiza página
        if self._update_page_content(page_id, content):
            print("    [✓] Atualizado")
            self.stats["success"] += 1
        else:
            self.stats["failed"] += 1

        time.sleep(1)

    def _extract_title(self, page: dict) -> str:
        """Extrai título da página."""
        try:
            props = page.get("properties", {})
            nome_prop = props.get("Nome", {})

            if nome_prop.get("type") == "title":
                rich_text = nome_prop.get("title", [])
                if rich_text:
                    return rich_text[0].get("plain_text", "Sem título")

            return "Sem título"
        except:
            return "Sem título"

    def _extract_external_url(self, page: dict) -> Optional[str]:
        """Extrai URL externa do título."""
        try:
            props = page.get("properties", {})
            nome_prop = props.get("Nome", {})

            if nome_prop.get("type") == "title":
                rich_text = nome_prop.get("title", [])
                for rt in rich_text:
                    if rt.get("type") == "text":
                        text_obj = rt.get("text", {})
                        link = text_obj.get("link")
                        if link:
                            url = link.get("url", "")
                            if "notion.site" in url:
                                return url

            return None
        except:
            return None

    def _update_page_content(self, page_id: str, content: str) -> bool:
        """Atualiza conteúdo da página."""
        try:
            # Divide em parágrafos
            paragraphs = content.split("\n\n")
            children = []

            for para in paragraphs[:30]:  # Limita a 30 parágrafos
                if para.strip():
                    children.append({
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": para.strip()[:2000]
                                    }
                                }
                            ]
                        }
                    })

            if not children:
                return False

            result = self.notion.append_block_children(page_id, children)

            return result is not None
        except Exception as e:
            print(f"    [ERRO] {str(e)[:100]}")
            return False

    def print_report(self):
        """Imprime relatório."""
        print(f"\n\n{'='*70}")
        print(f"RELATÓRIO FINAL")
        print(f"{'='*70}")
        print(f"Total:    {self.stats['total']}")
        print(f"Sucesso:  {self.stats['success']}")
        print(f"Falhas:   {self.stats['failed']}")

        if self.stats['total'] > 0:
            rate = (self.stats['success'] / self.stats['total'] * 100)
            print(f"Taxa:     {rate:.1f}%")

        print(f"{'='*70}\n")


class ContentScraper:
    """Web scraper para conteúdo."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })

    def scrape(self, url: str) -> Optional[str]:
        """Faz scraping de uma URL."""
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Remove scripts e styles
            for script in soup(["script", "style"]):
                script.decompose()

            # Encontra conteúdo principal
            content = self._extract_main_content(soup)

            if not content:
                return None

            # Limpa espaços
            lines = [line.strip() for line in content.split('\n') if line.strip()]
            content = '\n\n'.join(lines)

            # Limita tamanho
            if len(content) > 8000:
                content = content[:8000] + "\n\n[Conteúdo truncado...]"

            return content
        except Exception as e:
            print(f"        [SCRAPE ERROR] {str(e)[:60]}")
            return None

    def _extract_main_content(self, soup) -> Optional[str]:
        """Extrai conteúdo principal."""
        # Tenta encontrar main
        main = soup.find(['main', 'article'])

        if not main:
            main = soup.find('div', class_=re.compile('main|content|body', re.I))

        if not main:
            main = soup.find('div', {'role': 'main'})

        if main:
            return main.get_text(separator='\n', strip=True)

        # Fallback
        body = soup.find('body')
        if body:
            return body.get_text(separator='\n', strip=True)

        return None


def main():
    print("MIGRAÇÃO DE CONTEÚDO NOTION")
    print("="*70)

    migrator = ContentMigrator()

    for bunker_name, bunker_id in BUNKERS.items():
        migrator.migrate_bunker(bunker_name, bunker_id)

    migrator.print_report()

if __name__ == "__main__":
    main()
