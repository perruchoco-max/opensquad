---
execution: inline
agent: daniela-design
inputFile: squads/perrucho-content/output/instagram-content.md
outputFile: squads/perrucho-content/output/design-output.md
---

# Step 06: Criar Visuais do Carrossel

## Context Loading

Load these files before executing:
- `squads/perrucho-content/output/instagram-content.md` — Conteúdo aprovado do Iago (slides + legendas)
- `_opensquad/_memory/company.md` — Identidade visual da Perrucho & Co.
- `squads/perrucho-content/pipeline/data/domain-framework.md` — Referência de formatos visuais

## Instructions

### Process

1. **Ler o conteúdo do Iago**: Identificar o número de slides, as headlines e os textos de suporte. A estrutura visual segue exatamente o que foi aprovado.

2. **Identificar identidade visual**: Verificar em company.md se há informações de paleta de cores, tipografia ou template do Canva existente para a Perrucho & Co. Se não houver, usar paleta profissional (escuro dominante + accent claro) adequada para posicionamento premium.

3. **Criar os slides no Canva** (usando a skill canva):
   - Slide 1 (Capa): Máximo contraste — fundo escuro ou bold, headline em destaque, handle @perruchoco ou nome da marca
   - Slides 2-N: Template consistente com header (handle + data) e hierarquia visual (headline grande + suporte menor)
   - Slide final: Template de CTA com ação específica em destaque
   - Formato: 1080x1350px (3:4 portrait para Instagram Feed)

4. **Se necessário, gerar imagens de suporte** (usando skill image-generator) para slides que se beneficiem de imagem ilustrativa.

5. **Exportar e documentar**: Para cada slide, registrar o link do Canva e uma breve descrição.

## Output Format

```markdown
# Design Output — [Tema/Ângulo]

Data: [YYYY-MM-DD]
Total de slides criados: [N]
Formato: 1080x1350px (3:4 portrait)

## Slides Criados

### Slide 1 — Capa
- Canva link: [URL]
- Descrição: [headline usada, background, estilo]

### Slide 2
- Canva link: [URL]
- Descrição: [headline, suporte, elementos visuais]

[... demais slides]

## Status
- [ ] Todos os slides exportados em 1080x1350px
- [ ] Template consistente em todos os slides (header + footer)
- [ ] Slide 1 tem alto contraste e headline impactante

## Observações
[Qualquer desvio do planejado ou limitação encontrada]
```

## Veto Conditions

Reject and redo if ANY are true:
1. Slides exportados em resolução menor que 1080x1350px
2. Hierarquia visual ausente (headline e suporte do mesmo tamanho)
3. Template inconsistente entre slides (diferentes fundos ou tipografias sem intenção)

## Quality Criteria

- [ ] Slide 1 tem máximo contraste e headline de impacto
- [ ] Todos os slides têm hierarquia visual clara (headline > suporte)
- [ ] Template consistente (header com handle, footer com data)
- [ ] Links do Canva documentados para todos os slides
- [ ] Formato 1080x1350px confirmado
