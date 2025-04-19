import os
import time
import requests
import scriptSalvarPdfnaPasta
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# CONFIGURAÇÕES
manga_id = "bf55dd16-ba26-49de-adb3-cbf7d2bc6775"
volume = "1"
save_dir = r"C:\Users\fre12\OneDrive\Área de Trabalho\teste1\Mangas\kiss_x_sis_volume_1"  # <-- caminho do Windows onde salvar
numero_inicial = 0

# Prepara navegador
def iniciar_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # tira essa linha se quiser ver o navegador
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Faz requisição à API para pegar capítulos
def buscar_capitulos(manga_id, volume):
    url = f"https://api.mangadex.org/chapter?manga={manga_id}&translatedLanguage[]=pt-br&limit=100&volume[]={volume}&order[chapter]=asc"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()["data"]


    
# Salva screenshot central da página
def salvar_pagina(driver, pagina_idx, total_paginas):    

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
        nome_arquivo = os.path.join(save_dir, f"{numero_inicial}.png")
        numero_inicial += 1
        img_visivel.screenshot(nome_arquivo)

        print(f"-> Página {pagina_idx} de {total_paginas - 1} salva")

    else:
        print(f"⚠️ Imagem não encontrada na página {pagina_idx}")    

# Processa um capítulo
def baixar_capitulo(driver, cap_data):
    cap_id = cap_data["id"]
    volume = cap_data["attributes"]["volume"]
    cap_num = cap_data["attributes"]["chapter"]
    paginas = cap_data["attributes"]["pages"]
   

    print(f"Salvando: volume {volume} capítulo {cap_num}")

    base_url = f"https://mangadex.org/chapter/{cap_id}/"
    for idx in range(paginas):
        pagina_url = base_url + str(idx + 1)
        driver.get(pagina_url)
        salvar_pagina(driver,  idx, paginas)

# MAIN
def main():
    print("Iniciando download...")
    driver = iniciar_driver()

    try:
        capitulos = buscar_capitulos(manga_id, volume)
        for cap in capitulos:
            baixar_capitulo(driver, cap)
        scriptSalvarPdfnaPasta.criar_pdfs_para_pastas(save_dir)

    finally:
        driver.quit()
        print("Download finalizado.")

if __name__ == "__main__":
    main()
