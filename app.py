from flask import (Flask, request) # importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/<string:nome>", methods=('GET' ,)) # Assina uma rota
def index(nome): # Função rsponsável pela página
    # HTML retornado
    return f"""<h1>Página Inicial</h1>
        <p>Olá {nome}, que nome bonito!</p>
    """

@app.route("/galeria", methods=('GET' ,))
def galeria():
    return "<h1>Galeria</h1>"

@app.route("/contato", methods=('GET' ,))
def contato():
    return "<h1>Contato</h1>"

@app.route("/sobre", methods=('GET' ,))
def sobre():
    return "<h1>Sobre Nós</h1>"

@app.route("/personagens", methods=('GET' ,))
def personagens():
    per1 = request.args.get('per1')
    per2 = request.args.get('per2')
    per3 = request.args.get('per3')

    return f"""<h1>Página Inicial</h1>
        <ul><li>{per1}</li><li>{per2}</li><li>{per3}</li></ul>
    """


@app.route("/potencial/<string:n1>/<string:n2>", methods=('GET' ,))
def potencial(n1, n2):
    r = float(n1) ** float(n2)
    return f""" <h1>{n1} ^ {n2} = {r} </h1>"""