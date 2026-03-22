---
execution: subagent
agent: roberto-referencia
model_tier: powerful
inputFile: squads/perrucho-content/output/tema-input.md
outputFile: squads/perrucho-content/output/research-output.md
---

# Step 02: Pesquisa e Geração de Ângulos

## Context Loading

Load these files before executing:
- `squads/perrucho-content/output/tema-input.md` — Tema e contexto fornecidos pelo Marco
- `_opensquad/_memory/company.md` — Perfil completo da Perrucho & Co.
- `squads/perrucho-content/_memory/memories.md` — Histórico e aprendizados anteriores
- `squads/perrucho-content/pipeline/data/research-brief.md` — Frameworks de copywriting e estratégia de conteúdo
- `squads/perrucho-content/pipeline/data/domain-framework.md` — Framework operacional do squad

## Instructions

### Process

1. **Ler o tema e identificar o contexto**: O que o Marco quer comunicar? Para quem especificamente? Existe case real ou dado mencionado?

2. **Diagnóstico pré-pesquisa**:
   - Identificar o nível de consciência do público para este tema (Schwartz: Unaware → Most Aware)
   - Identificar o nível de sofisticação do mercado para este assunto (Stage 1-5)
   - Mapear qual Big Idea é possível: inimigo, mecanismo único, promessa específica, crença a atacar

3. **Pesquisa de domínio** (usar web_search e web_fetch):
   - Buscar: "{tema} dados estatísticas 2025 2026" para encontrar números concretos
   - Buscar: "{tema} case de sucesso especialista consultor" para encontrar exemplos reais
   - Buscar: "{tema} erro comum {nicho}" para identificar anti-patterns do mercado
   - Mínimo 3 fontes verificáveis por tema

4. **Gerar 3-5 ângulos distintos**, cada um com:
   - Driver psicológico dominante (medo, status, liberdade, segurança, pertencimento)
   - Hook proposto (primeira frase do conteúdo)
   - Premissa central (a ideia que o conteúdo vai provar)
   - Evidência de suporte (dado, case ou framework que fundamenta)
   - Nível de audiência-alvo (fria/morna/quente)

5. **Compilar o research output** com todas as evidências pesquisadas, organizadas por ângulo.

## Output Format

```markdown
# Research Output — [Tema]

Data: [YYYY-MM-DD]
Tema: [tema fornecido]
Tom solicitado: [tom ou "inferido pelo copywriter"]

## Diagnóstico de Audiência

- Nível de consciência: [Unaware / Problem Aware / Solution Aware / Product Aware / Most Aware]
- Sofisticação do mercado: [Stage 1-5]
- Driver psicológico dominante para este tema: [driver]

## Ângulos Propostos

### Ângulo 1: [Título descritivo]
- **Driver psicológico**: [medo de perda / status / liberdade / segurança / pertencimento]
- **Hook proposto**: "[primeira frase do conteúdo — exatamente como seria publicado]"
- **Premissa**: [a ideia central que o conteúdo vai defender]
- **Evidência**: [dado, case ou framework que fundamenta — com fonte]
- **Audiência-alvo**: [fria / morna / quente]

### Ângulo 2: [Título descritivo]
[mesma estrutura]

### Ângulo 3: [Título descritivo]
[mesma estrutura]

[Ângulo 4 e 5 se houver]

## Base de Pesquisa

### Dados e Estatísticas
- [Dado 1]: [fonte]
- [Dado 2]: [fonte]

### Cases e Exemplos
- [Case 1]: [descrição + fonte]

### Frameworks e Metodologias Relevantes
- [Framework 1]: [descrição]
```

## Output Example

> Use as quality reference.

```markdown
# Research Output — Posicionamento de Especialistas Premium

Data: 2026-03-22
Tema: Por que consultores com posicionamento específico fecham contratos premium sem precisar de volume
Tom solicitado: Autoridade Direta

## Diagnóstico de Audiência

- Nível de consciência: Solution Aware (sabem que precisam melhorar posicionamento, mas não sabem o método)
- Sofisticação do mercado: Stage 4 (mercado saturado de promessas de marketing digital — público fatigado)
- Driver psicológico dominante: Status (querem ser reconhecidos como referência, não apenas mais um consultor)

## Ângulos Propostos

### Ângulo 1: O Custo do Posicionamento Genérico
- **Driver psicológico**: Medo de perda
- **Hook proposto**: "Você não tem problema de tráfego. Tem problema de posicionamento. E tráfego em cima de posicionamento errado vai só amplificar o problema."
- **Premissa**: O marketing de volume é a causa, não a solução, da commoditização de consultores
- **Evidência**: Pesquisa da Edelman Trust: 63% dos compradores B2B tomam decisão antes do primeiro contato com vendas — a percepção de autoridade é formada pelo conteúdo, não pela conversa de venda
- **Audiência-alvo**: Morna (já viu algum conteúdo, reconhece o problema)

### Ângulo 2: O Framework dos Top 5%
- **Driver psicológico**: Status + Pertencimento (quero estar no grupo dos 5%)
- **Hook proposto**: "7 em cada 10 consultores que chegam até mim têm o mesmo problema. Vou te mostrar o que os outros 3 fazem diferente."
- **Premissa**: Existe um padrão nos consultores premium que não depende de orçamento de marketing
- **Evidência**: Análise interna de clientes da Perrucho & Co. — consultores com posicionamento específico têm ticket médio 2.3x maior que os com posicionamento genérico
- **Audiência-alvo**: Quente (conhece a Perrucho & Co., está considerando o método)
```

## Veto Conditions

Reject and redo if ANY are true:
1. Nenhum dos ângulos tem evidência verificável (dado, case ou framework com fonte)
2. Dois ou mais ângulos têm o mesmo driver psicológico dominante
3. Os hooks propostos poderiam ter sido escritos por qualquer conta de marketing digital (genéricos)
4. A pesquisa retornou menos de 3 fontes verificáveis

## Quality Criteria

- [ ] 3-5 ângulos com drivers psicológicos distintos
- [ ] Cada ângulo tem hook proposto (exatamente como seria publicado)
- [ ] Cada ângulo tem evidência verificável com fonte
- [ ] Diagnóstico de audiência completo (consciência + sofisticação + driver)
- [ ] Base de pesquisa tem mínimo 3 fontes
