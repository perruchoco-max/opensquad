import requests
import json

TOKEN = "ntn_c60671341229r0PxmmdICq6Uiq4WZSNLDo0KDsFSABv9ds"

# Tenta buscar informações sobre o workspace público
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Tenta buscar database/page info
urls_to_test = [
    "https://api.notion.com/v1/search",  # Search
]

for url in urls_to_test:
    try:
        print(f"Testando {url}...")
        resp = requests.post(url, headers=headers, json={}, timeout=5)
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            print(f"Resposta: {json.dumps(resp.json(), indent=2)[:200]}")
    except Exception as e:
        print(f"Erro: {str(e)[:100]}")

print("\nTentando criar página de teste...")
result = requests.post(
    "https://api.notion.com/v1/databases/e19169a11eaa82b49a5107ba8bfc68ef/query",
    headers=headers,
    json={},
    timeout=5
)
print(f"Query status: {result.status_code}")

