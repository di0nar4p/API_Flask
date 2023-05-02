from flask import Flask, url_for, request, jsonify, render_template, abort, redirect
from Controller.requests import select_all
from Controller.conexao import db_connect
from templates import *

app = Flask(__name__)









""" @app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form['login']
        senha = request.form['senha']
        return acesso(user, senha) """
    


""" @app.route('/dados', methods=['GET'])
def getAll():
    senha = request.form['senha']
    user = request.form['login']
    dados = select_all('root','5550123Pl@y')
    return jsonify(dados) """


""" @app.route('/dados/<int:id>', methods=['GET'])
def getId(id):
    dados = select_all()
    for dado in dados:
        if dado.get('id') == id:
            return jsonify(dado)
 """        

""" @app.route('/dados/<int:id>', methods=['PUT'])
def update(id):
    alteracao = request.get_json()
    dados = select_all()
    for indice,dado in enumerate(dados):
        if dado.get('id') == id:
          dados[indice].update(alteracao)
          return jsonify(dados[indice]) """


""" @app.route('/dados',methods=['POST'])
def include():
    new = request.get_json()
    dados = select_all()
    dados.append(new)
    return jsonify(dados) """
    

""" @app.route('/dados/<int:id>',methods=['DELETE'])
def delete(id):
    
    for indice,dado in enumerate(dados):
        if dado.get('id') == id:
            del dados[indice]
    
    return jsonify(dados) """


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/home', methods=['GET','POST'])
def main():
    senha = request.form['senha']
    user = request.form['login']
    if db_connect(user,senha):
        dados= select_all(user,senha)
        response= dados
        return render_template('main.html', dados=response)

        
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


    