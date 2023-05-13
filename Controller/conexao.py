import mysql.connector


#conexão com o banco de dados remoto
def db_connect(user:str,password:str) -> object:
    try:
        conn= mysql.connector.connect(
        host='sql812.main-hosting.eu',
        port='3306',
        user=user,
        passwd= password,
        db='u274908554_monitoriassa'
        )
    except Exception as error:
        raise error('Deu ruim')
    else:
        print('Sucessfully connected')
        return conn


#conexão com o banco de dados local
def dbl_connect(user:str,password:str) -> object:
    try:
        conn= mysql.connector.connect(
        host='localhost',
        port='3306',
        user=user,
        passwd= password,
        db='dados'
        )
    except Exception as error:
        raise error('Deu ruim')
    else:
        print('Sucessfully connected')
        return conn

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
    
    return acesso[0][0],acesso[0][1]



#autenticação do usuário
#def login(user:User) ->None:
    pass
