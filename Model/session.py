from Model.user import User


class Session():
    def __init__(self, *args:User) -> None:
        self.user = args
        self.session = []
        
    
    @property
    def getSession(self):
        return self.session
    
    
    def setSession(self,args):
        self.user = {'username':args.user["username"], 'password': args.user["password"]} 
        self.session.append(self.user)
             
""" teste = User('teste','teste2')
teste2 = User('teste','tedfsdf')
teste3= User('teste','testsdfsdfse2')

sessao = Session()

sessao.setSession(teste)
sessao.setSession(teste3)
sessao.setSession(teste)

print(sessao.session) """