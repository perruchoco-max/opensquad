#!/usr/bin/env python3
"""
Script para migrar conteúdo usando Notion MCP e web scraping.
Integra com as ferramentas notion-fetch e notion-search via subprocess.
"""

import subprocess
import json
import time
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import re

# IDs dos bunkers
BUNKERS = {
    "Bunker 1": "e19169a1-1eaa-82b4-9a51-07ba8bfc68ef",
    "Bunker 2": "d30169a1-1eaa-83b2-8b38-07a371dc3aae",
    "Bunker 3": "fbd169a1-1eaa-8374-a3e4-878a6c3535f2",
    "Bunker 5": "716169a1-1eaa-8346-bff4-87e4cc1c1ad0",
}

class NotionMCPMigrator:
    def __init__(self):
        self.stats = {
            "total_processed": 0,
            "successful": 0,
            "failed": 0,
            "errors": []
        }

        self.scrape_session = requests.Session()
        self.scrape_session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })

    def fetch_bunker_data(self, bunker_id: str) -> Optional[Dict]:
        """Busca dados do bunker usando notion-fetch MCP."""
        try:
            result = subprocess.run(
                ["notion-fetch", f"collection://{bunker_id}"],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                error = f"Erro ao buscar bunker: {result.stderr}"
                print(f"[ERRO] {error}")
                self.stats["errors"].append(error)
                return None

            # Parse do output JSON
            output = result.stdout.strip()
            if output.startswith('{') or output.startswith('['):
                return json.loads(output)

            return None
        except Exception as e:
            error = f"Exceção ao buscar bunker {bunker_id}: {str(e)}"
            print(f"[ERRO] {error}")
            self.stats["errors"].append(error)
            return None

    def scrape_external_page(self, external_url: str) -> Optional[str]:
        """Faz web scraping do conteúdo da página externa."""
        try:
            print(f"    [SCRAPE] Acessando {external_url[:60]}...")
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
                main = soup.find('div', class_=re.compile('main|content|body|page', re.I))
            if not main:
                main = soup.find('div', {'role': 'main'})

            if main:
                content = main.get_text(separator='\n', strip=True)
            else:
                # Fallback: pega todo o texto do body
                body = soup.find('body')
                if body:
                    content = body.get_text(separator='\n', strip=True)
                else:
                    content = soup.get_text(separator='\n', strip=True)

            # Limpa espaços em branco
            lines = [line.strip() for line in content.split('\n') if line.strip()]
            content = '\n'.join(lines)

            # Limita tamanho
            if len(content) > 8000:
                content = content[:8000] + "\n\n[Conteúdo truncado...]"

            return content if content else None
        except Exception as e:
            print(f"    [ERRO] Falha ao scraping: {str(e)}")
            return None

    def extract_url_from_page_content(self, page_content: str) -> Optional[str]:
        """Extrai URL da página do Notion do conteúdo."""
        # Procura por URLs que contêm notion.site
        urls = re.findall(r'https?://[^\s<>"{}|\\^`\[\]]*\.notion\.site[^\s<>"{}|\\^`\[\]]*', page_content)
        if urls:
            return urls[0]
        return None

    def migrate_bunker(self, bunker_name: str, bunker_id: str):
        """Migra conteúdo de um bunker."""
        print(f"\n{'='*70}")
        print(f"Iniciando migração: {bunker_name}")
        print(f"ID: {bunker_id}")
        print(f"{'='*70}")

        # Fetch bunker data
        bunker_data = self.fetch_bunker_data(bunker_id)
        if not bunker_data:
            print("[ERRO] Falha ao buscar dados do bunker")
            return

        # Processa páginas
        pages = bunker_data if isinstance(bunker_data, list) else bunker_data.get('results', [])
        print(f"[INFO] {len(pages)} páginas encontradas")

        if not pages:
            print("[AVISO] Nenhuma página encontrada")
            return

        for i, page in enumerate(pages[:5], 1):  # Teste com primeiras 5
            page_id = page.get('id') or page.get('url')
            title = page.get('title') or page.get('Nome', 'Sem título')

            print(f"\n[{i}/{min(5, len(pages))}] {title}")

            self.stats["total_processed"] += 1

            if not page_id:
                print("    [ERRO] Página sem ID")
                self.stats["failed"] += 1
                continue

            # Fetch page details para extrair URL
            page_details = self._fetch_page_details(page_id)
            if not page_details:
                print("    [ERRO] Falha ao obter detalhes da página")
                self.stats["failed"] += 1
                continue

            # Extrai URL externa
            external_url = self.extract_url_from_page_content(json.dumps(page_details))
            if not external_url:
                print("    [AVISO] Nenhuma URL externa encontrada")
                self.stats["failed"] += 1
                continue

            print(f"    [URL] {external_url[:60]}...")

            # Scrape content
            content = self.scrape_external_page(external_url)
            if not content:
                print("    [ERRO] Falha ao fazer scraping")
                self.stats["failed"] += 1
                continue

            print(f"    [SCRAP] Extraído: {len(content)} caracteres")

            # Update page via notion-update-page MCP
            if self._update_page_content(page_id, content):
                print("    [✓] Página atualizada com sucesso")
                self.stats["successful"] += 1
            else:
                self.stats["failed"] += 1

            time.sleep(1)

    def _fetch_page_details(self, page_id: str) -> Optional[Dict]:
        """Busca detalhes de uma página."""
        try:
            result = subprocess.run(
                ["notion-fetch", page_id],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                return None

            output = result.stdout.strip()
            if output.startswith('{'):
                return json.loads(output)

            return None
        except Exception as e:
            print(f"    [ERRO] Falha ao fetch página {page_id}: {str(e)}")
            return None

    def _update_page_content(self, page_id: str, content: str) -> bool:
        """Atualiza conteúdo da página via MCP."""
        try:
            # Limita conteúdo a 2000 caracteres por bloco
            content_truncated = content[:2000]

            result = subprocess.run(
                ["notion-update-page", page_id, "--content", content_truncated],
                capture_output=True,
                text=True,
                timeout=30
            )

            return result.returncode == 0
        except Exception as e:
            print(f"    [ERRO] Falha ao atualizar: {str(e)}")
            return False

    def print_report(self):
        """Imprime relatório."""
        print(f"\n\n{'='*70}")
        print(f"RELATÓRIO DE MIGRAÇÃO")
        print(f"{'='*70}")
        print(f"Total processado:  {self.stats['total_processed']}")
        print(f"Sucesso:           {self.stats['successful']}")
        print(f"Falhas:            {self.stats['failed']}")

        if self.stats['total_processed'] > 0:
            rate = (self.stats['successful'] / self.stats['total_processed'] * 100)
            print(f"Taxa de sucesso:   {rate:.1f}%")

        if self.stats['errors']:
            print(f"\nErros encontrados:")
            for error in self.stats['errors'][:5]:
                print(f"  - {error}")

        print(f"{'='*70}\n")

def main():
    print("Iniciando migração de conteúdo com Notion MCP...")
    print(f"Bunkers: {len(BUNKERS)}")

    migrator = NotionMCPMigrator()

    for bunker_name, bunker_id in BUNKERS.items():
        migrator.migrate_bunker(bunker_name, bunker_id)

    migrator.print_report()

if __name__ == "__main__":
    main()
