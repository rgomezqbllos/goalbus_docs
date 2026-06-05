# GoalBus Docs: automatización de traducción, capturas y maestros finales

Este repositorio contiene el flujo completo para localizar documentación de GoalBus:

1. Traducir HTML guardados del producto y sus archivos dependientes.
2. Rellenar datos dinámicos de formularios por idioma.
3. Regenerar imágenes desde HTML local con Playwright.
4. Copiar imágenes y carpetas HTML finales a `Maestros Finales`.
5. Traducir archivos Markdown de documentación con modelos locales.

La regla principal es simple: primero se construyen los HTML finales por idioma, luego se capturan las imágenes, después se sincroniza `Maestros Finales` y al final se traducen los Markdown que consumen esas imágenes.

## 1. Requisitos

Instala todo una vez antes de ejecutar el flujo.

```bash
python -m venv .venv
source .venv/bin/activate
pip install playwright
pip install -r requirements_translation.txt
python -m playwright install chromium
```

En Windows usa:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install playwright
pip install -r requirements_translation.txt
python -m playwright install chromium
```

Si tienes varios Python instalados, usa siempre el Python del entorno virtual:

```bash
.venv/bin/python scripts/core/goalbus_localize.py status
.venv/bin/python scripts/core/capture_screenshots.py status --all
.venv/bin/python run_pipeline.py --list
```

## 2. Entradas del proceso

Antes de tocar comandos, confirma que existen estos datos de entrada.

| Entrada | Archivo o carpeta | Para qué sirve |
|---|---|---|
| HTML fuente | `Español/PX/PX_imagenN/GoalBus.html` | Pantalla base guardada desde el navegador. |
| Assets del HTML | `Español/PX/PX_imagenN/GoalBus_files/` | JS, CSS, imágenes y recursos necesarios para renderizar. |
| Diccionario UI | `global_translations.json` | Textos fijos de interfaz: botones, títulos, labels, placeholders, mensajes. |
| Datos de formularios | `translation_data.csv` | Valores dinámicos por pantalla: inputs, selects, fechas, checkboxes. |
| Locale packs | `en.json`, `de.json`, `fr.json`, `it.json`, `pt_br.json`, `es.json` | Traducciones oficiales por clave cuando existen en el producto. |
| Selectores de captura | `Idioma/PX/PX_imagenN/selector.json` | Define qué parte del HTML se captura como imagen. |
| Markdown fuente | `Maestros Finales/Master Files (EN)/*.md` | Fuente recomendada para traducir Markdown a otros idiomas. |

Regla práctica:

- Si el texto es parte fija de la UI, va en `global_translations.json`.
- Si el texto es un valor escrito dentro de un formulario, va en `translation_data.csv`.
- Si una celda de un idioma está vacía porque ese campo no debe mostrarse, no inventes valor.
- Si una fila tiene traducción en algún idioma y falta en otro, rellena el hueco antes de generar HTML.

## 3. Idiomas soportados

| Código | Carpeta de trabajo | Carpeta en maestros finales |
|---|---|---|
| `ES` | `Español/` | `Maestros Finales/Archivos Maestros (ES)/` |
| `EN` | `English/` | `Maestros Finales/Master Files (EN)/` |
| `FR` | `Frances/` | `Maestros Finales/Fichiers Maîtres (FR)/` |
| `PT_BR` | `Portugues/` | `Maestros Finales/Arquivos Mestres (PT_BR)/` |
| `IT` | `Italiano/` | `Maestros Finales/Archivi Maestri (IT)/` |
| `DE` | `Deutsch/` | `Maestros Finales/Master Files (DE)/` |

Si agregas un idioma nuevo, actualiza `FOLDER_TO_LANG` y `LANG_TO_FOLDER` en `scripts/core/goalbus_localize.py`, y agrega su destino en `scripts/core/sync_final.py`.

## 4. Fase HTML: crear idioma destino

Usa esta fase cuando necesitas crear o refrescar HTML localizados.

### 4.1. Aplicar traducciones oficiales del producto

Si tienes un JSON del producto para el idioma destino, úsalo primero. Ejemplo para alemán:

```bash
.venv/bin/python scripts/core/apply_language_pack.py --lang DE --target-json de.json
```

Esto cruza `en.json` contra `de.json` y actualiza:

- `global_translations.json`
- `translation_data.csv`

Ejemplos para otros idiomas:

```bash
.venv/bin/python scripts/core/apply_language_pack.py --lang FR --target-json fr.json
.venv/bin/python scripts/core/apply_language_pack.py --lang IT --target-json it.json
.venv/bin/python scripts/core/apply_language_pack.py --lang PT_BR --target-json pt_br.json
```

### 4.2. Inicializar carpetas destino

Para una pantalla:

```bash
.venv/bin/python scripts/core/goalbus_localize.py init Español/P20/P20_imagen4 --target DE
```

Para una carpeta completa:

```bash
.venv/bin/python scripts/core/goalbus_localize.py init Español/P20 --target DE
```

Para todo el idioma:

```bash
.venv/bin/python scripts/core/goalbus_localize.py init Español --target DE
```

El comando `init` hace tres cosas:

- Crea la carpeta destino, por ejemplo `Deutsch/P20/P20_imagen4`.
- Copia `GoalBus.html` y `GoalBus_files`.
- Registra campos dinámicos en `translation_data.csv`.

### 4.3. Extraer vocabulario nuevo de UI

Ejecuta extracción cuando llegan HTML nuevos o aparecen textos sin registrar:

```bash
.venv/bin/python scripts/core/goalbus_localize.py extract Español/P20
```

Vista previa sin escribir:

```bash
.venv/bin/python scripts/core/goalbus_localize.py extract Español/P20 --dry-run
```

La extracción escribe entradas nuevas en `global_translations.json` con valor `PENDING` para los idiomas que falten.

### 4.4. Exportar pendientes, traducir e importar

Exporta pendientes a TSV:

```bash
.venv/bin/python scripts/core/goalbus_localize.py translate --from ES --to DE --export pending_DE_Español.tsv
```

Abre el TSV y rellena la columna del idioma destino. Después importa:

```bash
.venv/bin/python scripts/core/goalbus_localize.py translate --import pending_DE_Español.tsv --to DE
```

También puedes ver pendientes en consola:

```bash
.venv/bin/python scripts/core/goalbus_localize.py translate --from ES --to DE
```

### 4.5. Revisar `translation_data.csv`

Antes de construir HTML, revisa la columna del idioma destino.

Para alemán revisa `DE`; para francés `FR`; para italiano `IT`; para portugués `PT_BR`; para inglés `EN`.

Reglas:

- No dejes valores en inglés dentro de una columna destino.
- No pongas valores donde el resto de idiomas está vacío por diseño.
- No uses el `field_id` como valor visible. Si ves `vehicleTypeName`, `propulsionTypeId`, `capacity`, etc. en una captura, el HTML no fue reconstruido correctamente.
- Los códigos técnicos pueden quedarse iguales si son identificadores reales: `DEP05`, `L1`, `BD`, `GTFS`.

Estado general:

```bash
.venv/bin/python scripts/core/goalbus_localize.py status --lang DE
```

## 5. Fase HTML: construir pantallas finales

Construye una pantalla:

```bash
.venv/bin/python scripts/core/goalbus_localize.py build Deutsch/P20/P20_imagen4 --from ES
```

Construye una carpeta:

```bash
.venv/bin/python scripts/core/goalbus_localize.py build Deutsch/P20 --from ES
```

Construye todo un idioma:

```bash
.venv/bin/python scripts/core/goalbus_localize.py build_all --from ES --to DE
```

Construye todos los idiomas existentes:

```bash
.venv/bin/python scripts/core/goalbus_localize.py build_all --from ES
```

Salida esperada:

- HTML actualizado en `Deutsch/PX/PX_imagenN/GoalBus.html`.
- Formularios con valores correctos desde `translation_data.csv`.
- Textos fijos traducidos desde `global_translations.json`.

## 6. Fase imágenes: selector y captura

Cada carpeta `Idioma/PX/PX_imagenN` debe tener un `selector.json`.

Estado de una carpeta:

```bash
.venv/bin/python scripts/core/capture_screenshots.py status Deutsch/P20
```

Estado completo:

```bash
.venv/bin/python scripts/core/capture_screenshots.py status --all
```

Captura una imagen:

```bash
.venv/bin/python scripts/core/capture_screenshots.py capture Deutsch/P20/P20_imagen4
```

Captura una carpeta:

```bash
.venv/bin/python scripts/core/capture_screenshots.py capture Deutsch/P20
```

Captura un idioma completo:

```bash
.venv/bin/python scripts/core/capture_screenshots.py capture Deutsch
```

Captura todos los idiomas:

```bash
.venv/bin/python scripts/core/capture_screenshots.py capture Español
.venv/bin/python scripts/core/capture_screenshots.py capture English
.venv/bin/python scripts/core/capture_screenshots.py capture Frances
.venv/bin/python scripts/core/capture_screenshots.py capture Portugues
.venv/bin/python scripts/core/capture_screenshots.py capture Italiano
.venv/bin/python scripts/core/capture_screenshots.py capture Deutsch
```

El capturador hace un preflight: si detecta formularios con placeholders sin inyectar, reconstruye el HTML antes de capturar.

Si el recorte sale mal, edita `selector.json`:

- Usa selectores estables: `data-qa-id`, `gsqaid`, `gs-*`, `otto-web-*`.
- Usa varios `selectors` cuando el recorte necesite anclas superior e inferior.
- Ajusta `bbox_mode`: `element`, `content` o `smart`.
- Ajusta `padding`, `viewport_width` y `viewport_height` cuando cambie la geometría.
- Usa `pre_capture_js` para overlays, tooltips o textos dinámicos.

## 7. Fase Maestros Finales

Después de capturar imágenes, sincroniza todo a `Maestros Finales`.

```bash
.venv/bin/python scripts/core/sync_final.py
```

El sincronizador copia:

- PNG actuales desde `Español/`, `English/`, `Frances/`, `Portugues/`, `Italiano/`, `Deutsch/`.
- Carpetas `PX_imagenN` con sus `GoalBus.html`, `GoalBus_files` y `selector.json`.
- Todo al destino correcto dentro de `Maestros Finales`.

El sincronizador no copia `*_old.png` y además elimina `*_old.png` que ya existan dentro de `Maestros Finales`.

Validación esperada:

```text
old_png_remaining=0
```

## 8. Fase Markdown

Los Markdown viven en `Maestros Finales/<carpeta idioma>/*.md`.

La fuente recomendada para nuevos idiomas es inglés:

```text
Maestros Finales/Master Files (EN)/*.md
```

### 8.1. Ver perfiles disponibles

```bash
.venv/bin/python run_pipeline.py --list
```

Perfiles actuales:

```text
ES -> EN
EN -> PT_BR
EN -> IT
ES -> FR
EN -> DE
```

### 8.2. Traducir todos los perfiles

```bash
.venv/bin/python run_pipeline.py
```

Esto traduce todos los perfiles definidos en `run_pipeline.py`.

### 8.3. Traducir solo alemán desde inglés

```bash
.venv/bin/python run_pipeline.py --only "EN -> DE"
```

Salida esperada:

- Markdown alemanes en `Maestros Finales/Master Files (DE)`.
- `filename_map.json` en la carpeta destino.
- `translation.log` con advertencias y enlaces no resueltos.

### 8.4. Traducir un solo archivo manualmente con el motor

Usa esto para pruebas puntuales:

```bash
.venv/bin/python translate_docs.py --file P2_Creating_The_Calendar_Base_With_Day_And_Holiday_Types.md --force
```

Antes de usar `translate_docs.py` directamente, confirma que el perfil activo dentro del archivo apunta al idioma correcto.

## 9. Orden completo recomendado

Ejemplo para actualizar alemán desde HTML español y Markdown inglés:

```bash
# 1) Aplicar traducciones oficiales del producto
.venv/bin/python scripts/core/apply_language_pack.py --lang DE --target-json de.json

# 2) Crear o actualizar carpetas HTML destino
.venv/bin/python scripts/core/goalbus_localize.py init Español --target DE

# 3) Extraer vocabulario de UI nuevo
.venv/bin/python scripts/core/goalbus_localize.py extract Español

# 4) Exportar pendientes de UI
.venv/bin/python scripts/core/goalbus_localize.py translate --from ES --to DE --export pending_DE_Español.tsv

# 5) Importar el TSV después de completarlo
.venv/bin/python scripts/core/goalbus_localize.py translate --import pending_DE_Español.tsv --to DE

# 6) Construir HTML finales
.venv/bin/python scripts/core/goalbus_localize.py build_all --from ES --to DE

# 7) Verificar estado de UI y formularios
.venv/bin/python scripts/core/goalbus_localize.py status --lang DE

# 8) Generar imágenes
.venv/bin/python scripts/core/capture_screenshots.py capture Deutsch

# 9) Copiar imágenes y carpetas HTML a Maestros Finales
.venv/bin/python scripts/core/sync_final.py

# 10) Traducir Markdown EN -> DE
.venv/bin/python run_pipeline.py --only "EN -> DE"
```

## 10. Checklist de control antes de subir a GitHub

Ejecuta estas validaciones:

```bash
.venv/bin/python scripts/core/goalbus_localize.py status --lang DE
.venv/bin/python scripts/core/capture_screenshots.py status Deutsch
.venv/bin/python scripts/core/sync_final.py
git status --porcelain
```

Revisa manualmente:

- No hay `*_old.png` en `Maestros Finales`.
- Las capturas no muestran textos en el idioma incorrecto.
- Los formularios no muestran `field_id` como valor visible.
- `translation_data.csv` no tiene columnas destino con huecos accidentales.
- `translation.log` no contiene warnings importantes sin revisar.

## 11. Problemas comunes

| Problema | Causa probable | Solución |
|---|---|---|
| Sale texto en inglés dentro de una imagen destino | Falta traducción en `global_translations.json` o `translation_data.csv` | Rellena el valor y ejecuta `build_all`, luego recaptura. |
| Un formulario muestra `vehicleTypeName` o `capacity` | HTML destino no fue reconstruido después de editar CSV | Ejecuta `build_all --from ES --to <IDIOMA>` y recaptura. |
| La captura sale cortada | `selector.json` apunta a un elemento incompleto | Usa varios `selectors`, ajusta `bbox_mode` y `padding`. |
| Markdown genera nombres raros | El modelo tradujo títulos literalmente | Revisa el `.md` generado y corrige nombres de archivo/títulos si hace falta. |
| Playwright no abre Chromium | Falta instalar navegador o hay permisos del sistema | Ejecuta `python -m playwright install chromium`; en macOS puede requerir ejecutar fuera de sandbox. |
| `torch` no existe | Dependencias de markdown no instaladas en esa venv | Ejecuta `pip install -r requirements_translation.txt` con la venv activa. |

## 12. Inteligencia Semántica con CodeGraph

Este repositorio está preparado para integrarse con **CodeGraph**, una herramienta de inteligencia semántica local que indexa los símbolos, clases, funciones y dependencias del código. Esto permite que cualquier IA (como Claude Code, Cursor, Windsurf, etc.) entienda de inmediato el contexto y la arquitectura completa del proyecto sin tener que escanear todos los archivos en cada turno.

### 12.1. ¿Cómo funciona en este proyecto?
El repositorio incluye la carpeta `.codegraph/` con la configuración del índice. El archivo de base de datos local `codegraph.db` está ignorado en `.gitignore` para no subir binarios pesados al repositorio, por lo que cada desarrollador (o su agente de IA) debe generar su propio índice local la primera vez.

### 12.2. Guía para otras IA / Desarrolladores

Para inicializar y utilizar el índice semántico:

1. **Inicializar e indexar el proyecto localmente:**
   ```bash
   npx -y @colbymchenry/codegraph init -i
   ```
   *Esto creará la base de datos SQLite local indexando las funciones, importaciones y dependencias de los módulos Python.*

2. **Verificar el estado del índice:**
   ```bash
   npx @colbymchenry/codegraph status
   ```

3. **Sincronizar cambios recientes:**
   Si realizas cambios en el código, puedes sincronizar el índice rápidamente:
   ```bash
   npx @colbymchenry/codegraph sync
   ```

4. **Integración con Agentes de IA (Claude Code / Cursor):**
   * **Claude Code:** Al entrar al repositorio, Claude detectará la carpeta `.codegraph/` automáticamente y activará sus herramientas semánticas en caso de que esté configurado como servidor de MCP.
   * **MCP Server:** Puedes iniciar CodeGraph como un servidor MCP ejecutando:
     ```bash
     npx @colbymchenry/codegraph serve
     ```
     Agrega este servidor a tu configuración de Claude Desktop o IDE para dotarlo de herramientas avanzadas de exploración de código (como buscar llamadas a funciones, ver dependencias cruzadas y saltar a definiciones).

---

## 13. Publicación

Cuando todo esté validado:

```bash
git status --porcelain
git add -A
git commit -m "Update localized documentation and add CodeGraph context configuration"
git push origin main
```

Si trabajas en rama:

```bash
git checkout -b codex/update-localized-docs
git add -A
git commit -m "Update localized documentation and add CodeGraph context configuration"
git push -u origin codex/update-localized-docs
```

