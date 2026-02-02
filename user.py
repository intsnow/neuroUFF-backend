from datetime import date as Data

class User:

    def __init__(self, nome, email, hash_senha, curso, dataIngresso, status, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.hash_senha = hash_senha  
        self.curso = curso
        self.dataIngresso = dataIngresso
        self.status = status
        
    @classmethod
    def empty(cls):
        return cls("", "", "", "", "", "")
    
    
    @classmethod
    def inputDados(cls, dados):
        # O duplo asterisco desempacota por chaves (keywords) do DICIONÁRIO "dados"
        return cls(**dados)