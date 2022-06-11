from Pessoa import Pessoa

class Locatario(Pessoa):

    def __init__(self, nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento, codigo_do_locatario):
        super().__init__(nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento)
        self._codigo_do_locatario = codigo_do_locatario


    def __str__(self):
        return """ 
        Nome: {nome}
        Código do locatário : {codigo_do_locatario}
        Endereço: {endereco}
        CPF: {cpf}
        RG: {rg}
        Estado civil: {estado_civil}
        Profissão: {profissao}
        Nacionalidade: {nacionalidade}
        Data de nascimento: {data_de_nascimento}
        """.format(   nome = self.nome
                    , codigo_do_locatario = self.codigo_do_locatario
                    , endereco = self.endereco
                    , cpf = self.cpf 
                    , rg = self.rg
                    , estado_civil = self.estado_civil
                    , profissao = self.profissao
                    , nacionalidade = self.nacionalidade
                    , data_de_nascimento = self.data_de_nascimento)
       
    @property
    def codigo_do_locatario (self):
        return self._codigo_do_locatario

    @codigo_do_locatario.setter
    def codigo_do_locatario (self, codigo_do_locatario):
        self._codigo_do_locatario = codigo_do_locatario
        return True