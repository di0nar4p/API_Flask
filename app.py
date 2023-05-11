from flask import Flask, url_for, request, jsonify, render_template, abort, redirect
from Controller.requests import select_all
from Controller.conexao import db_connect
from Model.session import *
from Model.user import *
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
    dados = select_all('credenciais do banco de dados')
      
    return jsonify(dados)
    


@app.route('/dados/<int:id>', methods=['GET'])
def getId(id):
    dados = select_all('credenciais do banco de dados')
    for dado in dados:
        if dado.get('id') == id:
            return jsonify(dado)
        

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

sessao= Session()
""" 
@app.route('/home', methods=['GET','POST'])
def main():
    
    if sessao.getSession == []:
        login = request.form['login']
        senha = request.form['senha']
        user = User(login,senha)
        sessao.setSession(user)
        
        for usuario in sessao.session:
            if usuario['username'] == login and usuario['password'] == senha:
                dados= select_all(usuario['username'],usuario['password'])
                return render_template('main.html', dados=dados)
            elif usuario['username'] and usuario['password'] in sessao.session:
                dados= select_all(usuario['username'],usuario['password'])
                return render_template('main.html', dados=dados)
    else:       
        return redirect(url_for('index'))
     """
    
    


@app.route('/logout')
def logout():
    sessao.clear()
    return jsonify(sessao['username'])        
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


    