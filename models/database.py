from flask_sqlalchemy import SQLAlchemy

# Criando uma instancia do SQLAlchemy
db = SQLAlchemy()

# Classe responsável por criar a entidade 'Constelacao', com seus atributos


class Constelacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_constelacao = db.Column(db.String(150))
    distancia = db.Column(db.Float)
    magnitude = db.Column(db.String(20))
    nome_usuario = db.Column(db.String(50))
    data_registro = db.Column(db.Date)
    imagem = db.Column(db.String(100))

    # Método Construtor da Classe
    def __init__(self, nome_constelacao, distancia, magnitude, nome_usuario, data_registro, imagem):
        self.nome_constelacao = nome_constelacao
        self.distancia = distancia
        self.magnitude = magnitude
        self.nome_usuario = nome_usuario
        self.data_registro = data_registro
        self.imagem = imagem
