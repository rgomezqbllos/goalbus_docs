import json
import csv

def translate_dict():
    with open('global_translations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    translations = {
        "Nombre Comercial": "Nome Comercial",
        "Nombre Largo": "Nome Longo",
        "Nueva Parada": "Nova Parada",
        "Puntos de Recarga": "Pontos de Recarga",
        "Testing / Hola Consultant": "Teste / Olá Consultor",
        "Tipo de Parada": "Tipo de Parada",
        "Ubicación": "Localização",
        "Viajes en Vacío y Desplazamientos": "Viagens em Vazio e Deslocamentos",
        "Comercial": "Comercial",
        "Latitud": "Latitude",
        "Longitud": "Longitude",
        "UNIVERSIDAD": "UNIVERSIDADE",
        "Crear Línea": "Criar Linha",
        "Líneas": "Linhas",
        "Todas las líneas": "Todas as linhas",
        "Nombre de la Línea": "Nome da Linha",
        "Agregar Nueva Ruta": "Adicionar Nova Rota",
        "Agregar Parada": "Adicionar Parada",
        "Claro": "Claro",
        "Híbrido": "Híbrido",
        "No en uso": "Não em uso",
        "Paradas: 2": "Paradas: 2",
        "Por: user.consultant@otto.com": "Por: usuario.consultor@otto.com",
        "Satélite": "Satélite",
        "Sentido 1": "Sentido 1",
        "Sentido 2": "Sentido 2",
        "Terreno": "Terreno",
        "Tráfico": "Trânsito",
        "Última actualización: 12/04/2026": "Última atualização: 12/04/2026",
        "Nombre": "Nome",
        "Nombre Corto": "Nome Curto",
        "Código": "Código",
        "Paradas": "Paradas",
        "Agregar": "Adicionar",
        "Color": "Cor",
        "Rutas": "Rotas",
        "Ruta": "Rota",
        "General": "Geral",
        "Actividades": "Atividades",
        "Colapsar Menú": "Colapsar Menu",
        "Conexiones Prohibidas": "Conexões Proibidas",
        "Configuración de Depósitos": "Configuração de Depósitos",
        "Configuración de Paradas": "Configuração de Paradas",
        "Configuración de Parkings": "Configuração de Estacionamentos",
        "Configuración de Tramos": "Configuração de Trechos",
        "Configuración de la Red": "Configuração da Rede",
        "ID Externo": "ID Externo",
        "No se han encontrado resultados": "Nenhum resultado encontrado",
        "UNI": "UNI",
        "L1: TN-TS": "L1: TN-TS",
        "L1: Terminal Norte - Terminal Sur": "L1: Terminal Norte - Terminal Sul",
        "TERMINAL NORTE - TERMINAL SUR": "TERMINAL NORTE - TERMINAL SUL",
        "Parkings": "Estacionamentos",
        "Map": "Mapa"
    }

    modified = False
    for key, item in data.items():
        if item.get("PT_BR") == "PENDING":
            es_val = item["ES"].strip(">").strip("<")
            if es_val in translations:
                item["PT_BR"] = f">{translations[es_val]}<" if item["ES"].startswith(">") else translations[es_val]
                item["EN"] = es_val # Placeholder
                item["FR"] = es_val # Placeholder
                modified = True
            elif "alt=" in item["ES"] or "title=" in item["ES"] or "placeholder=" in item["ES"] or "aria-label=" in item["ES"]:
                # Attribute translation logic
                attr_content = item["ES"].split('="')[1][:-1]
                if attr_content in translations:
                    new_val = item["ES"].replace(attr_content, translations[attr_content])
                    item["PT_BR"] = new_val
                    modified = True
            elif item["ES"].islower() and len(item["ES"]) < 20: # Likely an icon or tag
                item["PT_BR"] = item["ES"]
                modified = True

    if modified:
        with open('global_translations.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Dictionary updated.")

def update_csv():
    rows = []
    with open('translation_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            if row['folder'].startswith('P4_') and not row['PT_BR']:
                # Logic for P4 data
                if row['field_id'] == 'stopType': row['PT_BR'] = 'Parada de Ônibus'
                elif row['field_id'] == 'code': row['PT_BR'] = 'USP01'
                elif row['field_id'] == 'shortName' and row['folder'] == 'P4_imagen2': row['PT_BR'] = 'UNI'
                elif row['field_id'] == 'name' and row['folder'] == 'P4_imagen2': row['PT_BR'] = 'UNIVERSIDADE'
                elif row['field_id'] == 'commercialName': row['PT_BR'] = 'Ponto da Universidade'
                elif row['field_id'] == 'latitude': row['PT_BR'] = '-23.5505'
                elif row['field_id'] == 'longitude': row['PT_BR'] = '-46.6333'
                elif row['field_id'] == 'externalId': row['PT_BR'] = 'EXT-001'
                elif row['field_id'] == 'name' and row['folder'] == 'P4_imagen4': row['PT_BR'] = 'Linha 1'
                elif row['field_id'] == 'shortName' and row['folder'] == 'P4_imagen4': row['PT_BR'] = 'L1'
                elif row['field_id'] == 'parkings': row['PT_BR'] = 'Garagem Central'
                elif row['field_id'] == 'vehicleTypes': row['PT_BR'] = 'Ônibus Elétrico'
            rows.append(row)
            
    with open('translation_data.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print("CSV updated.")

translate_dict()
update_csv()
