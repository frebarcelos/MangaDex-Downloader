import os
import re
import shutil
from PIL import Image
import trocaCapa as t

def ordenar_naturalmente(lista):
    def alfanum(chave):
        return [int(texto) if texto.isdigit() else texto.lower() for texto in re.split(r'(\d+)', chave)]
    return sorted(lista, key=alfanum)

def criar_pdfs_para_pastas(diretorio_raiz,nome_pasta,troca_capa):   

    regex_caminho = r'^[a-zA-Z]:\\(?:[^<>:"/\\|?*\r\n]+\\)*[^<>:"/\\|?*\r\n]+\.(jpg|jpeg|png|gif|bmp|webp|tiff)$'            
    caminhoCapa = ''
    
    caminho_pasta = os.path.join(diretorio_raiz, nome_pasta)
   
    nome_arquivo_pdf = f"{nome_pasta}.pdf"
    caminho_pdf = os.path.join(diretorio_raiz, nome_arquivo_pdf)

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
            shutil.rmtree(caminho_pasta)
            print(f"Pasta '{caminho_pasta}' excluída com sucesso!")
            if troca_capa:
                while caminhoCapa == '':
                    caminho = input('Digite o caminho para (ex: C:\\imagens\\capa.jpg): ')
                    if re.match(regex_caminho, caminho):
                        caminhoCapa = caminho
                        t.main(caminhoCapa,caminho_pdf)
                    else:
                        print('Digite um caminho valido')
        except Exception as e:
            print(f"Erro ao salvar PDF {caminho_pdf}: {e}")
    else:
        print(f"Nenhuma imagem válida em: {caminho_pasta}")

diretorio_raiz = r"C:\Users\fre12\OneDrive\Área de Trabalho\teste1\Mangas\Mangas"
nome_pasta = 'one-piece_volume_7'
troca_capa = True

if __name__ == "__main__":
    criar_pdfs_para_pastas(diretorio_raiz,nome_pasta,troca_capa)
