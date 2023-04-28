from flask import Flask, request, jsonify, render_template
from Models.dados import dados

from templates import *

app = Flask(__name__)









""" @app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form['login']
        senha = request.form['senha']
        return acesso(user, senha) """
    


@app.route('/dados', methods=['GET'])
def getAll():
    
    return jsonify(dados)


@app.route('/dados/<int:id>', methods=['GET'])
def getId(id):
    for dado in dados:
        if dado.get('id') == id:
            return jsonify(dado)
        

@app.route('/dados/<int:id>', methods=['PUT'])
def update(id):
    alteracao = request.get_json()
    for indice,dado in enumerate(dados):
        if dado.get('id') == id:
          dados[indice].update(alteracao)
          return jsonify(dados[indice])


@app.route('/dados',methods=['POST'])
def include():
    new = request.get_json()
    dados.append(new)
    return jsonify(dados)
    

@app.route('/dados/<int:id>',methods=['DELETE'])
def delete(id):
    for indice,dado in enumerate(dados):
        if dado.get('id') == id:
            del dados[indice]
    
    return jsonify(dados)


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/home', methods=['GET','POST'])
def main():
    
    return render_template('main.html', dados=dados)
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


    