from flask import Flask, url_for, request, jsonify, render_template, abort, redirect
from Controller.requests import select_all, updateId, login
from Model.session import *
from Model.user import *
from templates import *

app = Flask(__name__)






# retorna todos os dados
@app.route('/dados', methods=['GET'])
def getAll():
    dados = select_all()
      
    return jsonify(dados)
    


# retorna dados pelo id
@app.route('/dados/<int:id>', methods=['GET'])
def getId(id)-> object:
    dados = select_all()
    for dado in dados:
        if dado.get('id') == id:
            return jsonify(dado)
        

@app.route('/dados/<int:id>/<nome>/<int:idade>/<nacionalidade>/<naturalidade>', methods=['PUT'])
def update(id,nome,idade,nacionalidade,naturalidade) -> object:
    dados = select_all()
    for indice,dado in enumerate(dados):
        if dado.get('id') == id:
          updateId(id,nome,idade,nacionalidade,naturalidade)
          return jsonify(dados[indice])


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





# vou alterar a lógica
@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')






sessao= Session()

@app.route('/home', methods=['POST'])
def main():
    
    mail = request.form['login']
    senha = request.form['senha']
    if login(mail,senha):        
         dados= select_all()
         user= User(mail,senha)
         sessao.setSession(user)
         return render_template('main.html', dados=dados)
    

        
    
    

# logout da api, vai ser alterado também
@app.route('/logout')
def logout():
    sessao.clear()
    return jsonify(sessao['username'])        
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


    