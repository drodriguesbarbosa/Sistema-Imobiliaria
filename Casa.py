from Imovel import Imovel

class Casa(Imovel):
    def __init__(self, codigo_imovel, endereco, metragem, qtdQuarto, qtdSala, qtsCozinha, qtdSuite, qtdBanheiro, qtdVaga, qtdVaranda, churrasqueira, piscina, portao, quintal, alarme, segurancaRua):
        super().__init__(codigo_imovel, endereco, metragem, qtdQuarto, qtdSala, qtsCozinha, qtdSuite, qtdBanheiro, qtdVaga, qtdVaranda, churrasqueira, piscina)
        self._portao = portao 
        self._quintal = quintal
        self._alarme = alarme
        self._segurancaRua = segurancaRua

    def __str__(self):
        return """ 
    Portão: {portao}
    Código Imóvel: {codigo_imovel}
    Segurança da Rua: {segurancaRua}
    """.format(   portao = self.portao
                , codigo_imovel = self.codigo_imovel 
                , segurancaRua = self.segurancaRua)

    
      
    @property
    def portao(self):
        return self._portao

    @portao.setter
    def portao (self, portao):
        self._portao = portao
        return True 

    @property
    def quintal(self):
        return self._quintal

    @quintal.setter
    def quintal (self, quintal):
        self._quintal = quintal
        return True

    @property
    def alarme(self):
        return self._alarme

    @alarme.setter
    def alarme (self, alarme):
        self._alarme = alarme
        return True

    @property
    def segurancaRua (self):
        return self._segurancaRua

    @segurancaRua.setter
    def segurancaRua (self, segurancaRua):
        self._segurancaRua = segurancaRua
        return True





