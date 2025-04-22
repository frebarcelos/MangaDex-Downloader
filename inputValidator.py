import os 
import re

def obter_url_manga():
    while True:
        url = input('Digite a URL do mangá (ex: https://mangadex.org/title/UUID/NOME): ').strip()
        parts = url.split('/')
        if len(parts) >= 6 and parts[2].endswith("mangadex.org") and parts[3] == 'title':
            return parts[4], parts[5]  # uuid, nome
        print("⚠️  URL inválida. Tente novamente.")
        
def obter_diretorio_destino():
    while True:
        path = input("Digite o diretório onde os volumes serão salvos: ").strip()
        if os.path.isdir(path):
            return path
        print("⚠️  Caminho inválido. Certifique-se de que o diretório existe.")
        
def obter_linguagem():
    while True:
        lang = input("Digite o código do idioma (ex: pt-br, en, es): ").strip().lower()
        if re.match(r"^[a-z]{2}(-[a-z]{2})?$", lang):
            return lang
        print("⚠️  Código de idioma inválido.")

def confirmar_pergunta(msg):
    while True:
        resposta = input(msg + " (S/n): ").strip().lower()
        if resposta in ['s', 'n', '']:
            return resposta == 's' or resposta == ''
        print("⚠️  Digite apenas 'S' ou 'N'.")
        
def obter_volumes():
    while True:
        entrada = input("Quais volumes deseja baixar? (ex: 1;2;3): ").strip()
        try:
            volumes = [int(v.strip()) for v in entrada.split(';') if v.strip().isdigit()]
            if volumes:
                return volumes
        except ValueError:
            pass
        print("⚠️  Entrada inválida. Digite números separados por ponto e vírgula.")
