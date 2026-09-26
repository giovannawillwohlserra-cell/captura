const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1500 } });
  await p.goto('file://' + __dirname + '/carrossel.html');
  await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  // estado final das animações para o PNG estático
  await p.evaluate(() => document.getAnimations().forEach(a => { a.pause(); a.currentTime = 3600; }));
  for (let i = 1; i <= 5; i++) await p.locator('#s' + i).screenshot({ path: `AGTU_Tendencias_01_${i}.png` });
  if (process.argv[2] === 'video') {
    fs.mkdirSync('frames', { recursive: true });
    const fps = 30, secs = 6;
    for (let f = 0; f < fps * secs; f++) {
      const t = f * 1000 / fps;
      await p.evaluate(t => document.getAnimations().forEach(a => { a.pause(); a.currentTime = t; }), t);
      await p.locator('#s1').screenshot({ path: `frames/f${String(f).padStart(4, '0')}.png` });
    }
  }
  await b.close();
})();
