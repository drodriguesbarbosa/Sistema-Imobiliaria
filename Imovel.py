class Imovel (object):
    def __init__(self, codigo_imovel, endereco, codigo_locatario, metragem, qtdQuarto, qtdSala, qtsCozinha, qtdSuite, qtdBanheiro, qtdVaga, qtdVaranda, churrasqueira, piscina):
        self.codigo_imovel = codigo_imovel
        self.endereco = endereco
        self.codigo_locatario = codigo_locatario
        self.metragem = metragem
        self.qtdQuarto = qtdQuarto
        self.qtdSala = qtdSala
        self.qtsCozinha = qtsCozinha
        self.qtdSuite = qtdSuite
        self.qtdBanheiro = qtdBanheiro
        self.qtdVaga = qtdVaga
        self.qtdVaranda = qtdVaranda
        self.churrasqueira = churrasqueira
        self.piscina = piscina


    def __str__(self):
         return""" 
        Endereço: {endereco}
        Código Imóvel: {codigo_imovel}
        Metragem: {metragem}
        """.format(   endereco = self.endereco
                    , codigo_imovel = self.codigo_imovel 
                    , metragem = self.metragem)



