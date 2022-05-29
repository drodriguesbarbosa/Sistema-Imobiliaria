from mailbox import NotEmptyError

from pkg_resources import ensure_directory


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
