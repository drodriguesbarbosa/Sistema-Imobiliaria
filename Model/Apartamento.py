from Model.Imovel import Imovel

class Apartamento(Imovel):
    def __init__(self, codigo_imovel, endereco, metragem, qtdQuarto, qtdSala, qtsCozinha, qtdSuite, qtdBanheiro, qtdVaga, qtdVaranda, churrasqueira, piscina, porteiro, apPorAndar, permiteAnimais, andar, qtdElevador, numApartamento, bloco, playground, salaoDeFesta, academia):
        super().__init__(codigo_imovel, endereco, metragem, qtdQuarto, qtdSala, qtsCozinha, qtdSuite, qtdBanheiro, qtdVaga, qtdVaranda, churrasqueira, piscina)
        self._porteiro = porteiro
        self._apPorAndar = apPorAndar
        self._permiteAnimais = permiteAnimais
        self._andar = andar
        self._qtdElevador = qtdElevador
        self._numApartamento = numApartamento
        self._bloco = bloco
        self._playground = playground
        self._salaoDeFesta = salaoDeFesta
        self._academia = academia

    def __str__(self):
        return """ 
Código do imóvel: {codigo_imovel}
Endereço: {endereco}
Metragem: {metragem}
Quartos: {qtdQuarto}
Sala: {qtdSala}
Cozinha: {qtdCozinha}
Suítes:{qtdSuite}
Banheiros: {qtdBanheiro}
Vagas na garagem: {qtdVaga}
Varanda: {qtdVaranda}
Churrasqueira: {churrasqueira}
Piscina: {piscina}
Porteiro: {porteiro}
Apartamentos por andar: {apPorAndar}
Permite animais: {permiteAnimais}
Andar: {andar}
Elevadores: {qtdElevador}
Número do apartamento: {numApartamento}
Bloco: {bloco}
Playground: {playground}
Salão de festa: {salaoDeFesta}
Academia: {academia}
    """.format(   codigo_imovel = self.codigo_imovel
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
                , piscina = self.piscina
                , porteiro = self.porteiro
                , apPorAndar = self.apPorAndar
                , permiteAnimais = self.permiteAnimais
                , andar = self.andar
                , qtdElevador = self.qtdElevador
                , numApartamento = self.numApartamento
                , bloco = self.bloco
                , playground = self.playground
                , salaoDeFesta = self.salaoDeFesta 
                , academia = self.academia)

    @property
    def porteiro (self):
        return self._porteiro

    @porteiro.setter
    def porteiro (self, porteiro):
        self._porteiro = porteiro
        return True

    @property
    def apPorAndar (self):
        return self._apPorAndar

    @apPorAndar.setter
    def apPorAndar (self, apPorAndar):
        self._apPorAndar = apPorAndar
        return True

    @property
    def permiteAnimais (self):
        return self._permiteAnimais

    @permiteAnimais.setter
    def permiteAnimais (self, permiteAnimais):
        self._permiteAnimais = permiteAnimais
        return True

    @property
    def andar (self):
        return self._andar

    @andar.setter
    def andar (self, andar):
        self._andar = andar
        return True
    
    @property
    def qtdElevador (self):
        return self._qtdElevador

    @qtdElevador.setter
    def qtdElevador (self, qtdElevador):
        self._qtdElevador = qtdElevador
        return True

    @property
    def numApartamento (self):
        return self._numApartamento

    @numApartamento.setter
    def numApartamento (self, numApartamento):
        self._numApartamento = numApartamento
        return True

    @property
    def bloco (self):
        return self._bloco

    @bloco.setter
    def bloco (self, bloco):
        self._bloco = bloco
        return True

    @property
    def playground (self):
        return self._playground

    @playground.setter
    def playground (self, playground):
        self._playground = playground
        return True

    @property
    def salaoDeFesta (self):
        return self._salaoDeFesta

    @salaoDeFesta.setter
    def salaoDeFesta (self, salaoDeFesta):
        self._salaoDeFesta = salaoDeFesta
        return True

    @property
    def academia (self):
        return self._academia

    @academia.setter
    def academia (self, academia):
        self._academia = academia
        return True