#!/usr/bin/env python3
"""
Script de migração Notion - FASE 1: Teste de scraping + atualização
Extrai conteúdo de URLs externas e atualiza cards no Notion
"""

import requests
from bs4 import BeautifulSoup
import time
from typing import Optional, Dict, List
import json

# URLs reais para teste (fornecidas)
TEST_URLS = {
    "Bunker 5": [
        "https://seen-molecule-999.notion.site/ROTEIRO-412-Comparando-coisas-do-seu-nicho-com-coisas-comuns-27d5a2221e7c8073a00ee857a0f4b925",
        "https://seen-molecule-999.notion.site/ROTEIRO-438-Explicando-TEMA-COMPLEXO-usando-COISA-SIMPLES-27d5a2221e7c80c79f49c37f28dd7246",
        "https://seen-molecule-999.notion.site/ROTEIRO-447-Você-não-sabe-fazer-coisa-básica-e-eu-vou-te-provar-2e55a2221e7c800ebda2fdb37fe0e8a8",
    ],
    "Bunker 3": [
        "https://seen-molecule-999.notion.site/ROTEIRO-270-Trocando-coisa-cara-por-acessível-c3ec8ef950544e64bdc178624e475811",
        "https://seen-molecule-999.notion.site/ROTEIRO-269-Estrutura-Viral-Nikolas-de0659239a604606b4df41717aa15293",
        "https://seen-molecule-999.notion.site/ROTEIRO-279-A-volta-do-Neymar-a8bae08a43bf446dad9ce3aea49e874f",
    ],
    "Bunker 2": [
        "https://seen-molecule-999.notion.site/ROTEIRO-236-Qual-foi-o-mais-3374257ad95442aa9c1d8655c58aa00f",
        "https://seen-molecule-999.notion.site/ROTEIRO-204-Momentos-que-quase-me-fizeram-3a7922ddbdaf407ebd4415a2a83b179c",
        "https://seen-molecule-999.notion.site/ROTEIRO-212-Obrigações-para-não-se-dar-mal-1d27a35266d84239953c641741ec2f46",
    ],
    "Bunker 1": [
        "https://seen-molecule-999.notion.site/ROTEIRO-154-Cobrei-X-reais-pra-fazer-tal-coisa-a54707473b6143cab2b7890b83d9595d",
        "https://seen-molecule-999.notion.site/ROTEIRO-39-História-impactante-de-alguma-celebridade-82b9472da00342ecb6890f0f33d38f5a",
        "https://seen-molecule-999.notion.site/ROTEIRO-199-Em-X-anos-como-profissional-e-eu-nunca-e71ce6299e5142a1959280f243363b6b",
    ],
}

class ContentScraper:
    """Faz web scraping de conteúdo Notion."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        self.stats = {"success": 0, "failed": 0, "total": 0}

    def extract_roteiro_number(self, url: str) -> str:
        """Extrai número do roteiro da URL."""
        import re
        match = re.search(r'ROTEIRO-(\d+)', url)
        return match.group(1) if match else "?"

    def scrape_url(self, url: str) -> Optional[str]:
        """Faz scraping de uma URL."""
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Remove scripts e styles
            for script in soup(["script", "style"]):
                script.decompose()

            # Encontra conteúdo principal
            main = soup.find(['main', 'article'])
            if not main:
                main = soup.find('div', class_='notion')
            if not main:
                main = soup.find('div', {'role': 'main'})

            if main:
                content = main.get_text(separator='\n', strip=True)
            else:
                # Fallback: pega todo o body
                body = soup.find('body')
                if body:
                    content = body.get_text(separator='\n', strip=True)
                else:
                    content = soup.get_text(separator='\n', strip=True)

            # Limpa espaços
            lines = [line.strip() for line in content.split('\n') if line.strip()]
            content = '\n'.join(lines)

            # Remove junk comum
            junk_patterns = [
                'Updated',
                'Favorited',
                'Duplicate',
                'Delete',
                'Share',
                'Add to',
            ]

            for pattern in junk_patterns:
                content = content.replace(pattern, '')

            # Limita tamanho
            if len(content) > 10000:
                content = content[:10000] + "\n\n[Conteúdo truncado...]"

            return content if content and len(content) > 50 else None

        except Exception as e:
            print(f"        [ERRO SCRAPING] {str(e)[:60]}")
            return None

    def test_all_urls(self) -> Dict[str, List[Dict]]:
        """Testa scraping de todas as URLs."""
        results = {}

        for bunker, urls in TEST_URLS.items():
            print(f"\n{'='*70}")
            print(f"TESTANDO {bunker}")
            print(f"{'='*70}")

            bunker_results = []

            for i, url in enumerate(urls, 1):
                roteiro_num = self.extract_roteiro_number(url)
                print(f"\n[{i}/{len(urls)}] ROTEIRO-{roteiro_num}")
                print(f"    URL: {url[:60]}...")

                self.stats["total"] += 1

                content = self.scrape_url(url)

                if content:
                    print(f"    ✓ Conteúdo extraído: {len(content)} caracteres")
                    bunker_results.append({
                        "roteiro": roteiro_num,
                        "url": url,
                        "content": content,
                        "status": "success"
                    })
                    self.stats["success"] += 1
                else:
                    print(f"    ✗ Falha ao extrair conteúdo")
                    bunker_results.append({
                        "roteiro": roteiro_num,
                        "url": url,
                        "status": "failed"
                    })
                    self.stats["failed"] += 1

                time.sleep(0.5)  # Rate limiting

            results[bunker] = bunker_results

        return results

    def print_summary(self):
        """Imprime sumário de teste."""
        print(f"\n\n{'='*70}")
        print(f"SUMÁRIO DO TESTE - FASE 1 (SCRAPING)")
        print(f"{'='*70}")
        print(f"Total testado:     {self.stats['total']}")
        print(f"Sucesso:           {self.stats['success']}")
        print(f"Falhas:            {self.stats['failed']}")

        if self.stats['total'] > 0:
            rate = (self.stats['success'] / self.stats['total'] * 100)
            print(f"Taxa de sucesso:   {rate:.1f}%")

        print(f"{'='*70}\n")

        if self.stats['success'] >= 5:
            print("✓ FASE 1 SUCESSO - Scraping de 5+ URLs funcionou")
            print("→ Próximo: Atualizar cards no Notion com conteúdo extraído")
        else:
            print("✗ FASE 1 FALHA - Poucos resultados bem-sucedidos")
            print("→ Necessário investigar URLs ou padrão de extração")


def main():
    print("MIGRAÇÃO NOTION - FASE 1: TESTE DE SCRAPING")
    print("="*70)
    print(f"Total de URLs a testar: {sum(len(urls) for urls in TEST_URLS.values())}")
    print("="*70)

    scraper = ContentScraper()
    results = scraper.test_all_urls()
    scraper.print_summary()

    # Salva resultados
    output = {
        "fase": "1_scraping_test",
        "stats": scraper.stats,
        "results": results
    }

    with open("/home/user/opensquad/phase1_results.json", 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"[✓] Resultados salvos em: phase1_results.json")

    return scraper.stats['success'] >= 5


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
