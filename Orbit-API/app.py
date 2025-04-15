from flask import Flask, render_template
from controllers import routes
from models.database import db, Constelacao
import os

# criando a instancia do flask na variavel do app
app = Flask(__name__, template_folder='views')

app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "static", "uploads")

# Certifique-se de que a pasta existe
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

routes.init_app(app)

#Permite ler um diretório absoluto de um determinado diretório
dir = os.path.abspath(os.path.dirname(__file__))
                      
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/games.sqlite3')

if __name__ == '__main__':
    db.init_app(app)
    with app.test_request_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)

