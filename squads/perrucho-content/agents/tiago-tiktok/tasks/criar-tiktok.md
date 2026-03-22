---
task: "Criar Conteúdo TikTok"
order: 1
input: |
  - angulo: Ângulo selecionado com driver psicológico, hook e evidência
  - research_output: Briefing de pesquisa com dados e frameworks
  - company: Perfil e tom de voz da Perrucho & Co.
output: |
  - tiktok_script: Script completo de 15-60s com timecodes e on-screen text
  - tiktok_caption: Legenda do TikTok com hook + CTA + hashtags
---

# Criar Conteúdo TikTok

Produz script de vídeo TikTok (15-60 segundos) com on-screen text e legenda, otimizado para audiência fria e algoritmo de descoberta.

## Process

1. **Recontextualizar para audiência fria**: O espectador do TikTok provavelmente nunca ouviu falar do Marco. Cada elemento — hook, credencial, argumento — precisa funcionar sem contexto prévio.

2. **Construir hook dos 3 primeiros segundos**: Uma frase que cria dissonância, curiosidade ou medo de perda antes de qualquer apresentação. Testar com "alguém que não me conhece vai parar?"

3. **Estruturar o script completo**:
   - 0-3s: Hook + [ON-SCREEN: texto de impacto]
   - 3-10s: Credencial implícita (não curriculum — resultado ou observação que prova expertise)
   - 10-fim: Demonstração ou framework em 2-4 passos com [ON-SCREEN] em cada ponto
   - Últimos 5s: CTA de baixo atrito

4. **Verificar stand-alone**: Reler como espectador novo. Funciona sem contexto? Vale o tempo investido?

5. **Escrever legenda do TikTok** (150-300 chars ideal): Hook complementar → contexto → CTA → 3-5 hashtags.

## Output Format

```markdown
# TikTok Content — [Tema]

Duração estimada: [X segundos]
Palavras no script: [N]

## SCRIPT DO TIKTOK

HOOK (0-3s):
[ON-SCREEN: "texto"]
"[fala]"

CONTEXTO (3-8s):
[Script]: "[fala]"

DELIVERY (8-Ns):
[Script]: "[fala]"
[ON-SCREEN: "ponto 1"]
[Script]: "[fala]"
[ON-SCREEN: "ponto 2"]

CTA (N-5s até fim):
[Script]: "[CTA]"
[ON-SCREEN: "[instrução visual]"]

## LEGENDA DO TIKTOK
[hook complementar]
[contexto 1-2 linhas]
[CTA]
#hashtag1 #hashtag2 #hashtag3
```

## Quality Criteria

- [ ] Hook está nos 3 primeiros segundos sem introdução prévia
- [ ] Mínimo 3 [ON-SCREEN] indicados no script
- [ ] Script entre 60-150 palavras (15-60 segundos)
- [ ] CTA de baixo atrito (não pede compra)
- [ ] Funciona para audiência que nunca viu o Marco

## Veto Conditions

Reject and redo if ANY are true:
1. Script começa com apresentação antes do hook
2. Menos de 3 indicações de on-screen text
3. Script acima de 180 palavras (mais de 70 segundos)
