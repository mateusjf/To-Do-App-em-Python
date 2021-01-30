class Tarefa(object):
    
    def __init__(self, identifier, text):
        self.__id = identifier
        self.__text = text
        self.__completed = False
        self.__Pessoa = None

    @property
    def identifier(self):
        return self.__id

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    @property
    def completed(self):
        return self.__completed

    @completed.setter
    def completed(self, value):
        self.__completed = value

    @property
    def Pessoa(self):
        return self.__Pessoa

    @Pessoa.setter
    def Pessoa(self, value):
        self.__Pessoa = value


    