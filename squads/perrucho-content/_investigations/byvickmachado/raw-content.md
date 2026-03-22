# Raw Content: @byvickmachado (TikTok)

Investigated: 2026-03-22
Total contents analyzed: 0 (bloqueio de acesso)
Content types: vídeos curtos

---

## Nota de Investigação — Acesso Bloqueado

### Obstáculos Encontrados

**1. Playwright MCP — Browser não disponível**
- O servidor MCP Playwright tentou usar `/opt/google/chrome/chrome` (Chrome não instalado)
- O Chromium do Playwright está disponível em `/root/.cache/ms-playwright/chromium-1194/chrome-linux/chrome`
- O config `_opensquad/config/playwright.config.json` foi atualizado com o caminho correto e `chromiumSandbox: false`, mas o MCP server precisa ser reiniciado para aplicar as mudanças

**2. Proxy de egresso bloqueia TikTok**
- O ambiente usa um proxy de controle de egresso (Anthropic) que possui uma lista de hosts permitidos
- `tiktok.com` NÃO está na lista de hosts permitidos
- Tentativa de acesso via curl retornou: `HTTP/1.1 403 Forbidden` com `x-deny-reason: host_not_allowed`
- Tentativa via Node.js playwright retornou: `net::ERR_INVALID_AUTH_CREDENTIALS`
- WebFetch retornou: `Request failed with status code 403`

### Impacto
Não foi possível acessar o perfil `https://www.tiktok.com/@byvickmachado` a partir deste ambiente. Nenhum dado de vídeo pôde ser extraído.

### Próximos Passos Recomendados
1. **Reiniciar o Claude Code** para que o Playwright MCP recarregue com o config atualizado (caminho correto do Chromium + `chromiumSandbox: false`)
2. Após reiniciar, rodar a investigação novamente — o browser poderá funcionar, mas o proxy ainda bloqueará TikTok
3. Alternativa: Executar a investigação em um ambiente local (não sandboxed) onde o acesso ao TikTok seja permitido
4. Alternativa: Fazer login manual no TikTok em uma sessão de browser com o perfil persistente e exportar os dados

---

## Conteúdo Extraído

Nenhum conteúdo pôde ser extraído devido ao bloqueio de rede.

```
Status: BLOQUEADO
Plataforma: TikTok
Perfil: @byvickmachado
URL: https://www.tiktok.com/@byvickmachado
Data: 2026-03-22
Erro: Proxy de egresso bloqueia acesso a tiktok.com (host_not_allowed)
```
