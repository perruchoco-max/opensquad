# Raw Content: @leticiavazlv (TikTok)

Investigated: 2026-03-22
Total contents analyzed: 0
Content types: vídeos curtos

---

## Nota de Investigação — Acesso Bloqueado

A investigação do perfil @leticiavazlv no TikTok encontrou dois obstáculos:

### Obstáculo 1: Browser Playwright sem Chrome instalado
O servidor MCP do Playwright está configurado para usar o navegador "chrome" (`/opt/google/chrome/chrome`), que não está disponível no ambiente. O Chromium está instalado em `~/.cache/ms-playwright/chromium-1194/chrome-linux/chrome`, mas o servidor MCP já estava em execução com a configuração antiga e não reconhece o Chromium.

- Config atual: `_opensquad/config/playwright.config.json` (atualizada para apontar ao Chromium)
- Erro recebido: `Chromium distribution 'chrome' is not found at /opt/google/chrome/chrome`

### Obstáculo 2: Proxy de rede bloqueia TikTok
O ambiente de execução usa um proxy HTTP que possui uma lista de permissões (allowlist) de hosts. O TikTok (`www.tiktok.com`) **não está** na lista de hosts permitidos.

- Resposta do proxy: `HTTP/1.1 403 Forbidden` com header `x-deny-reason: host_not_allowed`
- Tentativas realizadas:
  - `https://www.tiktok.com/@leticiavazlv` — 403
  - `https://www.tiktok.com/oembed?url=...` — 403

### Hosts permitidos no proxy (confirmados)
- github.com ✓
- pypi.org ✓
- npmjs.org ✓
- (outros relacionados a pacotes de desenvolvimento)

---

## O que foi tentado

1. Navegação direta com Playwright MCP → falhou (chrome não instalado)
2. Instalação do Chrome via `npx playwright install chrome` → falhou (proxy bloqueou download do Google)
3. Fetch HTTP via `curl` → falhou (proxy bloqueou www.tiktok.com)
4. TikTok oEmbed API → falhou (mesmo bloqueio de proxy)

---

## Recomendações para investigação manual

Para completar esta investigação, acesse manualmente:
- URL do perfil: https://www.tiktok.com/@leticiavazlv
- Colete as legendas dos 10 vídeos mais recentes
- Registre views, likes e comentários de cada vídeo
- Salve os dados neste arquivo seguindo o formato abaixo

```
## Content 1: [Vídeo | {tipo}]

**Date:** {data se visível}
**Metrics:** {views} views, {likes} likes, {comments} comentários
**URL:** {url se visível}

### Caption/Legenda
{texto completo da legenda}

### Hashtags
{hashtags}
```

---

*Investigação parcial — nenhum conteúdo extraído devido a restrições de rede e ambiente.*
