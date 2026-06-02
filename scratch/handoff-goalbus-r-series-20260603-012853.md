# Handoff: GoalBus R1/R2 Locale-Pack Screenshot Flow

Generated: 2026-06-03 local time

## Next-Session Focus
Continue or review the GoalBus `R1/R2` multilingual screenshot workflow. The latest strategy is to regenerate destination-language folders from `Español` using official locale-pack JSON files as the source of truth, with `en.json` fallback when a target language lacks a key/value.

## Current State
The user deleted all non-Spanish language folders and asked to regenerate them from the latest strategy. This was completed for `English`, `Portugues`, `Italiano`, `Deutsch`, and `Frances`.

For each target language, `R1` and `R2` were recreated from `Español`, localized using the locale packs, and screenshots were captured. Final verification showed 7 PNGs per language, no copied `_old.png` files in target languages, and no small/bad images by dimension check.

## Decisions and Constraints
The authoritative translation source is now the per-language JSON pack at repo root: `en.json`, `pt_br.json`, `it.json`, `de.json`, `fr.json`.

Fallback rule: if a semantic key exists in `es.json` but is missing/empty in the target language pack, use `en.json`.

Preserve operational data/codes rather than translating them: examples include `Veh_1`, `T01`, `T01A`, `PKT01`, route IDs like `6576_1`, `kWh`, `h`, vehicle type codes, and depot/location codes.

`fr.json` currently has very low coverage, so most French R1/R2 UI strings fall back to English. This is expected under the current user rule.

Selectors copied from Spanish must not depend on Spanish header text. The localizer normalizes `otto-web-grid-header:has-text(...)` to `otto-web-grid-header` in target language folders.

The worktree has unrelated existing deletions/changes elsewhere in the repo. Do not revert unrelated files.

## Artifacts to Reference
- `C:\tmp\Proyectos\goalbus_docs\scripts\localize_r_series_by_locale_pack.py`: new generator/auditor for R1/R2 locale-pack-driven localization.
- `C:\tmp\Proyectos\goalbus_docs\scratch\r_series_locale_pack_report.tsv`: generated key/value report showing `pack`, `fallback_en`, and `preserved` statuses.
- `C:\tmp\Proyectos\goalbus_docs\Español\R1` and `C:\tmp\Proyectos\goalbus_docs\Español\R2`: Spanish source HTML, selectors, and `_old.png` references.
- Target folders regenerated: `English/R1`, `English/R2`, `Portugues/R1`, `Portugues/R2`, `Italiano/R1`, `Italiano/R2`, `Deutsch/R1`, `Deutsch/R2`, `Frances/R1`, `Frances/R2`.

## Suggested Skills
- `handoff`: Use again if the next session needs another compact continuation note.
- `browser:control-in-app-browser`: Useful if the next agent needs visual/local web verification beyond static PNG inspection.
- `spreadsheets:Spreadsheets`: Useful if the TSV report needs richer filtering, QA tables, or workbook export.

## Next Actions
1. If continuing QA, open `scratch\r_series_locale_pack_report.tsv` and review fallback-heavy languages, especially `FR`, `IT`, and `DE`.
2. If the user provides a fuller `fr.json`, rerun:
   `python scripts\localize_r_series_by_locale_pack.py --targets FR --report scratch\r_series_locale_pack_report.tsv`
   then capture `Frances/R1` and `Frances/R2`.
3. If terminology needs adjustment, prefer updating the official language JSON or adding a deliberate override mechanism to the script, rather than ad hoc HTML replacement.
4. Re-run capture after any translation changes:
   `python scripts\capture_screenshots.py capture <Language>/R1`
   `python scripts\capture_screenshots.py capture <Language>/R2`
5. Keep `_old.png` only in `Español` as references unless the user explicitly wants old references in target languages.

## Open Questions
- Should `fr.json` be replaced with a full official French locale pack? Current French output falls back mostly to English by design.
- Should location names such as `Aeropuerto - Expo GDL` remain operational proper nouns, or should future workflow support translating route/place display names from another source?

## Verification
Commands completed successfully:
- `scripts\localize_r_series_by_locale_pack.py --targets EN,PT_BR,IT,DE,FR --report scratch\r_series_locale_pack_report.tsv`
- Captures for all target language R1/R2 folders.

Final dimension/count check showed:
- `English`: 7 PNG, 0 `_old.png`, 0 small/bad
- `Portugues`: 7 PNG, 0 `_old.png`, 0 small/bad
- `Italiano`: 7 PNG, 0 `_old.png`, 0 small/bad
- `Deutsch`: 7 PNG, 0 `_old.png`, 0 small/bad
- `Frances`: 7 PNG, 0 `_old.png`, 0 small/bad

Known gap: visual QA was sampled earlier, but not every final image was individually inspected after the last regeneration.
