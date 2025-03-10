from flask import Flask, render_template
from controllers import routes
import os

# criando a instancia do flask na variavel do app
app = Flask(__name__, template_folder='views')

app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "static", "uploads")

# Certifique-se de que a pasta existe
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

routes.init_app(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

