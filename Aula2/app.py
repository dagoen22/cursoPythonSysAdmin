#!/usr/bin/env python3

import flask
import json

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Olá Turma'

@app.route('/pagina/<any("id","name"):type>')
def pagina2(id,name):
    return f'Olá Turma, estou na pagina {id}'

@app.route('/api')
def api():
    # dados = {
    #     'name':'Daniel',
    #     'id':'666'
    # }
    # return flask.jsonify(dados)
    header = {'content-type':'application/json'}
    retorno = {'message':'Resposta'}
    return flask.make_response(json.dumps(retorno),404,header)
    
app.run(port='8080')