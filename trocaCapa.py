from PyPDF2 import PdfMerger
from PIL import Image



def converteImagemToPdf(imagem):
    img = Image.open(imagem)
    img.save("temp_capa.pdf", "PDF", resolution=100.0)

# Junta capa + conteúdo

def juntaImagemAoPdf(pdf):
    merger = PdfMerger()
    merger.append("temp_capa.pdf")
    merger.append(pdf)
    merger.write(pdf)
    merger.close()

def main(caminho_imagem,caminho_pdf):
    converteImagemToPdf(caminho_imagem)
    juntaImagemAoPdf(caminho_pdf)
    print("Troca de capa Concluida")
        


