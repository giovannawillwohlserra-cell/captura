# Skills de conteúdo — AGTU

Skills selecionadas em 26/09/2026 para produzir Reels, Stories, carrosséis e posts de LinkedIn, Instagram e YouTube com texto humano e visual minimalista. Todas foram lidas antes da instalação: nenhuma envia dados para fora nem roda código sozinha. Algumas citam ferramentas externas (Gemini, HeyGen, Remotion) só como opção, e nada é usado sem a sua chave e o seu pedido.

## O que tem aqui

| Skill | Para que serve | Fonte |
|---|---|---|
| `humanizer` | Tira os vícios de texto de IA (regra de três, travessão em excesso, "não é X, é Y", conclusões genéricas). Passar todo texto por ela antes de publicar. | blader/humanizer (MIT) |
| `voice-builder` | Monta os arquivos `about-me.md` e `voice.md` com a voz da marca. É a primeira a rodar: as outras leem esses arquivos. | charlie947/social-media-skills (MIT) |
| `post-writer` | Escreve posts de LinkedIn na voz definida pelo voice-builder. | charlie947/social-media-skills (MIT) |
| `hook-generator` | Gera ganchos (primeira linha, primeiros 3 segundos). | charlie947/social-media-skills (MIT) |
| `content-matrix` | Cruza pilares de conteúdo com formatos e gera 24 a 40 ideias de posts. | charlie947/social-media-skills (MIT) |
| `graphic-designer` | Decide e monta a arte do post (HTML/CSS editável ou prompt de imagem). | charlie947/social-media-skills (MIT) |
| `social` | Estratégia e criação por plataforma (LinkedIn, Instagram, TikTok, YouTube), calendário e reaproveitamento. | coreyhaines31/marketingskills (MIT) |
| `content-strategy` | Pilares, clusters de tema e calendário editorial. | coreyhaines31/marketingskills (MIT) |
| `copywriting` | Texto persuasivo (páginas, anúncios, legendas). | coreyhaines31/marketingskills (MIT) |
| `copy-editing` | Revisão de texto em várias passadas (clareza, voz, prova, especificidade). | coreyhaines31/marketingskills (MIT) |
| `marketing-psychology` | Gatilhos e vieses aplicados com critério (prova social, aversão à perda, ancoragem). | coreyhaines31/marketingskills (MIT) |
| `video` | Planejamento e produção de vídeo curto com IA ou código (Remotion, HeyGen, Veo). | coreyhaines31/marketingskills (MIT) |
| `image` | Prompts e produção de imagem para redes, com regras de consistência de marca. | coreyhaines31/marketingskills (MIT) |
| `ad-creative` | Variações de criativo para anúncio pago (Meta, LinkedIn, YouTube). | coreyhaines31/marketingskills (MIT) |
| `agtu-conteudo` | **A ferramenta da AGTU.** Regras de marca, série AGTU Tendências, mascote coruja, template do carrossel, exportação em PNG e biblioteca com mais de 25 prompts (pauta, ganchos, legenda, humor, imagem, vídeo, stories, revisão). | Criada para a AGTU |
| `instagram-carousel` | Gera carrosséis em HTML com sistema de design e exporta PNG 1080×1350. | jeevanbavandla/instagram-carousel-skill (MIT) |
| `frontend-design` | Direção visual que foge do "template de IA": tipografia, grid, hierarquia. Base dos carrosséis e artes em HTML. | anthropics/skills (Apache 2.0) |

Já disponíveis na sua conta e não duplicadas aqui: `canvas-design`, `theme-factory`, `motion-design`, `ux-writing`, `pptx`, `pdf`.

## Ficaram de fora, e por quê

- `reels-scripting`, `post-scorer`, `gemini-carousel`: dependem de chaves pagas (Apify, Gemini). Instalar quando houver conta.
- Skills da Remotion (remotion-dev/skills): ótimas para Reels com tipografia animada, mas exigem Node e renderização de vídeo. Entram na fase da ferramenta, se o formato for aprovado.
- `brand-guidelines` (Anthropic): aplica a marca da Anthropic, não serve para a AGTU.
- `sergebulaev/instagram-skills`: boas regras de legenda e gancho, mas amarradas ao serviço pago Publora para publicar. As ideias úteis foram para a biblioteca de prompts.

## Como instalar no seu computador

1. Baixe esta pasta (`.claude/skills`) do repositório `captura`, branch `claude/serene-ramanujan-kwne6e`.
2. **Claude Code:** copie as pastas para `~/.claude/skills/` (vale para todos os projetos) ou deixe em `.claude/skills/` dentro do projeto.
3. **Claude.ai / app desktop:** em Configurações → Capacidades → Skills, envie cada pasta compactada em .zip (uma skill por arquivo).

## Ordem de uso

Para qualquer post da AGTU, comece pela `agtu-conteudo`: ela chama as outras na ordem certa.

Ordem geral:

1. `voice-builder` com o material da AGTU → gera `about-me.md` e `voice.md`.
2. `content-strategy` + `content-matrix` → pilares e ideias por etapa do funil.
3. `hook-generator` → `post-writer` / `social` / `video` → roteiro e texto.
4. `graphic-designer` + `frontend-design` → arte.
5. `humanizer` + `copy-editing` → revisão final antes de publicar.
