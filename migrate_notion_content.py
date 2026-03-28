#!/usr/bin/env python3
"""
Script para migrar conteúdo de roteiros entre workspaces do Notion.
Busca templates em bunkers locais, extrai URLs de páginas externas,
faz web scraping e escreve o conteúdo de volta.
"""

import os
import sys
import json
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import subprocess

# Token do Notion
NOTION_TOKEN = "ntn_c60671341229r0PxmmdICq6Uiq4WZSNLDo0KDsFSABv9ds"

# IDs dos bunkers
BUNKERS = {
    "Bunker 1": "e19169a1-1eaa-82b4-9a51-07ba8bfc68ef",
    "Bunker 2": "d30169a1-1eaa-83b2-8b38-07a371dc3aae",
    "Bunker 3": "fbd169a1-1eaa-8374-a3e4-878a6c3535f2",
    "Bunker 5": "716169a1-1eaa-8346-bff4-87e4cc1c1ad0",
}

# Workspace público para scraping
PUBLIC_WORKSPACE = "https://seen-molecule-999.notion.site"

class NotionMigrator:
    def __init__(self):
        self.stats = {
            "total_processed": 0,
            "successful": 0,
            "failed": 0,
            "errors": []
        }
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })

    def fetch_bunker_pages(self, bunker_id: str) -> list:
        """Busca todas as páginas de um bunker usando Notion MCP."""
        try:
            # Usar ferramenta notion-search para buscar páginas
            result = subprocess.run(
                ["notion-search", "--token", NOTION_TOKEN, "--database", f"collection://{bunker_id}"],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                print(f"[ERRO] Falha ao buscar bunker {bunker_id}")
                self.stats["errors"].append(f"Bunker {bunker_id}: {result.stderr}")
                return []

            pages = json.loads(result.stdout) if result.stdout else []
            return pages
        except Exception as e:
            error = f"Erro ao buscar bunker {bunker_id}: {str(e)}"
            print(f"[ERRO] {error}")
            self.stats["errors"].append(error)
            return []

    def extract_external_url(self, page_url: str) -> str:
        """Extrai URL externa da página do Notion."""
        # A URL está no link do título - precisamos acessar a página para extrair
        try:
            response = self.session.get(page_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            # Procura por links externos
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if 'notion.site' in href and href != page_url:
                    return href

            return None
        except Exception as e:
            print(f"[ERRO] Falha ao extrair URL de {page_url}: {str(e)}")
            return None

    def scrape_external_page(self, external_url: str) -> str:
        """Faz web scraping do conteúdo da página externa."""
        try:
            response = self.session.get(external_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extrai texto principal
            # Remove scripts e styles
            for script in soup(["script", "style"]):
                script.decompose()

            # Encontra o conteúdo principal
            content = ""

            # Tenta encontrar elemento principal
            main = soup.find(['main', 'article']) or soup.find('div', class_=['main', 'content'])
            if main:
                content = main.get_text(separator='\n', strip=True)
            else:
                # Fallback: pega todo o texto
                content = soup.get_text(separator='\n', strip=True)

            # Limpa espaços em branco
            lines = [line.strip() for line in content.split('\n') if line.strip()]
            content = '\n'.join(lines)

            return content[:5000]  # Limita a 5000 caracteres
        except Exception as e:
            print(f"[ERRO] Falha ao fazer scraping de {external_url}: {str(e)}")
            return None

    def update_notion_page(self, page_id: str, content: str) -> bool:
        """Atualiza conteúdo da página no Notion usando MCP."""
        try:
            # Usa Notion MCP para atualizar a página
            result = subprocess.run(
                ["notion-update", "--token", NOTION_TOKEN, "--page", page_id, "--content", content],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode != 0:
                print(f"[ERRO] Falha ao atualizar página {page_id}")
                self.stats["errors"].append(f"Página {page_id}: {result.stderr}")
                return False

            return True
        except Exception as e:
            print(f"[ERRO] Erro ao atualizar página {page_id}: {str(e)}")
            self.stats["errors"].append(str(e))
            return False

    def migrate_bunker(self, bunker_name: str, bunker_id: str):
        """Migra conteúdo de um bunker completo."""
        print(f"\n{'='*60}")
        print(f"Iniciando migração: {bunker_name} (ID: {bunker_id})")
        print(f"{'='*60}")

        # Fetch pages from bunker
        pages = self.fetch_bunker_pages(bunker_id)
        print(f"[INFO] {len(pages)} páginas encontradas")

        for i, page in enumerate(pages, 1):
            print(f"\n[{i}/{len(pages)}] Processando: {page.get('Nome', 'Sem título')}")

            self.stats["total_processed"] += 1
            page_id = page.get('id') or page.get('url')

            if not page_id:
                print("[ERRO] Página sem ID")
                self.stats["failed"] += 1
                continue

            # Extract external URL
            external_url = self.extract_external_url(page_id)
            if not external_url:
                print("[AVISO] Nenhuma URL externa encontrada")
                continue

            print(f"[INFO] URL externa: {external_url}")

            # Scrape content
            content = self.scrape_external_page(external_url)
            if not content:
                print("[ERRO] Falha ao fazer scraping")
                self.stats["failed"] += 1
                continue

            print(f"[INFO] Conteúdo extraído: {len(content)} caracteres")

            # Update Notion page
            if self.update_notion_page(page_id, content):
                print("[✓] Página atualizada com sucesso")
                self.stats["successful"] += 1
            else:
                self.stats["failed"] += 1

            # Rate limiting
            time.sleep(1)

    def print_report(self):
        """Imprime relatório de progresso."""
        print(f"\n\n{'='*60}")
        print(f"RELATÓRIO FINAL")
        print(f"{'='*60}")
        print(f"Total processado: {self.stats['total_processed']}")
        print(f"Sucesso: {self.stats['successful']}")
        print(f"Falhas: {self.stats['failed']}")

        if self.stats['errors']:
            print(f"\nErros encontrados:")
            for error in self.stats['errors'][:10]:  # Mostra até 10 erros
                print(f"  - {error}")

        print(f"{'='*60}\n")

def main():
    migrator = NotionMigrator()

    for bunker_name, bunker_id in BUNKERS.items():
        migrator.migrate_bunker(bunker_name, bunker_id)

    migrator.print_report()

if __name__ == "__main__":
    main()
