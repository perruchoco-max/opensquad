---
task: "Criar Conteúdo Instagram"
order: 1
input: |
  - angulo: Ângulo selecionado com driver psicológico, hook e evidência
  - research_output: Briefing de pesquisa com dados e frameworks
  - company: Perfil e tom de voz da Perrucho & Co.
output: |
  - carousel_slides: 8-10 slides com headline + suporte
  - legenda_carrossel: Legenda completa com hook + CTA + hashtags
  - reel_script: Script completo de 15-30s com timecodes
  - legenda_reel: Legenda do Reel com hook + CTA
---

# Criar Conteúdo Instagram

Produz carrossel (8-10 slides), legenda do carrossel, script do Reel e legenda do Reel a partir do ângulo selecionado.

## Process

1. **Absorver ângulo e briefing**: Identificar driver psicológico dominante, hook proposto, evidência principal e audiência-alvo. Tudo que sair daqui precisa estar alinhado com o driver emocional do ângulo.

2. **Gerar 3 opções de hook para o slide 1** e escolher a mais forte: qual versão causa pausa espontânea no scroll? Registrar a escolha com motivo.

3. **Construir carrossel (8-10 slides)**: Slide 1 com hook escolhido → Slides 2-8 com progressão lógica (uma ideia por slide, 40-80 palavras por slide) → Slide final com CTA específico. Nunca repetir o mesmo ponto em slides diferentes.

4. **Escrever legenda do carrossel**: Hook visível nos primeiros 125 chars → 2-4 linhas de contexto → 2-3 insights adicionais → CTA específico → 5-15 hashtags.

5. **Criar script do Reel (15-30s)**: Hook de 0-2s com text overlay → Setup 2-5s → Delivery com pontos-chave e text overlays → CTA específico. Incluir legenda do Reel.

## Output Format

```markdown
# Instagram Content — [Tema]

## CARROSSEL

### Slide 1 — Capa
**Headline**: [texto]
**Suporte**: [texto]

### Slide N
**Headline**: [texto]
**Suporte**: [40-80 palavras]

## LEGENDA DO CARROSSEL
[hook 125 chars]
[contexto]
[insights]
[CTA]
[#hashtags]

## SCRIPT DO REEL
HOOK (0-2s): ...
SETUP (2-5s): ...
DELIVERY (5-25s): ...
CTA (25-30s): ...

## LEGENDA DO REEL
[hook]
[CTA]
[#hashtags]
```

## Output Example

> See pipeline/data/output-examples.md for complete example.

## Quality Criteria

- [ ] Slide 1 tem hook forte (3 opções geradas, melhor escolhida com justificativa)
- [ ] Todos os slides têm headline + suporte (40-80 palavras)
- [ ] Legenda tem hook nos primeiros 125 characters
- [ ] Script do Reel cabe em 15-30 segundos (máx 80 palavras faladas)
- [ ] CTA específico em carrossel, legenda e Reel

## Veto Conditions

Reject and redo if ANY are true:
1. Slide 1 abre com saudação ("Oi pessoal") ou frase sem hook
2. Qualquer slide tem mais de 80 palavras no suporte
3. Script do Reel acima de 100 palavras
