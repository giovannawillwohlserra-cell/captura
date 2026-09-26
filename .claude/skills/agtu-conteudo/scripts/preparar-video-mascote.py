"""Prepara os quadros do vídeo do mascote para a capa.

1. Corrige o logo do cachecol: a IA do vídeo troca o brasão da AGTU por outro escudo
   a partir de ~1 s. Em cada quadro, apaga o logo do quadro e cola o logo certo do
   1º quadro, alinhado pelas letras AGTU (que o vídeo mantém certas).
2. Deixa o fundo branco puro (o vídeo vem com cinza 239-251 e ruído), para a
   mesclagem "multiplicar" sobre a capa branca não mostrar caixa. Só o fundo:
   o que está dentro do contorno do mascote não é alterado (evita rosto "estourado").
3. Reduz para o tamanho usado na capa.
Uso: python3 preparar_quadros.py <pasta com f001.png...> <pasta de saída> <largura>
"""
import sys, glob, os
import numpy as np, cv2
from PIL import Image

SRC, OUT, LARG = sys.argv[1], sys.argv[2], int(sys.argv[3])
os.makedirs(OUT, exist_ok=True)
fs = sorted(glob.glob(os.path.join(SRC, 'f*.png')))

def color_masks(a):
    a = a.astype(int); r, g, b = a[..., 0], a[..., 1], a[..., 2]
    navy = (b - r > 45) & (b - g > 15) & (b > 85)
    red = (r - g > 80) & (r - b > 60) & (r > 130)
    green = (g - r > 20) & (g - b > 10)
    gold = (r - b > 95) & (g - b > 55) & (r > 170)
    return navy, (navy | red | green | gold)

def track(a, prev):
    x0, y0 = prev[0] - 95, prev[1] - 45
    win = a[y0:y0 + 90, x0:x0 + 190]
    navy, m = color_masks(win)
    m = m.astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    keep = np.zeros_like(m)
    for k in range(1, n):
        if st[k, 4] >= 4: keep[lab == k] = 1
    full = np.zeros(a.shape[:2], np.uint8); full[y0:y0 + 90, x0:x0 + 190] = keep
    ys, xs = np.where(keep)
    bb = (xs.min() + x0, xs.max() + x0, ys.min() + y0, ys.max() + y0)
    nys, nxs = np.where(navy)
    right = nxs.max()
    sel = nxs > right - 60                      # só as letras (à direita do escudo)
    letters = (right + x0, (nys[sel].min() + nys[sel].max()) / 2 + y0)
    return full, bb, letters

# logo de referência (1º quadro, com o brasão certo)
ref = np.asarray(Image.open(fs[0]).convert('RGB')).copy()
ref_mask, ref_bb, ref_let = track(ref, (518, 695))
m_ref = cv2.dilate(ref_mask, np.ones((5, 5), np.uint8))
m_ref = cv2.GaussianBlur(m_ref.astype(np.float32), (0, 0), 0.8)
X0, X1, Y0, Y1 = ref_bb[0] - 6, ref_bb[1] + 6, ref_bb[2] - 6, ref_bb[3] + 6
patch = ref[Y0:Y1 + 1, X0:X1 + 1].astype(np.float32)
pmask = np.clip(m_ref[Y0:Y1 + 1, X0:X1 + 1] * 1.6, 0, 1)[..., None]

def whiten(a):
    # clareia SÓ o fundo (fora do contorno do mascote); rosto, pelo e cachecol ficam intactos
    mn = a.min(axis=2)
    ch = (mn < 230).astype(np.uint8)
    ch = cv2.morphologyEx(ch, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))
    ff = ch * 255
    cv2.floodFill(ff, np.zeros((ff.shape[0] + 2, ff.shape[1] + 2), np.uint8), (0, 0), 128)
    sil = (ff != 128).astype(np.uint8)                   # contorno cheio (inclui cachecol e rosto)
    n, lab, st, _ = cv2.connectedComponentsWithStats(sil)
    sil = (lab == 1 + int(np.argmax(st[1:, 4]))).astype(np.float32)
    fundo = 1 - cv2.GaussianBlur(sil, (0, 0), 1.5)
    af = a.astype(np.float32)
    return af + (255 - af) * fundo[..., None]

prev = (518, 695)
for i, f in enumerate(fs):
    a = np.asarray(Image.open(f).convert('RGB')).copy()
    m, bb, let = track(a, prev)
    prev = ((bb[0] + bb[1]) // 2, (bb[2] + bb[3]) // 2)
    if i > 0:
        # apaga o logo do quadro (escudo errado) e cola o certo alinhado pelas letras
        hole = cv2.dilate(m, np.ones((7, 7), np.uint8))
        a = cv2.inpaint(a, hole * 255, 5, cv2.INPAINT_TELEA)
        dx = int(round(let[0] - ref_let[0])); dy = int(round(let[1] - ref_let[1]))
        ys, xs = Y0 + dy, X0 + dx
        reg = a[ys:ys + patch.shape[0], xs:xs + patch.shape[1]].astype(np.float32)
        a[ys:ys + patch.shape[0], xs:xs + patch.shape[1]] = (patch * pmask + reg * (1 - pmask)).astype(np.uint8)
    a = whiten(a)
    h = round(a.shape[0] * LARG / a.shape[1])
    img = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).resize((LARG, h), Image.LANCZOS)
    img.save(os.path.join(OUT, os.path.basename(f)), optimize=True)
print('quadros prontos:', len(fs), '| tamanho', LARG, 'x', h)
