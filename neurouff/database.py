import sqlite3 as sql
from neurouff.user import User

class Database:

    def __init__(self, dbName):
        self.dbName = dbName
        self.startBD()


    def createTables(self):

        # Desabilitar journal para evitar possiveis LOCK erros
        with self.start_conn() as conn:
            cursor = conn.cursor()

            cursor.execute("PRAGMA journal_mode=OFF;")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (                            
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    email TEXT NOT NULL UNIQUE,
                    hash_senha TEXT NOT NULL, 
                    curso TEXT,
                    dataIngresso VARCHAR(10),
                    status TEXT 
                )   
            """)

            conn.commit()


    #   Remoção do uso de "vars()"
    def addUser(self, user):
        dict_user = user.to_dict()

        atributos = list(dict_user.keys())
        valores = list(dict_user.values())

        atributos = ",".join(atributos)     #   Cria a tupla de atributos da lista_keys
        placeholders = ",".join(["?"]* len(valores))    # Cria "?, ?, ..., ?" para N valores

        sql = f"""
            INSERT INTO users ({atributos})
            VALUES ({placeholders})
        """
    
        try:
            with self.start_conn() as conn:
                cursor = conn.cursor()
                cursor.execute(sql, valores)
                conn.commit()

            return True, None
        
        except sql.IntegrityError:
            return False, "Email já cadastrado." # Pega o UNIQUE constraint
        
        except Exception as e:
            return False, str(e)

                

    def rmv_user(self, user):
        
        try:
            with self.start_conn() as conn:

                sql = f"""
                    DELETE from users WHERE email = ?
                """
                # user.email formatado como tupla
                cursor = conn.cursor()
                cursor.execute(sql, (user.email,))   
                conn.commit()
                
            #  Rowcount possui valor acima de zero, caso alguma mudança 
            # tenha sido feita no BD, retornando True se removeu, e False se não encontrou.
            return cursor.rowcount > 0
        
        except Exception:
            return False
        
        
    def getUser_byEmail(self, email):

        try:
            with self.start_conn() as conn:

                sql = """
                    SELECT * FROM users WHERE email = ?   
                """

                cursor = conn.cursor()
                row = cursor.execute(sql, (email,)).fetchone()

                if row:
                    dict_row = dict(row)
                    return User.from_dict(dict_row)
                
                return None
            
        except Exception:
                return None


    #   Remoção de "inputDados()"
    def getAll_users(self):

        try:
            with self.start_conn() as conn:
                sql = """
                    SELECT * FROM users   
                """
                #   Nao usou-se cursor por ser um simples
                #   comando de operação rapida. Conn.execute() 
                #   ja cria um cursor temp, o retornando diretamente
                #   para poder ja invocar fetchAll()

                rows = conn.execute(sql).fetchall()
                lista_users = []

                for row in rows:
                    dict_row = dict(row)
                    user = User.from_dict(dict_row)
                    lista_users.append(user)

            return lista_users
        
        except Exception:
            return []


    def verify_password(self, login, senha):

        with self.start_conn() as conn:
            sql =  "SELECT * FROM users WHERE login = ? AND hash_senha = ?"
            cursor = conn.cursor()
            row = cursor.execute(sql, (login, senha)).fetchone()

            if row:
                return dict(row)
            else:
                return None


    def verify_email(self, email):

        with self.start_conn() as conn:

            sql =  "SELECT email FROM users WHERE email = ? AND hash_senha = ?"




    def start_conn(self):
        conn = sql.connect(self.dbName)
        conn.row_factory = sql.Row
    
        return conn


    def startBD(self):

        try:
            conn = self.start_conn()
            self.createTables()
            if conn: 
                # UIV.db_printBegin()
                return True

        except Exception as e:
            return False, e

                