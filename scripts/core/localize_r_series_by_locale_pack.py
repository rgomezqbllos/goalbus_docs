#!/usr/bin/env python3
"""
Localize selected screenshot series from the official locale packs.

This deliberately lets the per-language JSON files drive translation:
  - Source text is matched against es.json to obtain the semantic key.
  - Target text is read from the target locale pack only.
  - Missing target keys are left in Spanish and reported.
  - Operational identifiers/codes are preserved.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import shutil
import unicodedata
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent.parent
SOURCE_LANG_FOLDER = "Español"
TARGETS = {
    "EN": ("English", "en.json"),
    "PT_BR": ("Portugues", "pt_br.json"),
    "IT": ("Italiano", "it.json"),
    "DE": ("Deutsch", "de.json"),
    "FR": ("Frances", "fr.json"),
}
TARGET_GLOSSARY_OVERRIDES = {
    "PT_BR": {
        "Vazio": "Ocioso",
        "vazio": "ocioso",
        "VAZIO": "OCIOSO",
        "viagem ociosa": "ocioso externo",
        "Descanso": "refeição",
        "descanso": "refeição",
    }
}
MANUAL_TEXT_REPLACEMENTS = {
    "EN": {
        "Reglas de Notificaciones en Paradas": "Stop Notification Rules",
        "Crea, edita y gestiona Reglas para notificar acciones en Paradas.": "Create, edit and manage rules to notify actions at stops.",
        "Configuración Driver App": "Driver App Settings",
        "New Rule Model": "New Rule Model",
        "Reglas L5": "L5 Rules",
        "Reglas asignación": "Assignment Rules",
        "486982 Reglas asignación": "486982 Assignment Rules",
        "GRUPO DE TRABAJO T01": "WORKING GROUP T01",
        "TURNO T01": "SHIFT T01",
        "WORKING_GROUP:": "WORKING GROUP:",
        "DEPOT:": "DEPOT:",
        "APERTURA": "OPENING",
        "APERTURA -": "OPENING -",
        "GENERAL -": "GENERAL -",
        "Habili": "Enabled",
        "Día libre": "Day off",
        "Sin asignar": "Unassigned",
        "A órdenes": "On call",
        "Trabajando sin solape": "Working without overlap",
        "Errores": "Errors",
    },
    "PT_BR": {
        "Reglas de Notificaciones en Paradas": "Regras de Notificação em Paradas",
        "Crea, edita y gestiona Reglas para notificar acciones en Paradas.": "Crie, edite e gerencie regras para notificar ações em paradas.",
        "Configuración Driver App": "Configurações do Driver App",
        "New Rule Model": "Novo Modelo de Regra",
        "Reglas L5": "Regras L5",
        "Reglas asignación": "Regras de Atribuição",
        "486982 Reglas asignación": "486982 Regras de Atribuição",
        "GRUPO DE TRABAJO T01": "GRUPO DE TRABALHO T01",
        "TURNO T01": "TURNO T01",
        "WORKING_GROUP:": "GRUPO DE TRABALHO:",
        "DEPOT:": "DEPÓSITO:",
        "APERTURA": "ABERTURA",
        "APERTURA -": "ABERTURA -",
        "GENERAL -": "GERAL -",
        "Habili": "Habilitado",
        "Día libre": "Dia livre",
        "Sin asignar": "Não atribuído",
        "A órdenes": "À disposição",
        "Trabajando sin solape": "Trabalhando sem sobreposição",
        "Errores": "Erros",
    },
    "IT": {
        "Reglas de Notificaciones en Paradas": "Regole di Notifica alle Fermate",
        "Crea, edita y gestiona Reglas para notificar acciones en Paradas.": "Crea, modifica e gestisci regole per notificare azioni alle fermate.",
        "Configuración Driver App": "Configurazione Driver App",
        "New Rule Model": "Nuovo Modello Regola",
        "Reglas L5": "Regole L5",
        "Reglas asignación": "Regole di Assegnazione",
        "486982 Reglas asignación": "486982 Regole di Assegnazione",
        "GRUPO DE TRABAJO T01": "GRUPPO DI LAVORO T01",
        "TURNO T01": "TURNO T01",
        "WORKING_GROUP:": "GRUPPO DI LAVORO:",
        "DEPOT:": "DEPOSITO:",
        "APERTURA": "APERTURA",
        "APERTURA -": "APERTURA -",
        "GENERAL -": "GENERALE -",
        "Habili": "Abilitato",
        "Día libre": "Giorno libero",
        "Sin asignar": "Non assegnato",
        "A órdenes": "A disposizione",
        "Trabajando sin solape": "In servizio senza sovrapposizione",
        "Errores": "Errori",
    },
    "DE": {
        "Reglas de Notificaciones en Paradas": "Haltestellen-Benachrichtigungsregeln",
        "Crea, edita y gestiona Reglas para notificar acciones en Paradas.": "Erstellen, bearbeiten und verwalten Sie Regeln für Benachrichtigungen an Haltestellen.",
        "Configuración Driver App": "Driver-App-Einstellungen",
        "New Rule Model": "Neues Regelmodell",
        "Reglas L5": "L5-Regeln",
        "Reglas asignación": "Zuweisungsregeln",
        "486982 Reglas asignación": "486982 Zuweisungsregeln",
        "GRUPO DE TRABAJO T01": "ARBEITSGRUPPE T01",
        "TURNO T01": "SCHICHT T01",
        "WORKING_GROUP:": "ARBEITSGRUPPE:",
        "DEPOT:": "BETRIEBSHOF:",
        "APERTURA": "ERÖFFNUNG",
        "APERTURA -": "ERÖFFNUNG -",
        "GENERAL -": "ALLGEMEIN -",
        "Habili": "Aktiviert",
        "Día libre": "Freier Tag",
        "Sin asignar": "Nicht zugewiesen",
        "A órdenes": "Auf Abruf",
        "Trabajando sin solape": "Arbeitet ohne Überschneidung",
        "Errores": "Fehler",
    },
    "FR": {
        "Reglas de Notificaciones en Paradas": "Règles de Notification aux Arrêts",
        "Crea, edita y gestiona Reglas para notificar acciones en Paradas.": "Créez, modifiez et gérez des règles pour notifier les actions aux arrêts.",
        "Configuración Driver App": "Configuration Driver App",
        "New Rule Model": "Nouveau Modèle de Règle",
        "Reglas L5": "Règles L5",
        "Reglas asignación": "Règles d'Affectation",
        "486982 Reglas asignación": "486982 Règles d'Affectation",
        "GRUPO DE TRABAJO T01": "GROUPE DE TRAVAIL T01",
        "TURNO T01": "SERVICE T01",
        "WORKING_GROUP:": "GROUPE DE TRAVAIL :",
        "DEPOT:": "DÉPÔT :",
        "APERTURA": "OUVERTURE",
        "APERTURA -": "OUVERTURE -",
        "GENERAL -": "GÉNÉRAL -",
        "Habili": "Activé",
        "Día libre": "Jour libre",
        "Sin asignar": "Non affecté",
        "A órdenes": "Disponible",
        "Trabajando sin solape": "Travail sans chevauchement",
        "Errores": "Erreurs",
    },
}
SYNTHETIC_NAME_POOLS = {
    "EN": (["James", "Robert", "John", "Michael", "William", "David", "Richard", "Thomas"], ["Smith", "Johnson", "Brown", "Taylor", "Wilson", "Miller", "Davis", "Clark"]),
    "PT_BR": (["João", "Carlos", "Pedro", "Paulo", "Rafael", "Lucas", "Marcos", "André"], ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Costa", "Rodrigues", "Almeida"]),
    "IT": (["Marco", "Luca", "Giuseppe", "Antonio", "Francesco", "Andrea", "Matteo", "Giovanni"], ["Rossi", "Bianchi", "Russo", "Ferrari", "Esposito", "Romano", "Colombo", "Ricci"]),
    "DE": (["Thomas", "Michael", "Andreas", "Stefan", "Klaus", "Markus", "Peter", "Christian"], ["Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker"]),
    "FR": (["Jean", "Michel", "Pierre", "Alain", "Nicolas", "Laurent", "Christophe", "Julien"], ["Martin", "Bernard", "Dubois", "Thomas", "Richard", "Petit", "Durand", "Moreau"]),
}
SPECIFIC_NAME_REPLACEMENTS = {
    "EN": {
        "Nico Cadena": "Nick Carter",
        "Carlos Jimenez": "Charles Jenkins",
        "David Perez": "David Parker",
        "Pedro Rivas": "Peter Rivers",
        "Ricardo Flores": "Richard Flowers",
    },
    "PT_BR": {
        "Nico Cadena": "Nico Cardoso",
        "Carlos Jimenez": "Carlos Almeida",
        "David Perez": "Davi Pereira",
        "Pedro Rivas": "Pedro Ribeiro",
        "Ricardo Flores": "Ricardo Florêncio",
    },
    "IT": {
        "Nico Cadena": "Nico Conti",
        "Carlos Jimenez": "Carlo Galli",
        "David Perez": "Davide Parisi",
        "Pedro Rivas": "Pietro Riva",
        "Ricardo Flores": "Riccardo Fiore",
    },
    "DE": {
        "Nico Cadena": "Niklas Kramer",
        "Carlos Jimenez": "Karl Zimmermann",
        "David Perez": "David Peters",
        "Pedro Rivas": "Peter Reiter",
        "Ricardo Flores": "Richard Blum",
    },
    "FR": {
        "Nico Cadena": "Nicolas Caron",
        "Carlos Jimenez": "Charles Germain",
        "David Perez": "David Perrin",
        "Pedro Rivas": "Pierre Rivière",
        "Ricardo Flores": "Richard Fleury",
    },
}
SERIES_FOLDERS = [
    "R1/R1_imagen1",
    "R1/R1_imagen2",
    "R1/R1_imagen3",
    "R2/R2_imagen1",
    "R2/R2_imagen2",
    "R2/R2_imagen3",
    "R2/R2_imagen4",
    "R3/R3_imagen1",
    "R3/R3_imagen2",
    "R3/R3_imagen3",
    "R3/R3_imagen4",
    "R3/R3_imagen5",
    "R4/R4_imagen1",
    "R4/R4_imagen2",
    "R4/R4_imagen3",
    "R4/R4_imagen4",
    "R4/R4_imagen5",
    "R4/R4_imagen6",
    "R4/R4_imagen7",
    "R4/R4_imagen8",
    "R4/R4_imagen9",
    "R4/R4_imagen10",
    "R4/R4_imagen11",
    "R4/R4_imagen12",
    "O11/O11_Imagen1",
    "O11/O11_Imagen2",
    "O11/O11_Imagen3",
    "O12/O12_Imagen1",
    "O12/O12_Imagen2",
    "O12/O12_Imagen3",
]


PRESERVE_RE = re.compile(
    r"^(?:"
    r"GoalBus|SITEUR(?: GDL)? / Hola Consultant|C|TEST|"
    r"TEST GOAL(?: 2)?|T01 HSD SIN DESC|"
    r"Veh_\d+(?:-[A-Z0-9_]+)?|T\d+[A-Z]?|PKT\d+|:\s*(?:T\d+[A-Z]?|PKT|\d+(?:\.\d+)? km)|"
    r"\d+_\d+|\d+(?:\.\d+)?x \(\d+ h\)|"
    r"\d+ h|\d+ kWh|\d+(?:\.\d+)? km|\+1|"
    r"ELEC(?: .*)?|LUMINUS|DP TALLERES.*|DP TETLAN.*|PK TETLAN ELEC|"
    r"T\d+[- ][A-ZÁÉÍÓÚÑ]+|T\d+ .+-.+|Aeropuerto - .+|.+ - \d{2}:\d{2} to \d{2}:\d{2}"
    r")$"
)


class VisibleTextParser(HTMLParser):
    """Collect visible-ish text nodes for the saved GoalBus HTML."""

    SKIP = {"script", "style", "noscript", "template", "code"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.texts: list[str] = []

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag.lower())

    def handle_endtag(self, tag):
        tag = tag.lower()
        for idx in range(len(self.stack) - 1, -1, -1):
            if self.stack[idx] == tag:
                del self.stack[idx:]
                break

    def handle_data(self, data):
        if any(tag in self.SKIP for tag in self.stack):
            return
        text = " ".join(data.split()).strip()
        if text:
            self.texts.append(text)


def normalize(text: str) -> str:
    value = html.unescape(text or "")
    value = unicodedata.normalize("NFKC", value).strip().lower()
    return re.sub(r"\s+", " ", value)


def load_pack(filename: str) -> dict[str, str]:
    path = ROOT / filename
    data = json.loads(path.read_text(encoding="utf-8"))
    return {k: v for k, v in data.items() if isinstance(v, str)}


def load_driver_name_replacements(target_lang: str) -> dict[str, str]:
    lang_key = {
        "EN": "en",
        "PT_BR": "pt",
        "IT": "it",
        "DE": "de",
        "FR": "fr",
    }.get(target_lang)
    if not lang_key:
        return {}
    path = ROOT / "driver_names_localization.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    replacements: dict[str, str] = {}
    for item in data.get("name_mappings", []):
        source = item.get("es")
        target = item.get(lang_key)
        if isinstance(source, str) and isinstance(target, str) and source and target:
            replacements[source] = target
    return replacements


def build_synthetic_name_replacements(target_lang: str) -> dict[str, str]:
    replacements = dict(SPECIFIC_NAME_REPLACEMENTS.get(target_lang, {}))
    first_names, last_names = SYNTHETIC_NAME_POOLS.get(target_lang, SYNTHETIC_NAME_POOLS["EN"])
    for number in range(0, 1000):
        first = first_names[number % len(first_names)]
        last = last_names[(number // len(first_names)) % len(last_names)]
        replacements[f"Nombre{number} Apellido{number}"] = f"{first} {last}"
    return replacements


def build_reverse_index(pack: dict[str, str]) -> dict[str, str]:
    index: dict[str, str] = {}
    for key, value in pack.items():
        norm = normalize(value)
        if norm:
            index.setdefault(norm, key)
    return index


def resolve_translation(
    source_text: str,
    es_index: dict[str, str],
    target_lang: str,
    target_pack: dict[str, str],
    en_pack: dict[str, str],
) -> tuple[str | None, str, str]:
    """Resolve plain and small composed UI strings via locale-pack keys."""
    variants = [(source_text, "{target}")]
    stripped = source_text.strip()

    if stripped.startswith(":"):
        value = stripped[1:].strip()
        if value:
            variants.append((value, ": {target}"))

    if stripped.endswith(":"):
        value = stripped[:-1].strip()
        if value:
            variants.append((value, "{target} :"))

    if stripped.endswith(":") is False and stripped.endswith(" :"):
        value = stripped[:-2].strip()
        if value:
            variants.append((value, "{target} :"))

    prefix_match = re.match(r"^(.+?):\s*(\d+)$", stripped)
    if prefix_match:
        variants.append((prefix_match.group(1).strip(), "{target}: " + prefix_match.group(2)))

    minutes_match = re.match(r"^(\d+)\s+minutos$", stripped, flags=re.IGNORECASE)
    if minutes_match:
        variants.append(("minutos", minutes_match.group(1) + " {target}"))

    tooltip_minutes_match = re.match(r"^:\s*(\d+)\s+minutos$", stripped, flags=re.IGNORECASE)
    if tooltip_minutes_match:
        key = "common.minutes"
        target_text = target_pack.get(key) or en_pack.get(key, "")
        if target_text:
            status = "pack" if target_pack.get(key) else "fallback_en"
            return key, f": {tooltip_minutes_match.group(1)} {target_text}", status

    for candidate, template in variants:
        key = es_index.get(normalize(candidate))
        if not key:
            continue
        target_text = target_pack.get(key, "")
        if target_text:
            if "{{total}}" in target_text and prefix_match:
                target_text = target_text.replace("{{total}}", prefix_match.group(2))
            return key, template.format(target=target_text), "pack"
        target_text = en_pack.get(key, "")
        if target_text:
            if "{{total}}" in target_text and prefix_match:
                target_text = target_text.replace("{{total}}", prefix_match.group(2))
            return key, template.format(target=target_text), "fallback_en"
        return key, "", "missing_target"

    page_range_match = re.match(r"^(\d+\s*-\s*\d+)\s+de\s+(\d+)$", stripped, flags=re.IGNORECASE)
    if page_range_match:
        connector_by_lang = {
            "EN": "of",
            "PT_BR": "de",
            "IT": "di",
            "DE": "von",
            "FR": "sur",
        }
        connector = connector_by_lang.get(target_lang, "of")
        return "common.table.paginator.range", f"{page_range_match.group(1)} {connector} {page_range_match.group(2)}", "composed"

    paginator_count_match = re.match(r"^Resultados:\s*(\d+)$", stripped, flags=re.IGNORECASE)
    if paginator_count_match:
        key = "common.table.paginator.count"
        target_text = target_pack.get(key) or en_pack.get(key, "")
        if target_text:
            status = "pack" if target_pack.get(key) else "fallback_en"
            return key, target_text.replace("{{total}}", paginator_count_match.group(1)), status

    return None, "", ""


def collect_texts(html_path: Path) -> list[str]:
    parser = VisibleTextParser()
    parser.feed(html_path.read_text(encoding="utf-8", errors="replace"))
    seen: set[str] = set()
    result: list[str] = []
    for text in parser.texts:
        if len(text) > 120:
            continue
        if re.fullmatch(r"[\d\s:.,%_\-]+", text):
            continue
        if text not in seen:
            seen.add(text)
            result.append(text)
    return result


def replace_text(content: str, source: str, target: str) -> tuple[str, int]:
    if not source or source == target:
        return content, 0
    count = content.count(source)
    if not count:
        return content, 0
    return content.replace(source, target), count


def apply_target_glossary(target_lang: str, text: str) -> str:
    for source, target in TARGET_GLOSSARY_OVERRIDES.get(target_lang, {}).items():
        text = text.replace(source, target)
    return text


def apply_manual_text_replacements(target_lang: str, content: str) -> str:
    replacements = MANUAL_TEXT_REPLACEMENTS.get(target_lang, {})
    for source, target in sorted(replacements.items(), key=lambda item: len(item[0]), reverse=True):
        content, _ = replace_text(content, source, target)
    return content


def apply_composed_localization(target_lang: str, content: str) -> str:
    time_connector = {
        "EN": "to",
        "PT_BR": "a",
        "IT": "a",
        "DE": "bis",
        "FR": "à",
    }.get(target_lang, "to")
    date_connector = {
        "EN": "to",
        "PT_BR": "a",
        "IT": "a",
        "DE": "bis",
        "FR": "au",
    }.get(target_lang, "to")
    month = {
        "EN": "Jun",
        "PT_BR": "jun",
        "IT": "giu",
        "DE": "Jun",
        "FR": "juin",
    }.get(target_lang, "Jun")
    content = re.sub(r"(\d{2}:\d{2})\s+a\s+(\d{2}:\d{2})", rf"\1 {time_connector} \2", content)
    content = re.sub(r"(\d{2})\s+jun\s+a\s+(\d{2})\s+jun\s+(\d{4})", rf"\1 {month} {date_connector} \2 {month} \3", content)
    content = re.sub(r"jun\s+(\d+)º", rf"{month} \1", content)
    return content


def apply_synthetic_name_patterns(target_lang: str, content: str) -> str:
    first_names, last_names = SYNTHETIC_NAME_POOLS.get(target_lang, SYNTHETIC_NAME_POOLS["EN"])

    def replacement(match: re.Match[str]) -> str:
        number = int(match.group(1))
        first = first_names[number % len(first_names)]
        last = last_names[(number // len(first_names)) % len(last_names)]
        return f"{first} {last}"

    return re.sub(
        r"\b(?:Nombre|Nome|Name|Nom|Nome|Vorname)\s*(\d+)\s+"
        r"(?:Apellido|Sobrenome|Surname|Cognome|Nachname|Nom)\s*\1\b",
        replacement,
        content,
    )


def build_translation_rows(
    es_pack: dict[str, str],
    es_index: dict[str, str],
    target_lang: str,
    target_pack: dict[str, str],
    en_pack: dict[str, str],
    series_folders: list[str],
) -> tuple[list[dict[str, str]], dict[str, str]]:
    rows: list[dict[str, str]] = []
    replacements: dict[str, str] = {}

    source_root = ROOT / SOURCE_LANG_FOLDER
    for rel in series_folders:
        html_path = source_root / rel / "GoalBus.html"
        for source_text in collect_texts(html_path):
            key, target_text, status = resolve_translation(source_text, es_index, target_lang, target_pack, en_pack)
            if key:
                if target_text:
                    target_text = apply_target_glossary(target_lang, target_text)
                    replacements[source_text] = target_text
            elif PRESERVE_RE.match(source_text):
                status = "preserved"
                target_text = source_text
            else:
                status = "missing_source_key"
                target_text = source_text

            rows.append(
                {
                    "folder": rel.replace("/", "\\"),
                    "target_lang": target_lang,
                    "status": status,
                    "key": key or "",
                    "source_es": source_text,
                    "target": target_text,
                    "source_pack_value": es_pack.get(key or "", ""),
                }
            )
    return rows, replacements


def reset_target_dirs(target_folder: str, series_names: list[str]) -> None:
    def handle_remove_error(func, path, exc_info):
        try:
            os.chmod(path, 0o700)
            func(path)
        except OSError:
            raise

    for series in series_names:
        target_dir = ROOT / target_folder / series
        resolved = target_dir.resolve()
        expected_parent = (ROOT / target_folder).resolve()
        if not str(resolved).startswith(str(expected_parent)):
            raise RuntimeError(f"Refusing to delete unexpected path: {resolved}")
        if target_dir.exists():
            shutil.rmtree(target_dir, onerror=handle_remove_error)


def copy_source_tree(target_folder: str, series_names: list[str]) -> None:
    for series in series_names:
        src = ROOT / SOURCE_LANG_FOLDER / series
        if not src.exists():
            continue
        dst = ROOT / target_folder / series
        shutil.copytree(src, dst)
        for old_png in dst.glob("*_old.png"):
            old_png.unlink()
        for selector_path in dst.glob("R*_imagen*/selector.json"):
            config = json.loads(selector_path.read_text(encoding="utf-8"))
            config["selectors"] = [
                "otto-web-grid-header"
                if isinstance(selector, str) and selector.startswith("otto-web-grid-header")
                else selector
                for selector in config.get("selectors", [])
            ]
            selector_path.write_text(
                json.dumps(config, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )


def localize_html(
    target_folder: str,
    target_lang: str,
    replacements: dict[str, str],
    name_replacements: dict[str, str],
    series_folders: list[str],
) -> None:
    generated_name_replacements = build_synthetic_name_replacements(target_lang)
    for rel in series_folders:
        html_path = ROOT / target_folder / rel / "GoalBus.html"
        content = html_path.read_text(encoding="utf-8", errors="replace")
        for source, target in sorted(replacements.items(), key=lambda item: len(item[0]), reverse=True):
            content, _ = replace_text(content, source, target)
        content = apply_manual_text_replacements(target_lang, content)
        content = apply_composed_localization(target_lang, content)
        for source, target in sorted(name_replacements.items(), key=lambda item: len(item[0]), reverse=True):
            content, _ = replace_text(content, source, target)
        for source, target in sorted(generated_name_replacements.items(), key=lambda item: len(item[0]), reverse=True):
            content, _ = replace_text(content, source, target)
        content = apply_synthetic_name_patterns(target_lang, content)
        html_path.write_text(content, encoding="utf-8")


def write_report(rows: list[dict[str, str]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "folder",
                "target_lang",
                "status",
                "key",
                "source_es",
                "target",
                "source_pack_value",
            ],
            delimiter="\t",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--targets", default="EN,PT_BR,IT,DE,FR")
    parser.add_argument("--report", default="scratch/r_series_locale_pack_report.tsv")
    parser.add_argument(
        "--series",
        default="",
        help="Comma-separated top-level series to process, e.g. R3,R4. Defaults to all configured series.",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    es_pack = load_pack("es.json")
    en_pack = load_pack("en.json")
    es_index = build_reverse_index(es_pack)
    all_rows: list[dict[str, str]] = []
    selected_series = [item.strip() for item in args.series.split(",") if item.strip()]
    selected_folders = [
        rel for rel in SERIES_FOLDERS
        if not selected_series or rel.split("/", 1)[0] in selected_series
    ]
    selected_top_series = sorted({rel.split("/", 1)[0] for rel in selected_folders})

    for lang in [item.strip().upper() for item in args.targets.split(",") if item.strip()]:
        if lang not in TARGETS:
            raise SystemExit(f"Unknown target: {lang}")
        target_folder, filename = TARGETS[lang]
        target_pack = load_pack(filename)
        name_replacements = load_driver_name_replacements(lang)
        rows, replacements = build_translation_rows(
            es_pack,
            es_index,
            lang,
            target_pack,
            en_pack,
            selected_folders,
        )
        all_rows.extend(rows)
        if not args.dry_run:
            reset_target_dirs(target_folder, selected_top_series)
            copy_source_tree(target_folder, selected_top_series)
            localize_html(target_folder, lang, replacements, name_replacements, selected_folders)
        counts: dict[str, int] = {}
        for row in rows:
            counts[row["status"]] = counts.get(row["status"], 0) + 1
        print(f"{lang}: {counts}")

    write_report(all_rows, ROOT / args.report)
    print(f"Report: {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
