
class UI_View:

    @staticmethod
    def user_input(atributo, modo_delete=None): 
        if modo_delete is None:
            return input(f"\n\tDigite o {atributo} do User:\t")

        return input(f"\n\tDigite o {atributo} do usuário à sua remoção:\t")


    @staticmethod
    def user_printStatus(status, user=None, modo_delete=None):

        if modo_delete is None:
            if status and user:
                print("\nIniciando adição ao BD...")
                print(f"\nRegistro do user [{user.nome}] bem sucedido!  ")

            elif user and not status:
                print(f"\nEmail JÁ cadastrado!! Falha ao adicionar novo usuário... Por favor, tente novamente!\n")

            else:            
                print("\nERRO inesperado! Falha ao registrar...\n")

        else:
            if status and user:
                print("\nIniciando Remoção ao BD...")
                print(f"\nExclusão do user [{user.nome}], com email [{user.email}] bem sucedida!  ")

            elif not user and not status:
                print(f"\nEmail NÃO existente!! Falha ao remover usuário... Por favor, tente novamente!\n")

            else:            
                print("\nERRO inesperado! Falha ao excluir...\n")


    # Lista de users trazida do main
    @staticmethod
    def list_users(users):

        if users:
            print("__"*30)
            print("\nUsuários carregados com sucesso!\n")
          
            for user in users:                
                print("__"*30)
                user_limpo = user.to_dict()

                for atributo, valores in user_limpo.items():
                    print(f"\n{atributo}:\t{valores}")

            print("__"*30)

        else:
            print("\n Lista de usuários não feita...")


    @staticmethod
    def db_printExit():
        print("\nDesconexão bem sucedida!")


    @staticmethod
    def db_printBegin():
        print("\nConexão bem sucedida!")


    @staticmethod
    def db_printErro(e):
        print("\n\nErro ao conectar: ", type(e).__name__, "-", e)


    @staticmethod
    def opcao_printErro():
        print("\n\tFalha ao selecionar opção! Por favor, redigite sua escolha...\t")