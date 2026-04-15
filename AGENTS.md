# GoalBus Capture Agent

Este repositorio usa un agente especializado para iterar capturas `PX_imagenN` desde HTML local.

## Objetivo

Para cada `Idioma/PX/PX_imagenN`:
1. Definir/ajustar `selector.json`.
2. Ejecutar captura con Playwright.
3. Verificar que no se pierdan elementos importantes (cabecero/lateral/texto seleccionado).

## Flujo obligatorio

1. Revisar HTML y confirmar el/los elementos objetivo.
2. Preferir selectores estables:
   - `data-qa-id`, `gsqaid`
   - tags `gs-*`, `otto-web-*`
   - `:has(...)`, `:has-text(...)` cuando ayude
3. Guardar `selector.json` en la carpeta de la imagen.
4. Ejecutar:
   - `.venv/bin/python scripts/capture_screenshots.py capture Idioma/PX/PX_imagenN`
5. Si el recorte es malo:
   - usar múltiples `selectors` (anclas superior/inferior)
   - ajustar `bbox_mode` (`element`, `content`, `smart`)
   - ajustar `padding`
   - fijar `viewport_width` / `viewport_height` si hay drift
6. Para overlays/tooltips inestables, usar `pre_capture_js`.

## Reglas de recorte

- Si el selector es `body/html`, no recortar cabecero ni lateral.
- Recortar vacío inferior solo cuando no elimine contenido útil.
- En vistas complejas, usar anclas:
  - `gs-header`
  - lateral visible
  - toolbar de módulo
  - tabla/contenido
  - paginador o footer útil

## Caso especial: botón + tooltip

Usar 2 selectores:
- botón objetivo
- tooltip por texto

Y si hay desalineación por resolución:
- fijar viewport en `selector.json`
- añadir `pre_capture_js` para anclar tooltip al botón
- ocultar botones hermanos si contaminan el recorte

## Comandos rápidos

- Captura única:
  - `.venv/bin/python scripts/capture_screenshots.py capture Español/P7/P7_imagen8`
- Estado:
  - `.venv/bin/python scripts/capture_screenshots.py status Español/P7`
- Dry run:
  - `.venv/bin/python scripts/capture_screenshots.py capture Español/P7 --dry-run`

