#!/usr/bin/env python3
"""
GoalBus Screenshot Capture Tool
================================
Abre archivos HTML locales guardados desde el navegador y captura
elementos específicos como imágenes PNG usando Playwright.

Cada carpeta de imagen (ej: P2_imagen1/) debe contener:
  - Un archivo HTML (GoalBus.html o GoalBus Settings.html)
  - Un archivo selector.json que define QUÉ capturar

Uso:
  # Capturar UNA imagen específica:
  python capture_screenshots.py Español/P6/P6_imagen1

  # Capturar todas las imágenes de una página:
  python capture_screenshots.py Español/P6

  # Capturar TODO un idioma:
  python capture_screenshots.py Español

  # Capturar TODO (todos los idiomas):
  python capture_screenshots.py --all

  # Ver qué capturaría sin ejecutar:
  python capture_screenshots.py Español/P6 --dry-run

  # Especificar viewport personalizado:
  python capture_screenshots.py Español/P6/P6_imagen1 --width 1920 --height 1080
"""

import json
import os
import sys
import glob
import argparse
from pathlib import Path
from html.parser import HTMLParser

# Evita UnicodeEncodeError en consolas Windows con codificación heredada.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ─── Configuración ──────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent  # Raíz del proyecto (goalbus_docs/)
DEFAULT_VIEWPORT_WIDTH = 1920
DEFAULT_VIEWPORT_HEIGHT = 1080
SELECTOR_FILENAME = "selector.json"
HTML_FILENAMES = ["GoalBus.html", "GoalBus Settings.html"]  # Busca en este orden

# Carpetas de idioma conocidas (se detectan automáticamente, esto es solo referencia)
LANGUAGE_FOLDERS = ["Español", "Portugues"]
IGNORED_CLASS_PREFIXES = ("ng-", "_ng", "cdk-", "mapboxgl-")
IGNORED_CLASSES = {
    "ng-star-inserted",
    "gs-text-ellipsis",
}


class HtmlNode:
    """Nodo HTML mínimo para inferir selectores a partir de un fragmento."""

    def __init__(self, tag: str, attrs: list[tuple[str, str | None]], parent=None):
        self.tag = tag.lower()
        self.attrs = {k.lower(): (v or "") for k, v in attrs}
        self.parent = parent
        self.children: list["HtmlNode"] = []
        self.text_parts: list[str] = []

    @property
    def text_content(self) -> str:
        return " ".join(" ".join(self.text_parts).split()).strip()


class SnippetParser(HTMLParser):
    """Parser sencillo para convertir un snippet HTML en un árbol navegable."""

    VOID_TAGS = {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr",
    }

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = HtmlNode("document", [])
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = HtmlNode(tag, attrs, self.stack[-1])
        self.stack[-1].children.append(node)
        if tag.lower() not in self.VOID_TAGS:
            self.stack.append(node)

    def handle_endtag(self, tag):
        tag = tag.lower()
        for idx in range(len(self.stack) - 1, 0, -1):
            if self.stack[idx].tag == tag:
                del self.stack[idx:]
                break

    def handle_data(self, data):
        text = " ".join(data.split())
        if text:
            self.stack[-1].text_parts.append(text)


def walk_nodes(node: HtmlNode):
    """Recorre recursivamente un árbol HTML."""
    for child in node.children:
        yield child
        yield from walk_nodes(child)


def stable_classes(node: HtmlNode) -> list[str]:
    """Devuelve solo clases suficientemente estables para construir selectores."""
    class_attr = node.attrs.get("class", "")
    classes = []
    for cls in class_attr.split():
        if not cls or cls in IGNORED_CLASSES:
            continue
        if cls.startswith(IGNORED_CLASS_PREFIXES):
            continue
        classes.append(cls)
    return classes


def short_text(text: str, limit: int = 80) -> str | None:
    """Normaliza textos cortos útiles para :has-text()."""
    normalized = " ".join(text.split()).strip()
    if not normalized or len(normalized) > limit:
        return None
    return normalized


def css_text_literal(text: str) -> str:
    """Escapa texto para usarlo dentro de :has-text('...')."""
    return text.replace("\\", "\\\\").replace("'", "\\'")


def child_anchor_selector(node: HtmlNode) -> str | None:
    """Genera una ancla interna útil para :has(...) si existe un hijo estable."""
    for child in node.children:
        qa_id = child.attrs.get("data-qa-id") or child.attrs.get("gsqaid")
        if qa_id:
            return f"{child.tag}[data-qa-id='{qa_id}']"

        child_classes = stable_classes(child)
        if child_classes:
            return f"{child.tag}.{'.'.join(child_classes[:2])}"

        child_text = short_text(child.text_content, limit=50)
        if child_text:
            return f"{child.tag}:has-text('{css_text_literal(child_text)}')"
    return None


def describe_node(node: HtmlNode) -> str:
    """Crea una descripción legible a partir del nodo objetivo."""
    text = short_text(node.text_content, limit=100)
    if text:
        return text

    for child in node.children:
        child_text = short_text(child.text_content, limit=100)
        if child_text:
            return child_text

    qa_id = node.attrs.get("data-qa-id") or node.attrs.get("gsqaid")
    if qa_id:
        return f"Elemento {qa_id}"

    classes = stable_classes(node)
    if node.tag == "body":
        return "Página completa"
    if classes:
        return f"Elemento {classes[0]}"

    return f"Elemento {node.tag}"


def infer_selector_candidates(node: HtmlNode) -> list[str]:
    """Construye una lista ordenada de selectores candidatos para el nodo."""
    candidates: list[str] = []
    tag = node.tag
    qa_id = node.attrs.get("data-qa-id")
    legacy_qa = node.attrs.get("gsqaid")
    classes = stable_classes(node)
    text = short_text(node.text_content)

    if tag == "body":
        candidates.append("body")

    if qa_id:
        candidates.append(f"{tag}[data-qa-id='{qa_id}']")
        candidates.append(f"[data-qa-id='{qa_id}']")

    if legacy_qa and not qa_id:
        candidates.append(f"{tag}[gsqaid='{legacy_qa}']")
        candidates.append(f"[gsqaid='{legacy_qa}']")

    if tag in {"body", "main", "header", "article", "section", "button"} or "-" in tag:
        candidates.append(tag)

    if classes:
        class_selector = f"{tag}.{'.'.join(classes[:2])}"
        anchor = child_anchor_selector(node)
        if anchor:
            candidates.append(f"{class_selector}:has({anchor})")

        candidates.append(class_selector)

        if text:
            candidates.append(f"{class_selector}:has-text('{css_text_literal(text)}')")

    if text and tag != "body":
        candidates.append(f"{tag}:has-text('{css_text_literal(text)}')")

    unique_candidates = []
    seen = set()
    for candidate in candidates:
        if candidate not in seen:
            unique_candidates.append(candidate)
            seen.add(candidate)
    return unique_candidates


def extract_primary_node(snippet: str) -> HtmlNode | None:
    """Obtiene el primer nodo real de un fragmento HTML."""
    parser = SnippetParser()
    parser.feed(snippet)
    for node in walk_nodes(parser.root):
        if node.tag != "document":
            return node
    return None


def load_snippet_from_args(args) -> str | None:
    """Lee el snippet desde argumento, fichero o stdin."""
    if getattr(args, "snippet", None):
        return args.snippet
    if getattr(args, "snippet_file", None):
        return Path(args.snippet_file).read_text(encoding="utf-8")
    if getattr(args, "stdin", False):
        return sys.stdin.read()
    return None


def write_selector_config(image_folder: Path, config: dict):
    """Escribe selector.json en la carpeta de imagen."""
    config_path = image_folder / SELECTOR_FILENAME
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        f.write("\n")


def cmd_suggest(args):
    """Sugiere o crea selector.json a partir de un fragmento HTML."""
    folders = discover_image_folders(args.target)
    if not folders:
        print("No se encontró la carpeta de imagen objetivo.")
        return
    image_folder = folders[0]["image_folder"]

    snippet = load_snippet_from_args(args)
    if not snippet or not snippet.strip():
        print("❌ Debes proporcionar un fragmento HTML con --snippet, --snippet-file o --stdin.")
        return

    node = extract_primary_node(snippet)
    if not node:
        print("❌ No se pudo detectar un nodo HTML en el fragmento proporcionado.")
        return

    selector_candidates = infer_selector_candidates(node)
    if not selector_candidates:
        print("❌ No pude inferir un selector razonable para ese fragmento.")
        return

    config = {
        "selector": selector_candidates[0],
        "description": args.description or describe_node(node),
        "padding": args.padding,
    }

    if args.write:
        write_selector_config(image_folder, config)
        print(f"✅ selector.json actualizado en: {image_folder / SELECTOR_FILENAME}")

    print("\nSelector propuesto:")
    print(json.dumps(config, indent=2, ensure_ascii=False))

    if len(selector_candidates) > 1:
        print("\nAlternativas:")
        for candidate in selector_candidates[1:6]:
            print(f"  - {candidate}")


def find_html_file(image_folder: Path) -> Path | None:
    """Busca el archivo HTML principal dentro de una carpeta de imagen."""
    for name in HTML_FILENAMES:
        candidate = image_folder / name
        if candidate.exists():
            return candidate
    # Fallback: buscar cualquier .html que NO esté en _files
    for f in image_folder.glob("*.html"):
        if "_files" not in f.name and "_test" not in f.name:
            return f
    return None


def load_selector_config(image_folder: Path) -> dict | None:
    """
    Lee el archivo selector.json de una carpeta de imagen.

    Formato esperado de selector.json:
    {
        "selector": "div.configuration__card",
        "description": "Card de Gestión de Días Tipo",
        "padding": 10,
        "wait_for": "networkidle",
        "viewport_width": 1920,
        "viewport_height": 1080
    }

    Campos obligatorios: selector
    Campos opcionales: description, padding, wait_for, viewport_width, viewport_height
    """
    config_path = image_folder / SELECTOR_FILENAME
    if not config_path.exists():
        return None

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        if "selector" not in config:
            print(f"  ⚠️  {config_path}: Falta el campo 'selector'")
            return None

        return config
    except json.JSONDecodeError as e:
        print(f"  ❌ Error leyendo {config_path}: {e}")
        return None


def discover_image_folders(target_path: str) -> list[dict]:
    """
    Descubre las carpetas de imagen a procesar según el argumento dado.

    Acepta:
      - "Español/P6/P6_imagen1"  → una imagen específica
      - "Español/P6"             → todas las imágenes de P6
      - "Español"                → todas las imágenes de Español
      - "--all"                  → todo

    Retorna lista de dicts con: language, page, image_name, image_folder
    """
    full_path = BASE_DIR / target_path
    results = []

    if not full_path.exists():
        print(f"❌ Ruta no encontrada: {full_path}")
        return results

    # Caso 1: Es una carpeta de imagen directa (contiene HTML)
    html = find_html_file(full_path)
    if html:
        parts = Path(target_path).parts
        if len(parts) >= 3:
            results.append({
                "language": parts[0],
                "page": parts[1],
                "image_name": parts[2],
                "image_folder": full_path,
            })
        return results

    # Caso 2: Es una carpeta de página (P6/) o idioma (Español/)
    # Buscar subcarpetas que contengan HTMLs
    for root, dirs, files in os.walk(full_path):
        # Excluir carpetas de assets (_files) y ocultas
        dirs[:] = [d for d in dirs if not d.endswith("_files") and not d.startswith(".")]
        root_path = Path(root)
        html = find_html_file(root_path)
        if html:
            try:
                rel = root_path.relative_to(BASE_DIR)
                parts = rel.parts
                if len(parts) >= 3:
                    results.append({
                        "language": parts[0],
                        "page": parts[1],
                        "image_name": parts[2],
                        "image_folder": root_path,
                    })
            except ValueError:
                continue

    return sorted(results, key=lambda x: (x["language"], x["page"], x["image_name"]))


def discover_all_folders() -> list[dict]:
    """Descubre TODAS las carpetas de imagen en todos los idiomas."""
    results = []
    for lang_dir in BASE_DIR.iterdir():
        if lang_dir.is_dir() and not lang_dir.name.startswith(".") and lang_dir.name != "scripts":
            # Verificar que parece un directorio de idioma (contiene carpetas P#)
            has_pages = any(d.name.startswith("P") and d.name[1:].isdigit()
                          for d in lang_dir.iterdir() if d.is_dir())
            if has_pages:
                results.extend(discover_image_folders(lang_dir.name))
    return results


async def capture_element(
    page,
    html_path: Path,
    selector: str,
    output_path: Path,
    padding: int = 0,
    wait_for: str = "load",
):
    """
    Abre un HTML local en Playwright y captura un elemento como PNG.

    Args:
        page: Playwright page object
        html_path: Ruta al archivo HTML local
        selector: CSS selector del elemento a capturar
        output_path: Ruta donde guardar el PNG
        padding: Píxeles de padding alrededor del elemento
        wait_for: Estrategia de espera ("load", "domcontentloaded", "networkidle")
    """
    file_url = html_path.resolve().as_uri()

    await page.goto(file_url, wait_until=wait_for, timeout=30000)

    # Esperar un momento para que se renderice todo
    await page.wait_for_timeout(500)

    # Intentar encontrar el elemento
    try:
        element = page.locator(selector).first
        await element.wait_for(state="visible", timeout=10000)
    except Exception as e:
        print(f"    ❌ No se encontró el elemento con selector: {selector}")
        print(f"       Error: {e}")
        return False

    # Crear directorio de salida si no existe
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if padding > 0:
        # Capturar con padding: obtener bounding box y hacer screenshot de área
        box = await element.bounding_box()
        if box:
            await page.screenshot(
                path=str(output_path),
                clip={
                    "x": max(0, box["x"] - padding),
                    "y": max(0, box["y"] - padding),
                    "width": box["width"] + padding * 2,
                    "height": box["height"] + padding * 2,
                },
            )
        else:
            await element.screenshot(path=str(output_path))
    else:
        await element.screenshot(path=str(output_path))

    return True


async def run_captures(folders: list[dict], viewport_w: int, viewport_h: int, dry_run: bool = False):
    """Ejecuta las capturas para todas las carpetas descubiertas."""
    from playwright.async_api import async_playwright

    if not folders:
        print("No se encontraron carpetas de imagen para procesar.")
        return

    # Filtrar solo las que tienen selector.json
    tasks = []
    skipped_no_selector = 0
    skipped_no_html = 0

    for folder_info in folders:
        image_folder = folder_info["image_folder"]
        config = load_selector_config(image_folder)

        if not config:
            skipped_no_selector += 1
            continue

        html_path = find_html_file(image_folder)
        if not html_path:
            skipped_no_html += 1
            print(f"  ⚠️  {folder_info['image_name']}: No se encontró archivo HTML")
            continue

        # La imagen se guarda en la carpeta padre (P6/) con el nombre de la imagen
        output_path = image_folder.parent / f"{folder_info['image_name']}.png"

        tasks.append({
            **folder_info,
            "config": config,
            "html_path": html_path,
            "output_path": output_path,
        })

    # Resumen
    print(f"\n{'='*60}")
    print(f"  GoalBus Screenshot Capture")
    print(f"{'='*60}")
    print(f"  Total carpetas encontradas:    {len(folders)}")
    print(f"  Con selector.json configurado: {len(tasks)}")
    print(f"  Sin selector.json (omitidas):  {skipped_no_selector}")
    print(f"  Sin archivo HTML (omitidas):   {skipped_no_html}")
    print(f"  Viewport: {viewport_w}x{viewport_h}")
    print(f"{'='*60}\n")

    if dry_run:
        print("🔍 MODO DRY-RUN (no se capturarán imágenes):\n")
        for task in tasks:
            desc = task["config"].get("description", "Sin descripción")
            print(f"  📷 {task['language']}/{task['page']}/{task['image_name']}")
            print(f"     Selector: {task['config']['selector']}")
            print(f"     Descripción: {desc}")
            print(f"     HTML: {task['html_path'].name}")
            print(f"     Salida: {task['output_path']}")
            print()
        return

    # Ejecutar capturas con Playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        success = 0
        failed = 0

        for task in tasks:
            config = task["config"]

            # Viewport por captura o global
            vw = config.get("viewport_width", viewport_w)
            vh = config.get("viewport_height", viewport_h)

            context = await browser.new_context(
                viewport={"width": vw, "height": vh},
                device_scale_factor=2,  # Retina para mejor calidad
            )
            page = await context.new_page()

            print(f"  📷 Capturando {task['language']}/{task['page']}/{task['image_name']}...")

            ok = await capture_element(
                page=page,
                html_path=task["html_path"],
                selector=config["selector"],
                output_path=task["output_path"],
                padding=config.get("padding", 0),
                wait_for=config.get("wait_for", "load"),
            )

            if ok:
                success += 1
                print(f"    ✅ Guardado: {task['output_path'].name}")
            else:
                failed += 1

            await context.close()

        await browser.close()

        print(f"\n{'='*60}")
        print(f"  Resultado: {success} capturadas, {failed} fallidas")
        print(f"{'='*60}\n")


def generate_selector_template(image_folder: Path):
    """Genera un archivo selector.json plantilla en una carpeta de imagen."""
    config_path = image_folder / SELECTOR_FILENAME
    if config_path.exists():
        print(f"  ℹ️  Ya existe: {config_path}")
        return

    template = {
        "selector": "EDITAR_AQUÍ",
        "description": "Describir qué se captura aquí",
        "padding": 0,
    }

    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(template, f, indent=2, ensure_ascii=False)

    print(f"  📝 Creado: {config_path}")


def cmd_init(args):
    """Genera selector.json en todas las carpetas que no lo tengan."""
    if args.all_targets:
        folders = discover_all_folders()
    else:
        folders = discover_image_folders(args.target)

    if not folders:
        print("No se encontraron carpetas de imagen.")
        return

    created = 0
    for folder_info in folders:
        config_path = folder_info["image_folder"] / SELECTOR_FILENAME
        if not config_path.exists():
            generate_selector_template(folder_info["image_folder"])
            created += 1

    print(f"\n✅ Se crearon {created} archivos selector.json (de {len(folders)} carpetas)")
    print(f"   Ahora edita cada selector.json con el CSS selector correcto.")
    print(f"   Consulta el README.md para ejemplos de selectores.")


def cmd_status(args):
    """Muestra el estado de configuración de cada carpeta."""
    if args.all_targets:
        folders = discover_all_folders()
    else:
        folders = discover_image_folders(args.target)

    if not folders:
        print("No se encontraron carpetas de imagen.")
        return

    configured = 0
    pending = 0

    for folder_info in folders:
        config = load_selector_config(folder_info["image_folder"])
        html = find_html_file(folder_info["image_folder"])

        status_html = "✅" if html else "❌"

        if config and config["selector"] != "EDITAR_AQUÍ":
            status_sel = "✅"
            configured += 1
        elif config:
            status_sel = "⏳"
            pending += 1
        else:
            status_sel = "❌"
            pending += 1

        name = f"{folder_info['language']}/{folder_info['page']}/{folder_info['image_name']}"
        sel_text = config["selector"][:50] if config else "—"
        print(f"  {status_html} HTML  {status_sel} Selector  {name}  →  {sel_text}")

    print(f"\n  Total: {len(folders)} | Configurados: {configured} | Pendientes: {pending}")


def main():
    parser = argparse.ArgumentParser(
        description="GoalBus Screenshot Capture Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  %(prog)s capture Español/P6/P6_imagen1     Captura una imagen específica
  %(prog)s capture Español/P6                 Captura todas las imágenes de P6
  %(prog)s capture Español                    Captura todo el idioma Español
  %(prog)s capture --all                      Captura todo
  %(prog)s capture Español/P6 --dry-run       Vista previa sin capturar
  %(prog)s init Español/P6                    Crea selector.json en carpetas de P6
  %(prog)s init --all                         Crea selector.json en todas las carpetas
  %(prog)s status --all                       Muestra estado de configuración
  %(prog)s suggest Portugues/P2/P2_imagen1 --stdin --write
                                              Sugiere selector.json desde un snippet HTML
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Comando a ejecutar")

    # Comando: capture
    cap_parser = subparsers.add_parser("capture", help="Capturar screenshots")
    cap_parser.add_argument("target", nargs="?", default=None,
                           help="Ruta: Idioma/Página/Imagen, Idioma/Página, o Idioma")
    cap_parser.add_argument("--all", action="store_true", dest="all_targets",
                           help="Procesar todos los idiomas y carpetas")
    cap_parser.add_argument("--dry-run", action="store_true",
                           help="Solo mostrar qué se capturaría, sin ejecutar")
    cap_parser.add_argument("--width", type=int, default=DEFAULT_VIEWPORT_WIDTH,
                           help=f"Ancho del viewport (default: {DEFAULT_VIEWPORT_WIDTH})")
    cap_parser.add_argument("--height", type=int, default=DEFAULT_VIEWPORT_HEIGHT,
                           help=f"Alto del viewport (default: {DEFAULT_VIEWPORT_HEIGHT})")

    # Comando: init
    init_parser = subparsers.add_parser("init", help="Crear selector.json en carpetas")
    init_parser.add_argument("target", nargs="?", default=None,
                            help="Ruta objetivo")
    init_parser.add_argument("--all", action="store_true", dest="all_targets",
                            help="Procesar todas las carpetas")

    # Comando: status
    status_parser = subparsers.add_parser("status", help="Ver estado de configuración")
    status_parser.add_argument("target", nargs="?", default=None,
                              help="Ruta objetivo")
    status_parser.add_argument("--all", action="store_true", dest="all_targets",
                              help="Procesar todas las carpetas")

    # Comando: suggest
    suggest_parser = subparsers.add_parser("suggest", help="Inferir selector.json desde un snippet HTML")
    suggest_parser.add_argument("target", help="Ruta objetivo de una carpeta de imagen")
    suggest_parser.add_argument("--snippet", help="Fragmento HTML inline")
    suggest_parser.add_argument("--snippet-file", help="Archivo de texto/HTML con el fragmento")
    suggest_parser.add_argument("--stdin", action="store_true",
                               help="Leer el fragmento HTML desde stdin")
    suggest_parser.add_argument("--description", help="Descripción manual para selector.json")
    suggest_parser.add_argument("--padding", type=int, default=10,
                               help="Padding del selector sugerido (default: 10)")
    suggest_parser.add_argument("--write", action="store_true",
                               help="Escribir el selector sugerido en selector.json")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Validar que se proporcionó target o --all
    if hasattr(args, "all_targets"):
        if not args.all_targets and not args.target:
            print("❌ Debes proporcionar una ruta o usar --all")
            print("   Ejemplo: python capture_screenshots.py capture Español/P6")
            print("   Ejemplo: python capture_screenshots.py capture --all")
            return

    if args.command == "init":
        cmd_init(args)
    elif args.command == "status":
        cmd_status(args)
    elif args.command == "suggest":
        cmd_suggest(args)
    elif args.command == "capture":
        import asyncio

        if args.all_targets:
            folders = discover_all_folders()
        else:
            folders = discover_image_folders(args.target)

        asyncio.run(run_captures(folders, args.width, args.height, args.dry_run))


if __name__ == "__main__":
    main()
