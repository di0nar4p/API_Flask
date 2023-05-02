from Controller.conexao import db_connect


""" def select_all(param:str)-> None:
    query= (f'''SELECT * FROM {param}''')
    conn = db_connect()
    cursor = conn.cursor()

    cursor.execute(query)
    registros = cursor.fetchall() """
    
    
def select_all(user:str,senha:str)-> None:
    query= (f'''SELECT * FROM dados''')
    conn = db_connect(user,senha)
    cursor = conn.cursor()

    cursor.execute(query)
    registros = cursor.fetchall()
    return list(registros)


