from PyPDF2 import PdfMerger
from PIL import Image



def converteImagemToPdf(imagem):
    img = Image.open(imagem)
    img.save("TEMP_PDF", "PDF", resolution=100.0)


def juntaImagemAoPdf(pdf):
    merger = PdfMerger()
    merger.append("temp_capa.pdf")
    merger.append(pdf)
    merger.write(pdf)
    merger.close()
    
    if os.path.exists(TEMP_PDF):
        os.remove(TEMP_PDF)

def main(caminho_imagem,caminho_pdf):
    converteImagemToPdf(caminho_imagem)
    juntaImagemAoPdf(caminho_pdf)
    print("✅ Troca de capa concluída!")
        


