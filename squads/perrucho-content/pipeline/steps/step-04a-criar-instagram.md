---
execution: subagent
agent: iago-instagram
model_tier: powerful
format: instagram-feed
inputFile: squads/perrucho-content/output/angulo-selecionado.md
outputFile: squads/perrucho-content/output/instagram-content.md
---

# Step 04a: Criar Conteúdo Instagram

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

1. **Absorver o ângulo selecionado**: Identificar o driver psicológico dominante, o hook proposto e a evidência principal. O ângulo é o fio condutor de tudo.

2. **Gerar 3 opções de hook para o slide 1** e escolher o mais forte com base no driver psicológico do ângulo. Registrar a escolha e o motivo brevemente.

3. **Criar o carrossel (8-10 slides)**:
   - Slide 1: Capa com headline de alto impacto (hook escolhido)
   - Slides 2-8: Um ponto por slide (headline bold + suporte 40-80 palavras)
   - Slide 9-10 (opcional): Síntese e CTA específico
   - Manter progressão lógica — cada slide avança, não repete

4. **Criar a legenda do carrossel**:
   - Hook nos primeiros 125 caracteres (visível antes do corte "...mais")
   - Contexto de 2-4 linhas curtas
   - 2-3 insights adicionais
   - CTA específico (não genérico)
   - 5-15 hashtags estratégicas (nicho + descoberta)

5. **Criar o script do Reel (15-30 segundos)**:
   - Hook de 0-2s com texto de tela sobreposto
   - Setup contextual de 2-5s
   - Entrega do valor de 5-25s (3 pontos práticos ou demonstração)
   - CTA específico nos últimos 3-5s
   - Legenda do Reel com hook + CTA

## Output Format

```markdown
# Instagram Content — [Tema/Ângulo]

Data: [YYYY-MM-DD]
Ângulo: [título do ângulo selecionado]
Driver psicológico: [driver]
Tom: [tom selecionado]

## Hook Options (interno)
1. [Hook opção 1]
2. [Hook opção 2]
3. [Hook opção 3]
**Escolhido**: #[número] — [motivo em 1 frase]

---

## CARROSSEL (Instagram Feed)

### Slide 1 — Capa
**Headline**: [headline de impacto máximo]
**Suporte**: [frase complementar, opcional]

### Slide 2
**Headline**: [claim principal]
**Suporte**: [40-80 palavras de contexto/evidência]

[... slides 3-9]

### Slide 10 — CTA
**Headline**: [CTA principal]
**Suporte**: [instrução específica]

---

## LEGENDA DO CARROSSEL

[Hook linha 1 — máx 125 chars]
[Hook linha 2 se necessário]

[Contexto em 2-4 linhas]

[2-3 insights adicionais separados por linha]

[CTA específico]

[hashtags]

---

## SCRIPT DO REEL

=== REEL SCRIPT ===

HOOK (0-2s):
[Visual]: [o que aparece na tela]
[Audio]: [fala exata]
[Text Overlay]: [texto sobreposto — máx 10 palavras]

SETUP (2-5s):
[Script]: [fala de contexto — máx 2 frases]

DELIVERY (5-25s):
[Visual]: [descrição das cenas]
[Script]: [fala completa]
[Text Overlays]: [bullets na tela]

CTA (25-30s):
[Script]: [fala do CTA]
[Text Overlay]: [texto do CTA na tela]

=== LEGENDA DO REEL ===
[Hook]

[1-2 linhas de contexto]

[CTA]
[hashtags]
```

## Output Example

> See squads/perrucho-content/pipeline/data/output-examples.md for complete example.

## Veto Conditions

Reject and redo if ANY are true:
1. Slide 1 abre com "Oi pessoal" ou qualquer variante de saudação
2. Qualquer slide tem mais de 80 palavras no texto de suporte
3. Legenda não tem hook nos primeiros 125 caracteres
4. Script do Reel tem mais de 100 palavras (passa dos 30 segundos)
5. CTA do carrossel ou Reel é genérico ("curta e compartilhe")

## Quality Criteria

- [ ] 3 opções de hook geradas e a escolhida tem justificativa
- [ ] Carrossel tem 8-10 slides com hierarquia headline + suporte
- [ ] Cada slide avança a narrativa sem repetir o anterior
- [ ] Legenda tem hook visível nos primeiros 125 chars
- [ ] Script do Reel tem timecodes e text overlay indicados
- [ ] CTA específico em carrossel e Reel
- [ ] Tom alinhado com driver psicológico do ângulo selecionado
