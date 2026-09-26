---
name: agtu-conteudo
description: Produz conteúdo de redes sociais da AGTU (American Global Tech University) — carrosséis, Reels, Stories e posts de LinkedIn — com a voz, o mascote coruja, a série AGTU Tendências e as regras de marca e de funil da AGTU. Use sempre que pedirem um post, carrossel, roteiro de Reels, stories, legenda ou calendário para a AGTU, ou quando disserem "post do AGTU Tendências", "tendência da semana" ou citarem o mascote coruja.
---

# AGTU Conteúdo

Ferramenta de produção de conteúdo da AGTU. Junta as regras da marca com as outras skills instaladas e a biblioteca de prompts em `references/prompts.md`.

## Antes de escrever

1. Leia `references/marca.md` (voz, público, cores, regras que nunca mudam).
2. Se for AGTU Tendências, leia `references/serie-tendencias.md`.
3. Se o post tiver mascote, leia `references/mascote.md`.
4. Pegue o prompt certo em `references/prompts.md` e adapte ao pedido.

## Fluxo de produção

1. **Pesquisa.** Todo fato, número, data e nome de produto vem de fonte primária (site oficial, central de ajuda, comunicado). Anote a fonte. Se não achar, não use o dado.
2. **Etapa do funil.** Decida topo, meio ou fundo antes de escrever. Isso define o CTA (ver `marca.md`).
3. **Estrutura.** Carrossel da série: 5 telas (capa com mascote, 3 de conteúdo, fechamento com mascote). Outros carrosséis: 4 ou 5 telas. Use a skill `social` (referência `carousel-frameworks.md`) para escolher o formato narrativo.
4. **Gancho.** Gere 5 opções com a skill `hook-generator` e escolha a mais específica.
5. **Texto.** Escreva e passe pela skill `humanizer` e pela lista de vícios em português de `marca.md`.
6. **Arte.** Parta de `assets/template-tendencias.html`. Regras da skill `frontend-design`. Exporte com `node assets/exportar-png-e-video.js` (PNG de todas as telas; com o argumento `video`, gera os quadros da capa animada, depois junte em MP4 com ffmpeg).
7. **Revisão visual.** Abra os PNGs e confira: texto sobreposto, mascote espelhado (o cachecol tem texto: nunca espelhar), legibilidade em miniatura, logo na capa.
8. **Entrega.** PNGs 1080×1350 + legenda + texto alternativo + resposta automática da palavra-chave + fontes.

## Regras que não mudam

- Logo AGTU no alto da primeira tela de todo carrossel e na primeira cena de todo Reels.
- Nada de "grátis", "gratuito", "sem custo" ou "30 dias". A AGTU não tem oferta gratuita.
- Nada de promessa de emprego, salário, promoção ou prazo não confirmado (o site informa conclusão em até 18 meses).
- Marca de terceiros (ex.: Muse, da Meta) só em conteúdo informativo, com a linha "X é marca de Y. Conteúdo informativo, sem vínculo com Y."
- Depoimento só de aluno real e autorizado. A coruja nunca é apresentada como mascote oficial da AGTU, aluna, professora ou produto.
- Um CTA por etapa. A última tela pode juntar topo (compartilhar) e fundo (palavra-chave no direct).
