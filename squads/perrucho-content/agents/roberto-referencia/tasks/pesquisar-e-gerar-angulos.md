---
task: "Pesquisar Tema e Gerar Ângulos"
order: 1
input: |
  - tema: Tema ou assunto fornecido pelo Marco no checkpoint
  - contexto: Case, dado ou evento adicional (opcional)
  - tom_preferido: Tom de voz selecionado pelo Marco (opcional)
output: |
  - research_output: Arquivo completo com diagnóstico de audiência, 3-5 ângulos e base de pesquisa
---

# Pesquisar Tema e Gerar Ângulos

Recebe um tema bruto do Marco, pesquisa dados e frameworks relevantes, e produz 3-5 ângulos de conteúdo com evidências para o Marco escolher.

## Process

1. **Diagnóstico pré-pesquisa**: Ler o tema e identificar nível de consciência do público (Schwartz: Unaware → Most Aware), nível de sofisticação do mercado (Stage 1-5) e driver psicológico mais potente para este tema.

2. **Pesquisa de evidências** (mínimo 3 fontes verificáveis):
   - Buscar dados estatísticos: "{tema} dados estatísticas 2025 2026"
   - Buscar cases práticos: "{tema} case resultado consultor especialista"
   - Buscar anti-patterns do mercado: "erro comum {nicho} {tema}"

3. **Big Idea check**: Para cada ângulo candidato, verificar se tem inimigo claro + mecanismo único + promessa específica + crença a atacar. Descartar ângulos sem Big Idea.

4. **Gerar 3-5 ângulos** com drivers psicológicos distintos: cada um tem hook proposto (frase exata), premissa central, evidência de suporte e audiência-alvo.

5. **Compilar e estruturar** o research output conforme o formato definido no step-02.

## Output Format

```yaml
tema: "..."
data: "YYYY-MM-DD"
diagnostico:
  nivel_consciencia: "..."
  sofisticacao_mercado: "Stage X"
  driver_dominante: "..."
angulos:
  - titulo: "..."
    driver: "..."
    hook: "..."
    premissa: "..."
    evidencia: "..."
    audiencia: "fria/morna/quente"
base_pesquisa:
  dados:
    - item: "..."
      fonte: "..."
  cases:
    - item: "..."
```

## Output Example

> Use as quality reference, not as rigid template.

```yaml
tema: "Por que consultores com posicionamento específico fecham mais premium"
data: "2026-03-22"
diagnostico:
  nivel_consciencia: "Solution Aware"
  sofisticacao_mercado: "Stage 4"
  driver_dominante: "Status (querem ser referência, não mais um)"
angulos:
  - titulo: "O Custo do Posicionamento Genérico"
    driver: "Medo de perda"
    hook: "Você não tem problema de tráfego. Tem problema de posicionamento. E tráfego em cima de posicionamento errado vai amplificar o problema."
    premissa: "Marketing de volume é a causa da commoditização de consultores"
    evidencia: "63% dos compradores B2B decidem antes do primeiro contato com vendas (Edelman Trust 2025)"
    audiencia: "morna"
  - titulo: "O Framework dos Top 5%"
    driver: "Status + Pertencimento"
    hook: "7 em cada 10 consultores que chegam até mim têm o mesmo problema. Vou te mostrar o que os outros 3 fazem diferente."
    premissa: "Existe padrão identificável nos consultores premium que não depende de orçamento"
    evidencia: "Análise de 40 clientes: ticket médio 2.3x maior com posicionamento específico vs. genérico"
    audiencia: "quente"
base_pesquisa:
  dados:
    - item: "63% dos compradores B2B fazem a decisão antes do primeiro contato"
      fonte: "Edelman Trust Barometer 2025"
    - item: "Mercado de consultoria no Brasil cresce 12% ao ano mas margem média cai 8%"
      fonte: "IBGE + relatório setorial 2025"
```

## Quality Criteria

- [ ] 3-5 ângulos gerados com drivers psicológicos distintos (nenhum repetido)
- [ ] Cada ângulo tem hook proposto em linguagem exatamente como seria publicado
- [ ] Mínimo 3 fontes verificáveis na base de pesquisa
- [ ] Diagnóstico de audiência completo (consciência + sofisticação + driver)

## Veto Conditions

Reject and redo if ANY are true:
1. Menos de 3 ângulos gerados
2. Dois ou mais ângulos com o mesmo driver psicológico dominante
3. Nenhuma evidência verificável em nenhum dos ângulos
