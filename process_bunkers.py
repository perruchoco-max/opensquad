#!/usr/bin/env python3
"""
Script para processar bunkers do Notion e migrar conteúdo.
Executa passo a passo com informações de debug.
"""

import sys
import time
from pathlib import Path

# Adiciona a pasta do projeto
sys.path.insert(0, str(Path(__file__).parent))

BUNKER_1_ID = "e19169a1-1eaa-82b4-9a51-07ba8bfc68ef"
BUNKER_2_ID = "d30169a1-1eaa-83b2-8b38-07a371dc3aae"
BUNKER_3_ID = "fbd169a1-1eaa-8374-a3e4-878a6c3535f2"
BUNKER_5_ID = "716169a1-1eaa-8346-bff4-87e4cc1c1ad0"

print("="*70)
print("PROCESSAMENTO DE BUNKERS DO NOTION")
print("="*70)
print()
print("BUNKER 1: " + BUNKER_1_ID)
print("BUNKER 2: " + BUNKER_2_ID)
print("BUNKER 3: " + BUNKER_3_ID)
print("BUNKER 5: " + BUNKER_5_ID)
print()
print("Próximos passos:")
print("1. Buscar páginas em cada bunker via Notion MCP")
print("2. Extrair URLs das páginas externas")
print("3. Fazer web scraping do conteúdo")
print("4. Atualizar páginas no Notion")
print()
print("="*70)
