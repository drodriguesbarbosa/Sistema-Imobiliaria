from Imovel import Imovel

class Casa(Imovel):
    def __init__(self, codigo_imovel, endereco, codigo_locatario, metragem, qtdQuarto, qtdSala, qtsCozinha, qtdSuite, qtdBanheiro, qtdVaga, qtdVaranda, churrasqueira, piscina, portao, quintal, alarme, segurancaRua):
        super().__init__(codigo_imovel, endereco, codigo_locatario, metragem, qtdQuarto, qtdSala, qtsCozinha, qtdSuite, qtdBanheiro, qtdVaga, qtdVaranda, churrasqueira, piscina)
        self.portao = portao 
        self.quintal = quintal
        self.alarme = alarme
        self.segurancaRua = segurancaRua

    def __str__(self):
            return""" 
            Portão: {portao}
            Código Imóvel: {codigo_imovel}
            Segurança da Rua: {segurancaRua}
            """.format(   portao = self.portao
                        , codigo_imovel = self.codigo_imovel 
                        , segurancaRua = self.segurancaRua)
                        