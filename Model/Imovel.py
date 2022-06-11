class Imovel (object):
    def __init__(self, codigo_imovel, endereco, metragem, qtdQuarto, qtdSala, qtdCozinha, qtdSuite, qtdBanheiro, qtdVaga, qtdVaranda, churrasqueira, piscina):
        self._codigo_imovel = codigo_imovel
        self._endereco = endereco
        self._metragem = metragem
        self._qtdQuarto = qtdQuarto
        self._qtdSala = qtdSala
        self._qtdCozinha = qtdCozinha
        self._qtdSuite = qtdSuite
        self._qtdBanheiro = qtdBanheiro
        self._qtdVaga = qtdVaga
        self._qtdVaranda = qtdVaranda
        self._churrasqueira = churrasqueira
        self._piscina = piscina


    def __str__(self):
         return""" 
        Código do imóvel: {codigo_imovel}
        Endereço:  {endereco}
        Metragem: {metragem}
        Quartos: {qtdQuarto}
        Sala: {qtdSala}
        Cozinha: {qtdCozinha}
        Suíte: {qtdSuite}
        Banheiro: {qtdBanheiro}
        Número de vagas: {qtdVaga}
        Varanda: {qtdVaranda}
        Churrasqueira: {churrasqueira}
        Piscina: {piscina}
        """.format(   codigo_imovel =  self.codigo_imovel
                    , endereco = self.endereco 
                    , metragem = self.metragem
                    , qtdQuarto = self.qtdQuarto
                    , qtdSala = self.qtdSala
                    , qtdCozinha = self.qtdCozinha
                    , qtdSuite = self.qtdSuite
                    , qtdBanheiro = self.qtdBanheiro
                    , qtdVaga = self.qtdVaga
                    , qtdVaranda = self.qtdVaranda
                    , churrasqueira = self.churrasqueira
                    , piscina = self.piscina)

    @property
    def codigo_imovel(self):
        return self._codigo_imovel

    @codigo_imovel.setter
    def codigo_imovel(self, codigo_imovel):
        self._codigo_imovel = codigo_imovel
        return True

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
        return True

    @property
    def metragem(self):
        return self._metragem

    @metragem.setter
    def metragem(self, metragem):
        self._metragem = metragem
        return True
 
    @property
    def qtdQuarto(self):
        return self._qtdQuarto
    
    @qtdQuarto.setter
    def qtdQuarto(self, qtdQuarto):
        self._qtdQuarto = qtdQuarto
        return True

    @property
    def qtdSala(self):
        return self._qtdSala

    @qtdSala.setter
    def qtdSala(self, qtdSala):
        self._qtdSala = qtdSala
        return True
    
    @property
    def qtdCozinha(self):
        return self._qtdCozinha

    @qtdCozinha.setter
    def qtdCozinha(self, qtdCozinha):
        self._qtdCozinha = qtdCozinha
        return True
    
    @property
    def qtdSuite(self):
        return self._qtdSuite

    @qtdSuite.setter
    def qtdSuite(self, qtdSuite):
        self._qtdSuite = qtdSuite
        return True

    @property
    def qtdBanheiro(self):
        return self._qtdBanheiro

    @qtdBanheiro.setter
    def qtdBanheiro(self, qtdBanheiro):
        self._qtdBanheiro = qtdBanheiro
        return True

    @property
    def qtdVaga(self):
        return self._qtdVaga

    @qtdVaga.setter
    def qtdVaga(self, qtdVaga):
        self._qtdVaga = qtdVaga
        return True
    
    @property
    def qtdVaranda(self):
        return self._qtdVaranda

    @qtdVaranda.setter
    def qtdVaranda(self, qtdVaranda):
        self._qtdVaranda = qtdVaranda
        return True
    
    @property
    def churrasqueira(self):
        return self._churrasqueira

    @churrasqueira.setter
    def churrasqueira(self, churrasqueira):
        self._churrasqueira = churrasqueira
        return True

    @property
    def piscina(self):
        return self._piscina

    @piscina.setter
    def piscina(self, piscina):
        self._piscina = piscina
        return True

    
