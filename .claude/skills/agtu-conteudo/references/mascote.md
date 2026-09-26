# Mascote da série

**Atual (26/09/2026):** personagem de pelúcia bege, rosto claro com bochechas rosadas, óculos redondos de aro azul-marinho, cachecol branco de tricô com o logo AGTU bordado na ponta. Arquivo com fundo transparente: `assets/mascote.png`. A coruja (`coruja.png`, `coruja_final.png`) foi substituída e não deve mais ser usada.

Não é apresentado como mascote oficial da AGTU, nem como aluno, professor ou produto, nem como criado em alguma IA. Aparece pequeno, só na capa, com o balão "Série: AGTU Tendências".

## Descrição fixa (usar igual em todo prompt)
Personagem fofo de pelúcia, corpo arredondado e peludo cor bege-areia, rosto liso claro com bochechas rosadas, olhos pretos brilhantes, boca aberta sorrindo, óculos redondos finos de aro azul-marinho, cachecol branco felpudo enrolado no pescoço com uma ponta caindo na frente e o logo AGTU (brasão vermelho e azul + AGTU) bordado nessa ponta. Estilo 3D de brinquedo, iluminação suave de estúdio.

## Regras de uso
- Nunca espelhar a imagem: o cachecol tem o logo e vira texto invertido.
- Aparece só na capa. A última tela é do curso, sem mascote.
- Fala só no balão da capa: "Série: AGTU Tendências" (Nunito 800, azul AGTU).
- Tamanho: cerca de 330 px de largura na arte de 1080 px, no canto inferior direito, com sombra suave encostada nos pés.

## Capa em vídeo (aprovada em 26/09/2026)
A capa usa o vídeo do mascote acenando enviado pela Giovanna: `assets/mascote_acenando.mp4` (10 s, 24 fps, com som). Ele começa e termina na mesma pose, então repete sem corte.
- A IA do vídeo troca o brasão do cachecol por outro escudo a partir de ~1 s. `bash scripts/quadros-do-mascote.sh` extrai os quadros, cola o logo certo em cada um (alinhado pelas letras AGTU), deixa o fundo branco puro e reduz para 362 px em `assets/mframes/`.
- No template, o quadro entra com mesclagem "multiplicar" sobre o fundo branco (sem caixa em volta), abaixo do balão, com sombra suave nos pés. A capa parada usa o quadro 25 (braço erguido, olhos abertos).
- Exportar: `bash scripts/quadros-do-mascote.sh`, depois `node assets/exportar-png-e-video.js video` e juntar os quadros em MP4 a 24 fps com o áudio do vídeo original (comando no `SKILL.md`).
- Todo vídeo novo do mascote: conferir o logo do cachecol quadro a quadro antes de usar.

### Alternativa sem vídeo: aceno por camadas
Se não houver vídeo, o mascote parado acena por camadas (mesmo tamanho da imagem original, nesta ordem): `m_base.png`, `m_antebraco.png` (gira no cotovelo, origem 22,34% × 48,51%), `m_cotovelo.png`, `m_olho_e.png` e `m_olho_d.png` (piscam com scaleY). O CSS e os keyframes continuam no template (classe `rig`). Marcação:
```html
<div class="mwrap rig">
  <div class="mshadow"></div>
  <div class="breath"><div class="lean">
    <img class="lay" src="m_base.png" alt="Mascote">
    <img class="lay fore" src="m_antebraco.png" alt="">
    <img class="lay" src="m_cotovelo.png" alt="">
    <img class="lay eye e" src="m_olho_e.png" alt="">
    <img class="lay eye d" src="m_olho_d.png" alt="">
  </div></div>
</div>
```
Para refazer as camadas a partir de outra imagem: `scripts/montar-aceno-mascote.py`.

## Prompt para novas poses (Nano Banana / Gemini, GPT Image ou similar, sempre com a imagem de referência anexada)
```
Use the attached image as the character reference. Keep the exact same plush character: round fluffy sand-beige body, smooth light face with pink cheeks, shiny black eyes, open smiling mouth, thin round navy glasses, fluffy white scarf with one end hanging in front and the AGTU shield logo embroidered on it exactly as in the reference. Same 3D rendering style, same lighting.
New pose: [DESCREVER A POSE, ex.: pointing up with the right arm, surprised expression, holding a smartphone with a blank screen].
Plain pure white background, full body, centered, soft shadow under the feet. No extra text, no extra logos.
```

### Poses úteis para ter no banco
1. Apontando para cima (explicando)
2. Segurando um celular de tela branca (a tela entra na edição)
3. Lendo um livro grosso
4. Surpreso, com as mãos no rosto
5. Fazendo "joinha"
6. Com lupa (post de "confira você mesmo")
7. Sentado na frente de um notebook à noite (rotina de estudo)
8. Com fone de ouvido (aula ao vivo)

Depois de gerar: recortar o fundo, conferir se o logo do cachecol continua correto e sem letras trocadas. Se a IA deformar o logo, corrigir na edição com o arquivo oficial.
