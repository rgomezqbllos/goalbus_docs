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

## Caso especial: Grids con Virtual Scroll (CDK)

Para grids de Angular que usan `cdk-virtual-scroll` (como la asignación de vehículos), las filas se destruyen al hacer scroll. Para capturas estáticas:

1.  **Aislamiento Automático:** Usar la propiedad `"filter_grid_rows": ["PLACA1", "PLACA2"]` en el `selector.json`.
2.  Esto realiza automáticamente:
    *   Clonación del DOM para detener el motor de Angular.
    *   Eliminado de filas no deseadas.
    *   Reset de `transform` y `absolute positioning` para que las filas se apilen naturalmente.
3.  **Selectors:** Deben incluir el header y las filas específicas. Ejemplo:
    ```json
    {
      "selectors": ["otto-web-grid-header", "otto-web-grid-row:has-text('0031-LFX')"],
      "filter_grid_rows": ["0031-LFX"],
      "viewport_width": 2500
    }
    ```
4.  **Timeline:** Si el timeline sale cortado, aumentar `"viewport_width"` (p.ej. 2500 o 3000) para expandir la vista hacia la derecha.

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

