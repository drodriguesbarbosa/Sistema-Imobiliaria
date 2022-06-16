from Model.Locador import Locador
from Model.Imovel import Imovel


class Locacao():

    def __init__(self, imovel, duracao, valorAluguel, dtPagamento, multaMora, locador):
        self._duracao = duracao
        self._valorAluguel = valorAluguel
        self._dtPagamento = dtPagamento
        self._multaMora = multaMora
        self._locador = locador
        self._imovel = imovel

    def __str__(self):
        return """ 
    Imóvel: {imovel}
    Duração do contrato : {duracao}
    Valor do aluguel: {valorAluguel}
    Data de pagamento: {dtPagamento}
    Multa Mora: {multaMora}
    Locador: {locador}
    """.format(   imovel = self.imovel
                , duracao = self.duracao
                , valorAluguel = self.valorAluguel
                , dtPagamento = self.dtPagamento
                , multaMora = self.multaMora 
                , locador = self.locador)

    
    @property
    def duracao (self):
        return self._duracao

    @duracao.setter
    def duracao (self, duracao):
        self._duracao = duracao
        return True

    @property
    def valorAluguel (self):
        return self._valorAluguel

    @valorAluguel.setter
    def valorAluguel (self, valorAluguel):
        self._valorAluguel = valorAluguel
        return True

    @property
    def dtPagamento (self):
        return self._dtPagamento

    @dtPagamento.setter
    def dtPagamento (self, dtPagamento):
        self._dtPagamento = dtPagamento
        return True

    @property
    def multaMora (self):
        return self._multaMora

    @multaMora.setter
    def multaMora (self, multaMora):
        self._multaMora = multaMora
        return True

    @property
    def locador (self):
        return self._locador

    @locador.setter
    def locador (self, locador):
        self._locador = locador
        return True

    @property
    def imovel (self):
        return self._imovel

    @imovel.setter
    def imovel (self, imovel):
        self._imovel = imovel
        return True