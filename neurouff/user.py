from datetime import date as Data
from dataclasses import dataclass, asdict
from typing import Optional 

@dataclass
class User:
    nome : str 
    email : str 
    hash_senha : str 
    curso : str 
    dataIngresso : str 
    status : str 
    id : Optional[int] = None
        
    @classmethod
    def empty(cls):
        return cls("", "", "", "", "", "")
    

    #   Substuição de "inputDados()" ao "from_dict()":  metodo anterior
    #  utilizava um padrão pouco profissional e seguro.
    @classmethod
    def from_dict(cls, dados: dict):

        # Filtrando chaves validas, que têm que estar na classe
        chaves_validas = { k: v for k, v in dados.items()
                           if k in cls.__annotations__}

        return cls(**chaves_validas)
    

    #   Excluindo o uso de vars():  Retornar dicionario pronto ao BD, 
    #  excluindo o atributo "id" por ser tratado pelo proprio BD
    def to_dict(self):
        dic = asdict(self)

        if dic["id"] is None:
            del dic["id"] 

        return dic