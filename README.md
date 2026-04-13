# GoalBus DOM Localization Pipeline v2.0

Localización nativa (HTML/DOM) de las pantallas de GoalBus. En lugar de editar imágenes manualmente, reconstruimos las vistas renderizando el HTML real y traduciendo textos y datos mediante un pipeline automatizado en Python.

## Arquitectura

El sistema se apoya en 3 componentes:

1. **`global_translations.json`** — Diccionario maestro de textos de UI. Almacena texto limpio (sin wrappers) con un campo `_match` que indica la estrategia de reemplazo (`tag` para contenido entre tags HTML, `attr:nombre` para atributos como `aria-label`, `placeholder`, etc.).

2. **`translation_data.csv`** — Datos dinámicos de formularios. Guarda valores específicos por pantalla (inputs, selects, checkboxes) organizados por `folder`, `field_id`, `type` y columnas de idioma.

3. **`scripts/goalbus_localize.py`** — Motor CLI parametrizable. Soporta cualquier combinación de idioma origen → destino.

## Idiomas Soportados

| Código | Carpeta | Estado |
|--------|---------|--------|
| ES | Español/ | Fuente principal |
| PT_BR | Portugues/ | Completo |
| EN | English/ | Parcial |
| FR | Frances/ | Parcial |
| IT | Italiano/ | Disponible |
| DE | Deutsch/ | Disponible |

Para agregar un nuevo idioma, edita `FOLDER_TO_LANG` y `LANG_TO_FOLDER` en el script.

## Inicialización del Entorno (Python)

Para poder ejecutar los scripts, primero debes crear y activar el ambiente de Python:

```bash
# Crear el ambiente virtual (solo la primera vez)
python -m venv .venv

# Activar el ambiente (en Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Activar el ambiente (en Windows CMD)
.\.venv\Scripts\activate.bat
```

**Nota para Windows:** Los scripts han sido optimizados para evitar errores de codificación (`UnicodeEncodeError`) en terminales estándar de Windows (reemplazando caracteres especiales por ASCII).

## Flujo de Trabajo

### Qué guarda cada archivo

- `global_translations.json`: textos de UI reutilizables.
  Ejemplos: títulos, tabs, labels, botones, mensajes de tabla vacía, textos de navegación.
- `translation_data.csv`: datos dinámicos por pantalla.
  Ejemplos: nombres, descripciones, selects, checkboxes, fechas, valores de formularios.

Regla práctica:
- Si el texto es parte fija de la interfaz, debe acabar en `global_translations.json`.
- Si el texto es un valor propio de una pantalla concreta, debe acabar en `translation_data.csv`.

### 1. Preparación
Coloca el HTML original y su carpeta `_files` en la ruta del idioma fuente:
```
Español/P8/P8_imagen1/GoalBus.html
Español/P8/P8_imagen1/GoalBus_files/
```

### 2. Caso A: procesar una sola pantalla `PX_imagenY`

Ejemplo: `Español/P8/P8_imagen1`

```bash
# 1) Inicializar la pantalla destino y extraer estructura + vocabulario
python3 scripts/goalbus_localize.py init Español/P8/P8_imagen1 --target PT_BR

# 2) Revisar qué textos de UI siguen pendientes
python3 scripts/goalbus_localize.py translate --from ES --to PT_BR

# 3) Construir la pantalla traducida
python3 scripts/goalbus_localize.py build Portugues/P8/P8_imagen1 --from ES
```

Qué hace `init` en este caso:
- crea `Portugues/P8/P8_imagen1` si no existe
- detecta campos dinámicos y los registra en `translation_data.csv`
- detecta textos de UI nuevos y los añade a `global_translations.json`

Qué debes revisar después:
- `translation_data.csv`
  Aquí rellenas los valores dinámicos de `P8_imagen1` para `PT_BR`
- `global_translations.json`
  Aquí traduces las entradas nuevas que hayan quedado como `PENDING`

### 3. Caso B: procesar una carpeta completa `Español/PX`

Ejemplo: `Español/P8`

```bash
# 1) Inicializar todas las imágenes de la carpeta
python3 scripts/goalbus_localize.py init Español/P8 --target PT_BR

# 2) Ver pendientes de vocabulario
python3 scripts/goalbus_localize.py translate --from ES --to PT_BR

# 3) Reconstruir toda la carpeta traducida
python3 scripts/goalbus_localize.py build Portugues/P8 --from ES
```

Usa este modo cuando ya tengas varias `P8_imagen1`, `P8_imagen2`, etc. y quieras:
- registrar todos los campos de formulario de la carpeta
- extraer todas las etiquetas de UI nuevas de ese bloque
- reconstruir todo `Portugues/P8`

### 4. Caso C: procesar un idioma completo

Ejemplo: todo `Español/` hacia portugués

```bash
# 1) Inicializar todas las pantallas fuente
python3 scripts/goalbus_localize.py init Español --target PT_BR

# 2) Revisar / exportar todas las traducciones pendientes
python3 scripts/goalbus_localize.py translate --from ES --to PT_BR

# 3) Reconstruir todo el idioma destino
python3 scripts/goalbus_localize.py build_all --from ES --to PT_BR
```

Esto es útil cuando:
- acabas de insertar muchas pantallas nuevas
- quieres poner al día `global_translations.json`
- quieres refrescar todo `Portugues/`

### 5. Extraer solo vocabulario de UI

Si no quieres tocar carpetas destino ni CSV, puedes lanzar solo extracción:

```bash
# Preview
python3 scripts/goalbus_localize.py extract Español/P8 --dry-run

# Guardar en global_translations.json
python3 scripts/goalbus_localize.py extract Español/P8
```

Esto solo afecta a `global_translations.json`.
No crea carpetas ni modifica `translation_data.csv`.

### 6. Traducir pendientes

```bash
# Ver pendientes en consola
python3 scripts/goalbus_localize.py translate --from ES --to PT_BR

# Exportar a TSV para trabajo offline/AI
python3 scripts/goalbus_localize.py translate --from ES --to EN --export pending_en.tsv

# Importar traducciones completadas
python3 scripts/goalbus_localize.py translate --import pending_en.tsv --to EN
```

### 7. Construcción

```bash
# Una pantalla específica
python3 scripts/goalbus_localize.py build Portugues/P8/P8_imagen1 --from ES

# Un bloque entero
python3 scripts/goalbus_localize.py build Portugues/P8 --from ES

# Todo el proyecto (un idioma)
python3 scripts/goalbus_localize.py build_all --from ES --to PT_BR

# Todo el proyecto (todos los idiomas existentes)
python3 scripts/goalbus_localize.py build_all
```

### 8. Verificación

```bash
# Estado general
python3 scripts/goalbus_localize.py status

# Detalle de un idioma
python3 scripts/goalbus_localize.py status --lang PT_BR
```

### 9. Resumen rápido de comandos

```bash
# Una sola pantalla
python3 scripts/goalbus_localize.py init Español/P8/P8_imagen1 --target PT_BR
python3 scripts/goalbus_localize.py build Portugues/P8/P8_imagen1 --from ES

# Una carpeta PX completa
python3 scripts/goalbus_localize.py init Español/P8 --target PT_BR
python3 scripts/goalbus_localize.py build Portugues/P8 --from ES

# Un idioma completo
python3 scripts/goalbus_localize.py init Español --target PT_BR
python3 scripts/goalbus_localize.py build_all --from ES --to PT_BR
```

## Combinaciones de Idioma

El pipeline es parametrizable. Cualquier idioma puede ser fuente o destino:

```bash
# Español → Portugués (caso más común)
python3 scripts/goalbus_localize.py build_all --from ES --to PT_BR

# Inglés → Español
python3 scripts/goalbus_localize.py build_all --from EN --to ES

# Español → Francés + Inglés
python3 scripts/goalbus_localize.py build_all --from ES --to EN,FR
```

## Formato del JSON

Cada entrada almacena texto limpio (sin decoradores HTML):
```json
{
  "ui_text_8": {
    "ES": "Nombre",
    "PT_BR": "Nome",
    "EN": "Name",
    "FR": "Nom",
    "_match": "tag"
  },
  "ui_text_27": {
    "ES": "Servicios",
    "PT_BR": "Serviços",
    "_match": "attr:aria-label"
  }
}
```

El campo `_match` controla cómo se busca el texto en el HTML:
- `"tag"` — busca entre tags: `>Texto<`
- `"attr:placeholder"` — busca en atributos: `placeholder="Texto"`
- `"attr:aria-label"` — busca en: `aria-label="Texto"`

## Guía para Asistentes de IA

1. Al ejecutar `extract`, lee `global_translations.json` y traduce todos los `"PENDING"` al idioma destino.
2. Al ejecutar `init`, ayuda a rellenar `translation_data.csv` con datos realistas.
3. Después de cualquier cambio al JSON o CSV, ejecuta `build_all` para refrescar todo.
4. Usa `translate --export` para obtener un TSV limpio y `translate --import` para devolver las traducciones.
