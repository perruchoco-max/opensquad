# Plano de Migração de Conteúdo Notion

## Status: INICIADO

### Objetivo
Migrar ~174 templates entre workspaces do Notion, extraindo conteúdo de páginas públicas externas e atualizando as páginas locais.

### Estrutura Identificada

#### Bunkers (Coleções Notion)
1. **Bunker 1**: `e19169a1-1eaa-82b4-9a51-07ba8bfc68ef` (Objetivos)
   - Propriedades: Nome (title), Categoria (multi_select)
   - Status: ✓ Estrutura mapeada

2. **Bunker 2**: `d30169a1-1eaa-83b2-8b38-07a371dc3aae`
   - Status: Pendente mapeamento

3. **Bunker 3**: `fbd169a1-1eaa-8374-a3e4-878a6c3535f2`
   - Status: Pendente mapeamento

4. **Bunker 5**: `716169a1-1eaa-8346-bff4-87e4cc1c1ad0`
   - Status: Pendente mapeamento

#### Workspace Público
- URL: https://seen-molecule-999.notion.site/
- Contém templates com conteúdo
- Será usado para web scraping

### Fluxo de Migração
```
Para cada bunker:
  Para cada página (card/template):
    1. [✓] Obter detalhes da página (Nome, ID)
    2. [ ] Extrair URL externa (link no título)
    3. [ ] Fazer web scraping (BeautifulSoup)
    4. [ ] Atualizar página com conteúdo (Notion MCP)
```

### Ferramentas Disponíveis
- **Notion MCP**: notion-fetch, notion-update-page, notion-search
- **Web Scraping**: requests, BeautifulSoup4

### Desafios Identificados
1. ⚠️ Limite de proxy na rede (bloqueio de requisições diretas)
2. ⚠️ Playwright não pode ser instalado (dependências de sistema)
3. ✓ Web scraping via requests + BeautifulSoup funciona

### Próximos Passos
1. Mapear estrutura dos outros bunkers
2. Buscar uma amostra de páginas para testar o fluxo
3. Implementar processamento em lotes
4. Gerar relatório de progresso

### Estatísticas de Progresso
- Total de bunkers: 4
- Templates esperados: ~174
- Processados: 0
- Sucesso: 0
- Falhas: 0
