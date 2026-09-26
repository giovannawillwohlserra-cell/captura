const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
// ordem das telas no carrossel
const ordem = ['s1', 's2', 's3', 'sd', 's4', 's5'];
const QUADRO_CAPA = 25;           // quadro do vídeo do mascote usado na capa parada
const FPS = 24, TOTAL = 240;      // vídeo do mascote: 10 s a 24 fps
const nome = n => `mframes/f${String(n).padStart(3, '0')}.png`;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1500 } });
  const arquivo = fs.existsSync(__dirname + '/carrossel.html') ? 'carrossel.html' : 'template-tendencias.html';
  await p.goto('file://' + __dirname + '/' + arquivo);
  await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const quadro = async n => p.evaluate(async src => { const i = document.getElementById('mvid'); if (!i) return; i.src = src; await i.decode(); }, nome(n));
  // capa parada: texto completo (2,9 s) e mascote no meio do aceno
  await p.evaluate(() => document.getAnimations().forEach(a => { a.pause(); a.currentTime = 2900; }));
  await quadro(QUADRO_CAPA);
  for (let i = 0; i < ordem.length; i++) await p.locator('#' + ordem[i]).screenshot({ path: `AGTU_Tendencias_01_${i + 1}.png` });
  if (process.argv[2] === 'video') {
    fs.mkdirSync('frames', { recursive: true });
    for (let f = 0; f < TOTAL; f++) {
      const t = f * 1000 / FPS;
      await p.evaluate(t => document.getAnimations().forEach(a => { a.pause(); a.currentTime = t; }), t);
      await quadro(f + 1);
      await p.locator('#s1').screenshot({ path: `frames/f${String(f).padStart(4, '0')}.png` });
    }
  }
  await b.close();
})();
