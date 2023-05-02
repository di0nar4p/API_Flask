from Controller.conexao import db_connect


""" def select_all(param:str)-> None:
    query= (f'''SELECT * FROM {param}''')
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute(query)
    registros = cursor.fetchall() """
    
    
def select_all(user:str,password:str)-> list:
    query= (f'''SELECT * FROM dados''')
    conn = db_connect(user,password)
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
