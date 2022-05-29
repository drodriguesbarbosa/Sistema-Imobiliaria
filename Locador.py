from Pessoa import Pessoa

class Locador(Pessoa):

     def __init__(self, nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento, codido_do_locador):
         super().__init__(nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento)
         self.codigo_do_locador = codigo_do_locador
        
