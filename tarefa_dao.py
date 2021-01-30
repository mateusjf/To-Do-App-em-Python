from connection_factory import ConnectionFactory

class TarefaDAO(object):

    instance = None

    def __init__(self):
        self.__factory = ConnectionFactory.get_instance()
        self.__conn = self.__factory.get_connection()
        self.__criar_tabela()
        
        
    def buscar(self, identifier):
        cursor = self.__conn.cursor()
        cursor.execute(
                '''
                    SELECT * FROM tarefa WHERE id == {}
                '''.format(identifier)
            )
        return cursor.fetchone()
        
        

    def persistir(self, item):
        cursor = self.__conn.cursor()

        if item.identifier == 0:
            cursor.execute(
                '''
                    INSERT INTO tarefa (text, completed) 
                    VALUES ('{}', '{}')
                '''.format(item.text, item.completed)
            )
        else:
            cursor.execute(
                '''
                    UPDATE tarefa SET completed = '{}'  WHERE id = {}
                '''.format(item.completed, item.identifier)
            )

        self.__conn.commit()
            

    def deletar(self, identifier):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                DELETE FROM tarefa WHERE id = {}
            '''.format(identifier)
        )
        self.__conn.commit()
    
    def buscar_todos(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM tarefa
            '''
        )
        return cursor.fetchall()

    @staticmethod
    def get_instance():
        if TarefaDAO.instance == None:
            TarefaDAO.instance = TarefaDAO()

        return TarefaDAO.instance

    def __criar_tabela(self):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS tarefa (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                text TEXT NOT NULL,
                completed INTEGER NOT NULL
            );
            '''
        )
        

