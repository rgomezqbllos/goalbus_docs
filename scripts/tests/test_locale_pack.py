"""Smoke tests for scripts/locale_pack.py.

Run with:  python scripts/test_locale_pack.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "core"))

from locale_pack import (  # noqa: E402
    LANG_TO_FILE,
    build_reverse_index,
    load_pack,
    lookup_by_key,
    lookup_by_text,
    normalize_placeholders,
    pack_health,
)


def _ok(name: str) -> None:
    print(f"  PASS  {name}")


def _fail(name: str, detail: str) -> None:
    print(f"  FAIL  {name}: {detail}")
    raise SystemExit(1)


def test_packs_load() -> None:
    for lang in LANG_TO_FILE:
        pack = load_pack(lang)
        # fr.json is known to be a stub; everything else should be populated
        if lang == "fr":
            continue
        if len(pack) < 100:
            _fail("test_packs_load", f"{lang} has only {len(pack)} entries")
    _ok("test_packs_load")


def test_reverse_index_es_finds_known_value() -> None:
    pack_es = load_pack("es")
    if not pack_es:
        _fail("test_reverse_index_es_finds_known_value", "es.json is empty")
    sample_key = next(iter(pack_es))
    sample_val = pack_es[sample_key]
    index = build_reverse_index("es")
    found_key = index.get(_norm(sample_val))
    if not found_key:
        _fail(
            "test_reverse_index_es_finds_known_value",
            f"value {sample_val!r} for key {sample_key!r} not in reverse index",
        )
    _ok("test_reverse_index_es_finds_known_value")


def _norm(t: str) -> str:
    from locale_pack import _normalize_text  # type: ignore

    return _normalize_text(t)


def test_lookup_es_to_de_known_term() -> None:
    # Pick a key present in both es.json and de.json
    pack_es = load_pack("es")
    pack_de = load_pack("de")
    common_keys = [k for k in pack_es if k in pack_de and pack_es[k].strip() and pack_de[k].strip()]
    if not common_keys:
        _fail("test_lookup_es_to_de_known_term", "no common keys ES↔DE")
    key = common_keys[0]
    es_val = pack_es[key]
    de_val = pack_de[key]
    res = lookup_by_text(es_val, src_lang="es", target_lang="de")
    if res.is_orphan:
        _fail(
            "test_lookup_es_to_de_known_term",
            f"orphan for ES={es_val!r} (expected DE={de_val!r})",
        )
    if res.text.strip().lower() != normalize_placeholders(de_val).strip().lower():
        _fail(
            "test_lookup_es_to_de_known_term",
            f"got {res.text!r}, expected {de_val!r}",
        )
    _ok("test_lookup_es_to_de_known_term")


def test_lookup_falls_back_to_en_when_target_missing() -> None:
    # Pick a key present in ES and EN but absent in IT (IT pack has fewer entries).
    pack_es = load_pack("es")
    pack_en = load_pack("en")
    pack_it = load_pack("it")
    candidates = [
        k for k in pack_es
        if k in pack_en
        and k not in pack_it
        and pack_es[k].strip()
        and pack_en[k].strip()
    ]
    if not candidates:
        _fail(
            "test_lookup_falls_back_to_en_when_target_missing",
            "no ES↔EN key absent from IT",
        )
    key = candidates[0]
    res = lookup_by_text(pack_es[key], src_lang="es", target_lang="it")
    if res.source not in ("fallback:en", "fallback:es"):
        _fail(
            "test_lookup_falls_back_to_en_when_target_missing",
            f"expected fallback, got {res.source} (key={key!r}, text={res.text!r})",
        )
    _ok("test_lookup_falls_back_to_en_when_target_missing")


def test_orphan_for_unknown_text() -> None:
    res = lookup_by_text(
        "zzz_this_text_definitely_not_in_any_pack_zzz",
        src_lang="es",
        target_lang="de",
    )
    if not res.is_orphan:
        _fail("test_orphan_for_unknown_text", f"expected orphan, got {res}")
    _ok("test_orphan_for_unknown_text")


def test_normalize_placeholders() -> None:
    cases = [
        ("Hallo {name}", "Hallo {{name}}"),
        ("Hi {{name}}", "Hi {{name}}"),
        ("{a} and {{b}}", "{{a}} and {{b}}"),
        ("no placeholders", "no placeholders"),
    ]
    for src, expected in cases:
        got = normalize_placeholders(src)
        if got != expected:
            _fail("test_normalize_placeholders", f"{src!r} → {got!r}, expected {expected!r}")
    _ok("test_normalize_placeholders")


def test_lookup_by_key_direct() -> None:
    pack_de = load_pack("de")
    if not pack_de:
        _fail("test_lookup_by_key_direct", "de.json empty")
    key = next(iter(pack_de))
    res = lookup_by_key(key, target_lang="de")
    if res.source != "pack:de" or not res.text:
        _fail("test_lookup_by_key_direct", f"got {res}")
    _ok("test_lookup_by_key_direct")


def test_pack_health_reports_counts() -> None:
    h = pack_health("de")
    if h["entries"] < 100:
        _fail("test_pack_health_reports_counts", f"de has {h['entries']} entries")
    _ok("test_pack_health_reports_counts")


def main() -> int:
    print("locale_pack smoke tests:")
    test_packs_load()
    test_reverse_index_es_finds_known_value()
    test_lookup_es_to_de_known_term()
    test_lookup_falls_back_to_en_when_target_missing()
    test_orphan_for_unknown_text()
    test_normalize_placeholders()
    test_lookup_by_key_direct()
    test_pack_health_reports_counts()
    print("All tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
