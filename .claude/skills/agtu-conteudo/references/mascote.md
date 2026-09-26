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

## Animação da capa (aprovada em 26/09/2026)
O mascote não entra deslizando e não balança. Ele fica no lugar e:
- pisca duas vezes (0,4 s e 4,2 s);
- respira (1,4% de escala vertical a cada 3 s);
- depois que o balão aparece, levanta o antebraço do lado do texto e acena chamando (1,4 s a 3,5 s), com o corpo inclinando de leve e girando um pouco em 3D;
- a imagem parada da capa é o quadro de 2,9 s, com o aceno no alto.

Camadas em `assets/`, todas do tamanho da imagem original e empilhadas nesta ordem:
1. `m_base.png`: corpo sem o antebraço e sem os olhos;
2. `m_antebraco.png`: gira no cotovelo (origem 22,34% × 48,51%);
3. `m_cotovelo.png`: disco de pelo que esconde a emenda;
4. `m_olho_e.png` e `m_olho_d.png`: piscam com scaleY.

CSS e keyframes em `template-tendencias.html` (classe `rig`). Para refazer as camadas a partir de outra imagem do mascote, use `scripts/montar-aceno-mascote.py` (ajustar a dobra do braço, o cotovelo e a posição dos olhos) e confira a folha de poses que ele gera.

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
