from Pessoa import Pessoa

class Locador(Pessoa):

    def __init__(self, nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento, codigo_do_locador):
        super().__init__(nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento)
        self._codigo_do_locador = codigo_do_locador

    
    def __str__(self):
        return """ 
    Código do locador : {codigo_do_locador}
    CPF: {cpf}
    Nacionalidade: {nacionalidade}
    """.format(   codigo_do_locador = self.codigo_do_locador
                , cpf = self.cpf 
                , nacionalidade = self.nacionalidade)

    @property
    def codigo_do_locador (self):
        return self.codigo_do_locador

    @codigo_do_locador.setter
    def codigo_do_locador (self, codigo_do_locador):
        self._codigo_do_locador = codigo_do_locador
        return True
        
