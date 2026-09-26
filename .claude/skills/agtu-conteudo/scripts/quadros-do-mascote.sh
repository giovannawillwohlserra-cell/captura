#!/usr/bin/env bash
# Gera assets/mframes/ (quadros do mascote acenando, prontos para a capa) a partir de assets/mascote_acenando.mp4.
# Uso (dentro da pasta da skill): bash scripts/quadros-do-mascote.sh
set -euo pipefail
cd "$(dirname "$0")/.."
FF=$(python3 -c "import imageio_ffmpeg as f; print(f.get_ffmpeg_exe())" 2>/dev/null || command -v ffmpeg)
TMP=$(mktemp -d)
"$FF" -hide_banner -loglevel error -y -i assets/mascote_acenando.mp4 "$TMP/f%03d.png"
python3 scripts/preparar-video-mascote.py "$TMP" assets/mframes 362
echo "Quadros em assets/mframes. Exporte com: node assets/exportar-png-e-video.js video"
