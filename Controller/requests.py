from Controller.conexao import db_connect, dbl_connect

""" def select_all(param:str)-> None:
    query= (f'''SELECT * FROM {param}''')
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute(query)
    registros = cursor.fetchall() """
    

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


def updateId(id:int,nome:str,idade:int,nacionalidade:str,naturalidade:str)-> list:
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
    request=[]
    cursor.close() 
    return request


def login(login:str,password:str)->bool:
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

            
 