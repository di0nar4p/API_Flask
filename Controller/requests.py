from Controller.conexao import db_connect, local

""" def select_all(param:str)-> None:
    query= (f'''SELECT * FROM {param}''')
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute(query)
    registros = cursor.fetchall() """
    


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
    return request




