# GoalBus Localization Tool (`goalbus_localize.py`)

Esta herramienta permite traducir automáticamente los archivos HTML guardados de GoalBus (screenshots) a cualquier idioma, manteniendo el diseño y los datos, pero traduciendo la interfaz (labels, botones, placeholders).

## Flujo de Trabajo (Paso a Paso)

Si necesitas generar un reporte en un nuevo idioma (ej: Inglés) basándote en el de Español, sigue estos pasos:

### 1. Inicializar las carpetas
Crea la estructura de carpetas en el idioma destino copiando los archivos fuente (HTML, assets, etc.).
```bash
python scripts/goalbus_localize.py init Español/O2 --target EN
```
*Esto creará la carpeta `English/O2` con todo lo necesario.*

### 2. Extraer vocabulario pendiente
Escanea el HTML en busca de textos en español que no estén en la base de datos de traducciones.
```bash
python scripts/goalbus_localize.py extract Español/O2
```
*Los nuevos términos aparecerán como `PENDING` en `global_translations.json`.*

### 3. Traducir (Manual o con IA)
Si no tienes a la IA disponible para hacerlo por ti, puedes hacerlo manualmente así:

**A) Exportar a un archivo de texto:**
```bash
python scripts/goalbus_localize.py translate --from ES --to EN --export pending_en.tsv
```

**B) Traducir el archivo:**
Abre `pending_en.tsv` (es un archivo separado por tabuladores, puedes usar Excel o un editor de texto). Rellena la columna de la derecha (`EN`) con las traducciones.

**C) Importar las traducciones:**
```bash
python scripts/goalbus_localize.py translate --import pending_en.tsv --to EN
```

### 4. Construir el HTML localizado
Aplica las traducciones del JSON a los archivos HTML de la carpeta destino.
```bash
python scripts/goalbus_localize.py build English/O2 --from ES
```
*Esto sobreescribirá los `GoalBus.html` en `English/O2` con los textos traducidos.*

### 5. Generar las capturas
Una vez que el HTML está en inglés, ejecuta el motor de capturas normal.
```bash
python scripts/capture_screenshots.py capture English/O2
```

---

## Comandos Útiles

| Acción | Comando |
|--------|---------|
| **Ver estado** | `python scripts/goalbus_localize.py status --lang EN` |
| **Re-construir todo** | `python scripts/goalbus_localize.py build_all --to EN` |
| **Ayuda** | `python scripts/goalbus_localize.py --help` |

## Notas Importantes
- **Traducciones Técnicas:** Intenta mantener la consistencia con los términos de GoalBus (ej: usar *Duty* en lugar de *Task* si así lo prefiere el cliente).
- **Global vs UI Strings:** La herramienta usa `global_translations.json` para el contenido dinámico del DOM y `ui_strings.json` para textos específicos del reporte.
- **Limpieza:** Si el HTML original tiene basura o datos sensibles, la herramienta intenta limpiar los nodos invisibles durante la extracción.
