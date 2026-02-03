from neurouff.sistema import Sistema
from neurouff.ui_view import UI_View as UIV


def startMenu(sys: Sistema):

        while True:
            op = input(
                "\n\n\n\t\t=== Menu NeuroUFF === \n" \
                "\n\t1. Cadastrar Novo Aluno " \
                "\n\t2. Listar Alunos (Ler do Banco de Dados)" \
                "\n\t3. Excluir Aluno (Pelo E-mail)"   \
                "\n\t4. Sair" \
                "\n\n\tDigite o numero_comando:\t"
            )

            match int(op):

                case 1:

                    fill = int(input("\nRegistrar manualmente (1) ou automaticamente/dummy (2)? "))

                    while fill not in (1,2):
                        UIV.opcao_printErro()
                        fill = int(input("\nRegistrar manualmente (1) ou automaticamente/dummy (2)? "))

                    if fill == 1:
                        dados = {"nome": " ", "email": " ",
                                 "hash_senha": " ", "curso": " ", 
                                 "dataIngresso": " ", "status": " "}
                        
                        for atr in dados.keys():
                            dados.__setitem__(atr, UIV.user_input(atr))
                 

                    elif fill == 2:                        
                        dados = {"nome": "Ana", "email": "ana@email.com",
                                 "hash_senha": "anasenha", "curso": "S.I", 
                                 "dataIngresso": "03/03/2026", "status": "Ativo"}   

                    status, user = sys.registrar_novoUser(dados)
                    
                    if user:
                        UIV.user_printStatus(status, user)
                    else:
                        UIV.user_printStatus(status)

                case 2:
                    users = sys.listarUsers()
                    UIV.list_users(users)
                
                case 3:
                    email = UIV.user_input("EMAIL", True)
                    user = sys.coletarUser_porEmail(email)
                    
                    status = sys.removerUser_porEmail(email)

                    UIV.user_printStatus(status, user, True)


                case 4:
                    print("\nSaindo dos registros...")

                    return 
                
def main():
    sys = Sistema("neuro_uff.db")

    if sys:
        print("\Conectando de BD...")
        startMenu(sys)


if __name__ == "__main__":
    main()

