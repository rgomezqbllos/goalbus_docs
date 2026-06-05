# /translate-pending

Detecta y resuelve traducciones pendientes (`PENDING`) en `global_translations.json` para uno o más idiomas.

## Uso

```
/translate-pending [--lang idioma] [--scope serie] [--auto]
```

**Ejemplos:**
- `/translate-pending` — lista todos los PENDING en todos los idiomas
- `/translate-pending --lang Deutsch` — muestra PENDING solo para alemán
- `/translate-pending --lang Deutsch --scope R4` — PENDING relevantes para la serie R4
- `/translate-pending --lang Deutsch --auto` — traduce automáticamente usando los packs oficiales de idioma

## Comportamiento

### Sin `--auto` (modo inspección)
1. Lee `global_translations.json` y cuenta entradas con valor `PENDING` por idioma
2. Cruza con los HTML de `--scope` (si se indica) para filtrar solo los PENDING que afectan esa serie
3. Muestra tabla:

```
Idioma   | PENDING | Afecta scope R4
---------|---------|----------------
Deutsch  |   47    |      12
Frances  |   23    |       8
Italiano |   31    |      10
```

4. Ofrece opciones:
   - Exportar TSV para edición manual
   - Resolver automáticamente con pack oficial (`--auto`)

### Con `--auto`
1. Para cada entrada `PENDING` del idioma indicado:
   a. Busca el texto ES en el pack oficial (`es.json`) → obtiene la clave
   b. Busca esa clave en el pack del idioma destino (`de.json`)
   c. Si la encuentra → reemplaza `PENDING` con la traducción oficial
   d. Si no → deja `PENDING` y lo reporta como no resuelto
2. Reporta: N resueltos, M sin resolver con sus textos

## Códigos de idioma → archivos de pack

| Idioma    | Pack oficial |
|-----------|-------------|
| English   | `en.json`   |
| Deutsch   | `de.json`   |
| Frances   | `fr.json`   |
| Italiano  | `it.json`   |
| Portugues | `pt_br.json`|

## Notas

- Después de resolver PENDING, ejecutar `/localize <serie> --step build` para reconstruir los HTML
- Los packs oficiales no cubren el 100% de los textos (algunos son propios de las pantallas de configuración)
- Para textos no cubiertos por el pack, la traducción debe hacerse manualmente editando `global_translations.json`
- El campo `_match` en cada entrada indica cómo fue detectado el texto: `tag`, `attr:placeholder`, `attr:title`, etc.
