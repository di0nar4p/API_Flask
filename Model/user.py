class User():
    
    def __init__(self,login:str, password:str) -> None:
        
        self.user = {'username':login, 'password':password}
        
        @property
        def getUser(self):
            return self.user
        