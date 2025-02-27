from flask import render_template, request, redirect, url_for
import urllib
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

jogadores = []
gamelist = [{"Titulo": "CS-GO",
         "Ano": 2017,
          "Categoria": "FPS-Online"
         }, {
             
         }]


def init_app(app):
    # criando a primeira rota da aplicação
    @app.route('/')
    # view function -> função de visualização
    def home():
        return render_template('index.html')

    @app.route('/games', methods=['POST', 'GET'])
    def games():
        games = gamelist[0]
        if request.method == 'POST':
            nome_jogador = request.form.get('Jogador')
            jogadores.append(nome_jogador)
            return redirect(url_for('games'))

        return render_template('games.html', games=games, jogadores=jogadores)

    
    @app.route('/imagens_marte', methods=['GET', 'POST'])
    def marte():

        earth_date = request.form.get('earth_date', '2022-01-01')
        camera = request.form.get('camera', 'fhaz')
        API_KEY = os.getenv("API_KEY")
        page = request.args.get('page', 1, type=int)  # Pegando a página corretamente

        url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={earth_date}&camera={camera}&api_key={API_KEY}'
        response = requests.get(url) 
        data_marte = response.json()  
        
        return render_template('imagens_marte.html', data=data_marte, current_page=page)


    @app.route('/nasateste', methods=['GET', 'POST'])
    def nasateste():
        url = 'https://api.nasa.gov/planetary/apod?api_key=9UouOIjOPm74WfGTenuMGmicMteJkzwOPixwfxzn'
        response = requests.get(url)  # Melhor do que urllib
        data = response.json()  # Converte diretamente para JSON
    
        return render_template('apigames.html', gamesjson=data)

