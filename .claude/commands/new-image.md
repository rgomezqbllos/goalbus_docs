# /new-image

Crea una nueva imagen en una serie existente de GoalBus Docs, partiendo de Español.

## Uso

```
/new-image <serie> <numero> [--from carpeta-html-fuente] [--clone-from imagen-existente]
```

**Ejemplos:**
- `/new-image R3 6` — crea `traducciones/Español/R3/R3_imagen6/` con HTML y selector.json vacío
- `/new-image R3 6 --clone-from R3_imagen5` — clona selector.json y HTML desde R3_imagen5
- `/new-image P20 4 --from "ruta/al/GoalBus.html"` — usa HTML externo como fuente

## Comportamiento

1. **Crea la carpeta** `traducciones/Español/<Serie>/<Serie>_imagen<N>/`
2. **Copia el HTML** fuente (o clona desde imagen existente)
3. **Crea `selector.json`** inicial:
   - Si `--clone-from`: copia el selector.json de la imagen origen
   - Si no: genera un selector.json básico con `bbox_mode: "smart"`, viewport 1920x1080
4. **Registra en `translation_data.csv`**: agrega fila con los campos del HTML
5. **Muestra el siguiente paso**: ejecutar `/selector` para ajustar el selector, luego `/capture`

## selector.json inicial generado

```json
{
  "description": "<Serie> imagen <N>",
  "selector": "body",
  "bbox_mode": "smart",
  "padding": 0,
  "viewport_width": 1920,
  "viewport_height": 1080,
  "device_scale_factor": 1
}
```

## Flujo recomendado después de crear

```
1. /selector traducciones/Español/R3/R3_imagen6          # Ajustar selector
2. /capture traducciones/Español/R3/R3_imagen6           # Verificar captura
3. /localize R3/R3_imagen6                  # Localizar a todos los idiomas
4. /capture-all R3/R3_imagen6               # Capturar en todos los idiomas
```

## Notas

- El número de imagen debe ser consecutivo (revisar qué número sigue con `/new-image R3 --list`)
- Si `--list` se pasa como número, muestra las imágenes existentes de la serie
- No crea automáticamente las carpetas de otros idiomas; eso lo hace `/localize`
