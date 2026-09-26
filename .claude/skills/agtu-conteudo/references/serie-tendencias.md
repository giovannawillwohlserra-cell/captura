# Série AGTU Tendências

Um post por semana com uma tendência real das áreas em que a AGTU tem curso. Quando pedirem "post do AGTU Tendências", siga este padrão (aprovado pela Giovanna na edição 01, em 26/09/2026).

## Formato fixo
- Carrossel de 6 telas + capa em vídeo de 10 s sem áudio (o vídeo do mascote acenando, `assets/mascote_acenando.mp4`, com o texto completo desde o 1º quadro, que vira a miniatura do post; ver `mascote.md`) + capa parada com o mascote por camadas acenando.
- Nome da série só no balão do mascote: "Série: AGTU Tendências" (Nunito 800). Não repetir nas páginas internas.
- Mascote de pelúcia pequeno só na capa. Nunca dizer que ele foi criado em alguma IA.
- Se a tendência for um produto, trazer a identidade dele na capa (ícone oficial, nome e slogan do fabricante) e a fonte no rodapé da tela do fato.
- Arquivo-base: `assets/template-tendencias.html`. Exportação: `assets/exportar-png-e-video.js`.

## Ângulo
O público tem 40 a 55 anos e é especialista. Nada de passo a passo de instalação. O post responde: o que muda no trabalho de quem decide, onde isso entra na semana, e o que continua sendo decisão humana.

## Roteiro das 6 telas (edição 01)
1. **Capa (gancho):** provocação concreta e grande ("A IA já está começando a *negociar por você.*") + uma frase com o fato + identidade do produto + mascote com balão.
2. **O fato:** o que foi lançado e o que ele faz, em lista numerada curta, com fonte e data no rodapé; fecha com uma frase que resume a mudança.
3. **Na empresa:** a tendência dentro de uma empresa, em três linhas curtas + frase de fechamento em caixa cinza.
4. **O dado de mercado:** número grande de fonte reconhecida (ex.: Gartner) escrito com a precisão da fonte ("pelo menos 15%"), gráfico de 100 quadrados, o ponto de partida em destaque ("Em 2024, eram 0%.") e uma frase em caixa azul que motiva a estudar ("Quem decide vai precisar *entender de IA.*").
5. **O desafio de quem lidera:** título com a competência em destaque ("O novo desafio será *governar agentes de IA.*"), três perguntas de liderança e a pergunta principal em caixa azul.
6. **A formação:** frase de impacto, cartão do curso, "O que você estuda" com 4 itens da página do curso ligados ao tema, CTA com a palavra-chave e "grade completa" e "condições de bolsa" em destaque (ver `marca.md`).

## Legenda
Não repetir as telas. Acrescentar contexto (ex.: o aviso do próprio fabricante), um segundo dado, uma pergunta para comentário, o CTA com a palavra-chave, fontes com data, a linha de marca de terceiros, "Toda semana, uma tendência nova na série AGTU Tendências." e hashtags (#AGTUTendencias + 3 a 4 do tema). Entregar junto a resposta automática da palavra-chave.

## Divulgação para alunos
Para o grupo de alunos do curso ligado ao tema: convite curto com o dado mais forte, o link do post, uma pergunta aberta para comentarem e o pedido de compartilhar com quem precisa ver. Nunca pedir que comentem a palavra-chave: a automação mandaria a grade para quem já é aluno.

## Banco de temas (confirmar fatos na semana)
| Curso AGTU | Onde procurar a tendência |
|---|---|
| Inteligência Artificial | Lançamentos de agentes e modelos (salas de imprensa de Meta, Google, OpenAI, Anthropic, Microsoft) |
| Cybersecurity | Outubro é o mês da conscientização em cibersegurança; golpes novos, alertas oficiais (CISA, CERT.br) |
| Cloud Computing | Anúncios de AWS, Google Cloud, Azure; custos e soberania de dados |
| Digital Business & IA | IA em vendas, atendimento e compras (agentes que compram, como o Muse) |
| ESG / Sustentabilidade | Regras novas de relato (ISSB, CVM), consumo de energia da IA |
| Gestão de Saúde | IA em diagnóstico, prontuário, telemedicina (Anvisa, CFM) |
| Direito | Regulação de IA (PL 2338 no Brasil, AI Act na Europa), LGPD |
| Tecnologias Digitais (Educação) | IA na sala de aula, políticas do MEC |
| Ciência da Computação | Linguagens, ferramentas de programação com IA |

## Edição 01
Muse, o agente de IA da Meta (lançado nos EUA em 8/9/2026). Dado: Gartner, projeção divulgada em 25/6/2025. Curso: Mestrado em Inteligência Artificial. Palavra-chave: MESTRADO.

## Aprendizados da edição 01
- Provocação concreta funciona melhor que metáfora ("A IA ganhou mãos" foi recusada).
- Exemplos que impressionam um executivo (negocia em seu nome, trabalha com o app fechado) valem mais que tarefa doméstica.
- Perguntas para quem lidera levam a tendência para dentro da empresa.
- A cena na empresa (tela 3) vem antes do dado (tela 4): a cena cria a imagem e o dado mostra que ela é real.
- Vídeo do mascote gerado por IA trocou o brasão do cachecol por outro escudo. Conferir o logo quadro a quadro em todo vídeo novo e corrigir com `scripts/preparar-video-mascote.py`.
- Um dado de fonte reconhecida, com a precisão da fonte, dá autoridade de universidade e motiva a estudar.
- O texto final da edição 01 foi escrito pela Giovanna: usar como referência de tom (frases diretas, perguntas para quem lidera, fechamento que vende o curso).
- Uma versão B feita 100% pelo pacote `agtu-academic-carousel` (fato, dado, alerta, competência, formação) foi testada; ficou só a tela do dado.
- Não citar Harvard/MIT e outras universidades parceiras sem confirmação jurídica. Não citar duração do curso.
