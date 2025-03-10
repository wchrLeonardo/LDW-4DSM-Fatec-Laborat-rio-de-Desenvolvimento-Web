from flask import render_template, request, redirect, url_for, current_app

import urllib
import json
import requests
import os
from datetime import datetime
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
load_dotenv()


constelacoes = []

def init_app(app):
    # criando a primeira rota da aplicação
    @app.route('/')
    # view function -> função de visualização
    def home():
        return render_template('index.html')

    @app.route('/exo_planetas', methods=['POST', 'GET'])
    def planetas():
        
        page = int(request.args.get('page', 1))  # Obtém a página atual, padrão 1
        per_page = 20  # Quantidade por página
        start = (page - 1) * per_page
        end = start + per_page
        
        url = f'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=SELECT+pl_name,hostname,disc_year,pl_orbper,pl_rade,pl_bmasse,st_teff,st_rad,st_mass,sy_dist+FROM+pscomppars&format=json'
        response = requests.get(url)
        exo_data = response.json()
        
        total_pages = len(exo_data) // per_page + 1
        return render_template('exo_planetas.html', data=exo_data[start:end], current_page=page, total_pages=total_pages)
    
    @app.route('/imagens_marte', methods=['GET', 'POST'])
    def marte():
        API_KEY = os.getenv("API_KEY")
        if request.method == 'POST':
            earth_date = request.form.get('earth_date', '2022-01-01')
            camera = request.form.get('camera', 'fhaz')
            return redirect(url_for('marte', earth_date=earth_date, camera=camera))
        
        earth_date = request.args.get('earth_date', '2022-01-13')
        camera = request.args.get('camera', 'mahli')
        page = request.args.get('page', 1, type=int)  # Pegando a página corretamente

        url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={earth_date}&camera={camera}&api_key={API_KEY}'
        response = requests.get(url) 
        data_marte = response.json()  
        
        return render_template('imagens_marte.html', data=data_marte, current_page=page)


    @app.route('/imagem_do_dia', methods=['GET', 'POST'])
    def nasateste():
        url = 'https://api.nasa.gov/planetary/apod?api_key=9UouOIjOPm74WfGTenuMGmicMteJkzwOPixwfxzn'
        response = requests.get(url)  # Melhor do que urllib
        data_imagem = response.json()  # Converte diretamente para JSON
    
        return render_template('imagem_dia.html', data=data_imagem)
    


    @app.route('/sua_constelacao', methods=['GET', 'POST'])
    def constelacao():
        if request.method == "POST":
            nome_constelacao = request.form["nome_constelacao"]
            distancia = request.form["distancia"]
            magnitude = request.form["magnitude"]
            nome_usuario = request.form["nome_usuario"]

            imagem = request.files["imagem"]

            if imagem and imagem.filename:
                filename = secure_filename(imagem.filename)
                caminho = os.path.join("uploads", filename)
                imagem.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
                # Corrigir a barra invertida para barra normal (no caso do Windows)
                caminho = caminho.replace("\\", "/")

            else:
                caminho = "uploads/default.jpg"
            
            data_registro = datetime.now().strftime("%Y-%m-%d %H:%M")

            constelacoes.append({
                "nome_constelação": nome_constelacao,
                "distancia": distancia,
                "magnitude": magnitude,
                "nome_usuario": nome_usuario,
                "data_registro": data_registro,
                "imagem": caminho
            })

            return redirect(url_for("constelacao"))
        

        return render_template("constelacao.html", constelacoes=constelacoes)