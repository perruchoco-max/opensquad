---
execution: inline
agent: vera-veredito
inputFile: squads/perrucho-content/output/instagram-content.md
outputFile: squads/perrucho-content/output/review-output.md
---

# Step 07: Revisão de Qualidade

## Context Loading

Load these files before executing:
- `squads/perrucho-content/output/instagram-content.md` — Conteúdo do Iago
- `squads/perrucho-content/output/tiktok-content.md` — Conteúdo do Tiago
- `squads/perrucho-content/output/design-output.md` — Visuais da Daniela
- `squads/perrucho-content/output/angulo-selecionado.md` — Ângulo aprovado pelo Marco
- `squads/perrucho-content/pipeline/data/quality-criteria.md` — Critérios de qualidade
- `squads/perrucho-content/pipeline/data/anti-patterns.md` — Anti-patterns a verificar
- `_opensquad/_memory/company.md` — Tom e identidade da Perrucho & Co.

## Instructions

### Process

1. **Carregar e revisar quality-criteria.md**: Esses são os únicos critérios válidos. Não criar critérios novos no momento da review.

2. **Ler o ângulo selecionado**: O driver psicológico e o hook proposto definem o padrão de tom para toda a review.

3. **Avaliar cada formato separadamente**:
   - Carrossel: slide por slide (headline + suporte + progressão)
   - Legenda do carrossel: hook 125 chars + estrutura + CTA
   - Script do Reel: hook 0-2s + duração + CTA
   - Script do TikTok: hook 0-3s + on-screen text + CTA stand-alone
   - Visuais: hierarquia + consistência de template

4. **Pontuar cada critério** (1-10) com justificativa específica de 1-2 frases.

5. **Identificar itens bloqueantes vs. não-bloqueantes**:
   - Bloqueante: precisa mudar para aprovar
   - Não-bloqueante: melhoria recomendada mas não obrigatória

6. **Emitir veredito final**: APROVADO, APROVADO COM RESSALVAS ou REJEITADO.

## Output Format

```markdown
# Review — [Tema/Ângulo]

Data: [YYYY-MM-DD]
Revisora: Vera Veredito
Ciclo de revisão: [1 / 2 / 3]

## VEREDITO: [APROVADO / APROVADO COM RESSALVAS / REJEITADO]

---

## Pontuação por Critério

### Critérios Globais

| Critério | Score | Justificativa |
|---|---|---|
| Alinhamento de Marca | [X]/10 | [justificativa específica] |
| Especificidade | [X]/10 | [justificativa específica] |
| Alinhamento com Ângulo Emocional | [X]/10 | [justificativa específica] |

### Instagram Feed — Carrossel

| Critério | Score | Justificativa |
|---|---|---|
| Hook do Slide 1 | [X]/10 | [justificativa] |
| Hierarquia por slide | [X]/10 | [justificativa] |
| Progressão lógica | [X]/10 | [justificativa] |
| Slide final com CTA | [X]/10 | [justificativa] |
| Legenda estruturada | [X]/10 | [justificativa] |

### Instagram Reels

| Critério | Score | Justificativa |
|---|---|---|
| Hook 0-2s | [X]/10 | [justificativa] |
| Duração | [X]/10 | [justificativa] |
| CTA específico | [X]/10 | [justificativa] |

### TikTok

| Critério | Score | Justificativa |
|---|---|---|
| Hook 0-3s | [X]/10 | [justificativa] |
| On-screen text | [X]/10 | [justificativa] |
| CTA de baixo atrito | [X]/10 | [justificativa] |
| Stand-alone | [X]/10 | [justificativa] |

**Média geral**: [X]/10

---

## Feedback Bloqueante (obrigatório para aprovar)

[Se APROVADO: "Nenhum item bloqueante identificado."]

1. [Item bloqueante]: [descrição específica do problema] → [sugestão de correção acionável]

---

## Feedback Não-Bloqueante (recomendações)

1. [Sugestão de melhoria opcional]

---

## Agente Responsável por Correções

[Se houver itens bloqueantes:]
- Copy (carrossel, legenda, scripts) → Iago Instagram / Tiago TikTok
- Visuais → Daniela Design
```

## Veto Conditions

Reject and redo if ANY are true:
1. Score emitido sem justificativa textual específica
2. Veredito ambíguo (qualquer coisa diferente de APROVADO, APROVADO COM RESSALVAS ou REJEITADO)
3. Feedback bloqueante sem sugestão de correção acionável

## Quality Criteria

- [ ] Todos os critérios do quality-criteria.md avaliados
- [ ] Cada score tem justificativa de 1-2 frases
- [ ] Feedback bloqueante separado do não-bloqueante
- [ ] Veredito final claro e sem ambiguidade
- [ ] Agente responsável por correção identificado para cada item bloqueante
