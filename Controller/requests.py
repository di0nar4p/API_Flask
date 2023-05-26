from Controller.conexao import db_connect, dbl_connect
from flask import render_template

    

# Requisição de credencais
def local():
    access= ('SELECT * FROM credentials')
    connlocal = dbl_connect('root', '5550123Pl@y')
    cursor = connlocal.cursor()
    cursor.execute(access)
    credentials= cursor.fetchall()
    acesso=[]
    for credencial in credentials:
        acesso.append(list(credencial))
    cursor.close()
    return acesso[0][0],acesso[0][1]


# Requisição banco remoto
def select_all()-> list:
    query= (f'''SELECT * FROM dados''')
    login,password= local()
    conn = db_connect(login,password)
    cursor = conn.cursor()
    cursor.execute(query)
    registros= cursor.fetchall()
    request=[]
    for row in registros: 
        dados={ 'id': row[0],
                'nome':row[1],
                'idade': row[2],
                'nacionalidade':row[3],
                'naturalidade': row[4]
                            }
        request.append(dados)
        
    cursor.close() 
    return request

# Atualiza dados no banco remoto
def updateId(id:int,nome:str,idade:int,nacionalidade:str,naturalidade:str)-> None:
    query= (f'''UPDATE dados SET
            nome= "{nome}",
            idade= "{idade}",
            nacionalidade= "{nacionalidade}",
            naturalidade= "{naturalidade}"
            WHERE id = {id}''')
    login,password= local()
    conn = db_connect(login,password)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close() 
    

#Exclusão no banco de dados remoto
def deleteId(id:int) -> None:
    query = (f'''DELETE from dados WHERE id ={id}''')
    login,password= local()
    conn = db_connect(login,password)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
  
#Inserção no banco de dados remoto
def insertData(id:int,nome:str,idade:int,nacionalidade:str,naturalidade:str)-> None:
    query= (f'''INSERT INTO dados values(
            "{id}",
            "{nome}",
            "{idade}",
            "{nacionalidade}",
            "{naturalidade}"
            )''')
    login,password= local()
    conn = db_connect(login,password)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close() 




# Autenticação no banco remoto
def login(login,password):

    query= ('SELECT * FROM users')
    remote1,remote2= local()
    conn = db_connect(remote1,remote2)
    cursor = conn.cursor()
    cursor.execute(query)
    credentials= cursor.fetchall()
    acesso=[]
    for credencial in credentials:
        acesso.append(list(credencial))
        if login == acesso[0][0] and password == acesso[0][1]:
            cursor.close()
            return True
            
        else:
            return False

            