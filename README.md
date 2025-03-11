🌌 Exoplanet Explorer - API da NASA

Bem-vindo ao Exoplanet Explorer, um projeto que consome APIs públicas da NASA para exibir informações detalhadas sobre exoplanetas e imagens do espaço. Este repositório contém o código da aplicação, que apresenta dados de maneira interativa e estilosa.

🚨 Importante!

Para acessar as imagens da NASA, é obrigatório gerar uma API Key. Caso contrário, as requisições para a rota de imagens retornarão 404 - Not Found.

🔑 Como obter uma API Key da NASA?

Acesse https://api.nasa.gov/

Clique em "Get Started"

Registre-se e obtenha sua API Key

Adicione sua chave ao arquivo de configuração do projeto

📡 APIs Utilizadas

O projeto consome os seguintes endpoints públicos da NASA:

🔭 Exoplanet Archive: https://exoplanetarchive.ipac.caltech.edu/

📸 NASA Image & Video Library: https://images-api.nasa.gov/

🛰 Astronomy Picture of the Day (APOD): https://api.nasa.gov/planetary/apod

🖥 Funcionalidades do Sistema

🔎 Exoplanetas

Lista de exoplanetas com informações detalhadas

Dados sobre massa, raio, distância e ano da descoberta

Paginação dinâmica para navegar entre os planetas

🖼 Galeria Espacial

Imagens do espaço obtidas da NASA Image & Video Library

Cada imagem tem descrição e metadados importantes

Interface responsiva e moderna para exibição

🌠 Foto Astronômica do Dia

Exibe a "Astronomy Picture of the Day (APOD)"

Inclui descrição científica e metadados da imagem

Requer API Key da NASA para funcionamento

🛠 Como Rodar o Projeto

Clone este repositório:

git clone https://github.com/seu-usuario/exoplanet-explorer.git
cd exoplanet-explorer

Instale as dependências:

npm install  # ou pip install se for Python

Configure sua API Key da NASA no arquivo .env:

NASA_API_KEY=SUA_CHAVE_AQUI

Inicie o servidor:

npm start  # ou python app.py se for Flask

Acesse a aplicação no navegador:

http://localhost:3000

📌 Contribuição

Quer ajudar a melhorar o projeto? Sinta-se à vontade para abrir uma issue ou enviar um pull request!

📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

🚀 Explore o universo com o Exoplanet Explorer! 🌠

