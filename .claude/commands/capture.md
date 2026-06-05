# /capture

Captura screenshots de una carpeta, idioma o imagen específica del proyecto GoalBus Docs.

## Uso

```
/capture <scope> [--verify] [--fix-selector]
```

**Ejemplos:**
- `/capture English` — captura todas las imágenes del idioma English
- `/capture English/R3` — captura toda la serie R3 en inglés
- `/capture English/R3/R3_imagen1` — captura una imagen específica
- `/capture English/R3/R3_imagen1 --verify` — captura y compara con `_old.png`
- `/capture English/R3/R3_imagen1 --fix-selector` — analiza HTML y repara `selector.json` antes de capturar

## Comportamiento

Ejecuta el script de captura apropiado según el alcance:

```bash
python scripts/core/capture_scope.py <scope>
```

### Con `--verify`
Después de capturar, abre la imagen resultante y la compara visualmente con `*_old.png` si existe. Reporta diferencias notables (recorte, contenido faltante, elementos cortados).

### Con `--fix-selector`
Antes de capturar:
1. Lee el HTML de la carpeta objetivo
2. Analiza el `selector.json` actual
3. Verifica si hay problemas comunes:
   - `viewport_width`/`viewport_height` demasiado pequeños
   - `filter_grid_rows` que deja filas no deseadas
   - `pre_capture_js` con errores de sintaxis (comillas rotas, selectores inválidos)
   - Selector CSS que no existe en el HTML
4. Propone correcciones y aplica con confirmación

## Notas

- El PNG resultado se guarda en `Idioma/Serie/` (carpeta padre de la imagen)
- El PNG anterior se renombra a `*_old.png` automáticamente
- Si hay placeholders sin resolver (campo con su propio `field_id` como valor visible), el script lanza un rebuild automático del HTML antes de capturar
- Para grids CDK con virtual scroll, usar `filter_grid_rows` en `selector.json` en vez de intentar scroll
