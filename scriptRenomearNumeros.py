import os

def renomear_arquivos_numericamente(pasta):
    """
    Renomeia todos os arquivos de uma pasta para 1.ext, 2.ext, 3.ext, etc.
    Mantém a mesma ordem alfabética original.
    """
    arquivos = sorted(os.listdir(pasta))  # Lista ordenada dos arquivos
    
    for i, nome_arquivo in enumerate(arquivos, start=1):
        # Ignora subdiretórios
        if os.path.isdir(os.path.join(pasta, nome_arquivo)):
            continue
            
        # Obtém a extensão do arquivo
        extensao = os.path.splitext(nome_arquivo)[1]
        
        # Novo nome
        novo_nome = f"{i}{extensao}"
        
        # Caminhos completo
        caminho_antigo = os.path.join(pasta, nome_arquivo)
        caminho_novo = os.path.join(pasta, novo_nome)
        
        # Renomeia
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome_arquivo} -> {novo_nome}")

# Exemplo de uso:
pasta_alvo = r"C:\Users\fre12\OneDrive\Área de Trabalho\teste1\Mangas\Mangas\kiss-x-sis_2"  # Substitua pelo caminho real
renomear_arquivos_numericamente(pasta_alvo)