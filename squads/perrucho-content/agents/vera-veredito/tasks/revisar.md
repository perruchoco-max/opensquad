---
task: "Revisar Todo o Conteúdo"
order: 1
input: |
  - instagram_content: Carrossel + legendas + script do Reel
  - tiktok_content: Script + legenda do TikTok
  - design_output: Visuais criados pela Daniela
  - angulo_selecionado: Ângulo e driver psicológico aprovado pelo Marco
  - quality_criteria: Critérios de qualidade do squad
output: |
  - review_output: Pontuação por critério + veredito + feedback bloqueante e não-bloqueante
---

# Revisar Todo o Conteúdo

Avalia todo o conteúdo produzido (Instagram + TikTok + visuais) contra os critérios de qualidade e emite veredito claro.

## Process

1. **Carregar quality-criteria.md**: Esses critérios são a única base do julgamento. Não criar critérios novos.

2. **Verificar alinhamento com ângulo**: Identificar o driver psicológico do ângulo selecionado. Cada elemento de conteúdo deve estar alinhado com esse driver.

3. **Avaliar cada formato**: Carrossel (slide a slide) → Legenda do carrossel → Script do Reel → Script do TikTok → Visuais.

4. **Pontuar cada critério** (1-10) com justificativa de 1-2 frases. Identificar itens bloqueantes vs. não-bloqueantes.

5. **Calcular média e emitir veredito**:
   - APROVADO: média ≥ 7 e nenhum critério crítico < 4
   - APROVADO COM RESSALVAS: média ≥ 7 mas 1-2 critérios não-críticos entre 4-6
   - REJEITADO: média < 7 ou qualquer critério crítico < 4

## Output Format

```markdown
# Review — [Tema]

## VEREDITO: [APROVADO / APROVADO COM RESSALVAS / REJEITADO]

## Pontuação

| Critério | Score | Justificativa |
|---|---|---|
| Alinhamento de Marca | X/10 | [justificativa] |
| Especificidade | X/10 | [justificativa] |
| Hook Carrossel | X/10 | [justificativa] |
[...]

Média: X/10

## Feedback Bloqueante
[Nenhum] ou [lista com correção acionável por item]

## Feedback Não-Bloqueante
[sugestões opcionais]

## Agente responsável por correções
[Iago / Tiago / Daniela — por tipo de item]
```

## Quality Criteria

- [ ] Todos os critérios de quality-criteria.md avaliados com score
- [ ] Cada score tem justificativa de 1-2 frases
- [ ] Veredito final claro (APROVADO / APROVADO COM RESSALVAS / REJEITADO)
- [ ] Feedback bloqueante tem correção acionável

## Veto Conditions

Reject and redo if ANY are true:
1. Score emitido sem justificativa
2. Veredito ambíguo ou ausente
3. Feedback bloqueante sem sugestão de correção
