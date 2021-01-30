import sqlite3

class ConnectionFactory(object):
    
    instance = None

    def __init__(self):
        self.__conexao = sqlite3.connect('app.db')

    @staticmethod
    def get_instance():
        if ConnectionFactory.instance == None:
            ConnectionFactory.instance = ConnectionFactory()

        return ConnectionFactory.instance

    def get_connection(self):
        return self.__conexao
