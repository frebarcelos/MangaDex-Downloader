import os
import time
import requests
import salvarPdfnaPasta
import trocaCapa as t
from config_types import MangaConfig 
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


# CONFIGURAÇÕES
#manga_id = "bf55dd16-ba26-49de-adb3-cbf7d2bc6775"
#volume = "2"
#save_dir = r"C:\Users\fre12\OneDrive\Área de Trabalho\teste1\Mangas\kiss_x_sis_volume_1"  # <-- caminho do Windows onde salvar
numero_inicial = 0

# Prepara navegador
def iniciar_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # tira essa linha se quiser ver o navegador
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Faz requisição à API para pegar capítulos
def buscar_capitulos(manga_id, volume, linguagem):
    all_data = []
    offset = 0

    while True:
        url = (
            f"https://api.mangadex.org/chapter?manga={manga_id}"
            f"&translatedLanguage[]={linguagem}&limit=100&offset={offset}"
            f"&volume[]={volume}&order[chapter]=asc"
        )
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        all_data.extend(data.get("data", []))

        total = data.get("total", 0)
        offset += data.get("limit", 100)
        if offset >= total or not data.get("data"):
            break

    return all_data


    
# Salva screenshot central da página
def salvar_pagina(driver, pagina_idx, total_paginas, pasta_pdf):    

    global numero_inicial

    # Espera até alguma imagem visível aparecer
    wait = WebDriverWait(driver, 15)
    wait.until(lambda d: any(
        img.is_displayed() for img in d.find_elements(By.CSS_SELECTOR, "img.img.sp")
    ))

    # Busca a imagem visível
    img_visivel = None
    for img in driver.find_elements(By.CSS_SELECTOR, "img.img.sp"):
        if img.is_displayed():
            img_visivel = img
            break

    if img_visivel:
        # Aplica estilo para destacar só a imagem
        driver.execute_script("""           

            // Garante que a imagem esteja visível e bem posicionada
            arguments[0].style.position = 'absolute';
            arguments[0].style.zIndex = '9999';
            arguments[0].style.top = '0';
            arguments[0].style.left = '0';
            arguments[0].style.margin = '0';
            arguments[0].style.background = '#fff';
        """, img_visivel)

        time.sleep(1)  # espera pra renderizar estilo

        # Salva o screenshot da imagem diretamente
        nome_arquivo = os.path.join(pasta_pdf, f"{numero_inicial}.png")
        numero_inicial += 1
        img_visivel.screenshot(nome_arquivo)

        print(f"-> Página {pagina_idx} de {total_paginas - 1} salva")

    else:
        print(f"⚠️ Imagem não encontrada na página {pagina_idx}")    

# Processa um capítulo
def baixar_capitulo(driver, cap_data, pasta_pdf):
    cap_id = cap_data["id"]
    cap_num = cap_data["attributes"]["chapter"]
    total_paginas = cap_data["attributes"]["pages"]    
    
    print(f"\nIniciando capítulo {cap_num} ({total_paginas} páginas)")
    
    for idx in range(total_paginas):
        pagina_url = f"https://mangadex.org/chapter/{cap_id}/{idx+1}"
        
        for tentativa in range(10):  
            try:
                driver.get(pagina_url)
                # Verifica se a página carregou corretamente
                WebDriverWait(driver, 15).until(
                    lambda d: d.execute_script("return document.readyState") == "complete"
                )
                salvar_pagina(driver, idx, total_paginas, pasta_pdf)
                break
            except Exception as e:
                print(f"Erro na página {idx+1} (tentativa {tentativa+1}): {str(e)}")
                if tentativa == 2:
                    print("Muitas falhas. Continuando para próxima página...")
                    continue

# MAIN
def main(manga: MangaConfig):
    print("Iniciando download de "+ manga.manga_nome +"...")
    driver = iniciar_driver()     
    global numero_inicial
    
    try:
        for volume in manga.volumes:
            numero_inicial = 0
            nome_pasta = manga.manga_nome + '_volume_' + str(volume)
            pasta_pdf = os.path.join(manga.save_dir, nome_pasta)
            os.makedirs(pasta_pdf, exist_ok=True)
            capitulos = buscar_capitulos(manga.manga_id, volume,manga.linguagem)
            for cap in capitulos:
                baixar_capitulo(driver, cap, pasta_pdf)
            salvarPdfnaPasta.criar_pdfs_para_pastas(manga.save_dir,nome_pasta,manga.trocar_capa)            

    finally:
        driver.quit()
        print("Download finalizado.")

if __name__ == "__main__":
    main()
