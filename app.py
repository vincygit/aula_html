from flask import Flask # importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/", methods=('GET' ,)) # Assina uma rota
def index(): # Função rsponsável pela página
    return "<h1>Página inicial</h1>" # HTML retornado

@app.route("/outra_pagina", methods=('GET' ,))
def outra():
    return "<h1>Outra página</h1>"