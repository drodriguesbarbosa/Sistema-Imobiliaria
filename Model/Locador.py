from Model.Pessoa import Pessoa

class Locador(Pessoa):

    def __init__(self, nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento, codigo_do_locador, lista_de_imoveis):
        super().__init__(nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento)
        self._codigo_do_locador = codigo_do_locador
        self._lista_de_imoveis = lista_de_imoveis

    
    def __str__(self):
        return """ 
    Nome: {nome}
    Código de locador: {codigo_do_locador}
    Endereço: {endereco}
    CPF: {cpf}
    RG: {rg}
    Estado civil: {estado_civil}
    Profissão: {profissao}
    Nacionalidade: {nacionalidade}
    Data de nascimento: {data_de_nascimento}
    Lista de imóveis: {lista_de_imoveis}
    """.format(   nome = self.nome
                , codigo_do_locador = self._codigo_do_locador
                , endereco = self.endereco
                , cpf = self.cpf 
                , rg = self.rg
                , estado_civil = self.estado_civil
                , profissao = self.profissao
                , nacionalidade = self.nacionalidade
                , data_de_nascimento = self.data_de_nascimento
                , lista_de_imoveis = self.lista_de_imoveis)

    @property
    def codigo_do_locador (self):
        return self._codigo_do_locador

    @codigo_do_locador.setter
    def codigo_do_locador (self, codigo_do_locador):
        self._codigo_do_locador = codigo_do_locador
        return True
        
    @property
    def lista_de_imoveis (self):
        return self._lista_de_imoveis

    @lista_de_imoveis.setter
    def lista_de_imoveis (self, lista_de_imoveis):
        self._lista_de_imoveis = lista_de_imoveis
        return True