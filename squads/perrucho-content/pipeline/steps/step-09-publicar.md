---
execution: inline
agent: bruno-blotato
inputFile: squads/perrucho-content/output/design-output.md
outputFile: squads/perrucho-content/output/publish-report.md
---

# Step 09: Publicação

## Context Loading

Load these files before executing:
- `squads/perrucho-content/output/instagram-content.md` — Legendas e conteúdo final do Instagram
- `squads/perrucho-content/output/tiktok-content.md` — Script e legenda final do TikTok
- `squads/perrucho-content/output/design-output.md` — Links dos visuais do Canva + arquivos exportados
- `squads/perrucho-content/output/review-output.md` — Confirmação de aprovação da Vera

## Instructions

### Process

1. **Executar checklist pré-publicação**:
   - [ ] Legenda do Instagram carrossel está completa com CTA e hashtags?
   - [ ] Visuais do carrossel estão em 1080x1350px?
   - [ ] Legenda do Reel está completa?
   - [ ] Legenda do TikTok está dentro do limite (máx 2200 chars)?
   - [ ] Horário de publicação confirmado pelo Marco?

2. **Confirmar horários** antes de publicar:
   - Instagram Feed: 9-11h ou 19-21h, terça a quinta preferencialmente
   - TikTok: 12-14h ou 19-22h para audiência brasileira

3. **Publicar no Instagram** via Blotato:
   - Carrossel com todos os slides e legenda completa
   - Reel com legenda (se arquivo de vídeo disponível)
   - Registrar permalink

4. **Publicar no TikTok** via Blotato:
   - Script como referência para gravação (se vídeo não estiver pronto, agendar ou marcar como pendente)
   - Legenda completa
   - Registrar permalink quando disponível

5. **Registrar tudo no publish-report.md** e atualizar memories.md com aprendizados desta rodada.

## Output Format

```markdown
# Publish Report — [Tema/Ângulo]

Data de publicação: [YYYY-MM-DD HH:MM]
Executado por: Bruno Blotato

## Status por Plataforma

### Instagram Feed (Carrossel)
- Status: [Publicado / Agendado / Falhou]
- Horário: [HH:MM]
- Permalink: [URL ou "pendente"]
- Observações: [qualquer nota relevante]

### Instagram Reels
- Status: [Publicado / Agendado / Pendente — vídeo não gravado]
- Horário: [HH:MM]
- Permalink: [URL ou "pendente"]

### TikTok
- Status: [Publicado / Agendado / Pendente — vídeo não gravado]
- Horário: [HH:MM]
- Permalink: [URL ou "pendente"]

## Checklist Pré-Publicação

- [ ] Legenda Instagram completa com CTA e hashtags
- [ ] Visuais em resolução correta (1080x1350px)
- [ ] Legenda TikTok dentro do limite de caracteres
- [ ] Horário confirmado pelo Marco

## Aprendizados desta Rodada

[Notas para atualizar memories.md — o que funcionou, o que foi ajustado, decisões do Marco]
```

## Veto Conditions

Reject and redo if ANY are true:
1. Publicação executada sem confirmação do Marco no step-08
2. Legenda publicada com texto incompleto ou truncado
3. Erro de API não reportado ao Marco

## Quality Criteria

- [ ] Checklist pré-publicação completo antes de qualquer disparo
- [ ] Permalinks registrados para todos os posts publicados
- [ ] Erros de API documentados com mensagem completa
- [ ] Memories.md atualizado com aprendizados da rodada
