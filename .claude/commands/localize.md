# /localize

Localiza HTML de una serie o imagen desde Español a uno o más idiomas destino.

## Uso

```
/localize <serie-o-imagen> [--to idioma1,idioma2] [--step init|build|status]
```

**Idiomas válidos:** `English`, `Deutsch`, `Frances`, `Italiano`, `Portugues`  
(Si se omite `--to`, aplica a todos los idiomas)

**Ejemplos:**
- `/localize R4` — localiza toda la serie R4 a todos los idiomas
- `/localize R4/R4_imagen1 --to Deutsch,Frances` — localiza una imagen a dos idiomas
- `/localize R4 --step status` — muestra cobertura de traducción para R4
- `/localize R4 --step init --to Deutsch` — solo inicializa las carpetas destino
- `/localize R4 --step build --to English` — solo construye los HTML (ya deben estar inicializados)

## Pasos disponibles

### `init` — Inicializar carpetas destino
```bash
python scripts/core/goalbus_localize.py init Español/<serie> --target <LANG_CODE>
```
- Crea `Idioma/Serie/Serie_imagenN/` con copia del HTML y assets
- Registra formularios en `translation_data.csv`

### `build` — Construir HTML localizados
```bash
python scripts/core/goalbus_localize.py build_all --from ES --to <LANG_CODE>
```
- Inyecta traducciones de `global_translations.json` y `translation_data.csv`
- Genera `Idioma/Serie/Serie_imagenN/GoalBus.html` con textos en el idioma destino
- Reporta orphans (textos sin traducción)

### `status` — Ver cobertura
```bash
python scripts/core/goalbus_localize.py status --lang <LANG_CODE>
```
- Muestra qué carpetas tienen traducciones completas vs. con `PENDING`

### Sin `--step` (flujo completo)
Ejecuta: `init` → verifica `translation_data.csv` → `build` → reporta resultado

## Códigos de idioma internos

| Carpeta    | Código |
|------------|--------|
| English    | EN     |
| Deutsch    | DE     |
| Frances    | FR     |
| Italiano   | IT     |
| Portugues  | PT_BR  |
| Español    | ES     |

## Notas

- El HTML fuente siempre es `Español/`; otros idiomas son derivados
- Si `translation_data.csv` tiene columnas vacías para el idioma destino, el HTML puede quedar con placeholders sin resolver
- Los textos marcados `PENDING` en `global_translations.json` se mantienen en español en el HTML resultante
- Después de `build`, ejecutar `/capture` para generar los PNG
