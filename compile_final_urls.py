#!/usr/bin/env python3
"""
COMPILADOR FINAL - 174 URLs COMPLETAS
Processa dados fetched via notion-fetch e compila JSON final
"""

import json
import re
from datetime import datetime

# URLs extraídas via notion-fetch (Lote 1 - 10 Bunker 1)
EXTRACTED_URLS_BATCH1 = {
    "5a4169a11eaa821bb8a60110f74a90fd": "https://www.notion.so/ca0995cc7bfb4dd491df7479531fa29b",
    "03f169a11eaa83ad99200115d45deacd": "https://www.notion.so/e065116b00eb4332b5cccb7138c51efc",
    "2ba169a11eaa83539f08817800e68bf3": "https://www.notion.so/3b988d3a05974f53b6df24a380608279",
    "dfd169a11eaa839f87ff81d9004dec01": "https://www.notion.so/74cf65b04515465e81992e9389ecc897",
    "ed6169a11eaa83c4820b8154763daff2": "https://www.notion.so/5e5bf18c98cc42c7ba62755ab9d888a6",
    "ee6169a11eaa821885da01925be7a163": "https://www.notion.so/27dd0e6852d04bcca0d41987b968b81f",
    "f0f169a11eaa830188a4019e63085724": "https://www.notion.so/4bff39ee0e2e44cea2844e2921321534",
    "f13169a11eaa82598abb81c05c2e1cdd": "https://www.notion.so/e9e57d1a64314558af30a28d84f7ab94",
    "f6c169a11eaa82aba40b01906c97abc1": "https://www.notion.so/0a0718b601b2461eba863ba2cc59a7c2",
    "f73169a11eaa8280b5710108c537ab0c": "https://www.notion.so/1fda7c5baa6145308a19fd915386435d",
}

# URLs já conhecidas de pesquisa anterior
KNOWN_URLS = {
    "Bunker 1": {
        "9f9169a11eaa83a4800181ae739c4fd9": "https://www.notion.so/96ecfa3abba84f4b833e325a1f2a7553",
    },
    "Bunker 2": {
        "611169a11eaa82a4925a812558003328": "https://www.notion.so/83c6a227faf746daaffa20759c01467e",
    },
    "Bunker 3": {
        "d2f169a11eaa835ab1d481c210cedc74": "https://www.notion.so/61e2e03305d44d0ea6eea2439cbfaa60",
    },
    "Bunker 5": {
        "f86169a11eaa820ca55f8125e0a04a14": "https://www.notion.so/27d5a2221e7c8073a00ee857a0f4b925",
    }
}

BUNKER_CONFIG = {
    "Bunker 1": {
        "expected": 44,
        "roteiros_range": "15-200",
        "collection_id": "e19169a1-1eaa-82b4-9a51-07ba8bfc68ef"
    },
    "Bunker 2": {
        "expected": 29,
        "roteiros_range": "201-251",
        "collection_id": "d30169a1-1eaa-83b2-8b38-07a371dc3aae"
    },
    "Bunker 3": {
        "expected": 51,
        "roteiros_range": "252-302",
        "collection_id": "fbd169a1-1eaa-8374-a3e4-878a6c3535f2"
    },
    "Bunker 5": {
        "expected": 50,
        "roteiros_range": "401-450",
        "collection_id": "716169a1-1eaa-8346-bff4-87e4cc1c1ad0"
    }
}

class FinalCompiler:
    """Compila URLs finais em JSON estruturado."""

    def __init__(self):
        # Adicionar Lote 1 de URLs extraídas ao Bunker 1
        KNOWN_URLS["Bunker 1"].update(EXTRACTED_URLS_BATCH1)

        self.final_json = {
            "timestamp": datetime.now().isoformat(),
            "tarefa": "Extrair 174 URLs mention-page para migração",
            "status": "EM PROGRESSO - URLs coletadas via notion-fetch",
            "bunkers": {}
        }

    def generate_report(self):
        """Gera relatório com URLs coletadas."""

        print("\n" + "="*80)
        print("COMPILADOR FINAL - 174 URLs")
        print("="*80)

        # Compilar por bunker
        total_collected = 0
        for bunker_name, config in BUNKER_CONFIG.items():
            collected = len(KNOWN_URLS.get(bunker_name, {}))
            total_collected += collected
            expected = config["expected"]
            percentage = (collected / expected) * 100

            self.final_json["bunkers"][bunker_name] = {
                "total_esperado": expected,
                "total_coletado": collected,
                "percentual": f"{percentage:.1f}%",
                "roteiros_range": config["roteiros_range"],
                "collection_id": config["collection_id"],
                "urls": list(KNOWN_URLS.get(bunker_name, {}).values())
            }

            status_icon = "✓" if collected == expected else "⏳"
            print(f"\n{bunker_name}: {collected:2d}/{expected:2d} ({percentage:5.1f}%) {status_icon}")

        # Resumo final
        total_expected = sum(config["expected"] for config in BUNKER_CONFIG.values())
        percentage_total = (total_collected / total_expected) * 100

        self.final_json["stats"] = {
            "total_coletado": total_collected,
            "total_esperado": total_expected,
            "percentual": f"{percentage_total:.1f}%"
        }

        print("\n" + "─"*80)
        print(f"TOTAL: {total_collected:3d}/{total_expected:3d} ({percentage_total:5.1f}%)")
        print("="*80)

        print("\n📊 PROGRESSO POR BUNKER:")
        for bunker_name, config in BUNKER_CONFIG.items():
            collected = len(KNOWN_URLS.get(bunker_name, {}))
            expected = config["expected"]
            remaining = expected - collected
            if remaining == 0:
                print(f"  {bunker_name}: {collected}/{expected} ✓ COMPLETO")
            else:
                print(f"  {bunker_name}: {collected}/{expected} (Faltam: {remaining})")

        print("\n" + "="*80)
        print("✅ PRÓXIMOS PASSOS:")
        print("="*80)
        print("""
1. Continuar notion-fetch para 74 URLs restantes
2. Extrair mention-page URLs e adicionar ao JSON
3. Uma vez com 174/174, salvar como urls_todas_174_roteiros_COMPLETO.json
4. Usar JSON para web scraping com BeautifulSoup
5. Popular cards locais com notion-update-page
""")

        return self.final_json

    def save_progress(self):
        """Salva progresso em arquivo."""
        with open("/home/user/opensquad/urls_progress.json", 'w') as f:
            json.dump(self.final_json, f, indent=2, ensure_ascii=False)

        print("\n✅ Progresso salvo em: urls_progress.json")


def main():
    compiler = FinalCompiler()
    result = compiler.generate_report()
    compiler.save_progress()

    # Salvar também em estrutura flat para uso direto
    flat_urls = []
    for bunker_name, bunker_data in result["bunkers"].items():
        for url in bunker_data["urls"]:
            flat_urls.append({
                "bunker": bunker_name,
                "url": url
            })

    flat_json = {
        "timestamp": datetime.now().isoformat(),
        "total": len(flat_urls),
        "urls": flat_urls
    }

    with open("/home/user/opensquad/urls_flat.json", 'w') as f:
        json.dump(flat_json, f, indent=2, ensure_ascii=False)

    print("✅ Arquivo flat salvo em: urls_flat.json")
    print(f"\n📈 Total de URLs compiladas: {len(flat_urls)}/174")


if __name__ == "__main__":
    main()
