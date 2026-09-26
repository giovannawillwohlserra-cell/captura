# Biblioteca de prompts AGTU

Prompts testados ou adaptados de guias públicos (snubroot/Veo-3-Prompting-Guide, ZeroLu/awesome-nanobanana-pro, guias de Veo 3 e Nano Banana de Replicate, Morphic e Will Francis). Prompts de texto (para o Claude) estão em português. Prompts de imagem e vídeo estão em inglês, porque as ferramentas respondem melhor em inglês; o texto que vai aparecer na tela entra sempre na edição, nunca gerado pela IA.

Troque o que está em [colchetes].

---

## A. Pesquisa e pauta (Claude)

### A1 · Tendência da semana para o AGTU Tendências
```
Pesquise as notícias dos últimos 7 dias sobre [ÁREA: IA / cibersegurança / cloud / ESG / saúde / direito / educação digital].
Liste 5 candidatas a tendência da semana. Para cada uma: o que aconteceu, data, fonte primária (link oficial), por que interessa a um profissional brasileiro de 40 a 55 anos e qual curso da AGTU ela conecta.
Descarte o que não tiver fonte oficial. Recomende uma e diga por quê.
```

### A2 · Transformar uma notícia em 4 telas
```
Use a skill agtu-conteudo, série AGTU Tendências #[N].
Tema: [TENDÊNCIA]. Fonte: [LINK OFICIAL].
Monte as 4 telas no roteiro fixo (capa, como funciona, o que ninguém te conta, fechamento com o curso [CURSO]).
Para cada tela: título, texto (até 30 palavras), fala da coruja (até 12 palavras) e imagem oficial a usar.
Depois, a legenda, a palavra-chave do direct e a resposta automática.
```

### A3 · Calendário do mês por funil
```
Com base nos cursos da AGTU e na tese do mês "[TESE]", proponha [N] peças para [MÊS] com 45% topo, 35% meio e 20% fundo.
Para cada peça: data, canal, formato, etapa, gancho, CTA e métrica principal.
Inclua 1 AGTU Tendências por semana, 1 peça de humor por semana e 1 depoimento real por quinzena.
```

---

## B. Ganchos e textos (Claude)

### B1 · Dez ganchos para a capa ou para os 2 primeiros segundos
```
Tema: [TEMA]. Público: profissional de 40 a 55 anos que pensa em fazer mestrado.
Escreva 10 ganchos em português com até 12 palavras, dois de cada tipo:
1. Pergunta que a pessoa já se fez ("Você deixaria uma IA mandar e-mail por você?")
2. Número concreto com fonte
3. Cena do dia a dia ("21h40: a plateia chegou.")
4. Contraste expectativa × realidade
5. Segredo de bastidor ("O que ninguém te conta sobre…")
Sem "descubra", "transforme", "o futuro é agora". Marque o mais forte e diga por quê.
```

### B2 · Legenda que gera comentário
```
Escreva a legenda do post [RESUMO].
Estrutura: 1 frase de gancho diferente da capa; 2 a 3 frases com o fato principal e a fonte; 1 pergunta fácil de responder nos comentários; 1 linha de CTA com a palavra-chave [PALAVRA]; fontes; 4 hashtags.
Até 120 palavras. Depois passe pela skill humanizer.
```

### B3 · Humanizar um texto pronto
```
Use a skill humanizer e a lista de vícios em português de agtu-conteudo/references/marca.md.
Reescreva o texto abaixo mantendo todos os fatos. Devolva só a versão final e a lista do que mudou.
[TEXTO]
```

### B4 · Resposta automática da palavra-chave
```
Escreva a mensagem automática de direct para quem comentar [PALAVRA] no post sobre [TEMA].
Até 40 palavras, voz da coruja da AGTU, entrega o link [LINK] e termina com uma pergunta de sim ou não que leva ao consultor.
```

---

## C. Formatos de humor e emoção (Claude)

### C1 · "Coisas que só entende quem…"
```
Crie um roteiro de Reels de 20 a 25 segundos no formato "Coisas que só entende quem [SITUAÇÃO, ex.: estuda depois do expediente]".
5 a 6 cenas com horário na tela (19h02, 21h30…), cada uma com uma ação filmável em casa com celular, sem ator profissional.
Última cena: virada positiva + logo AGTU. Sugira o tipo de áudio em alta a procurar na biblioteca do Instagram.
```

### C2 · Expectativa × realidade (carrossel de 4 telas)
```
Tema: [ex.: primeira semana de mestrado aos 45].
Tela 1: título. Telas 2 e 3: uma expectativa e uma realidade engraçada e verdadeira em cada. Tela 4: virada emocional curta + CTA de compartilhar.
A coruja comenta cada tela com uma frase de até 10 palavras.
```

### C3 · POV da família
```
Roteiro de Reels de 20 segundos: "Eu contando para a família que vou fazer [CURSO] aos [IDADE]".
4 reações (mãe, filho, pai, amigo) em uma frase cada, interpretadas pela mesma pessoa do time.
Fechamento com emoção e sem promessa de resultado.
```

### C4 · Depoimento real (perguntas para gravar)
```
Crie 5 perguntas abertas para gravar um aluno real da AGTU sobre [TEMA: voltar a estudar, conciliar trabalho, aplicar o que aprendeu].
Perguntas que puxam história e detalhe concreto, sem induzir a resposta e sem pedir promessa de emprego ou salário.
```

---

## D. Imagem (Nano Banana / Gemini, GPT Image, Ideogram)

Regras gerais: descrever sujeito, ambiente, luz, lente e estilo; pedir "no text, no logos" quando o texto entrar na edição; para personagem, sempre anexar a imagem de referência.

### D1 · Nova pose da coruja
Ver `mascote.md`. Trocar só a linha "New pose".

### D2 · Coruja em cena (capa de carrossel)
```
Use the attached image as the character reference (same owl, same scarf with the AGTU logo, same 3D style).
Scene: the owl [ACTION, ex.: sitting at a small desk at night reading a thick manual titled nothing], cozy warm desk lamp, soft blue night light from a window.
Vertical 4:5 composition, the owl on the right third, empty space on the left third for headline text added later.
No text, no letters, no extra logos. Soft film-like lighting, high detail feathers.
```

### D3 · Fundo limpo para carrossel da série
```
Minimal abstract background for an Instagram carousel, 4:5, soft vertical gradient from pure white at the top to light sky blue (#EAF3FF) and a slightly deeper sky blue (#BFDBFF) at the bottom, very subtle paper grain, one soft blurred light blue shape in the lower right corner. No text, no objects, no logos.
```

### D4 · Objeto-símbolo da tendência (quando não houver imagem oficial)
```
3D isometric illustration of [OBJECT that represents the trend, ex.: a smartphone showing a blank permission dialog with toggle switches], clean white background, soft shadows, rounded friendly shapes, palette of navy #1E417D, sky blue #BFDBFF and a small red #EC2023 accent. No text, no brand logos. 4:5.
```

### D5 · Estilo "papel rasgado" para antes × depois
```
Torn paper collage effect, 4:5: the left half shows [BEFORE SCENE] in cold desaturated tones, the right half shows [AFTER SCENE] in warm tones, separated by a realistic torn white paper edge down the middle. No text, no logos.
```

### D6 · Quadro branco explicativo
```
Whiteboard marker drawing on a clean office whiteboard, hand-drawn diagram explaining [CONCEPT, ex.: read actions vs write actions of an AI agent] with simple icons and arrows, blue and red markers, photographed straight on with soft daylight. Leave labels as simple blank boxes; text will be added later.
```

---

## E. Vídeo (Veo 3, Kling, Sora)

Regras gerais (guia snubroot/Veo-3): um plano por prompt, até 8 segundos; descrever na ordem sujeito → ação → ambiente → câmera → luz → som; para ação em sequência, use "first…, then…"; para evitar legenda gerada, termine com "(no subtitles, no on-screen text)"; para fala, escreva `The owl says: "…"` com frase curta.

### E1 · Plano de abertura com a coruja (Reels)
```
Vertical 9:16, 6 seconds. The AGTU owl mascot from the reference image (blue and white feathers, round gold glasses, navy graduation cap and gown, white scarf with the AGTU logo) stands on a wooden desk next to a laptop at night, first looks at the camera, then raises one wing as if saying hello and tilts its head. Slow push-in, warm desk lamp light with a cool blue window glow. Soft ambient room tone, a short cheerful chime at the end. (no subtitles, no on-screen text)
```

### E2 · Coruja falando (para série curta)
```
Vertical 9:16, 8 seconds, close-up of the AGTU owl mascot from the reference image in a bright home office. The owl says in Brazilian Portuguese, calm and friendly: "Antes de liberar um agente de IA, comece no modo perguntar sempre." Natural beak movement synced to speech, blinking behind gold glasses. Static camera, soft daylight. (no subtitles, no on-screen text)
```

### E3 · Plano de rotina para "Coisas que só entende quem…"
```
Vertical 9:16, 5 seconds, handheld phone-style footage. A person in their late 40s, seen from behind the shoulder, opens a laptop on a dining table at 9:30 pm, first moves a dinner plate aside, then searches under a sofa cushion for a charger and smiles. Warm pendant lamp, lived-in home. Natural room sound. (no subtitles, no on-screen text)
```
Obs.: plano gerado com pessoa nunca é apresentado como aluno real.

### E4 · Transição de produto (tela entra na edição)
```
Vertical 9:16, 5 seconds, over-the-shoulder shot of a person at a laptop at night, the laptop screen is plain bright white with no content (to be replaced in post), slow push-in toward the screen, warm lamp light. (no subtitles, no on-screen text)
```

---

## F. Stories interativos (Claude)

### F1 · Sequência de 4 stories com figurinha
```
Crie 4 stories sobre [TEMA] para [ETAPA].
Story 1: pergunta com enquete. Story 2: resposta/curiosidade. Story 3: quiz ou controle deslizante. Story 4: caixa de pergunta ou link com a palavra-chave [PALAVRA].
Texto de até 15 palavras por story. Indique a figurinha de cada um.
```

### F2 · "Isso ou aquilo"
```
Crie 5 pares "isso ou aquilo" engraçados sobre a rotina de quem estuda trabalhando, com mais de 40 anos. O último par leva ao fundo de funil: "Quando você começa?" com caixa de resposta.
```

---

## G. Revisão final (Claude)

### G1 · Checagem antes de publicar
```
Revise o post abaixo contra agtu-conteudo/SKILL.md e references/marca.md. Aponte, em lista:
1. Todo fato tem fonte primária e data?
2. Aparece "grátis", promessa de emprego, salário ou prazo não confirmado?
3. Logo AGTU na capa? Selo da série, se for AGTU Tendências?
4. No máximo 4 telas? Texto legível (≥ 28 px)?
5. Um CTA coerente com a etapa? Palavra-chave com resposta pronta?
6. Vícios de texto de IA?
7. Marca de terceiros com o aviso de "sem vínculo"?
[POST]
```
