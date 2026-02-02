from database import Database 
from user import User

class Sistema:

    def __init__(self, dbName):
        self.dbName = dbName
        self.db = self.connectBD()



    def connectBD(self):
        db = Database(self.dbName)        
        return db


    
    def registrar_novoUser(self, dados):

        userTmp = self.db.getUser_byEmail(dados["email"])

        if not userTmp:
            
            user = User.inputDados(dados)
        
            if self.db.addUser(user):
                # UIV.user_printStatus(True, user)
                return True, user

        return False
    

    def coletarUser_porEmail(self, email):
        return self.db.getUser_byEmail(email)


    def removerUser_porEmail(self, email):

        user = self.coletarUser_porEmail(email)

        if user and self.db.rmv_user(user):
            return True
        
        return False


    def listarUsers(self):
       return self.db.getAll_users()

       

    
        #   Refazer todo o input de dados no MAIN, e trazer um DICT "dados" pronto para uso ao registro => renomear metodo
        #       como "registrar_novoUser(self, dados)"