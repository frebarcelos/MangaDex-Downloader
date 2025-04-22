MangaDex Downloader
MangaDex Downloader é uma aplicação de código aberto para baixar mangás do MangaDex diretamente para o seu computador. A versão atual é baseada em terminal, mas em breve terá uma interface gráfica. A ferramenta permite pesquisar, escolher volumes ou capítulos específicos, e até mesmo personalizar a capa do seu mangá. Perfeito para fãs de mangá que querem uma forma fácil e prática de armazenar suas coleções!

Funcionalidades
Busca de Mangás: Busque mangás por nome e idioma.

Seleção de Capítulos e Volumes: Escolha quais capítulos ou volumes deseja baixar.

Troca de Capa: Opção de trocar a capa do mangá.

Suporte a Diversos Idiomas: Baixe mangás em diversos idiomas, incluindo o português (pt-br).

Salvamento em PDF: Converta os mangás baixados para o formato PDF.

Versão Atual
A versão atual do MangaDex Downloader funciona através do terminal. A interface gráfica ainda está em desenvolvimento e será adicionada futuramente.

Para usuários que preferem usar o terminal:
Windows: Você pode baixar o .exe para rodar diretamente.

Linux/Mac: Você pode rodar o script diretamente com Python.

Tecnologias Utilizadas
Python: Linguagem principal para desenvolvimento.

Tkinter & CustomTkinter (futuro): Planejado para a criação da interface gráfica.

Requests: Para comunicação com a API do MangaDex.

Pillow: Para manipulação de imagens (como capas de mangás).

Selenium: Para navegação automatizada quando necessário (por exemplo, ao carregar conteúdo dinâmico).

Como Usar
Requisitos
Antes de rodar o aplicativo, você precisará instalar algumas bibliotecas. É possível fazer isso facilmente com o pip. O arquivo requirements.txt contém todas as dependências necessárias.

Execute o seguinte comando para instalar:

bash
Copiar
Editar
pip install -r requirements.txt
Rodando o Programa
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/usuario/MangaDex-Downloader.git
cd MangaDex-Downloader
Execute o script principal (mangasaveui.py) para iniciar a aplicação no terminal.

bash
Copiar
Editar
python mangasaveui.py
A aplicação no terminal solicitará que você insira as informações do mangá e escolha quais volumes ou capítulos deseja baixar. O programa irá baixar os mangás e, se escolhido, trocará a capa para um arquivo em PDF.

Versão .exe para Windows
Se você está no Windows e prefere usar o .exe, basta baixar o arquivo de release no GitHub e executá-lo. O programa rodará diretamente no terminal, sem necessidade de instalar o Python ou outras dependências.

Dependências
Python 3.x

Bibliotecas adicionais (instaláveis via pip):

requests

Pillow

selenium

customtkinter (futuramente para interface gráfica)

Como Contribuir
Fork o repositório.

Crie uma branch (git checkout -b feature/novo-recurso).

Faça suas alterações e commite-as (git commit -am 'Adiciona novo recurso').

Envie para o seu fork (git push origin feature/novo-recurso).

Crie um pull request.

Licença
Este projeto está licenciado sob a MIT License.

Aviso
Este projeto não tem afiliação oficial com o MangaDex ou quaisquer outros serviços mencionados. O uso do MangaDex Downloader deve seguir os Termos de Serviço do MangaDex e respeitar as leis de direitos autorais.