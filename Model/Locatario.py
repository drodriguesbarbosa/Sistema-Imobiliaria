from Pessoa import Pessoa

class Locatario(Pessoa):

    def __init__(self, nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento, codigo_do_locatario):
        super().__init__(nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento)
        self._codigo_do_locatario = codigo_do_locatario


    def __str__(self):
        return """ 
        Código do locatário : {codigo_do_locatario}
        CPF: {cpf}
        Nacionalidade: {nacionalidade}
        """.format(   codigo_do_locatario = self.codigo_do_locatario
                    , cpf = self.cpf 
                    , nacionalidade = self.nacionalidade)
       
    @property
    def codigo_do_locatario (self):
        return self._codigo_do_locatario

    @codigo_do_locatario.setter
    def codigo_do_locatario (self, codigo_do_locatario):
        self._codigo_do_locatario = codigo_do_locatario
        return True