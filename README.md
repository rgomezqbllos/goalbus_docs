# GoalBus Documentation Translation Pipeline

Traducción automática de los archivos Markdown de formación (P1–P27) a múltiples idiomas usando modelos de IA locales (Helsinki-NLP/opus-mt). **Corre 100 % offline en CPU — sin tokens de IA, sin APIs de pago.**

## Requisitos de Hardware

| Componente | Mínimo recomendado |
|---|---|
| CPU | 4 núcleos (8+ recomendado) |
| RAM | 8 GB (16 GB recomendado) |
| Disco | 2 GB libres (modelos en caché) |
| GPU | No requerida |
| Internet | Solo en la primera ejecución (descarga los modelos ~200 MB cada uno, luego todo es offline) |

## Instalación

```powershell
# 1. Crear entorno virtual (solo la primera vez)
python -m venv .venv

# 2. Activar el entorno
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# Windows CMD:
.\.venv\Scripts\activate.bat

# 3. Instalar dependencias de traducción
pip install -r requirements_translation.txt
```

> **Nota Windows:** Si `python` no funciona, usa `py`. Si aparece error de permisos en PowerShell, ejecuta primero:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Estructura de carpetas

```
goalbus_docs/
├── translate_docs.py              # Motor de traducción (un perfil)
├── run_pipeline.py                # Pipeline completo (todos los idiomas en secuencia)
├── requirements_translation.txt   # Dependencias Python
└── Maestros Finales/
    ├── Archivos Maestros (ES)/    # Fuente — archivos originales en español
    ├── Master Files (EN)/         # Generado por Profile A
    ├── Arquivos Mestres (PT_BR)/  # Generado por Profile C
    │   ├── glossary-transport-ops.md     # Glosario normativo ES/EN/PT-BR
    │   └── translation-guidelines.md    # Guía de estilo por idioma
    ├── Archivi Maestri (IT)/      # Generado por Profile D
    └── Fichiers Maîtres (FR)/     # Generado por Profile B
```

## Ejecución — Pipeline Completo (recomendado)

Traduce los 27 archivos a los 4 idiomas en secuencia (~2h 45min total en CPU de 4 núcleos):

```powershell
python run_pipeline.py
```

**Orden de ejecución:**

| Paso | Perfil | Fuente | Destino | Tiempo est. |
|------|--------|--------|---------|-------------|
| 1/4 | A | ES | EN | ~33 min |
| 2/4 | C | EN | PT_BR | ~50 min |
| 3/4 | D | EN | IT | ~50 min |
| 4/4 | B | ES | FR | ~33 min |

## Ejecución — Un solo idioma

Edita el bloque activo en `translate_docs.py` (descomenta el perfil deseado) y ejecuta:

```powershell
# Todos los archivos de ese idioma
python translate_docs.py

# Un solo archivo (útil para pruebas)
python translate_docs.py --file P1_Entendiendo_el_rol_del_planificador_y_el_flujo_end_to_end.md

# Re-traducir archivos ya existentes
python translate_docs.py --force
```

### Perfiles disponibles en `translate_docs.py`

```python
# Profile A: ES → EN  (descomenta este bloque y comenta el activo)
MODEL_NAME = "Helsinki-NLP/opus-mt-es-en"
TGT_LANG_TAG = "";  NLLB_SRC = "";  NLLB_TGT = ""
SRC_DIR = _ES;  TGT_DIR = _EN

# Profile B: ES → FR
MODEL_NAME = "Helsinki-NLP/opus-mt-es-fr"
TGT_LANG_TAG = "";  NLLB_SRC = "";  NLLB_TGT = ""
SRC_DIR = _ES;  TGT_DIR = _FR

# Profile C: EN → PT_BR  (requiere Profile A ejecutado primero)
MODEL_NAME = "Helsinki-NLP/opus-mt-en-ROMANCE"
TGT_LANG_TAG = ">>pt<<";  NLLB_SRC = "";  NLLB_TGT = ""
SRC_DIR = _EN;  TGT_DIR = _PT

# Profile D: EN → IT  (requiere Profile A ejecutado primero)
MODEL_NAME = "Helsinki-NLP/opus-mt-en-ROMANCE"
TGT_LANG_TAG = ">>it<<";  NLLB_SRC = "";  NLLB_TGT = ""
SRC_DIR = _EN;  TGT_DIR = _IT
```

## Glosario de terminología

El pipeline aplica automáticamente el glosario `glossary-transport-ops.md` (PT_BR) para garantizar términos correctos:

| Término EN | PT_BR correcto | Notas |
|---|---|---|
| Scheduling | Programação | Módulo GoalBus |
| Rostering | Alocação | Módulo GoalBus |
| Driver / Drivers | Motorista / Motoristas | ⚠️ Nunca "Condutor" |
| Empty trip | Viagem vazia | |
| Day off | Folga | |

Para añadir un glosario a otro idioma, crea un archivo `glossary-transport-ops.md` en la carpeta destino con la misma estructura de tablas y apunta `GLOSSARY_PATH` a él en `run_pipeline.py`.

## Añadir un nuevo idioma

1. Crea la carpeta destino en `Maestros Finales/`
2. Añade una nueva entrada en `PIPELINE` dentro de `run_pipeline.py`:

```python
(
    "EN -> DE",
    "Helsinki-NLP/opus-mt-en-de",   # busca el modelo en huggingface.co/Helsinki-NLP
    "",
    td._EN, td._DE,                 # añade _DE = BASE_DIR / "..." en translate_docs.py
    "de",
    None,                           # ruta al glosario o None
    "EN", "DE",
),
```

3. Añade la variable de ruta en el bloque de directorios de `translate_docs.py`:
```python
_DE = BASE_DIR / "Maestros Finales" / "Master Files (DE)"
```

## Archivos de log

Cada idioma genera su propio log en su carpeta destino:
```
Master Files (EN)/translation.log
Arquivos Mestres (PT_BR)/translation.log
...
```

Revisa los `[WARNING]` para detectar enlaces rotos o términos sin resolver.

---

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

```powershell
# Crear el ambiente virtual (solo la primera vez)
python -m venv .venv

# Activar el ambiente (en Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Activar el ambiente (en Windows CMD)
.\.venv\Scripts\activate.bat
```

**Nota para Windows:** Si el comando `python` no funciona, prueba con `py`. Los scripts han sido optimizados para evitar errores de codificación (`UnicodeEncodeError`) en terminales estándar de Windows.

## Instalación del Proceso de Captura (Playwright)

El módulo de captura automática de imágenes (`scripts/capture_screenshots.py`) utiliza Playwright para renderizar el HTML. Para configurarlo por primera vez:

1. **Instalar dependencias**:
   Con el entorno virtual activado, instala la librería:
   ```powershell
   pip install playwright
   ```

2. **Instalar navegadores de Playwright**:
   Ejecuta el siguiente comando para descargar el motor de Chromium:
   ```powershell
   python -m playwright install chromium
   ```

   > [!TIP]
   > En Windows, usar `python -m playwright` garantiza que se use la versión instalada en tu entorno virtual actual.

3. **Verificar estado de capturas**:
   ```powershell
   python scripts/capture_screenshots.py status --all
   ```


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
python scripts/goalbus_localize.py init Español/P8/P8_imagen1 --target PT_BR

# 2) Revisar qué textos de UI siguen pendientes
python scripts/goalbus_localize.py translate --from ES --to PT_BR

# 3) Construir la pantalla traducida
python scripts/goalbus_localize.py build Portugues/P8/P8_imagen1 --from ES
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
python scripts/goalbus_localize.py init Español/P8 --target PT_BR

# 2) Ver pendientes de vocabulario
python scripts/goalbus_localize.py translate --from ES --to PT_BR

# 3) Reconstruir toda la carpeta traducida
python scripts/goalbus_localize.py build Portugues/P8 --from ES
```

Usa este modo cuando ya tengas varias `P8_imagen1`, `P8_imagen2`, etc. y quieras:
- registrar todos los campos de formulario de la carpeta
- extraer todas las etiquetas de UI nuevas de ese bloque
- reconstruir todo `Portugues/P8`

### 4. Caso C: procesar un idioma completo

Ejemplo: todo `Español/` hacia portugués

```bash
# 1) Inicializar todas las pantallas fuente
python scripts/goalbus_localize.py init Español --target PT_BR

# 2) Revisar / exportar todas las traducciones pendientes
python scripts/goalbus_localize.py translate --from ES --to PT_BR

# 3) Reconstruir todo el idioma destino
python scripts/goalbus_localize.py build_all --from ES --to PT_BR
```

Esto es útil cuando:
- acabas de insertar muchas pantallas nuevas
- quieres poner al día `global_translations.json`
- quieres refrescar todo `Portugues/`

### 5. Extraer solo vocabulario de UI

Si no quieres tocar carpetas destino ni CSV, puedes lanzar solo extracción:

```bash
# Preview
python scripts/goalbus_localize.py extract Español/P8 --dry-run

# Guardar en global_translations.json
python scripts/goalbus_localize.py extract Español/P8
```

Esto solo afecta a `global_translations.json`.
No crea carpetas ni modifica `translation_data.csv`.

### 6. Traducir pendientes

```bash
# Ver pendientes en consola
python scripts/goalbus_localize.py translate --from ES --to PT_BR

# Exportar a TSV para trabajo offline/AI
python scripts/goalbus_localize.py translate --from ES --to EN --export pending_en.tsv

# Importar traducciones completadas
python scripts/goalbus_localize.py translate --import pending_en.tsv --to EN
```

### 7. Construcción

```bash
# Una pantalla específica
python scripts/goalbus_localize.py build Portugues/P8/P8_imagen1 --from ES

# Un bloque entero
python scripts/goalbus_localize.py build Portugues/P8 --from ES

# Todo el proyecto (un idioma)
python scripts/goalbus_localize.py build_all --from ES --to PT_BR

# Todo el proyecto (todos los idiomas existentes)
python scripts/goalbus_localize.py build_all
```

### 8. Verificación

```bash
# Estado general
python scripts/goalbus_localize.py status

# Detalle de un idioma
python scripts/goalbus_localize.py status --lang PT_BR
```

### 9. Resumen rápido de comandos

```bash
# Una sola pantalla
python scripts/goalbus_localize.py init Español/P8/P8_imagen1 --target PT_BR
python scripts/goalbus_localize.py build Portugues/P8/P8_imagen1 --from ES

# Una carpeta PX completa
python scripts/goalbus_localize.py init Español/P8 --target PT_BR
python scripts/goalbus_localize.py build Portugues/P8 --from ES

# Un idioma completo
python scripts/goalbus_localize.py init Español --target PT_BR
python scripts/goalbus_localize.py build_all --from ES --to PT_BR
```

## Combinaciones de Idioma

El pipeline es parametrizable. Cualquier idioma puede ser fuente o destino:

```bash
# Español → Portugués (caso más común)
python scripts/goalbus_localize.py build_all --from ES --to PT_BR

# Inglés → Español
python scripts/goalbus_localize.py build_all --from EN --to ES

# Español → Francés + Inglés
python scripts/goalbus_localize.py build_all --from ES --to EN,FR
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
