from PyPDF2 import PdfMerger
from PIL import Image
import os


TEMP_PDF = "temp_capa.pdf"



def converteImagemToPdf(imagem: str) -> None:
    """Converte a imagem fornecida para um PDF temporário."""
    img = Image.open(imagem)
    img.save(TEMP_PDF, "PDF", resolution=100.0)
    img.close()


def juntaImagemAoPdf(pdf: str) -> None:
    """Insere o PDF temporário como capa do PDF principal."""
    merger = PdfMerger()
    merger.append(TEMP_PDF)
    merger.append(pdf)
    merger.write(pdf)
    merger.close()

    if os.path.exists(TEMP_PDF):
        os.remove(TEMP_PDF)

def main(caminho_imagem,caminho_pdf):
    converteImagemToPdf(caminho_imagem)
    juntaImagemAoPdf(caminho_pdf)
    print("✅ Troca de capa concluída!")
        


