# GoalBus DOM Localization Pipeline

Este repositorio maneja la localización nativa (HTML/DOM) de los componentes y pantallas de la plataforma GoalBus. En lugar de editar imágenes de forma manual, reconstruimos las vistas renderizando el código HTML real y traduciendo sus textos y datos mediante un flujo automatizado en Python.

## Descripción de la Arquitectura

El ecosistema de localización se apoya en 3 pilares fundamentales:

1.  **`global_translations.json`**: Es el **Diccionario Maestro**. Aquí se almacenan todas las traducciones estáticas de la interfaz de usuario que no cambian (ej. Pestañas, Headers, Botones como "Guardar" o textos de navegación). Alimenta a todo el sistema por igual.
2.  **`translation_data.csv`**: Es la **Base de Datos Dinámica**. Guarda los valores específicos (ej. "Días Úteis", "1 Selecionado") que van "dentro" de los formularios, tablas y checkboxes (*casillas `<input>`, `<gs-select>`, `<gs-checkbox>`*). Se organiza por carpeta (`folder`), identificador (`field_id`) e idiomas (`ES`, `PT_BR`).
3.  **`scripts/goalbus_localize.py`**: Es el **Motor CLI**. Se encarga de hacer el "trabajo pesado": escanea HTMLs, crea directorios en idiomas destino, inyecta traducciones y sincroniza la data en todos los archivos.

---

## Flujo de Trabajo (Paso a Paso)

### Paso 1: Preparación de Nuevo Componente
Cuando necesites localizar una nueva pantalla (por ejemplo, la **P2_imagen6**):
1.  Descarga o copia el código HTML original y sus dependencias (carpeta `_files`).
2.  Pega ese contenido dentro de su respectiva ruta de origen, por ejemplo: `Español/P2/P2_imagen6/`.

### Paso 2: Inicialización (Auto-Escaneo)
En tu terminal, ejecuta el comando "init" apuntando a la carpeta que acabas de subir:

```bash
python3 scripts/goalbus_localize.py init Español/P2/P2_imagen6
```

**¿Qué hace esto?**
*   Crea la carpeta equivalente en el idioma destino (`Portugues/P2/P2_imagen6`).
*   Analiza el HTML y detecta todos los formularios interactivos vacíos.
*   Añade automáticamente las filas vacías para esta imagen en `translation_data.csv`.

### Paso 3: Entrada de Datos
1.  Abre el archivo `translation_data.csv`.
2.  Busca las nuevas filas que corresponden a tu imagen (ej. `P2_imagen6`).
3.  Rellena manualmente los valores bajo la columna origen (`ES`) y la columna destino (`PT_BR`) con los "datos de ejemplo" que deseas mostrar en la foto de esa pantalla.
4.  *(Opcional)* Si ves algún texto de fondo (como un menú nuevo) que aún no está siendo traducido, agrégalo permanentemente al `global_translations.json`.

### Paso 4: Extracción de Vocabulario (Auto-Mapeo)
Si la página tiene textos nuevos en el fondo (menús, etiquetas fijas, botones) que no aparecen traducidos, usa el motor de extracción:

```bash
python3 scripts/goalbus_localize.py extract Español/P2/P2_imagen6
```

**¿Qué hace esto?**
*   Escanea el HTML buscando todos los textos visibles.
*   Compara contra el diccionario global.
*   Si encuentra palabras nuevas, las inyecta en `global_translations.json` marcadas como `"PENDING"`.

### Paso 5: Construcción y Renderizado
Para inyectar todos los datos estructurados y traducciones en el código HTML:

**Opción A (Solo una carpeta)**:
```bash
python3 scripts/goalbus_localize.py build Portugues/P2/P2_imagen6
```

**Opción B (Reconstrucción Global - RECOMENDADA)**:
```bash
python3 scripts/goalbus_localize.py build_all
```

---

## 🤖 Guía para Asistentes de IA (Universal)

Si eres una IA ayudando en este proyecto, sigue este protocolo para garantizar resultados perfectos:

1.  **Mantenimiento del Diccionario**: Cuando el usuario ejecute `extract`, verás que el archivo `global_translations.json` se llena de valores `"PENDING"`. **Tu tarea es leer ese archivo y reemplazar todos los "PENDING" por sus traducciones reales y correctas** (por defecto al Portugués de Brasil `PT_BR`), manteniendo el formato `>Texto<`.
2.  **Mantenimiento de Datos (CSV)**: Al ejecutar `init`, el archivo `translation_data.csv` capturará los campos de formulario. Ayuda al usuario a rellenar las columnas `ES` y `PT_BR` con datos realistas para que las capturas de pantalla se vean "vivas".
3.  **Recursividad P***: El script está diseñado para trabajar con cualquier raíz `P1`, `P2`, `P3`, etc. No asumas que todo está en `P2`.
4.  **Idempotencia**: Siempre que hagas cambios en el CSV o JSON, ejecuta `python3 scripts/goalbus_localize.py build_all` para refrescar todo el repositorio.

---

---

## Capturas y Revisiones Finales
Abre el archivo `.html` resultante en tu navegador de preferencia. Notarás que el formulario ya incluye los datos que propusiste y la interfaz respeta el idioma meta con una fidelidad visual perfecta (CSS intacto). Procede a tomar tu captura de pantalla para la documentación oficial.
