#!/usr/bin/env python3
"""
Script de teste para verificar acesso ao Notion e estrutura dos dados.
"""

import requests
import json

NOTION_TOKEN = "ntn_c60671341229r0PxmmdICq6Uiq4WZSNLDo0KDsFSABv9ds"
BUNKER_1 = "e19169a1-1eaa-82b4-9a51-07ba8bfc68ef"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

print("="*70)
print("TESTE DE ACESSO AO NOTION")
print("="*70)

# Test 1: Query Bunker 1
print("\n[TEST 1] Queryando Bunker 1...")
url = f"https://api.notion.com/v1/databases/{BUNKER_1}/query"
response = requests.post(url, headers=headers, json={}, timeout=30)

if response.status_code == 200:
    data = response.json()
    print(f"✓ Status: 200 OK")
    print(f"✓ Total de páginas: {len(data.get('results', []))}")
    print(f"✓ Has more: {data.get('has_more')}")

    if data.get('results'):
        page = data['results'][0]
        print(f"\n[PRIMEIRA PÁGINA]")
        print(f"  ID: {page.get('id')}")

        props = page.get('properties', {})
        print(f"  Propriedades disponíveis: {list(props.keys())}")

        if 'Nome' in props:
            nome = props['Nome'].get('title', [])
            if nome:
                print(f"  Nome: {nome[0].get('plain_text', 'N/A')}")
                print(f"  Tipo de título: {nome[0].get('type', 'N/A')}")
                text_obj = nome[0].get('text', {})
                link = text_obj.get('link')
                print(f"  Link: {link}")
else:
    print(f"✗ Erro: {response.status_code}")
    print(f"Resposta: {response.text}")

# Test 2: Get page details
print("\n[TEST 2] Obtendo detalhes de uma página...")
if response.status_code == 200 and data.get('results'):
    page_id = data['results'][0]['id']
    url = f"https://api.notion.com/v1/pages/{page_id}"
    page_resp = requests.get(url, headers=headers, timeout=30)

    if page_resp.status_code == 200:
        page_data = page_resp.json()
        print(f"✓ Status: 200 OK")
        print(f"✓ ID: {page_data.get('id')}")

        props = page_data.get('properties', {})
        if 'Nome' in props:
            nome = props['Nome'].get('title', [])
            if nome:
                title_text = nome[0].get('plain_text', 'N/A')
                print(f"✓ Nome: {title_text}")

                # Check for link
                text_obj = nome[0].get('text', {})
                link = text_obj.get('link')
                if link:
                    print(f"✓ URL Externa: {link['url']}")
                else:
                    print(f"✗ Sem link no título")
    else:
        print(f"✗ Erro: {page_resp.status_code}")

# Test 3: Get page content
print("\n[TEST 3] Obtendo conteúdo da página...")
if page_id:
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    content_resp = requests.get(url, headers=headers, timeout=30)

    if content_resp.status_code == 200:
        content_data = content_resp.json()
        print(f"✓ Status: 200 OK")
        blocks = content_data.get('results', [])
        print(f"✓ Total de blocos: {len(blocks)}")

        if blocks:
            for i, block in enumerate(blocks[:3]):
                block_type = block.get('type', 'unknown')
                print(f"  [{i+1}] Tipo: {block_type}")
    else:
        print(f"✗ Erro: {content_resp.status_code}")

print("\n" + "="*70)
print("TESTE CONCLUÍDO")
print("="*70)
