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

### 1. Preparación
Coloca el HTML original y su carpeta `_files` en la ruta del idioma fuente:
```
Español/P8/P8_imagen1/GoalBus.html
Español/P8/P8_imagen1/GoalBus_files/
```

### 2. Inicialización
```bash
# Una sola pantalla
python3 scripts/goalbus_localize.py init Español/P8/P8_imagen1

# Un bloque entero (recursivo)
python3 scripts/goalbus_localize.py init Español/P8

# Con idioma destino específico (default: PT_BR)
python3 scripts/goalbus_localize.py init Español/P8 --target EN
```
Esto crea la carpeta destino, escanea el HTML, registra los campos de formulario en el CSV y extrae texto de UI nuevo hacia `global_translations.json`.

Si solo quieres revisar o actualizar vocabulario sin tocar la inicialización de carpetas/CSV:
```bash
python3 scripts/goalbus_localize.py extract Español/P8 --dry-run
python3 scripts/goalbus_localize.py extract Español/P8
```

### 3. Datos de Formularios
Edita `translation_data.csv` y rellena las columnas `ES` y el idioma destino con los valores que deseas mostrar en las capturas.

### 4. Extracción de Vocabulario
```bash
# Preview (sin cambios)
python3 scripts/goalbus_localize.py extract Español/P8 --dry-run

# Ejecutar
python3 scripts/goalbus_localize.py extract Español/P8
```
Detecta textos nuevos en el HTML y los agrega como `PENDING` al diccionario JSON.

### 5. Traducción (Asistida por IA)
```bash
# Ver pendientes en consola
python3 scripts/goalbus_localize.py translate --from ES --to PT_BR

# Exportar a TSV para trabajo offline/AI
python3 scripts/goalbus_localize.py translate --from ES --to EN --export pending_en.tsv

# Importar traducciones completadas
python3 scripts/goalbus_localize.py translate --import pending_en.tsv --to EN
```

### 6. Construcción
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

### 7. Verificación
```bash
# Estado general
python3 scripts/goalbus_localize.py status

# Detalle de un idioma
python3 scripts/goalbus_localize.py status --lang EN
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
