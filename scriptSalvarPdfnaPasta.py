import os
import re
from PIL import Image

def ordenar_naturalmente(lista):
    def alfanum(chave):
        return [int(texto) if texto.isdigit() else texto.lower() for texto in re.split(r'(\d+)', chave)]
    return sorted(lista, key=alfanum)

def criar_pdfs_para_pastas(diretorio_raiz):
    pasta_pdf = os.path.join(diretorio_raiz, 'pdf')
    os.makedirs(pasta_pdf, exist_ok=True)  # Cria a pasta 'pdf' se não existir

    for nome_pasta in os.listdir(diretorio_raiz):
        caminho_pasta = os.path.join(diretorio_raiz, nome_pasta)
        if os.path.isdir(caminho_pasta) and nome_pasta != 'pdf':  # Ignora a pasta de PDFs
            nome_arquivo_pdf = f"{nome_pasta}.pdf"
            caminho_pdf = os.path.join(pasta_pdf, nome_arquivo_pdf)

            # Verifica se o PDF já existe
            if os.path.exists(caminho_pdf):
                print(f"PDF já existe, pulando: {caminho_pdf}")
                continue

            imagens = []
            arquivos = [
                f for f in os.listdir(caminho_pasta)
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp'))
            ]

            arquivos_ordenados = ordenar_naturalmente(arquivos)

            for nome_arquivo in arquivos_ordenados:
                caminho_imagem = os.path.join(caminho_pasta, nome_arquivo)
                try:
                    img = Image.open(caminho_imagem).convert('RGB')
                    imagens.append(img)
                except Exception as e:
                    print(f"Erro ao abrir {caminho_imagem}: {e}")

            if imagens:
                try:
                    imagens[0].save(caminho_pdf, save_all=True, append_images=imagens[1:])
                    print(f"PDF criado: {caminho_pdf}")
                except Exception as e:
                    print(f"Erro ao salvar PDF {caminho_pdf}: {e}")
            else:
                print(f"Nenhuma imagem válida em: {caminho_pasta}")

# Caminho do diretório raiz
diretorio_raiz = r'C:\Users\fre12\OneDrive\Área de Trabalho\teste1\Mangas\kiss_x_sis_volume_1'
criar_pdfs_para_pastas(diretorio_raiz)
