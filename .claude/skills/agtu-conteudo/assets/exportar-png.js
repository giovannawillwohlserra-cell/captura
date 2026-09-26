// Exporta cada <section class="slide" id="sN"> do HTML em PNG 1080x1350.
// Uso: node exportar-png.js caminho/do/carrossel.html PREFIXO_DO_ARQUIVO
// Requer Playwright instalado (npm i -g playwright) ou ajuste o require abaixo.
const path = require('path');
let chromium;
try { ({ chromium } = require('playwright')); }
catch { ({ chromium } = require('/opt/node22/lib/node_modules/playwright')); }
(async () => {
  const [html, prefix = 'AGTU_carrossel'] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1500 } });
  await p.goto('file://' + path.resolve(html));
  await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const n = await p.locator('section.slide').count();
  for (let i = 0; i < n; i++) await p.locator('section.slide').nth(i).screenshot({ path: `${prefix}_${i + 1}.png` });
  await b.close();
  console.log(`${n} telas exportadas`);
})();
