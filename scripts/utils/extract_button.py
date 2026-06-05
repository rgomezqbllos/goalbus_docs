#!/usr/bin/env python3
import re
import argparse
import sys
import os

def extract_button(html_path, search_text, output_path):
    print(f"Buscando el botón con el texto: '{search_text}' en {html_path}...")
    
    if not os.path.exists(html_path):
        print(f"Error: El archivo {html_path} no existe.")
        return

    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Buscamos la posición del texto
    start_search = 0
    matches = []
    
    # Encontrar todas las ocurrencias del texto
    for m in re.finditer(re.escape(search_text), html_content, re.IGNORECASE):
        text_pos = m.start()
        # Buscar el <button anterior más cercano
        btn_start_match = list(re.finditer(r'<button[^>]*>', html_content[:text_pos], re.IGNORECASE))
        if not btn_start_match:
            continue
            
        btn_start_pos = btn_start_match[-1].start()
        
        # Buscar el </button> siguiente más cercano
        btn_end_match = re.search(r'</button>', html_content[text_pos:], re.IGNORECASE)
        if not btn_end_match:
            continue
            
        btn_end_pos = text_pos + btn_end_match.end()
        
        # Extraer el bloque y verificar que no contenga otros botones dentro (para seguridad)
        potential_button = html_content[btn_start_pos:btn_end_pos]
        if potential_button.count('<button') == 1:
            matches.append(potential_button)
            break # Encontramos el primero válido

    if not matches:
        print(f"No se encontró ningún botón único con el texto '{search_text}'.")
        return

    button_html = matches[0].strip()
    print("¡Botón encontrado!")

    # Template con los estilos estándar de GoalBus
    template = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Botón Extraído: {search_text}</title>
    <style>
        :root {{
            color-scheme: dark;
            --color-primary-lighter: #a5ffff;
            --color-primary: #6dffe7;
            --color-primary-darker: #29cbb5;
            --color-primary-lighter-contrast: #00001b;
            --color-primary-contrast: #00001b;
            --color-primary-darker-contrast: #00001b;
            --color-grey: #464a6c;
            --color-grey-darker: #555b94;
            --color-grey-darkest: #9197ca;
            --color-grey-lightest: #00001b;
        }}

        body {{
            background-color: var(--color-grey-lightest);
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }}

        .gs-button {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            cursor: pointer;
            transition: 0.2s ease-in-out all;
            border: none;
            outline: none;
            text-decoration: none;
            white-space: nowrap;
            user-select: none;
            font-family: inherit;
        }}

        .gs-button--color-primary {{
            --btn-color-darker: var(--color-primary-darker);
            --btn-color-darker-contrast: var(--color-primary-darker-contrast);
            --btn-color: var(--color-primary);
            --btn-color-contrast: var(--color-primary-contrast);
            --btn-color-lighter: var(--color-primary-lighter);
        }}

        .gs-button--variant-default {{
            background-color: var(--btn-color-darker);
            color: var(--btn-color-darker-contrast);
        }}

        .gs-button--variant-default:hover {{
            background-color: var(--btn-color);
            color: var(--btn-color-contrast);
        }}

        .gs-button--size-small {{
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.5rem 1rem;
            border-radius: 0.25rem;
            line-height: 120%;
        }}

        .button-container {{
            padding: 2rem;
            border: 1px dashed #464a6c;
            border-radius: 8px;
        }}
    </style>
</head>
<body>
    <div class="button-container">
        {button_html}
    </div>
</body>
</html>
"""

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"Archivo generado exitosamente en: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extraer un botón de un HTML y hacerlo independiente.")
    parser.add_argument("--html", required=True, help="Ruta al archivo HTML de origen.")
    parser.add_argument("--text", required=True, help="Texto del botón a buscar.")
    parser.add_argument("--output", required=True, help="Ruta de salida para el nuevo HTML.")

    args = parser.parse_args()
    extract_button(args.html, args.text, args.output)
