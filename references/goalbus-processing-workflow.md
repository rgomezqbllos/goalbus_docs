# GoalBus Processing Workflow Reference

## Inputs

Accept paths in these forms:
- `Español/R4`
- `Español/R4/R4_imagen5`
- `R4` with source language defaulting to `Español`
- Multiple folders separated by spaces or new lines

Resolve each to actual image folders containing local HTML and/or `selector.json`. If a top-level series folder is provided, process all direct `*_imagenN` folders with matching `_old.png` references.

## Preflight Commands

Use the repo Python runtime when `.venv` is absent:

```powershell
$py = "C:\Users\rgomez\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
Test-Path scripts\capture_screenshots.py
Test-Path scripts\localize_r_series_by_locale_pack.py
Test-Path driver_names_localization.json
Get-ChildItem -Filter *.json
```

Find candidate HTML and references:

```powershell
rg --files "Español\R4"
Get-ChildItem -Recurse "Español\R4" -Filter "*_old.png"
```

## Old PNG Normalization

Only rename source reference PNGs that do not already end in `_old.png`.

Rules:
- Never overwrite an existing `_old.png`.
- If both `imagen.png` and `imagen_old.png` exist, leave both and report the conflict.
- Preserve generated target language PNGs unless the user explicitly requested cleanup.

## Selector Creation

Inspect the HTML before editing:

```powershell
rg -n "data-qa-id|gsqaid|ruleModel|otto-web|gs-" "Español\R4\R4_imagen5"
```

Typical `selector.json` shape:

```json
{
  "selectors": [
    "[data-qa-id='stable-root']",
    "otto-web-grid-row[data-row-id='...']"
  ],
  "bbox_mode": "smart",
  "padding": 12,
  "viewport_width": 1600,
  "viewport_height": 1100
}
```

For dropdowns/tooltips:

```json
{
  "selectors": [
    "[data-qa-id='ruleModelId']",
    ".cdk-overlay-pane"
  ],
  "pre_capture_js": "(() => { const field = document.querySelector('[data-qa-id=\"ruleModelId\"]'); field?.click(); })();",
  "bbox_mode": "smart",
  "padding": 16
}
```

For highlighted blue rectangles, create or preserve the visual marker in `pre_capture_js` by anchoring to a stable target element:

```json
{
  "pre_capture_js": "(() => { const target = document.querySelector('[data-qa-id=\"target-info\"]'); if (!target) return; const r = target.getBoundingClientRect(); const box = document.createElement('div'); Object.assign(box.style, { position:'fixed', left:`${r.left-4}px`, top:`${r.top-4}px`, width:`${r.width+8}px`, height:`${r.height+8}px`, border:'3px solid #0b72ff', pointerEvents:'none', zIndex:'999999' }); document.body.appendChild(box); })();"
}
```

## Capture Commands

Single image folder:

```powershell
& $py scripts\capture_screenshots.py capture "Español\R4\R4_imagen5"
```

Series folder:

```powershell
& $py scripts\capture_screenshots.py capture "Español\R4"
```

Dry run:

```powershell
& $py scripts\capture_screenshots.py capture "Español\R4\R4_imagen5" --dry-run
```

## Localization

Prefer the repo localization script:

```powershell
& $py scripts\localize_r_series_by_locale_pack.py --series R3,R4
```

If the requested series is not configured, patch the script narrowly to include it or add a scoped runner following the same language-pack logic. Do not hard-code visible translations into HTML unless the language JSON files cannot express that string; if hard-coding is unavoidable, record it in the run log.

Language-pack contract:
- Spanish source text -> key through `es.json`
- Target text -> target JSON
- Missing target -> English fallback
- Names -> `driver_names_localization.json`
- Portuguese terminology -> `ocioso` and `refeição`

## Verification Checklist

For every processed image:
- Current source PNG exists and lines up with `_old.png`.
- Target language PNGs exist for English, Portuguese, Italian, German, and French.
- Dimensions match the old image unless a requested fix intentionally changes the crop.
- Required header/sidebar/toolbar/buttons/links/dropdowns/blue marks are visible.
- Disabled save/cancel/edit controls are not cropped when the old image shows them.
- No source-language labels remain in translated captures, except stable codes or intentionally preserved technical identifiers.
- Portuguese does not show `Vazio`, `Vazia`, or `Descanso` when those should be `Ocioso` or `Refeição`.

Finish with a compact Spanish summary and include the run evidence path.
