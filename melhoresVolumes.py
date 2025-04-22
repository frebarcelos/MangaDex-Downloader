import requests

def buscar_volumes(manga_id,linguagem):
    url = f"https://api.mangadex.org/chapter?manga={manga_id}&translatedLanguage[]={linguagem}&limit=100&order[chapter]=asc"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()  # Retorna todo o JSON, não apenas os dados

def selecionar_melhor_idioma_por_volume(dados_api):
    # Organizar os capítulos por volume e idioma
    volumes = {}
    
    for chapter in dados_api['data']:
        attrs = chapter['attributes']
        volume = attrs['volume'] if attrs['volume'] not in [None, "null"] else "0"
        language = attrs['translatedLanguage']
        
        if volume not in volumes:
            volumes[volume] = {}
        
        if language not in volumes[volume]:
            volumes[volume][language] = []
        
        volumes[volume][language].append({
            'chapter': attrs['chapter'],
            'id': chapter['id'],
            'pages': attrs['pages']
        })
    
    # Determinar a melhor língua para cada volume (pt-br > en > outros)
    resultado = []
    
    # Ordena volumes convertendo para float (trata "null" como 0)
    volumes_ordenados = sorted(volumes.keys(), key=lambda x: float(x) if str(x).replace('.','',1).isdigit() else 0)
    
    for volume in volumes_ordenados:
        linguagens_disponiveis = volumes[volume].keys()
        
        # Prioridade: pt-br > en > qualquer outra
        if 'pt-br' in linguagens_disponiveis:
            lingua_escolhida = 'pt-br'
        elif 'en' in linguagens_disponiveis:
            lingua_escolhida = 'en'
        else:
            # Pega a primeira língua disponível se não tiver pt-br ou en
            lingua_escolhida = next(iter(linguagens_disponiveis))
        
        # Ordenar os capítulos numericamente
        try:
            capitulos_ordenados = sorted(
                volumes[volume][lingua_escolhida],
                key=lambda x: float(x['chapter']) if str(x['chapter']).replace('.','',1).isdigit() else float('inf')
            )
        except (ValueError, AttributeError):
            capitulos_ordenados = volumes[volume][lingua_escolhida]
        
        resultado.append({
            'volume': volume,
            'idioma': lingua_escolhida,
            'capitulos': capitulos_ordenados,
            'total_paginas': sum(c['pages'] for c in capitulos_ordenados)
        })
    
    return resultado

def main(manga_id,linguagem):
    try:
        dados_api = buscar_volumes(manga_id,linguagem)
        melhores_volumes = selecionar_melhor_idioma_por_volume(dados_api)
        
        for vol in melhores_volumes:
            volume_num = vol['volume'] if vol['volume'] != "0" else "Sem Volume"
            print(f"Volume {volume_num} - {vol['idioma'].upper()} "
                  f"({len(vol['capitulos'])} capítulos, {vol['total_paginas']} páginas)")
            
            for cap in vol['capitulos']:
                print(f"  Cap. {cap['chapter']} (ID: {cap['id']})")
            
            print()
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

