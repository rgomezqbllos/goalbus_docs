# GoalBus Screenshot Capture Tool

Herramienta para capturar automáticamente screenshots de elementos específicos
desde los archivos HTML guardados localmente de GoalBus.

## Requisitos

```bash
pip install playwright
playwright install chromium
```

## Estructura de carpetas

```
goalbus_docs/
├── Español/
│   ├── P2/
│   │   ├── P2_imagen1/
│   │   │   ├── GoalBus.html          ← HTML guardado del navegador
│   │   │   ├── GoalBus_files/        ← Assets del HTML
│   │   │   └── selector.json         ← ⭐ Qué capturar (TÚ LO CONFIGURAS)
│   │   ├── P2_imagen2/
│   │   │   ├── GoalBus.html
│   │   │   ├── GoalBus_files/
│   │   │   └── selector.json
│   │   ├── P2_imagen1.png            ← 📸 Salida generada automáticamente
│   │   └── P2_imagen2.png
│   ├── P6/
│   │   └── ...
├── Portugues/
│   └── ...
└── scripts/
    └── capture_screenshots.py
```

## Cómo funciona

1. **Guardas la página web** desde el navegador (Ctrl+S → "Página completa")
   en la carpeta correspondiente (ej: `Español/P6/P6_imagen1/GoalBus.html`)

2. **Creas un `selector.json`** en la misma carpeta indicando QUÉ parte de
   la página quieres capturar

3. **Ejecutas el script** y genera el PNG automáticamente

## El archivo `selector.json`

Este es el archivo clave. Vive dentro de cada carpeta de imagen y le dice
al script qué elemento HTML capturar.

### Formato

```json
{
  "selector": "CSS_SELECTOR_AQUÍ",
  "description": "Descripción para recordar qué es",
  "padding": 10
}
```

### Campos

| Campo              | Obligatorio | Descripción                                      |
|--------------------|-------------|--------------------------------------------------|
| `selector`         | ✅ Sí       | CSS selector del elemento a capturar             |
| `description`      | No          | Nota para recordar qué captura esta imagen       |
| `padding`          | No          | Píxeles de margen extra alrededor (default: 0)   |
| `viewport_width`   | No          | Ancho del viewport para esta captura (def: 1920) |
| `viewport_height`  | No          | Alto del viewport para esta captura (def: 1080)  |
| `wait_for`         | No          | Esperar: "load", "domcontentloaded", "networkidle"|

---

## Guía de selectores CSS para GoalBus

La web de GoalBus usa componentes Angular con prefijos `gs-` y `otto-web-`.
Aquí están las estrategias para escribir selectores correctos:

### 1. Usar `data-qa-id` (⭐ LA MEJOR OPCIÓN)

Muchos elementos tienen un atributo `data-qa-id` que es estable y único:

```json
{"selector": "[data-qa-id='toolBarActionButton']"}
{"selector": "[data-qa-id='createParkingForm']"}
{"selector": "[data-qa-id='backButton']"}
{"selector": "[data-qa-id='openSidebar']"}
{"selector": "[data-qa-id='planning']"}
{"selector": "[data-qa-id='configureTenant']"}
```

**Cómo encontrarlo**: Busca `data-qa-id="..."` o `gsqaid="..."` en el HTML.
El valor de `gsqaid` se convierte en `data-qa-id` en el DOM.

### 2. Usar tags de componentes personalizados

Los componentes de GoalBus usan tags únicos:

```json
{"selector": "gs-modal"}
{"selector": "otto-web-create-parking"}
{"selector": "otto-web-tool-bar"}
{"selector": "gs-stepper"}
{"selector": "otto-web-info-routes"}
{"selector": "otto-web-side-panel"}
{"selector": "gs-header"}
```

### 3. Usar clases CSS

Para elementos que usan clases específicas del diseño:

```json
{"selector": "div.configuration__card"}
{"selector": "article.info_routes"}
{"selector": "section.content_header"}
{"selector": "div.create-parking__form"}
{"selector": "article.content_stops"}
```

### 4. Combinar selectores (para ser más preciso)

Cuando hay múltiples elementos similares, combina selectores:

```json
{"selector": "div.configuration__card:has(header:text('Gestión de Días'))"}
{"selector": "gs-modal:has(div:text('Nuevo Parking'))"}
{"selector": "button.gs-button:has(span:text('Nuevo Parking'))"}
{"selector": "[data-qa-id='toolBarActionButton']:has-text('Nuevo Parking')"}
```

### 5. Usar nth-child para elementos repetidos

Si hay varias cards iguales y quieres una específica:

```json
{"selector": "div.configuration__card:nth-of-type(1)"}
{"selector": "div.configuration__card:nth-of-type(3)"}
```

### 6. Capturar la página completa

Para capturar todo el body visible:

```json
{"selector": "body"}
```

Para capturar solo el contenido principal (sin header):

```json
{"selector": "main.layout__main"}
```

---

## Ejemplos reales por tipo de captura

### Card de configuración (como "Gestión de Días Tipo")

```json
{
  "selector": "div.configuration__card:has(header.configuration__card__title)",
  "description": "Card de configuración con icono y botón",
  "padding": 10
}
```

Si hay varias cards y quieres una específica por su texto:

```json
{
  "selector": "div.configuration__card:has(:text('Gestión de Días'))",
  "description": "Card de Gestión de Días Tipo y Festivos",
  "padding": 10
}
```

### Botón específico

```json
{
  "selector": "[data-qa-id='toolBarActionButton']",
  "description": "Botón 'Nuevo Parking' en la toolbar",
  "padding": 5
}
```

### Modal / Popup

```json
{
  "selector": "gs-modal",
  "description": "Modal de creación de Nuevo Parking",
  "padding": 0
}
```

### Formulario dentro de un modal

```json
{
  "selector": "gs-modal gs-form",
  "description": "Formulario de creación de parking",
  "padding": 10
}
```

### Header de la aplicación

```json
{
  "selector": "gs-header section.header",
  "description": "Barra superior con logo y navegación",
  "padding": 0
}
```

### Menú lateral (side panel)

```json
{
  "selector": "otto-web-side-panel",
  "description": "Panel lateral de navegación",
  "padding": 0
}
```

### Página completa sin header

```json
{
  "selector": "main.layout__main",
  "description": "Contenido principal de la página",
  "padding": 0
}
```

### Toolbar con botones de toggle

```json
{
  "selector": "otto-web-tool-bar",
  "description": "Barra de herramientas con filtros y acciones",
  "padding": 0
}
```

---

## Cómo encontrar el selector correcto

### Método rápido (recomendado)

1. Abre el HTML en tu navegador (doble clic en GoalBus.html)
2. Haz clic derecho en el elemento que quieres capturar → **Inspeccionar**
3. En DevTools, mira el elemento y busca:
   - ¿Tiene `data-qa-id`? → Usa `[data-qa-id='valor']`
   - ¿Es un componente custom (`gs-*`, `otto-web-*`)? → Usa el tag directamente
   - ¿Tiene una clase descriptiva? → Usa `.la-clase`

### Método para verificar tu selector

En la consola del navegador (F12 → Console), escribe:

```javascript
document.querySelector('TU_SELECTOR_AQUI')
```

Si devuelve el elemento correcto, ese es tu selector. Si devuelve `null`,
el selector no funciona.

Para ver cuántos elementos coinciden:

```javascript
document.querySelectorAll('TU_SELECTOR_AQUI').length
```

---

## Comandos del script

### Capturar screenshots

```bash
# Una imagen específica
python scripts/capture_screenshots.py capture Español/P6/P6_imagen1

# Todas las imágenes de una página
python scripts/capture_screenshots.py capture Español/P6

# Todo un idioma
python scripts/capture_screenshots.py capture Español

# Todo
python scripts/capture_screenshots.py capture --all

# Vista previa (no captura, solo muestra qué haría)
python scripts/capture_screenshots.py capture Español/P6 --dry-run

# Con viewport personalizado
python scripts/capture_screenshots.py capture Español --width 1440 --height 900
```

### Crear selector.json vacíos

```bash
# En todas las carpetas que no tengan selector.json
python scripts/capture_screenshots.py init --all

# Solo en carpetas de una página específica
python scripts/capture_screenshots.py init Español/P6
```

### Ver estado

```bash
# Ver qué carpetas tienen selector.json configurado
python scripts/capture_screenshots.py status --all
```

### Sugerir selector.json desde un snippet HTML

```bash
# Pegar un fragmento HTML largo por stdin y escribir selector.json
python scripts/capture_screenshots.py suggest Portugues/P2/P2_imagen1 --stdin --write

# O cargar el fragmento desde un fichero
python scripts/capture_screenshots.py suggest Portugues/P2/P2_imagen1 --snippet-file snippet.html --write
```

La heurística prioriza, por este orden:

1. `data-qa-id`
2. `gsqaid`
3. tags de componentes (`gs-*`, `otto-web-*`, `body`)
4. clases estables del diseño
5. anclas internas con `:has(...)` o `:has-text(...)`

---

## Tips

- Los atributos `_ngcontent-ng-c...` cambian entre builds de Angular.
  **NUNCA los uses en selectores**, no son estables.

- Si tu selector necesita capturar un elemento que contiene texto específico,
  Playwright soporta `:has-text('texto')` y `:text('texto')`.

- El campo `padding` es útil para botones o elementos pequeños que necesitan
  un poco de espacio alrededor.

- Usa `"wait_for": "networkidle"` si la página carga recursos lentamente.

- Si una página tiene temas claro/oscuro, el HTML guardado mantiene el tema
  que estaba activo al guardar.

---

## Modo Agente (Iteración PX_imagenN)

Para trabajar con un agente reutilizable en este repo:

1. Reglas del agente:
   - `AGENTS.md` (raíz del proyecto)
2. Prompt base para inicializar otro agente:
   - `scripts/AGENT_CAPTURE_PROMPT.md`
3. Wrapper de ejecución por objetivo:
   - `scripts/agent_capture_px.sh`

Uso rápido:

```bash
./scripts/agent_capture_px.sh Español/P7/P7_imagen8
```

Esto ejecuta:

```bash
.venv/bin/python scripts/capture_screenshots.py capture Español/P7/P7_imagen8
```
