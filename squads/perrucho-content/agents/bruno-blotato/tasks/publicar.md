---
task: "Publicar no Instagram e TikTok"
order: 1
input: |
  - design_output: Links dos visuais do Canva para o carrossel
  - instagram_content: Legendas finais do Instagram (carrossel + Reel)
  - tiktok_content: Legenda final do TikTok
  - horario_confirmado: Horário de publicação aprovado pelo Marco no step-08
output: |
  - publish_report: Status de publicação + permalinks + aprendizados da rodada
---

# Publicar no Instagram e TikTok

Executa a publicação via Blotato em todas as plataformas confirmadas, registra permalinks e atualiza memories.

## Process

1. **Checklist pré-publicação**: Verificar completude de cada item antes de qualquer disparo — legenda completa, visuais em resolução correta, horário definido.

2. **Confirmar horário com Marco**: Antes de agendar, confirmar: "Confirmo publicação do carrossel no Instagram para [dia] às [hora] e TikTok às [hora] — está ok?"

3. **Publicar Instagram Carrossel** via Blotato: Upload dos slides na sequência correta, legenda completa com hashtags, horário agendado. Registrar permalink.

4. **Publicar TikTok** via Blotato: Legenda completa, hashtags, horário. Se vídeo não estiver disponível, marcar como "Script pronto — aguardando gravação". Registrar permalink quando disponível.

5. **Publicar Instagram Reel** se vídeo estiver disponível. Caso contrário, marcar como pendente.

6. **Registrar tudo** no publish-report.md e atualizar squads/perrucho-content/_memory/memories.md com aprendizados desta rodada.

## Output Format

```markdown
# Publish Report — [Tema]

Data: [YYYY-MM-DD]

## Status

| Plataforma | Status | Horário | Permalink |
|---|---|---|---|
| Instagram Feed | [Publicado/Agendado/Falhou] | [HH:MM] | [URL] |
| Instagram Reel | [Publicado/Pendente] | [HH:MM] | [URL] |
| TikTok | [Publicado/Pendente] | [HH:MM] | [URL] |

## Aprendizados
[Notas para memories.md]
```

## Quality Criteria

- [ ] Checklist pré-publicação executado antes de qualquer disparo
- [ ] Horário confirmado pelo Marco antes do agendamento
- [ ] Permalinks registrados para posts publicados
- [ ] Memories.md atualizado

## Veto Conditions

Reject and redo if ANY are true:
1. Publicação sem confirmação do Marco no step-08
2. Legenda publicada incompleta ou truncada
3. Erro de API não reportado
