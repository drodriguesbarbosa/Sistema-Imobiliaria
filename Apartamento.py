from Imovel import Imovel

class Apartamento(Imovel):
    def __init__(self, codigo_imovel, endereco, codigo_locatario, metragem, qtdQuarto, qtdSala, qtsCozinha, qtdSuite, qtdBanheiro, qtdVaga, qtdVaranda, churrasqueira, piscina, porteiro, apPorAndar, permiteAnimais, andar, qtdElevador, numApartamento, bloco, playground, salaoDeFesta, academia):
        super().__init__(codigo_imovel, endereco, codigo_locatario, metragem, qtdQuarto, qtdSala, qtsCozinha, qtdSuite, qtdBanheiro, qtdVaga, qtdVaranda, churrasqueira, piscina)
        self.porteiro = porteiro
        self.apPorAndar = apPorAndar
        self.permiteAnimais = permiteAnimais
        self.andar = andar
        self.qtdElevador = qtdElevador
        self.numApartamento = numApartamento
        self.bloco = bloco
        self.playground = playground
        self.salaoDeFesta = salaoDeFesta
        self.academia = academia

    def __str__(self):
        return """ 
    Porteiro: {porteiro}
    Andar: {andar}
    Academia: {academia}
    """.format(   porteiro = self.porteiro
                , andar = self.andar 
                , academia = self.academia)
