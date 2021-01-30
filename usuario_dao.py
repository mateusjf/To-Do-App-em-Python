from connection_factory import ConnectionFactory

class UsuarioDAO(object):

    instance = None

    def __init__(self):
        self.__factory = ConnectionFactory.get_instance()
        self.__conn = self.__factory.get_connection()
        self.__criar_tabela()
        self.__valor_padrao()
        
    """    
    def buscar(self, identifier):
        cursor = self.__conn.cursor()
        cursor.execute(
                '''
                    SELECT * FROM tarefa WHERE id == {}
                '''.format(identifier)
            )
        return cursor.fetchone()
        """
        
        

    def persistir(self, item):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE usuario SET nome = '{}', username = '{}', password = '{}'
            '''.format(item[0], item[1], item[2])
        )
        self.__conn.commit()
            
    """
    def deletar(self, identifier):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                DELETE FROM tarefa WHERE id = {}
            '''.format(identifier)
        )
        self.__conn.commit()
    """

    def buscar_todos(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM usuario
            '''
        )
        return cursor.fetchone()

    @staticmethod
    def get_instance():
        if UsuarioDAO.instance == None:
            UsuarioDAO.instance = UsuarioDAO()

        return UsuarioDAO.instance

    def __criar_tabela(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS usuario (
                nome TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            );
            '''
        )

    def __valor_padrao(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO usuario (nome, username, password) 
                VALUES ('Administrador', 'admin', 'admin')
            '''
        )
        self.__conn.commit()

