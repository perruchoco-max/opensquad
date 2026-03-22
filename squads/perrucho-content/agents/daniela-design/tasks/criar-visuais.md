---
task: "Criar Visuais do Carrossel"
order: 1
input: |
  - instagram_content: Slides aprovados do Iago com headlines e textos de suporte
  - company: Identidade visual e paleta da Perrucho & Co.
output: |
  - design_output: Links do Canva + descrição de cada slide criado + checklist de exportação
---

# Criar Visuais do Carrossel

Transforma os slides de texto do Iago em designs visuais no Canva, mantendo hierarquia visual e identidade da Perrucho & Co.

## Process

1. **Ler todos os slides do Iago**: Mapear número de slides, headlines e textos de suporte. Identificar se há necessidade de imagem de suporte em algum slide.

2. **Configurar template no Canva**: Criar ou usar template existente com header (handle @perruchoco ou nome da marca + data) e footer consistente. Formato 1080x1350px.

3. **Criar cada slide**:
   - Slide 1 (capa): Máximo contraste — fundo dark ou color bold, headline em tipografia grande, subtítulo ou frase complementar. Elemento visual de destaque.
   - Slides 2-N: Template consistente com header, hierarquia headline grande (bold) + suporte menor, alternância intencional de fundo (claro/escuro para criar ritmo)
   - Slide final: Template de CTA — headline de ação + instrução específica em destaque

4. **Exportar** todos os slides em 1080x1350px e documentar links.

5. **Se necessário**: Usar image-generator para slide que se beneficia de imagem ilustrativa — não apenas decorativa.

## Output Format

```markdown
# Design Output

Slides criados: [N]
Formato: 1080x1350px

## Links

| Slide | Canva Link | Descrição |
|---|---|---|
| 1 — Capa | [URL] | [headline, estilo, elementos] |
| 2 | [URL] | [descrição] |
[...]

## Checklist
- [ ] Todos em 1080x1350px
- [ ] Template consistente (header + footer)
- [ ] Slide 1 com alto contraste
```

## Quality Criteria

- [ ] Todos os slides em 1080x1350px
- [ ] Hierarquia visual presente em todos os slides
- [ ] Template consistente com header/footer
- [ ] Links documentados para todos os slides

## Veto Conditions

Reject and redo if ANY are true:
1. Qualquer slide exportado em resolução menor que 1080x1350px
2. Template inconsistente entre slides sem justificativa
