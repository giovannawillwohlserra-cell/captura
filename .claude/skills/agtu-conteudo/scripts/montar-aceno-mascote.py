"""Monta as camadas do mascote para a animação de aceno e piscada.

Camadas (todas do tamanho da imagem original, para empilhar sem ajuste):
  m_base.png     corpo sem o antebraço esquerdo (lado do leitor), tronco preenchido, olhos apagados
  m_antebraco.png antebraço + mão, gira no cotovelo
  m_cotovelo.png  disco de pelo que esconde a emenda do cotovelo
  m_olho_e.png / m_olho_d.png  olhos, para piscar (scaleY)
Na pose de descanso, as camadas somadas reproduzem a imagem original.
"""
import numpy as np, cv2
from PIL import Image

SRC = '../assets/mascote.png'   # rode dentro de scripts/; gera as camadas m_*.png aqui (copie para assets/)
im = np.array(Image.open(SRC).convert('RGBA')).astype(np.float32)
H, W = im.shape[:2]
rgb, A = im[:, :, :3], im[:, :, 3]
ys, xs = np.mgrid[0:H, 0:W]

PIV = (258.0, 700.0)          # cotovelo (centro do braço na altura do corte)
R_TOPO = 95                   # topo arredondado do antebraço (fica sob o cotovelo)
R_CAP = 100                   # raio do disco do cotovelo

def interp(points, y):
    py = np.array([p[0] for p in points], float); px = np.array([p[1] for p in points], float)
    return np.interp(y, py, px)

# dobra entre braço e tronco (medida pelo vale de luminância) e fim da mão
crease = [(560, 364), (620, 362), (660, 360), (680, 356), (700, 351), (720, 346), (740, 342), (760, 339),
          (780, 337), (800, 331), (820, 327), (840, 324), (860, 321), (880, 320), (900, 317), (920, 312),
          (930, 300), (940, 291), (960, 286), (975, 282), (1000, 282)]
# silhueta do tronco atrás do antebraço (continua a borda visível abaixo da mão: 296 em y=940, 307 em y=980)
torso = [(700, 300), (760, 292), (820, 288), (880, 289), (920, 292), (940, 296), (960, 299), (980, 307), (1000, 309)]

c = interp(crease, ys)
s = interp(torso, ys)
dist = np.hypot(xs - PIV[0], ys - PIV[1])

# --- antebraço
m_fore = (xs < c) & (A > 0) & (ys <= 995) & ((ys >= PIV[1]) | ((ys >= 560) & (dist <= R_TOPO)))
m_fore_soft = cv2.GaussianBlur(m_fore.astype(np.float32), (0, 0), 1.3)
fore = np.dstack([rgb, A * m_fore_soft])

# --- base: remove o antebraço abaixo do cotovelo e preenche a faixa do tronco
base = im.copy()
below = (ys >= PIV[1]) & (xs < c) & (A > 0) & (ys <= 995)
base[below, 3] = 0

band = (ys >= PIV[1]) & (ys <= 985) & (xs >= s - 3) & (xs < c + 4)
yy, xx = np.where(band)
d = (c[yy, xx] - s[yy, xx]) + 26                       # copia pelo do tronco à direita da dobra
sx = np.clip((xx + d).astype(int), 0, W - 1)
tex = rgb[yy, sx]
t = np.clip((xx - s[yy, xx]) / np.maximum(c[yy, xx] - s[yy, xx], 1), 0, 1)
shade = 0.84 + 0.10 * t                                 # mais escuro na borda do tronco
occl = 1 - 0.12 * np.clip(1 - (yy - PIV[1]) / 90, 0, 1)  # sombra logo abaixo do cotovelo
tex = tex * (shade * occl)[:, None]
rng = np.random.default_rng(7)
edge = np.clip((xx - s[yy, xx] + 2 + rng.normal(0, 1.2, len(xx))) / 4.0, 0, 1)   # borda felpuda
right = np.clip((c[yy, xx] + 4 - xx) / 5.0, 0, 1)                                 # funde na dobra
a_fill = 255 * edge
keep = base[yy, xx, 3] / 255.0
w_new = right * (1 - keep) + keep * right * 0.6
base[yy, xx, :3] = tex * w_new[:, None] + base[yy, xx, :3] * (1 - w_new[:, None])
base[yy, xx, 3] = np.maximum(base[yy, xx, 3], a_fill * right)

# --- olhos: camadas próprias e pele reconstruída embaixo
EYES = {'e': (529, 276), 'd': (762, 277)}
RX, RY = 31, 34
b8 = np.clip(base[:, :, :3], 0, 255).astype(np.uint8)
mask_inp = np.zeros((H, W), np.uint8)
for cx, cy in EYES.values():
    cv2.ellipse(mask_inp, (cx, cy), (RX + 3, RY + 3), 0, 0, 360, 255, -1)
b8 = cv2.inpaint(b8, mask_inp, 9, cv2.INPAINT_TELEA)
base[:, :, :3] = b8.astype(np.float32)

def save(arr, name):
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    arr[arr[:, :, 3] == 0, :3] = 0          # cor zerada onde é transparente: arquivo bem menor
    Image.fromarray(arr, 'RGBA').save(name, optimize=True)

for k, (cx, cy) in EYES.items():
    m = np.zeros((H, W), np.float32)
    cv2.ellipse(m, (cx, cy), (RX, RY), 0, 0, 360, 1.0, -1)
    m = cv2.GaussianBlur(m, (0, 0), 1.2)
    save(np.dstack([rgb, A * m]), f'm_olho_{k}.png')

# --- disco do cotovelo (pixels originais)
cap = np.clip((R_CAP - dist) / 5.0, 0, 1)
save(np.dstack([rgb, A * cap]), 'm_cotovelo.png')
save(fore, 'm_antebraco.png')
save(base, 'm_base.png')

# --- conferência: descanso deve reproduzir a original
def over(dst, src):
    a = src[:, :, 3:4] / 255.0
    out = dst.copy()
    out[:, :, :3] = src[:, :, :3] * a + dst[:, :, :3] * (1 - a)
    out[:, :, 3:4] = 255 * (a + dst[:, :, 3:4] / 255.0 * (1 - a))
    return out

def load(n): return np.array(Image.open(n).convert('RGBA')).astype(np.float32)
bg = np.zeros_like(im); bg[:, :, :3] = [236, 239, 244]; bg[:, :, 3] = 255
orig = over(bg, im)
L = {n: load(n) for n in ['m_base.png', 'm_antebraco.png', 'm_cotovelo.png', 'm_olho_e.png', 'm_olho_d.png']}

def pose(angle):
    M = cv2.getRotationMatrix2D(PIV, -angle, 1.0)   # ângulo horário, como no CSS rotate()
    f = cv2.warpAffine(L['m_antebraco.png'], M, (W, H), flags=cv2.INTER_LINEAR, borderValue=(0, 0, 0, 0))
    out = over(bg, L['m_base.png']); out = over(out, f); out = over(out, L['m_cotovelo.png'])
    out = over(out, L['m_olho_e.png']); out = over(out, L['m_olho_d.png'])
    return out

rest = pose(0)
diff = np.abs(rest[:, :, :3] - orig[:, :, :3]).mean(axis=2)
print('descanso vs original: dif. média', round(float(diff.mean()), 3), '| pixels com dif>12:', int((diff > 12).sum()))
tiles = [orig, rest, pose(90), pose(128), pose(140), pose(155)]
sheet = np.concatenate([cv2.resize(t, (385, 481), interpolation=cv2.INTER_AREA) for t in tiles], axis=1)
Image.fromarray(np.clip(sheet, 0, 255).astype(np.uint8), 'RGBA').convert('RGB').save('_poses.png')
