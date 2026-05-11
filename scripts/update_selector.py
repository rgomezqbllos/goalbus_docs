import json

pre_capture_js = """async () => {
  // 1. Stop Angular CDK by replacing the viewport with a static clone
  const viewport = document.querySelector('cdk-virtual-scroll-viewport');
  if (viewport) {
    const newViewport = viewport.cloneNode(true);
    viewport.parentNode.replaceChild(newViewport, viewport);
  }

  // 2. Clean up rows
  const allRows = Array.from(document.querySelectorAll('otto-web-grid-row'));
  const targetPlates = ['0026-LFX', '0027-LFX', '0028-LFX'];
  
  allRows.forEach(row => {
    const isTarget = targetPlates.some(plate => row.textContent.includes(plate));
    if (!isTarget) {
      row.remove();
    } else {
      // Remove CDK translation
      row.style.transform = 'none';
      row.style.position = 'relative';
      row.style.top = '0';
    }
  });

  // 3. Reset the wrapper so remaining rows stack normally
  const wrapper = document.querySelector('.cdk-virtual-scroll-content-wrapper');
  if (wrapper) {
    wrapper.style.transform = 'none';
    wrapper.style.position = 'relative';
    wrapper.style.top = '0';
    wrapper.style.display = 'flex';
    wrapper.style.flexDirection = 'column';
  }
}"""

selector_json = {
  "selectors": [
    "otto-web-grid-header > div:nth-child(1)",
    "otto-web-grid-header > div:nth-child(2)",
    "otto-web-grid-row:has-text('0026-LFX') > div:nth-child(1)",
    "otto-web-grid-row:has-text('0026-LFX') > div:nth-child(2)",
    "otto-web-grid-row:has-text('0027-LFX') > div:nth-child(1)",
    "otto-web-grid-row:has-text('0027-LFX') > div:nth-child(2)",
    "otto-web-grid-row:has-text('0028-LFX') > div:nth-child(1)",
    "otto-web-grid-row:has-text('0028-LFX') > div:nth-child(2)"
  ],
  "description": "Cabecero y filas 0026, 0027, 0028 nativos (aislados de CDK)",
  "padding": 0,
  "viewport_width": 1440,
  "viewport_height": 900,
  "bbox_mode": "element",
  "pre_capture_js": pre_capture_js
}

with open(r'c:\Users\rgomez\OneDrive - GOAL SYSTEMS - B82096736\Rafael Gomez\Documentos\Python Projects GS\goalbus_docs\Español\O2\O2_Imagen2\selector.json', 'w', encoding='utf-8') as f:
    json.dump(selector_json, f, ensure_ascii=False, indent=2)

print("selector.json updated to native CSS + CDK isolation approach.")
