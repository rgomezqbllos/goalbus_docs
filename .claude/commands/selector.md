# /selector

Crea, repara o ajusta el `selector.json` de una carpeta de imagen GoalBus.

## Uso

```
/selector <image-folder> [--show] [--repair] [--set-field campo=valor]
```

**Ejemplos:**
- `/selector traducciones/English/R3/R3_imagen1` — analiza y propone `selector.json` óptimo
- `/selector traducciones/English/R3/R3_imagen1 --show` — muestra el `selector.json` actual y lo explica
- `/selector traducciones/English/R3/R3_imagen1 --repair` — detecta y corrige problemas automáticamente
- `/selector traducciones/English/R3/R3_imagen1 --set-field viewport_width=1920` — ajusta un campo concreto

## Comportamiento

### Sin flags (modo análisis y propuesta)
1. Lee `selector.json` actual (si existe) y el `GoalBus.html`
2. Identifica el elemento principal a capturar
3. Propone valores óptimos para:
   - `selector` (CSS selector del elemento)
   - `bbox_mode` (`smart` para body, `content` para paneles, `element` para componentes)
   - `viewport_width` / `viewport_height` (basado en el layout del HTML)
   - `filter_grid_rows` (si hay `otto-web-grid-row` en el HTML)
   - `pre_capture_js` (si hay elementos a ocultar como `gs-header`, `otto-web-side-panel`)
4. Muestra el JSON propuesto y pide confirmación antes de escribir

### Con `--repair`
Detecta y corrige estos problemas comunes:

| Problema | Síntoma | Fix |
|----------|---------|-----|
| Comillas rotas en JS | `querySelectorAll("[attr="val"]")` | Cambiar a comillas simples internas |
| Selector inexistente | No captura nada o error | Buscar selector alternativo en el HTML |
| Viewport muy pequeño | Imagen cortada | Aumentar según contenido del HTML |
| filter_grid_rows demasiado amplio | Muestra filas extra | Usar lista explícita `["5202_1","5202_2"]` |
| Side panel oculto cuando no debe | Panel no aparece | Revisar `pre_capture_js` |

### Campos de selector.json

```json
{
  "description": "Texto descriptivo de qué captura esta imagen",
  "selector": "body",
  "bbox_mode": "smart",
  "viewport_width": 1920,
  "viewport_height": 1080,
  "device_scale_factor": 1,
  "padding": [0, 0, 0, 0],
  "filter_grid_rows": ["prefijo1_", "prefijo2_"],
  "pre_capture_js": "// JS ejecutado antes de capturar",
  "wait_for": "networkidle"
}
```

## Patrones comunes de pre_capture_js

### Ocultar header y panel lateral
```javascript
const header = document.querySelector('gs-header');
if (header) header.style.display = 'none';
const panel = document.querySelector('otto-web-side-panel');
if (panel) panel.style.display = 'none';
window.dispatchEvent(new Event('resize'));
```

### Añadir recuadro de color sobre un elemento
```javascript
const el = document.querySelector('.mi-selector');
if (el) {
  const r = el.getBoundingClientRect();
  const ov = document.createElement('div');
  ov.style.cssText = 'position:fixed;pointer-events:none;z-index:9999;box-sizing:border-box;border:3px solid rgb(0,98,132);border-radius:4px;';
  ov.style.left = (r.left - 4) + 'px';
  ov.style.top = (r.top - 4) + 'px';
  ov.style.width = (r.width + 8) + 'px';
  ov.style.height = (r.height + 8) + 'px';
  document.body.appendChild(ov);
}
```

### Reemplazar texto traducible (transloco)
```javascript
// IMPORTANTE: usar comillas simples en el selector CSS
document.querySelectorAll('[transloco="clave.de.traduccion"]').forEach(function(span) {
  var parent = span.parentElement;
  parent.childNodes.forEach(function(n) {
    if (n.nodeType === 3 && n.textContent.includes('TextoOriginal'))
      n.textContent = n.textContent.replace('TextoOriginal', 'Traducción');
  });
});
```

### Scroll a un elemento en el panel lateral
```javascript
const el = document.querySelector('gs-tag.mi-clase');
if (el) el.scrollIntoView({ block: 'center' });
```
