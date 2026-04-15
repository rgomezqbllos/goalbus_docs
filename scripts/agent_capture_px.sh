#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Uso: $0 <IDIOMA/PX/PX_imagenN>"
  echo "Ejemplo: $0 Español/P7/P7_imagen8"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="$1"

cd "$ROOT_DIR"

if [[ ! -x ".venv/bin/python" ]]; then
  echo "Error: no existe .venv/bin/python"
  echo "Crea el entorno: python -m venv .venv && source .venv/bin/activate && pip install playwright && playwright install chromium"
  exit 1
fi

.venv/bin/python scripts/capture_screenshots.py capture "$TARGET"

