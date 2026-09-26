const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
// ordem das telas no carrossel
const ordem = ['s1', 's2', 's3', 'sd', 's4', 's5'];
const FPS = 24, TOTAL = 240;      // vídeo do mascote: 10 s a 24 fps
const nome = n => `mframes/f${String(n).padStart(3, '0')}.png`;
// o vídeo começa no quadro 25 (mascote já acenando) e dá a volta: o 1º quadro vira a miniatura do post
const INICIO = 25;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1500 } });
  const arquivo = fs.existsSync(__dirname + '/carrossel.html') ? 'carrossel.html' : 'template-tendencias.html';
  await p.goto('file://' + __dirname + '/' + arquivo);
  await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const quadro = async n => p.evaluate(async src => { const i = document.getElementById('mvid'); if (!i) return; i.src = src; await i.decode(); }, nome(n));
  // capa parada: texto completo (2,9 s) e mascote no meio do aceno
  await p.evaluate(() => document.getAnimations().forEach(a => { a.pause(); a.currentTime = 2900; }));
  // capa parada: mascote por camadas no meio do aceno (sem o brilho do vídeo)
  await p.evaluate(() => { const s = document.getElementById('s1'); s.classList.add('parado'); s.classList.remove('video'); });
  for (let i = 0; i < ordem.length; i++) await p.locator('#' + ordem[i]).screenshot({ path: `AGTU_Tendencias_01_${i + 1}.png` });
  if (process.argv[2] === 'video') {
    await p.evaluate(() => { const s = document.getElementById('s1'); s.classList.remove('parado'); s.classList.add('video'); });
    fs.mkdirSync('frames', { recursive: true });
    for (let f = 0; f < TOTAL; f++) {
      // texto completo desde o 1º quadro (miniatura do carrossel = 1º quadro do vídeo); só o mascote se mexe
      await p.evaluate(() => document.getAnimations().forEach(a => { a.pause(); a.currentTime = 2900; }));
      await quadro(((f + INICIO - 1) % TOTAL) + 1);
      await p.locator('#s1').screenshot({ path: `frames/f${String(f).padStart(4, '0')}.png` });
    }
  }
  await b.close();
})();
