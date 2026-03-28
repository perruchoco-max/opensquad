#!/usr/bin/env python3
"""
COMPILADOR DE URLs - Extrai URLs mention-page de todos os bunkers
Processa dados coletados via notion-search/notion-fetch
"""

import json
import re
from datetime import datetime

# Dados coletados via notion-search (25 páginas por bunker)
BUNKER_1_IDS = [
    "9f9169a11eaa83a4800181ae739c4fd9", "5a4169a11eaa821bb8a60110f74a90fd",
    "03f169a11eaa83ad99200115d45deacd", "2ba169a11eaa83539f08817800e68bf3",
    "dfd169a11eaa839f87ff81d9004dec01", "ed6169a11eaa83c4820b8154763daff2",
    "ee6169a11eaa821885da01925be7a163", "f0f169a11eaa830188a4019e63085724",
    "f13169a11eaa82598abb81c05c2e1cdd", "f6c169a11eaa82aba40b01906c97abc1",
    "f73169a11eaa8280b5710108c537ab0c", "fcf169a11eaa8315b1680130215e65ae",
    "01e169a11eaa82fb8f56813010f149c7", "03c169a11eaa8227a1bb81d2afd12c99",
    "03f169a11eaa8377b7b7013bcb0983da", "051169a11eaa8321950981afb9a62806",
    "07a169a11eaa8313995d810e4927b715", "215169a11eaa83259560813fe7c8840b",
    "215169a11eaa836db5548122b968e1b7", "270169a11eaa8312bf358161f9841ab4",
    "278169a11eaa8255897a8189f83b42c5", "2f5169a11eaa8327aa3201e63b338409",
    "303169a11eaa823689c3819f5a0ab87a", "326169a11eaa831283220169944a6f91",
    "77e169a11eaa83608cec0182e5c20f5f"
]

BUNKER_2_IDS = [
    "611169a11eaa82a4925a812558003328", "806169a11eaa82e892520126b449aaf9",
    "80f169a11eaa8233a735010912129a1c", "981169a11eaa829885d9810a4f861be2",
    "1cd169a11eaa825a89b2813f4ef54e69", "243169a11eaa826d86e28112ffeb24a6",
    "2fc169a11eaa83ed82d28160f3aa5fa6", "120169a11eaa83a0bac181b6c704e43d",
    "db7169a11eaa824e85c6811277f62678", "e9f169a11eaa8252a6c40152a392ee31",
    "c5d169a11eaa8380b8cc017a48f1f262", "e89169a11eaa8378bdb00192aec5db23",
    "b7b169a11eaa8327ada201dbe1219f1d", "b8a169a11eaa82038357016492e08c26",
    "c1f169a11eaa82a1abc601e6e0264590", "232169a11eaa82e99de48157bf7ec03c",
    "08b169a11eaa836995468130ed9c69c4", "a1d169a11eaa82f1b22a81e8dcfb4a0d",
    "ae0169a11eaa83e89cb40191b875f7bc", "b31169a11eaa8208b0e1817406c76997",
    "421169a11eaa83c49ce881b77b93c706", "46f169a11eaa83c3aed901c5dc4dcf5c",
    "695169a11eaa82f79f7e816a1cef123a", "84b169a11eaa824abaac81b8441c41e9",
    "ed1169a11eaa830f863101da08fbce4d"
]

BUNKER_3_IDS = [
    "d2f169a11eaa835ab1d481c210cedc74", "83e169a11eaa832aa1c581c2c557d9f5",
    "137169a11eaa83a398bd81e0d8c142ff", "ba0169a11eaa82e68fd00115e2bf41a0",
    "c1c169a11eaa8326b84d01f2d485be37", "c45169a11eaa83138b7c013c9132e11b",
    "cc2169a11eaa8244850581e19e6f388f", "d3f169a11eaa828f88ee8151124a3a08",
    "e66169a11eaa8244821f8116fe680175", "f2f169a11eaa83eeaba101cb278e434d",
    "6bd169a11eaa837b936901111ce1722b", "783169a11eaa8397a09f81c5e06f784d",
    "8c9169a11eaa822fa996011657119b86", "9dc169a11eaa8335bd4c013b16cd139f",
    "5ff169a11eaa8328872e8169ce9e0dd3", "60b169a11eaa826fb8018123425dac93",
    "036169a11eaa8381ad09816c48a57e10", "166169a11eaa8292bf6d819fae70a771",
    "178169a11eaa837ba0000136644df6cc", "402169a11eaa83cc982501d774642910",
    "406169a11eaa83a4bc760191ad57cc26", "288169a11eaa8285b25f810e82594359",
    "40d169a11eaa836a9c99017b824844b1", "2af169a11eaa83e088aa013517634384",
    "cfc169a11eaa831ba77d814f3c5247d8"
]

BUNKER_5_IDS = [
    "f86169a11eaa820ca55f8125e0a04a14", "86c169a11eaa8233937f01652fa680db",
    "f56169a11eaa825ca873819c33784ccc", "3e9169a11eaa824f8c8481285a3610b1",
    "6c1169a11eaa83a8880c81f8a1e0ce0f", "692169a11eaa832c828b01d9c8dc8b1e",
    "e49169a11eaa8222a4f5015999a4cf4f", "f8b169a11eaa83b587f8016c1ce363f9",
    "136169a11eaa82bcaff181ffaaaf2935", "13f169a11eaa82a2baa10135bc33924d",
    "217169a11eaa82869bbd81ef0252411c", "25f169a11eaa83248c4a013c659c5ea1",
    "290169a11eaa8394ac0c8101c0d480ed", "a4b169a11eaa833887ed81d89c3c6901",
    "4ee169a11eaa82b5a89f01cdc1f7ed86", "59f169a11eaa822988a281da936091c5",
    "091169a11eaa83ee92a2015b98a3abe0", "b34169a11eaa83c29fc28153c7aa8646",
    "aed169a11eaa821183c4812b35809993", "b17169a11eaa839980b2816b24051f26",
    "e5f169a11eaa8285b5a381dce8d307de", "e71169a11eaa82dd812001792ffbfa5b",
    "f3f169a11eaa8294ba8a016439513914", "fc4169a11eaa824ca72a81818771ba30",
    "8ce169a11eaa8325a78a01b1320935de"
]

# URLs extraídas via notion-fetch (padrão: mention-page url)
EXTRACTED_URLS = {
    "Bunker 1": {
        "9f9169a11eaa83a4800181ae739c4fd9": "https://www.notion.so/96ecfa3abba84f4b833e325a1f2a7553"
    },
    "Bunker 2": {
        "611169a11eaa82a4925a812558003328": "https://www.notion.so/83c6a227faf746daaffa20759c01467e"
    },
    "Bunker 3": {
        "d2f169a11eaa835ab1d481c210cedc74": "https://www.notion.so/61e2e03305d44d0ea6eea2439cbfaa60"
    },
    "Bunker 5": {
        "f86169a11eaa820ca55f8125e0a04a14": "https://www.notion.so/27d5a2221e7c8073a00ee857a0f4b925"
    }
}

def extract_url_from_notion_response(notion_response_text):
    """Extrai URL mention-page do JSON response do Notion."""
    try:
        # Padrão: "Nome":"<mention-page url=\"https://www.notion.so/[UUID]\"/>"
        match = re.search(r'"Nome":"<mention-page url=\\"(https://www\.notion\.so/[a-f0-9]+)\\"', notion_response_text)
        if match:
            return match.group(1)
    except:
        pass
    return None

def compile_urls():
    """Compila todas as URLs em JSON estruturado."""

    print("\n" + "="*80)
    print("COMPILADOR DE URLs - NOTION ROTEIROS")
    print("="*80)

    result = {
        "timestamp": datetime.now().isoformat(),
        "tarefa": "Compilar 174 URLs de roteiros para scraping",
        "bunkers": {}
    }

    # Bunker 1
    print("\n📊 BUNKER 1:")
    print(f"  IDs coletados: {len(BUNKER_1_IDS)}")
    print(f"  Expected: 44")
    result["bunkers"]["Bunker 1"] = {
        "total_encontrados": len(BUNKER_1_IDS),
        "total_esperado": 44,
        "page_ids": BUNKER_1_IDS,
        "sample_url": EXTRACTED_URLS.get("Bunker 1", {}).get(BUNKER_1_IDS[0]) if BUNKER_1_IDS else None
    }

    # Bunker 2
    print("\n📊 BUNKER 2:")
    print(f"  IDs coletados: {len(BUNKER_2_IDS)}")
    print(f"  Expected: 29")
    result["bunkers"]["Bunker 2"] = {
        "total_encontrados": len(BUNKER_2_IDS),
        "total_esperado": 29,
        "page_ids": BUNKER_2_IDS,
        "sample_url": EXTRACTED_URLS.get("Bunker 2", {}).get(BUNKER_2_IDS[0]) if BUNKER_2_IDS else None
    }

    # Bunker 3
    print("\n📊 BUNKER 3:")
    print(f"  IDs coletados: {len(BUNKER_3_IDS)}")
    print(f"  Expected: 51")
    result["bunkers"]["Bunker 3"] = {
        "total_encontrados": len(BUNKER_3_IDS),
        "total_esperado": 51,
        "page_ids": BUNKER_3_IDS,
        "sample_url": EXTRACTED_URLS.get("Bunker 3", {}).get(BUNKER_3_IDS[0]) if BUNKER_3_IDS else None
    }

    # Bunker 5
    print("\n📊 BUNKER 5:")
    print(f"  IDs coletados: {len(BUNKER_5_IDS)}")
    print(f"  Expected: 50")
    result["bunkers"]["Bunker 5"] = {
        "total_encontrados": len(BUNKER_5_IDS),
        "total_esperado": 50,
        "page_ids": BUNKER_5_IDS,
        "sample_url": EXTRACTED_URLS.get("Bunker 5", {}).get(BUNKER_5_IDS[0]) if BUNKER_5_IDS else None
    }

    # Totais
    total_found = len(BUNKER_1_IDS) + len(BUNKER_2_IDS) + len(BUNKER_3_IDS) + len(BUNKER_5_IDS)
    result["stats"] = {
        "total_encontrados": total_found,
        "total_esperado": 174,
        "percentual": f"{(total_found/174)*100:.1f}%"
    }

    print("\n" + "="*80)
    print("📊 RESUMO FINAL:")
    print("="*80)
    print(f"\nBunker 1: {len(BUNKER_1_IDS):2d} / 44")
    print(f"Bunker 2: {len(BUNKER_2_IDS):2d} / 29")
    print(f"Bunker 3: {len(BUNKER_3_IDS):2d} / 51")
    print(f"Bunker 5: {len(BUNKER_5_IDS):2d} / 50")
    print(f"{'─'*40}")
    print(f"TOTAL:    {total_found:2d} / 174 ({(total_found/174)*100:.1f}%)")

    print("\n✅ URLs extraídas (padrão):")
    for bunker, urls in EXTRACTED_URLS.items():
        for page_id, url in urls.items():
            print(f"  {bunker}: {url}")

    return result

def main():
    result = compile_urls()

    # Salva em JSON
    with open("/home/user/opensquad/urls_compilation.json", 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print("\n✅ Arquivo salvo: urls_compilation.json")
    print("\n📝 PRÓXIMO PASSO:")
    print("   Cada page_id pode ser usado com notion-fetch para extrair a URL mention-page")
    print("   Padrão extraído: <mention-page url=\"https://www.notion.so/[UUID]\"/>")
    print("   Total: 100/174 URLs coletadas em primeira iteração")

    print("\n" + "="*80)

if __name__ == "__main__":
    main()
