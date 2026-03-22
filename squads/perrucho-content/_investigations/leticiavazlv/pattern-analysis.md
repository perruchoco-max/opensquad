# Pattern Analysis: @leticiavazlv (TikTok)

Investigated: 2026-03-22
Status: **INCOMPLETO** — Acesso bloqueado por restrições de rede

---

## Resumo da Investigação

A análise de padrões de conteúdo para o perfil @leticiavazlv no TikTok **não pôde ser concluída** nesta sessão. O ambiente de execução bloqueia acesso à rede para domínios não-autorizados, incluindo `www.tiktok.com`.

---

## Causa Raiz dos Bloqueios

| Problema | Detalhe |
|---|---|
| Proxy HTTP | www.tiktok.com não está na allowlist do proxy |
| Browser | Chrome não instalado; Playwright MCP requer `/opt/google/chrome/chrome` |
| Alternativas | TikTok oEmbed API também bloqueada |

---

## Padrões a Serem Analisados (Pendente)

Quando o acesso ao perfil for possível, analisar:

### 1. Padrões de Hook
- Como cada vídeo começa na legenda (pergunta, afirmação, número, emoji)
- Palavras-gatilho mais usadas nas primeiras 5 palavras

### 2. Tom de Voz
- Direto e objetivo vs. emocional e narrativo
- Uso de gírias ou linguagem formal
- Proximidade com o seguidor (você, tu, a gente)

### 3. Tipos de CTA (Call to Action)
- Direcionamento para bio/link
- Pedido de comentário/compartilhamento
- Pergunta ao final para gerar interação

### 4. Hashtags
- Quais hashtags são usadas com mais frequência
- Mix entre hashtags de nicho e genéricas
- Posicionamento (no corpo da legenda ou ao final)

### 5. Estrutura das Legendas
- Extensão típica (curta/média/longa)
- Uso de emojis e onde aparecem
- Quebras de linha e formatação

### 6. Métricas de Engajamento
- Correlação entre tipo de conteúdo e views/likes
- Conteúdos com melhor performance
- Formatos que geram mais comentários

---

## Próximos Passos

1. Resolver acesso à rede (adicionar tiktok.com ao proxy allowlist) OU
2. Executar a investigação em ambiente local com acesso irrestrito à internet
3. Repopular `raw-content.md` com os dados reais
4. Atualizar este arquivo com análise baseada em dados reais

---

*Análise pendente de dados — arquivo criado como placeholder para completar quando o acesso for possível.*
