# Raw Content: @midsdotrafego (TikTok)

Investigated: 2026-03-22
Total contents analyzed: 0
Content types: vídeos curtos

---

## Nota de Investigação — Acesso Bloqueado

Durante a investigação do perfil @midsdotrafego no TikTok, foram encontradas as seguintes barreiras técnicas:

### Obstáculos encontrados

1. **Proxy de rede restrito**: O ambiente de execução utiliza um proxy corporativo (`https_proxy`) que bloqueia o acesso a domínios de redes sociais. Tentativas de acesso a `www.tiktok.com` retornaram erro `403 Forbidden (host_not_allowed)`.

2. **Playwright MCP indisponível**: O servidor Playwright MCP está configurado para usar o browser "Chrome" (`/opt/google/chrome/chrome`), mas esse binário não está disponível no ambiente. O Chromium está instalado em `/root/.cache/ms-playwright/chromium-1194/chrome-linux/chrome`, mas o servidor MCP não conseguiu inicializar com essa configuração.

3. **WebFetch bloqueado**: A ferramenta WebFetch retornou erro `403` ao tentar acessar `https://www.tiktok.com/@midsdotrafego`.

4. **Tentativas alternativas**: Foram testados endpoints da API pública do TikTok e o Wayback Machine (web.archive.org) — todos bloqueados pelo mesmo proxy.

### Métodos tentados

- `browser_navigate` via Playwright MCP → falhou (Chrome não encontrado)
- `WebFetch` direto para `https://www.tiktok.com/@midsdotrafego` → 403
- `curl` com user-agent de browser/mobile → 403 (host_not_allowed)
- `urllib` Python → 403 Tunnel connection failed
- API pública TikTok (`/api/user/detail/`) → 403
- Wayback Machine → 403

### O que foi possível confirmar

- O username `@midsdotrafego` é do nicho de **tráfego pago** (inferido pelo próprio username: "mids do tráfego")
- Sem acesso ao conteúdo real, não é possível extrair legendas, métricas, hashtags ou padrões de vídeo

---

## Recomendações para próxima tentativa

1. **Executar fora deste ambiente sandboxado**: Usar o Playwright em uma máquina local ou ambiente sem proxy restritivo.
2. **Login manual**: Na primeira execução com browser, realizar login no TikTok para armazenar sessão no `_browser_profile`.
3. **Alternativa manual**: Acessar o perfil manualmente e copiar as legendas dos 10 vídeos mais recentes para este arquivo.

---

*Investigação interrompida por restrições de acesso à rede. Arquivo gerado com documentação do obstáculo.*
