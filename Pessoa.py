class Pessoa(object):

    def __init__(self, nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento):
        self._nome = nome
        self._endereco = endereco 
        self._cpf = cpf 
        self._rg = rg 
        self._estado_civil = estado_civil 
        self._profissao = profissao 
        self._nacionalidade = nacionalidade 
        self._data_de_nascimento = data_de_nascimento 

    def __str__(self):
        return """ 
    Nome : {nome}
    CPF: {cpf}
    Data de Nascimento: {data_de_nascimento}
    """.format(   nome = self.nome
                , cpf = self.cpf 
                , data_de_nascimento = self.data_de_nascimento)

    
    @property
    def nome (self):
        return self.nome

    @nome.setter
    def nome (self, nome):
        self._nome = nome
        return True

    @property
    def endereco (self):
        return self.endereco

    @endereco.setter
    def endereco (self, endereco):
        self._endereco = endereco
        return True

    @property
    def cpf (self):
        return self.cpf

    @cpf.setter
    def cpf (self, cpf):
        self._cpf = cpf
        return True

    @property
    def rg (self):
        return self.rg

    @rg.setter
    def rg (self, rg):
        self._rg = rg
        return True
    
    @property
    def esatdo_civil (self):
        return self.rg

    @rg.setter
    def rg (self, rg):
        self._rg = rg
        return True

    @property
    def profissao (self):
        return self.profissao

    @profissao.setter
    def profissao (self, profissao):
        self._profissao = profissao
        return True
    
    @property
    def nacionalidade (self):
        return self.nacionalidade

    @nacionalidade.setter
    def nacionalidade (self, nacionalidade):
        self._nacionalidade = nacionalidade
        return True

    @property
    def data_de_nascimento (self):
        return self.data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento (self, data_de_nascimento):
        self._data_de_nascimento = data_de_nascimento
        return True