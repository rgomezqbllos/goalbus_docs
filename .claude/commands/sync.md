# /sync

Sincroniza imágenes y HTML a `Maestros Finales/` y opcionalmente hace commit + push a GitHub.

## Uso

```
/sync [--lang idioma] [--serie serie] [--git] [--git-message "mensaje"]
```

**Ejemplos:**
- `/sync` — sincroniza todos los idiomas a Maestros Finales
- `/sync --lang English` — sincroniza solo English
- `/sync --serie R3` — sincroniza solo la serie R3 de todos los idiomas
- `/sync --git` — sincroniza y hace commit + push con mensaje automático
- `/sync --git --git-message "Add R3 English screenshots"` — mensaje de commit personalizado

## Comportamiento

### Sincronización a Maestros Finales
```bash
python scripts/sync_final.py
```

Copia:
- PNG desde `Idioma/Serie/` → `Maestros Finales/<NombreCarpeta>/Serie/`
- Carpetas `Serie_imagenN/` completas (HTML + assets + selector.json)
- Ignora y elimina `*_old.png` en destino

Mapa de carpetas destino:

| Idioma    | Carpeta en Maestros Finales         |
|-----------|-------------------------------------|
| Español   | `Archivos Maestros (ES)/`           |
| English   | `Master Files (EN)/`                |
| Deutsch   | `Master Files (DE)/`                |
| Frances   | `Fichiers Maîtres (FR)/`            |
| Italiano  | `Archivi Maestri (IT)/`             |
| Portugues | `Arquivos Mestres (PT_BR)/`         |

### Con `--git`
Después de sincronizar:
1. Muestra resumen de archivos modificados (`git status`)
2. Stage de los archivos relevantes (excluye carpetas de idioma e imágenes según `.gitignore`)
3. Commit con mensaje descriptivo
4. Push a `origin main`

## Checklist pre-sync (verificación automática)

Antes de sincronizar, el skill verifica:
- [ ] No hay `*_old.png` sueltos en las carpetas de idioma
- [ ] Todos los PNG tienen su carpeta `Serie_imagenN/` correspondiente
- [ ] No hay carpetas vacías sin PNG ni HTML

Si alguna verificación falla, reporta el problema sin sincronizar.

## Notas

- `Maestros Finales/` y las carpetas de idioma están en `.gitignore`, por lo que `--git` solo commitea scripts, JSONs y configuración
- Si se quiere subir el contenido de Maestros Finales, debe hacerse manualmente o ajustar el `.gitignore`
