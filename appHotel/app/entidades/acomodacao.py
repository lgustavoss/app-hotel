class Acomodacao():
    def __init__(self, unidade, tipo, andar, ramal, capacidade, valor, status, situacao):
        self.__unidade = unidade
        self.__tipo = tipo
        self.__andar = andar
        self.__ramal = ramal
        self.__capacidade = capacidade
        self.__valor = valor
        self.__status = status
        self.__situacao = situacao

    @property
    def unidade(self):
        return self.__unidade

    @unidade.setter
    def unidade(self, unidade):
        self.__unidade = unidade

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def andar(self):
        return self.__andar

    @andar.setter
    def andar(self, andar):
        self.__andar = andar

    @property
    def ramal(self):
        return self.__ramal

    @ramal.setter
    def ramal(self, ramal):
        self.__ramal = ramal

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def situacao(self):
        return self.__situacao

    @situacao.setter
    def situacao(self, situacao):
        self.__situacao = situacao
