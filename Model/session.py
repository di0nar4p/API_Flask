from user import User


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
             
    
admin = User('root', 'admin')    
teste = User('Glauco','123')
teste2 = User('Ana','321')


sessao = Session()

sessao.setSession(admin)
sessao.setSession(teste2)
sessao.setSession(teste)


print(sessao.session)