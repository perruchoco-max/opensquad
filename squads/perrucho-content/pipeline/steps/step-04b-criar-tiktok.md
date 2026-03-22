---
execution: subagent
agent: tiago-tiktok
model_tier: powerful
format: tiktok
inputFile: squads/perrucho-content/output/angulo-selecionado.md
outputFile: squads/perrucho-content/output/tiktok-content.md
---

# Step 04b: Criar Conteúdo TikTok

## Context Loading

Load these files before executing:
- `squads/perrucho-content/output/angulo-selecionado.md` — Ângulo e ajustes selecionados pelo Marco
- `squads/perrucho-content/output/research-output.md` — Briefing de pesquisa completo com evidências
- `_opensquad/_memory/company.md` — Perfil e tom de voz da Perrucho & Co.
- `squads/perrucho-content/pipeline/data/tone-of-voice.md` — Guia de tom de voz
- `squads/perrucho-content/pipeline/data/anti-patterns.md` — O que nunca fazer
- `squads/perrucho-content/pipeline/data/output-examples.md` — Exemplos de qualidade esperada

## Instructions

### Process

1. **Recontextualizar para audiência fria**: O TikTok distribui para não-seguidores. O script precisa funcionar para alguém que nunca ouviu falar do Marco Perrucho. Não presuma conhecimento prévio.

2. **Construir o hook dos primeiros 3 segundos**: Uma frase que cria dissonância, curiosidade intensa ou medo de perda — sem introdução, sem contexto prévio. Testar: "alguém que não me conhece vai parar por causa dessa frase?"

3. **Criar o script completo (15-60 segundos)**:
   - 0-3s: Hook irresistível + text overlay
   - 3-10s: Credencial implícita (não curriculum — resultado ou observação que prova expertise)
   - 10-50s: Demonstração ou framework em 3-5 passos concretos
   - Últimos 5s: CTA de baixo atrito
   - Indicar [ON-SCREEN: texto] em pelo menos 3 momentos

4. **Criar a legenda do TikTok** (máx 2200 chars, ideal 150-300):
   - Hook que complementa (não repete) o hook do vídeo
   - 1-2 pontos de contexto
   - CTA para engajamento
   - 3-5 hashtags relevantes

5. **Verificar stand-alone**: Reler o script como se fosse um espectador que nunca viu o Marco. O conteúdo faz sentido e é valioso sem contexto prévio?

## Output Format

```markdown
# TikTok Content — [Tema/Ângulo]

Data: [YYYY-MM-DD]
Ângulo: [título do ângulo selecionado]
Driver psicológico: [driver]
Duração estimada: [X segundos]
Palavras no script: [N]

---

## SCRIPT DO TIKTOK

HOOK (0-3s):
[ON-SCREEN: "texto de impacto — máx 8 palavras"]
"[fala exata — a frase mais forte do vídeo]"

CONTEXTO (3-8s):
[Script]: "[credencial implícita em 1-2 frases — sem curriculum, com prova]"
[ON-SCREEN: "elemento de contexto"]

DELIVERY (8-[N]s):
[Script]: "[desenvolvimento completo com passos, dados ou demonstração]"
[ON-SCREEN: "[texto para ponto 1]"]
[Script continua...]
[ON-SCREEN: "[texto para ponto 2]"]
[Script continua...]
[ON-SCREEN: "[texto para ponto 3]"]

CTA ([N-5]s até fim):
[Script]: "[CTA de baixo atrito]"
[ON-SCREEN: "[instrução visual do CTA]"]

---

## LEGENDA DO TIKTOK

[Hook que complementa o vídeo]

[1-2 linhas de contexto]

[CTA de engajamento]

#[hashtag1] #[hashtag2] #[hashtag3] #[hashtag4] #[hashtag5]
```

## Output Example

> See squads/perrucho-content/pipeline/data/output-examples.md for complete example.

## Veto Conditions

Reject and redo if ANY are true:
1. Script começa com apresentação ("Oi, eu sou o Marco") antes do hook
2. Script tem menos de 3 indicações de [ON-SCREEN: texto]
3. CTA pede compra direta de audiência fria ("acesse o link para comprar")
4. Script pressupõe que o espectador conhece o Marco ou a Perrucho & Co.

## Quality Criteria

- [ ] Hook está nos primeiros 3 segundos sem contexto prévio
- [ ] Mínimo 3 indicações de on-screen text no script
- [ ] Script tem 60-150 palavras (15-60 segundos)
- [ ] CTA é de baixo atrito (engajamento, não compra)
- [ ] Conteúdo funciona stand-alone para audiência fria
- [ ] Tom consistente com o driver psicológico do ângulo
