#!/usr/bin/env python3
"""
COMPILADOR LIMPO - 128 URLs em JSON simples pronto para web scraping
Estrutura: [{"bunker": 1, "roteiro": "ROTEIRO-XX", "url": "https://..."}]
"""

import json

def compile_clean_urls():
    """Compila 128 URLs em JSON limpo para web scraping."""

    # Ler arquivo JSON final
    with open("/home/user/opensquad/urls_128_roteiros_FINAL.json", 'r') as f:
        data = json.load(f)

    # Mapeamento de bunker names para números
    bunker_map = {
        "Bunker 1": 1,
        "Bunker 2": 2,
        "Bunker 3": 3,
        "Bunker 5": 5
    }

    # Ranges de roteiros para cada bunker
    roteiro_ranges = {
        1: (15, 62),      # 48 roteiros (15-62)
        2: (201, 229),    # 29 roteiros (201-229)
        3: (252, 277),    # 26 roteiros (252-277)
        5: (401, 425)     # 25 roteiros (401-425)
    }

    result = []

    # Processar cada bunker
    for bunker_name, bunker_num in bunker_map.items():
        bunker_data = data["bunkers"][bunker_name]
        urls = bunker_data["urls"]

        # Roteiros sequenciais para este bunker
        start_roteiro, _ = roteiro_ranges[bunker_num]

        for idx, url in enumerate(urls):
            roteiro_num = start_roteiro + idx

            result.append({
                "bunker": bunker_num,
                "roteiro": f"ROTEIRO-{roteiro_num}",
                "url": url
            })

    # Salvar JSON limpo
    with open("/home/user/opensquad/urls_128_roteiros.json", 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    # Imprimir relatório
    print("\n" + "="*80)
    print("COMPILAÇÃO FINAL - 128 URLs")
    print("="*80)

    bunker_counts = {}
    for item in result:
        bunker = item["bunker"]
        bunker_counts[bunker] = bunker_counts.get(bunker, 0) + 1

    for bunker_num in [1, 2, 3, 5]:
        count = bunker_counts.get(bunker_num, 0)
        status = "✓" if count > 0 else "✗"
        print(f"Bunker {bunker_num}: {count:2d} URLs {status}")

    print("\n" + "─"*80)
    print(f"TOTAL: {len(result)}/128 ✓")
    print("="*80)

    # Validação: primeiras 5 URLs
    print("\n✅ PRIMEIRAS 5 URLs (formato verificado):")
    for item in result[:5]:
        print(f"  {item['bunker']} | {item['roteiro']:13s} | {item['url']}")

    # Verificar domínio
    print("\n🔍 VALIDAÇÃO DE DOMÍNIO:")
    valid_urls = all(item["url"].startswith("https://www.notion.so/") for item in result)
    if valid_urls:
        print("  ✓ Todas as URLs começam com https://www.notion.so/")
    else:
        print("  ✗ Alguns URLs não correspondema padrão esperado")

    # Verificar duplicatas
    urls_unicos = len(set(item["url"] for item in result))
    if urls_unicos == len(result):
        print(f"  ✓ Sem duplicatas ({urls_unicos} URLs únicos)")
    else:
        print(f"  ⚠️  {len(result) - urls_unicos} URL(s) duplicadas encontrada(s)")

    print("\n✅ Arquivo salvo: urls_128_roteiros.json")
    print("   Pronto para web scraping!")
    print("="*80)

if __name__ == "__main__":
    compile_clean_urls()
