from flask import Flask, request, jsonify, render_template, redirect, url_for
from Controller.requests import insertData,select_all,deleteId, updateId, login
from Model.session import *
from Model.user import *
from templates import *

app = Flask(__name__)


# Retorna dados pelo id
@app.route('/dados/<int:id>', methods=['GET'])
def getId(id)-> object:
    dados = select_all()
    for dado in dados:
        if dado.get('id') == id:
            return jsonify(dado)
        else:
            return redirect(url_for('getAll'))
    


        
# Create
@app.route('/dados/in/<int:id>/<nome>/<int:idade>/<nacionalidade>/<naturalidade>', methods=['GET','POST'])
def insert(id,nome,idade,nacionalidade,naturalidade)-> object:
    insertData(id,nome,idade,nacionalidade,naturalidade)
    dados = select_all()
    return jsonify(dados)
    


# Read
@app.route('/dados', methods=['GET'])
def getAll() -> object:
    dados = select_all()
      
    return jsonify(dados)

# Update 
@app.route('/dados/<int:id>/<nome>/<int:idade>/<nacionalidade>/<naturalidade>', methods=['GET','PUT'])
def update(id,nome,idade,nacionalidade,naturalidade) -> object:
    dados = select_all()
    for indice,dado in enumerate(dados):
        if dado.get('id') == id:
          updateId(id,nome,idade,nacionalidade,naturalidade)
          return jsonify(dados[indice])
        else:
            return redirect(url_for('getAll'))
# Delete
@app.route('/dados/del/<int:id>', methods=['GET','DELETE'])
def delete(id)-> object:
    deleteId(id)
    dados = select_all()
    return jsonify(dados)



# Página inicial
@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


# Usuário login
@app.route('/home', methods=['POST'])
def main():
    
    mail = request.form['login']
    senha = request.form['senha']
    if login(mail,senha):        
         dados= select_all()
         return render_template('main.html', dados=dados)
    else:
        return redirect(url_for('index'))

      
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


    



