from flask import Flask, render_template
from controllers import routes
import requests

# criando a instancia do flask na variavel do app
app = Flask(__name__, template_folder='views')

routes.init_app(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
