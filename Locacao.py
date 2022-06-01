from Locador import Locador
from Imovel import Imovel


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
    Duração do contrato : {duracao}
    Multa Mora: {multaMora}
    Imóvel: {imovel}
    """.format(   duracao = self.duracao
                , multaMora = self.multaMora 
                , imovel = self.imovel)

    
    @property
    def duracao (self):
        return self.duracao

    @duracao.setter
    def duracao (self, duracao):
        self._duracao = duracao
        return True

    @property
    def valorAluguel (self):
        return self.valorAluguel

    @valorAluguel.setter
    def valorAluguel (self, valorAluguel):
        self._valorAluguel = valorAluguel
        return True

    @property
    def dtPagamento (self):
        return self.dtPagamento

    @dtPagamento.setter
    def dtPagamento (self, dtPagamento):
        self._dtPagamento = dtPagamento
        return True

    @property
    def multaMora (self):
        return self.multaMora

    @multaMora.setter
    def multaMora (self, multaMora):
        self._multaMora = multaMora
        return True

    @property
    def locador (self):
        return self.locador

    @locador.setter
    def locador (self, locador):
        self._locador = locador
        return True

    @property
    def imovel (self):
        return self.imovel

    @imovel.setter
    def imovel (self, imovel):
        self._imovel = imovel
        return True