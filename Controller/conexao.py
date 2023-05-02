import mysql.connector


#conexão com o banco de dados
def db_connect(user:str,password:str) -> object:
    try:
        conn= mysql.connector.connect(
        host='localhost',
        port='3306',
        user=user,
        passwd= password,
        db='api'
        )
    except Exception as error:
        raise error('Deu ruim')
    else:
        print('Sucessfully connected')
        return conn

