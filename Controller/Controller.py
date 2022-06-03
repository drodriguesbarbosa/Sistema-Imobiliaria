from Model.Locador import Locador


class Controler():
    def __init__(self):
        self.lista_de_locadores = []
        self.lista_de_imoveis = []
        self.lista_de_locatarios = []
        self.lista_de_locacoes = []

    def cadastro_de_locador (self):
        print ('Insira as informações a seguir sobre o locatários que deseja cadastrar: ')
        nome = input ('Nome: ')
        endereco = input ('Endereço: ')
        cpf = input ('CPF: ')
        rg = input ('RG: ')
        estado_civil = input ('Estado civil: ')
        profissao = input ('Profissão: ')
        nacionalidade = input ('Nacionalidade: ' )
        data_de_nascimento = input ('Data de nascimento: ')
        codigo_do_locador = input ('Código do locador: ')

        locador1 = Locador(nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento, codigo_do_locador)
        self.lista_de_locadores.append (locador1)

    def mostrar_todos_locadores (self):
        for item in self.lista_de_locadores:
            print('- Codigo:' + str(item.codigo_locador + '\n - Nome: '+ str(item.nome)))

    def pesquisar_locador (self):
        codigo_locador = input ('Insira o código do locador: ')
        for item in self.lista_de_locadores:
            if codigo_locador == self.lista_de_locadores:
                print (item)
                break 
                
    def atualizar_locador(self):
        codigo_locador = input('digite o codigo do locador que deseja alterar')
        for item in self.lista_de_locadores:
            if codigo_locador == self.lista_de_locadores:
                print(item)
                print ('Insira as informações a seguir sobre o locatários que deseja cadastrar: ')
                nome = input ('Nome: ')
                endereco = input ('Endereço: ')
                cpf = input ('CPF: ')
                rg = input ('RG: ')
                estado_civil = input ('Estado civil: ')
                profissao = input ('Profissão: ')
                nacionalidade = input ('Nacionalidade: ' )
                data_de_nascimento = input ('Data de nascimento: ')
                codigo_do_locador = input ('Código do locador: ')

# Solicitar aqui todas as informacoes do cadastro, e atualizar os atributos com os valores novos

                break



