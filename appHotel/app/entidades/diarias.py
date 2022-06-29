class Diarias():
    def __init__(self, cliente, unidade, hospedes, entrada, saida, qnt_diarias, valor_diaria, total_diaria, adiantamento, observacao):
        self.__cliente = cliente
        self.__unidade = unidade
        self.__hospedes = hospedes
        self.__entrada = entrada
        self.__saida = saida
        self.__qnt_diarias = qnt_diarias
        self.__valor_diaria = valor_diaria
        self.__total_diaria = total_diaria
        self.__adiantamento = adiantamento
        self.__observacao = observacao

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def unidade(self):
        return self.__unidade

    @unidade.setter
    def unidade(self, unidade):
        self.__unidade = unidade

    @property
    def hospedes(self):
        return self.__hospedes

    @hospedes.setter
    def hospedes(self, hospedes):
        self.__hospedes = hospedes

    @property
    def entrada(self):
        return self.__entrada

    @entrada.setter
    def entrada(self, entrada):
        self.__entrada = entrada

    @property
    def saida(self):
        return self.__saida

    @saida.setter
    def saida(self, saida):
        self.__saida = saida

    @property
    def qnt_diarias(self):
        return self.__qnt_diarias

    @qnt_diarias.setter
    def qnt_diarias(self, qnt_diarias):
        self.__qnt_diarias = qnt_diarias

    @property
    def valor_diaria(self):
        return self.__valor_diaria

    @valor_diaria.setter
    def valor_diaria(self, valor_diaria):
        self.__valor_diaria = valor_diaria

    @property
    def total_diaria(self):
        return self.__total_diaria

    @total_diaria.setter
    def total_diaria(self, total_diaria):
        self.__total_diaria = total_diaria

    @property
    def adiantamento(self):
        return self.__adiantamento

    @adiantamento.setter
    def adiantamento(self, adiantamento):
        self.__adiantamento = adiantamento

    @property
    def observacao(self):
        return self.__observacao

    @observacao.setter
    def observacao(self, observacao):
        self.__observacao = observacao
