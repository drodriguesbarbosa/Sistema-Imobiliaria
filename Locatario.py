from Pessoa import Pessoa

class Locatario(Pessoa):

     def __init__(self, nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento, codido_do_locatario):
         super().__init__(nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento)
         self.codigo_do_locatario = codigo_do_locatario