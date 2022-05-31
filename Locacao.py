from Locador import Locador
from Imovel import Imovel


class Locacao():

    def __init__(self, imovel, duracao, valorAluguel, dtPagamento, multaMora, locador):
        self.duracao = duracao
        self.valorAluguel = valorAluguel
        self.dtPagamento = dtPagamento
        self.multaMora = multaMora
        self.locador = locador
        self.imovel = imovel

    def __str__(self):
        return """ 
    Duração do contrato : {duracao}
    Multa Mora: {multaMora}
    Imóvel: {imovel}
    """.format(   duracao = self.duracao
                , multaMora = self.multaMora 
                , imovel = self.imovel)