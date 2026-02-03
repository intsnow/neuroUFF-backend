from neurouff.database import Database 
from neurouff.user import User

class Sistema:

    def __init__(self, dbName):
        self.dbName = dbName
        self.db = self.connectBD()


    def connectBD(self):
        db = Database(self.dbName)        
        return db


    #   Uso de "from_dict()" no lugar de "inputDados()"
    def registrar_novoUser(self, dados):
        user = User.from_dict(dados)

        if self.db.addUser(user):
            return True, user

        return False, None
    

    def coletarUser_porEmail(self, email):
        return self.db.getUser_byEmail(email)


    def removerUser_porEmail(self, email):
        user = self.coletarUser_porEmail(email)

        if user and self.db.rmv_user(user):
            return True
        
        return False


    def listarUsers(self):
       return self.db.getAll_users()

       
