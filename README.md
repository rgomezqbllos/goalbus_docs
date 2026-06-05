# GoalBus Docs: automatización de traducción, capturas y maestros finales

Este repositorio contiene el flujo completo para localizar documentación de GoalBus:

1. Traducir HTML guardados del producto y sus archivos dependientes.
2. Rellenar datos dinámicos de formularios por idioma.
3. Regenerar imágenes desde HTML local con Playwright.
4. Copiar imágenes y carpetas HTML finales a `Maestros Finales`.
5. Traducir archivos Markdown de documentación con modelos locales.

La regla principal es simple: primero se construyen los HTML finales por idioma, luego se capturan las imágenes, después se sincroniza `Maestros Finales` y al final se traducen los Markdown que consumen esas imágenes.

---

## 1. Requisitos

Instala todo una vez antes de ejecutar el flujo.

```bash
python -m venv .venv
source .venv/bin/activate
pip install playwright
pip install -r requirements_translation.txt
python -m playwright install chromium
```

En Windows:

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

---

## 2. Estructura del proyecto

```
goalbus_docs/
├── Español/                      ← Fuente principal (HTML base en español)
│   └── <Serie>/<Serie>_imagenN/
│       ├── GoalBus.html          ← HTML guardado del navegador
│       ├── GoalBus_files/        ← JS, CSS e imágenes del HTML
│       └── selector.json         ← Configuración de captura
│
├── English/                      ← HTML y PNG localizados por idioma
├── Deutsch/
├── Frances/
├── Italiano/
├── Portugues/
│
├── Maestros Finales/             ← Output final (PNG + HTML) por idioma
│   ├── Archivos Maestros (ES)/
│   ├── Master Files (EN)/
│   ├── Master Files (DE)/
│   ├── Fichiers Maîtres (FR)/
│   ├── Archivi Maestri (IT)/
│   └── Arquivos Mestres (PT_BR)/
│
├── scripts/
│   ├── core/                     ← Scripts del flujo principal
│   │   ├── goalbus_localize.py   ← Motor de localización HTML
│   │   ├── capture_screenshots.py← Captura con Playwright
│   │   ├── capture_scope.py      ← Captura por alcance (idioma/serie/imagen)
│   │   ├── locale_pack.py        ← Carga y consulta packs oficiales
│   │   ├── series_utils.py       ← Parsing de nombres de series/imágenes
│   │   ├── localize_r_series_by_locale_pack.py
│   │   ├── series_capture_pipeline.py
│   │   ├── apply_language_pack.py
│   │   └── sync_final.py         ← Sincroniza a Maestros Finales
│   ├── utils/                    ← Herramientas de soporte
│   │   ├── auto_select_from_old.py
│   │   ├── batch_translate.py
│   │   ├── review_selectors.py
│   │   ├── create_compares.py
│   │   └── scrub_secrets.py
│   ├── tests/                    ← Suite de tests
│   │   ├── test_locale_pack.py
│   │   └── test_series_utils.py
│   └── docs/                     ← Documentación de scripts
│       ├── CAPTURE_README.md
│       ├── LOCALIZATION_README.md
│       └── AGENT_CAPTURE_PROMPT.md
│
├── global_translations.json      ← Diccionario UI centralizado (6 idiomas)
├── translation_data.csv          ← Valores dinámicos de formularios
├── es.json, en.json, de.json,
│   fr.json, it.json, pt_br.json  ← Packs oficiales del producto
├── driver_names_localization.json← Nombres de conductores por idioma
├── run_pipeline.py               ← Orquestador de traducción Markdown
├── translate_docs.py             ← Motor Helsinki-NLP para Markdown
├── check_pending.py              ← Lista PENDING en global_translations.json
└── fill_translations_E1_E2_R1.py ← Relleno de TSV para series E1/E2/R1
```

> Las carpetas de idiomas y `Maestros Finales/` están en `.gitignore`. Solo se versiona el código, los diccionarios y los selector.json.

---

## 3. Skills disponibles (Claude Code)

Usa estos slash commands para tareas frecuentes sin memorizar comandos:

| Skill | Uso |
|-------|-----|
| `/capture <scope>` | Captura screenshots de un idioma, serie o imagen |
| `/selector <carpeta>` | Crea, repara o ajusta un `selector.json` |
| `/localize <serie>` | Localiza HTML de Español a idiomas destino |
| `/new-image <serie> <N>` | Crea una imagen nueva en una serie existente |
| `/translate-pending` | Detecta y resuelve traducciones `PENDING` |
| `/sync` | Sincroniza a Maestros Finales y hace commit/push |
| `/run-processingImages <serie>` | Flujo completo de extremo a extremo |

---

## 4. Entradas del proceso

| Entrada | Archivo o carpeta | Para qué sirve |
|---|---|---|
| HTML fuente | `Español/<Serie>/<Serie>_imagenN/GoalBus.html` | Pantalla base guardada desde el navegador. |
| Assets del HTML | `Español/<Serie>/<Serie>_imagenN/GoalBus_files/` | JS, CSS, imágenes y recursos necesarios para renderizar. |
| Diccionario UI | `global_translations.json` | Textos fijos de interfaz: botones, títulos, labels, placeholders, mensajes. |
| Datos de formularios | `translation_data.csv` | Valores dinámicos por pantalla: inputs, selects, fechas, checkboxes. |
| Locale packs | `en.json`, `de.json`, `fr.json`, `it.json`, `pt_br.json`, `es.json` | Traducciones oficiales por clave cuando existen en el producto. |
| Selectores de captura | `<Idioma>/<Serie>/<Serie>_imagenN/selector.json` | Define qué parte del HTML se captura como imagen. |
| Markdown fuente | `Maestros Finales/Master Files (EN)/*.md` | Fuente recomendada para traducir Markdown a otros idiomas. |

Reglas del CSV:

- Si el texto es parte fija de la UI → `global_translations.json`.
- Si el texto es un valor de formulario → `translation_data.csv`.
- No inventes valores donde otros idiomas están vacíos por diseño.
- No uses el `field_id` como valor visible (`vehicleTypeName`, `capacity`, etc.).

---

## 5. Idiomas soportados

| Código | Carpeta de trabajo | Carpeta en maestros finales |
|---|---|---|
| `ES` | `Español/` | `Maestros Finales/Archivos Maestros (ES)/` |
| `EN` | `English/` | `Maestros Finales/Master Files (EN)/` |
| `FR` | `Frances/` | `Maestros Finales/Fichiers Maîtres (FR)/` |
| `PT_BR` | `Portugues/` | `Maestros Finales/Arquivos Mestres (PT_BR)/` |
| `IT` | `Italiano/` | `Maestros Finales/Archivi Maestri (IT)/` |
| `DE` | `Deutsch/` | `Maestros Finales/Master Files (DE)/` |

Para agregar un idioma nuevo: actualiza `FOLDER_TO_LANG` y `LANG_TO_FOLDER` en `scripts/core/goalbus_localize.py`, y agrega su destino en `scripts/core/sync_final.py`.

---

## 6. Fase HTML: crear idioma destino

### 6.1. Aplicar traducciones oficiales del producto

Si tienes un JSON del producto para el idioma destino, úsalo primero:

```bash
.venv/bin/python scripts/core/apply_language_pack.py --lang DE --target-json de.json
.venv/bin/python scripts/core/apply_language_pack.py --lang FR --target-json fr.json
.venv/bin/python scripts/core/apply_language_pack.py --lang IT --target-json it.json
.venv/bin/python scripts/core/apply_language_pack.py --lang PT_BR --target-json pt_br.json
```

Esto cruza `en.json` contra el pack destino y actualiza `global_translations.json` y `translation_data.csv`.

### 6.2. Inicializar carpetas destino

```bash
# Una imagen
.venv/bin/python scripts/core/goalbus_localize.py init Español/R3/R3_imagen1 --target DE

# Una serie completa
.venv/bin/python scripts/core/goalbus_localize.py init Español/R3 --target DE

# Todo el idioma
.venv/bin/python scripts/core/goalbus_localize.py init Español --target DE
```

El comando `init`:
- Crea la carpeta destino (ej. `Deutsch/R3/R3_imagen1`).
- Copia `GoalBus.html` y `GoalBus_files/`.
- Registra campos dinámicos en `translation_data.csv`.

### 6.3. Extraer vocabulario nuevo de UI

```bash
# Extracción
.venv/bin/python scripts/core/goalbus_localize.py extract Español/R3

# Vista previa sin escribir
.venv/bin/python scripts/core/goalbus_localize.py extract Español/R3 --dry-run
```

Escribe entradas nuevas en `global_translations.json` con valor `PENDING`.

### 6.4. Exportar pendientes, traducir e importar

```bash
# Exportar a TSV
.venv/bin/python scripts/core/goalbus_localize.py translate --from ES --to DE --export pending_DE.tsv

# Importar después de completar el TSV
.venv/bin/python scripts/core/goalbus_localize.py translate --import pending_DE.tsv --to DE

# Ver pendientes en consola
.venv/bin/python scripts/core/goalbus_localize.py translate --from ES --to DE
```

### 6.5. Estado de traducciones

```bash
.venv/bin/python scripts/core/goalbus_localize.py status --lang DE
```

---

## 7. Fase HTML: construir pantallas finales

```bash
# Una imagen
.venv/bin/python scripts/core/goalbus_localize.py build Deutsch/R3/R3_imagen1 --from ES

# Una serie
.venv/bin/python scripts/core/goalbus_localize.py build Deutsch/R3 --from ES

# Todo un idioma
.venv/bin/python scripts/core/goalbus_localize.py build_all --from ES --to DE

# Todos los idiomas
.venv/bin/python scripts/core/goalbus_localize.py build_all --from ES
```

Salida esperada: HTML actualizado con textos traducidos y formularios con valores correctos.

---

## 8. Fase imágenes: selector y captura

Cada carpeta `<Idioma>/<Serie>/<Serie>_imagenN/` debe tener un `selector.json`.

```bash
# Estado
.venv/bin/python scripts/core/capture_screenshots.py status Deutsch/R3
.venv/bin/python scripts/core/capture_screenshots.py status --all

# Captura por alcance (recomendado)
.venv/bin/python scripts/core/capture_scope.py English/R3/R3_imagen1
.venv/bin/python scripts/core/capture_scope.py English/R3
.venv/bin/python scripts/core/capture_scope.py English

# Captura directa
.venv/bin/python scripts/core/capture_screenshots.py capture Deutsch
```

El capturador hace preflight: si detecta formularios con placeholders sin inyectar, reconstruye el HTML antes de capturar.

### Campos de selector.json

```json
{
  "description": "Descripción de la imagen",
  "selector": "body",
  "bbox_mode": "smart",
  "viewport_width": 1920,
  "viewport_height": 1080,
  "device_scale_factor": 1,
  "padding": 0,
  "filter_grid_rows": ["5202_1", "5202_2"],
  "pre_capture_js": "// JS ejecutado antes de capturar"
}
```

Patrones frecuentes de `pre_capture_js`:

```javascript
// Ocultar header
const header = document.querySelector('gs-header');
if (header) header.style.display = 'none';
window.dispatchEvent(new Event('resize'));

// Recuadro azul sobre un elemento
const el = document.querySelector('.mi-selector');
if (el) {
  const r = el.getBoundingClientRect();
  const ov = document.createElement('div');
  ov.style.cssText = 'position:fixed;pointer-events:none;z-index:9999;box-sizing:border-box;border:3px solid rgb(0,98,132);border-radius:4px;';
  ov.style.left=(r.left-4)+'px'; ov.style.top=(r.top-4)+'px';
  ov.style.width=(r.width+8)+'px'; ov.style.height=(r.height+8)+'px';
  document.body.appendChild(ov);
}

// Traducir texto con transloco (comillas simples en el selector CSS)
document.querySelectorAll('[transloco="clave.de.traduccion"]').forEach(function(span) {
  var p = span.parentElement;
  p.childNodes.forEach(function(n) {
    if (n.nodeType === 3 && n.textContent.includes('TextoOriginal'))
      n.textContent = n.textContent.replace('TextoOriginal', 'Traducción');
  });
});
```

---

## 9. Fase Maestros Finales

```bash
.venv/bin/python scripts/core/sync_final.py
```

Copia PNG y carpetas HTML a `Maestros Finales/`. No copia `*_old.png` y elimina los que ya existan en destino.

---

## 10. Fase Markdown

Los Markdown viven en `Maestros Finales/<carpeta idioma>/*.md`.

```bash
# Ver perfiles disponibles
.venv/bin/python run_pipeline.py --list

# Traducir todos los perfiles
.venv/bin/python run_pipeline.py

# Traducir solo un perfil
.venv/bin/python run_pipeline.py --only "EN -> DE"
```

Perfiles actuales: `ES → EN`, `EN → PT_BR`, `EN → IT`, `ES → FR`, `EN → DE`.

---

## 11. Orden completo recomendado

Ejemplo para actualizar alemán desde HTML español y Markdown inglés:

```bash
# 1) Aplicar traducciones oficiales del producto
.venv/bin/python scripts/core/apply_language_pack.py --lang DE --target-json de.json

# 2) Inicializar carpetas HTML destino
.venv/bin/python scripts/core/goalbus_localize.py init Español --target DE

# 3) Extraer vocabulario de UI nuevo
.venv/bin/python scripts/core/goalbus_localize.py extract Español

# 4) Exportar, completar e importar pendientes de UI
.venv/bin/python scripts/core/goalbus_localize.py translate --from ES --to DE --export pending_DE.tsv
# ... completar TSV ...
.venv/bin/python scripts/core/goalbus_localize.py translate --import pending_DE.tsv --to DE

# 5) Construir HTML finales
.venv/bin/python scripts/core/goalbus_localize.py build_all --from ES --to DE

# 6) Verificar estado
.venv/bin/python scripts/core/goalbus_localize.py status --lang DE

# 7) Generar imágenes
.venv/bin/python scripts/core/capture_scope.py Deutsch

# 8) Copiar a Maestros Finales
.venv/bin/python scripts/core/sync_final.py

# 9) Traducir Markdown
.venv/bin/python run_pipeline.py --only "EN -> DE"
```

---

## 12. Checklist antes de subir a GitHub

```bash
.venv/bin/python scripts/core/goalbus_localize.py status --lang DE
.venv/bin/python scripts/core/capture_screenshots.py status Deutsch
.venv/bin/python scripts/core/sync_final.py
git status --porcelain
```

Revisa:

- No hay `*_old.png` en `Maestros Finales`.
- Las capturas no muestran textos en el idioma incorrecto.
- Los formularios no muestran `field_id` como valor visible.
- `translation_data.csv` no tiene columnas destino con huecos accidentales.

---

## 13. Problemas comunes

| Problema | Causa probable | Solución |
|---|---|---|
| Sale texto en inglés dentro de una imagen destino | Falta traducción en `global_translations.json` o `translation_data.csv` | Rellena el valor y ejecuta `build_all`, luego recaptura. |
| Un formulario muestra `vehicleTypeName` o `capacity` | HTML destino no fue reconstruido después de editar CSV | Ejecuta `build_all --from ES --to <IDIOMA>` y recaptura. |
| La captura sale cortada | `selector.json` apunta a un elemento incompleto | Ajusta `viewport_width`, `bbox_mode` y `padding`. |
| Playwright no abre Chromium | Falta instalar navegador | Ejecuta `python -m playwright install chromium`. |
| `torch` no existe | Dependencias de Markdown no instaladas | Ejecuta `pip install -r requirements_translation.txt`. |
| Texto de tooltip sigue en español en idioma destino | `pre_capture_js` tiene comillas dobles dentro del selector CSS | Usar `querySelectorAll('[transloco="clave"]')` con comillas simples externas. |

---

## 14. Inteligencia Semántica con CodeGraph

El repositorio incluye la carpeta `.codegraph/` con configuración del índice semántico. La base de datos local `codegraph.db` está en `.gitignore`; cada desarrollador genera su propio índice la primera vez.

```bash
# Inicializar e indexar
npx -y @colbymchenry/codegraph init -i

# Verificar estado
npx @colbymchenry/codegraph status

# Sincronizar cambios
npx @colbymchenry/codegraph sync

# Iniciar como servidor MCP (para Claude Code / Cursor)
npx @colbymchenry/codegraph serve
```

---

## 15. Publicación

```bash
git add -A
git commit -m "Update localized documentation"
git push origin main
```
