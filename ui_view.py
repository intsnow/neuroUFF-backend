

class UI_View:

    @staticmethod
    def user_input(atributo, modo_delete=None): 
        if modo_delete is None:
            return input(f"\n\tDigite o {atributo} do User:\t")

        return input(f"\n\tDigite o {atributo} do usuário à sua remoção:\t")

    # @staticmethod
    # def user_remove():


    @staticmethod
    def user_printStatus(status, user=None, modo_delete=None):

        if modo_delete is None:
            if status and user:
                print("\nIniciando adição ao BD...")
                print(f"\nRegistro do user [{user.nome}] bem sucedido!  ")

            elif user and not status:
                print(f"\Email JÁ cadastrado!! Falha ao adicionar novo usuário... Por favor, tente novamente!\n")

            else:            
                print("\nERRO inesperado! Falha ao registrar...\n")

        else:
            if status and user:
                print("\nIniciando Remoção ao BD...")
                print(f"\nExclusão do user [{user.nome}], com email [{user.email}] bem sucedida!  ")

            elif not user and not status:
                print(f"\Email NÃO existente!! Falha ao remover usuário... Por favor, tente novamente!\n")

            else:            
                print("\nERRO inesperado! Falha ao excluir...\n")



    # Lista de users trazida do main
    @staticmethod
    def list_users(users):

        # lista_users = db.getAll_users()
        lista_users = users

        if lista_users:
            print("\nUsuários carregados com sucesso!\n")
            cont = 0

          
            for user in lista_users:                
                
                print("__"*30)#len(dictUsers[user]))

                atributos = [atr for atr in vars(user).keys()]
                valores = [val for val in vars(user).values()]

                for i in range(len(atributos)):

                    print(f"\n{atributos[i]}:\t{valores[i]}")

            print("__"*30)#len(dictUsers[user]))
            # cont += 1

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
