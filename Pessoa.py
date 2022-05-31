class Pessoa(object):

    def __init__(self, nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento):
        self.nome = nome
        self.endereco = endereco 
        self.cpf = cpf 
        self.rg = rg 
        self.estado_civil = estado_civil 
        self.profissao = profissao 
        self.nacionalidade = nacionalidade 
        self.data_de_nascimento = data_de_nascimento 

    def __str__(self):
        return """ 
    Nome : {nome}
    CPF: {cpf}
    Data de Nascimento: {data_de_nascimento}
    """.format(   nome = self.nome
                , cpf = self.cpf 
                , data_de_nascimento = self.data_de_nascimento)