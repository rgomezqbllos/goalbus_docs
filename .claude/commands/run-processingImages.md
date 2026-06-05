# /run-processingImages

Procesa una serie o imagen de GoalBus de extremo a extremo: desde ajustar el selector hasta capturar en todos los idiomas.

## Uso

```
/run-processingImages <serie-o-imagen> [--source-language Español] [--targets English,Portugues,Italiano,Deutsch,Frances]
```

**Ejemplos:**
- `/run-processingImages R3` — procesa toda la serie R3 en todos los idiomas
- `/run-processingImages R3/R3_imagen4` — procesa solo R3_imagen4
- `/run-processingImages R3 --targets Deutsch,Frances` — solo alemán y francés

## Flujo completo

1. **Inspección**: Lee el `selector.json` de cada imagen y lo valida (comillas, selectores, viewport)
2. **Captura fuente**: Captura el HTML de `--source-language` y verifica contra `*_old.png` si existe
3. **Localización**: Construye HTML para cada idioma destino con `goalbus_localize.py build_all`
4. **Captura destino**: Captura PNG para cada idioma destino con `capture_scope.py`
5. **Reporte**: Muestra resumen en español — imágenes OK, con problemas, y blockers sin resolver

## Reglas de selector.json

Antes de capturar, valida automáticamente:

- **Comillas en pre_capture_js**: el `querySelectorAll` con atributo debe usar comillas simples internas:
  ```javascript
  // CORRECTO
  document.querySelectorAll('[transloco="clave"]')
  // INCORRECTO - rompe JSON
  document.querySelectorAll("[transloco="clave"]")
  ```
- **filter_grid_rows**: lista explícita `["5202_1","5202_2"]` es más precisa que prefijo `["5202_"]`
- **viewport**: si la imagen se corta, aumentar `viewport_width`/`viewport_height`
- **side panel**: si una imagen necesita mostrar el panel lateral, asegurarse de que `pre_capture_js` no tenga `panel.style.display = 'none'`

## Manejo de grids CDK (virtual scroll)

Para pantallas con `cdk-virtual-scroll-viewport` (grids de conductores, turnos, etc.):
- Usar `filter_grid_rows` para mostrar solo las filas necesarias
- No intentar hacer scroll dentro del grid; el virtual scroll no funciona como scroll normal
- Si se necesita un elemento específico del side panel, usar `scrollIntoView` sobre ese elemento

## Patrones de pre_capture_js frecuentes

```javascript
// Ocultar header y resize
const header = document.querySelector('gs-header');
if (header) header.style.display = 'none';
window.dispatchEvent(new Event('resize'));

// Recuadro azul sobre elemento
const el = document.querySelector('.selector');
if (el) {
  const r = el.getBoundingClientRect();
  const ov = document.createElement('div');
  ov.style.cssText = 'position:fixed;pointer-events:none;z-index:9999;box-sizing:border-box;border:3px solid rgb(0,98,132);border-radius:4px;';
  ov.style.left=(r.left-4)+'px'; ov.style.top=(r.top-4)+'px';
  ov.style.width=(r.width+8)+'px'; ov.style.height=(r.height+8)+'px';
  document.body.appendChild(ov);
}

// Traducir texto con transloco (comillas simples en el selector)
document.querySelectorAll('[transloco="clave.de.traduccion"]').forEach(function(span){
  var p=span.parentElement;
  p.childNodes.forEach(function(n){
    if(n.nodeType===3&&n.textContent.includes('TextoES'))
      n.textContent=n.textContent.replace('TextoES','Traducción');
  });
});
```

## Mapa de idiomas

| Carpeta    | Código | Pack    |
|------------|--------|---------|
| Español    | ES     | es.json |
| English    | EN     | en.json |
| Deutsch    | DE     | de.json |
| Frances    | FR     | fr.json |
| Italiano   | IT     | it.json |
| Portugues  | PT_BR  | pt_br.json |
