from Model.Imovel import Imovel
from Model.Locacao import Locacao
from Model.Locador import Locador
from Model.Locatario import Locatario


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
        codigo_locador_pesquisar = input ('Insira o código do locador: ')
        for item in self.lista_de_locadores:
            if codigo_locador_pesquisar == self.lista_de_locadores:
                print (item)
                break 
                
    def atualizar_locador(self):
        codigo_locador_atualizar = input('digite o codigo do locador que deseja alterar')
        for item in self.lista_de_locadores:
            if codigo_locador_atualizar == self.lista_de_locadores:
                print(item)
                print ('Insira as informações a seguir sobre o locatário que deseja atualizar: ')
                nome = input ('Nome: ')
                endereco = input ('Endereço: ')
                cpf = input ('CPF: ')
                rg = input ('RG: ')
                estado_civil = input ('Estado civil: ')
                profissao = input ('Profissão: ')
                nacionalidade = input ('Nacionalidade: ' )
                data_de_nascimento = input ('Data de nascimento: ')
                codigo_do_locador = input ('Código do locador: ')

                break



#FUNÇÕES DE IMÓVEL
    def cadastro_de_imoveis (self):
        print ('Insira as informações a seguir sobre os imóveis que deseja cadastrar: ')
        codigo_imovel = input ('Código do imóvel: ')
        endereco = input ('Endereço: ')
        metragem = input ('Metragem: ')
        qtdQuarto = input ('Quantidade de quartos: ')
        qtdSala = input ('Quantidade de salas: ')
        qtdCozinha = input ('Quantidade de cozinhas')
        qtdSuite = input ('Quantidade de suítes: ')
        qtdBanheiro = input ('Quantidade de banheiros: ')
        qtdVaga = input ('Quantidade de Vagas: ')
        qtdVaranda = input ('Quantidade de varandas: ')
        churrasqueira = input ('Churrasqueira? Sim/Não ')
        piscina = input ('Piscina? Sim/Não: ')

        imovel1 = Imovel(codigo_imovel, endereco, metragem, qtdQuarto, qtdSala, qtdCozinha, qtdSuite, qtdBanheiro, qtdVaga, qtdVaranda, churrasqueira, piscina)
        self.lista_de_imoveis.append (imovel1)

    def mostrar_todos_imoveis (self):
        for item in self.lista_de_imoveis:
            print('- Codigo:' + str(item.codigo_imovel + '\n - Endereço: '+ str(item.endereco)))

    def pesquisar_imoveis (self):
        codigo_imovel_pesquisar = input ('Insira o código do imóvel: ')
        for item in self.lista_de_imoveis:
            if codigo_imovel_pesquisar == self.lista_de_imoveis:
                print (item)
                break 
                
    def atualizar_imoveis (self):
        codigo_imovel_atualizar = input('Digite o codigo do Imóvel que deseja alterar')
        for item in self.lista_de_imoveis:
            if codigo_imovel_atualizar == self.lista_de_imoveis:
                print(item)
                print ('Insira as informações a seguir sobre o imóvel que deseja atualizar: ')
                codigo_imovel = input ('Código do imóvel: ')
                endereco = input ('Endereço: ')
                metragem = input ('Metragem: ')
                qtdQuarto = input ('Quantidade de quartos: ')
                qtdSala = input ('Quantidade de salas: ')
                qtdCozinha = input ('Quantidade de cozinhas')
                qtdSuite = input ('Quantidade de suítes: ')
                qtdBanheiro = input ('Quantidade de banheiros: ')
                qtdVaga = input ('Quantidade de Vagas: ')
                qtdVaranda = input ('Quantidade de varandas: ')
                churrasqueira = input ('Churrasqueira? Sim/Não ')
                piscina = input ('Piscina? Sim/Não: ')
                break

#FUNÇÕES DE LOCATARIOS

    def cadastro_de_locatarios (self):
        print ('Insira as informações a seguir sobre os locatários que deseja cadastrar: ')
        nome = input ('Nome: ')
        endereco = input ('Endereço: ')
        cpf = input ('Endereço: ')
        rg = input ('RG: ')
        estado_civil = input ('Estado civi: ')
        profissao = input ('Profissão: ')
        nacionalidade = input ('Nacionalidade: ')
        data_de_nascimento = input ('Data de Nascimento, ex. 00/00/0000: ')
        codigo_do_locatario = input ('Código do locatário: ')

        locatario1 = Locatario(nome, endereco, cpf, rg, estado_civil, profissao, nacionalidade, data_de_nascimento, codigo_do_locatario)
        self.lista_de_locatarios.append (locatario1)

    def mostrar_todos_locatarios (self):
        for item in self.lista_de_locatarios:
            print('- Codigo:' + str(item.codigo_do_locatario + '\n - Nome: '+ str(item.nome)))

    def pesquisar_locatarios (self):
        codigo_locatario_pesquisar = input ('Insira o código do locatário: ')
        for item in self.lista_de_locatarios:
            if codigo_locatario_pesquisar == self.lista_de_locatarios:
                print (item)
                break 
                
    def atualizar_locatario (self):
        codigo_do_locatario_atualizar = input('Digite o codigo do Locatário que deseja alterar')
        for item in self.lista_de_locatarios:
            if codigo_do_locatario_atualizar == self.lista_de_locatarios:
                print(item)
                print ('Insira as informações a seguir sobre o locatário que deseja atualizar: ')
                nome = input ('Nome: ')
                endereco = input ('Endereço: ')
                cpf = input ('Endereço: ')
                rg = input ('RG: ')
                estado_civil = input ('Estado civi: ')
                profissao = input ('Profissão: ')
                nacionalidade = input ('Nacionalidade: ')
                data_de_nascimento = input ('Data de Nascimento, ex. 00/00/0000: ')
                codigo_do_locatario = input ('Código do locatário: ')
                break

#FUNÇÕES DE LOCAÇÕES
    def cadastro_de_locacoes (self):
        print ('Insira as informações a seguir sobre as locações que deseja cadastrar: ')
        imovel = input ('Casa ou apartamento: ')
        duracao = input ('Duração do contrato: ')
        valorAluguel = input ('Valor do aluguel: ')
        dtPagamento = input ('Data de pagamento: ')
        multaMora = input ('Valor da multa: ')
        locador = input ('Digite o código do locador: ')

        locacao1 = Locacao (imovel, duracao, valorAluguel, dtPagamento, multaMora, locador)
        self.lista_de_locacoes.append (locacao1)

    def mostrar_todas_locacoes (self):
        for item in self.lista_de_locacoes:
            print('- Imóvel:' + str(item.imovel + '\n - Valor do aluguel: '+ str(item.valorAluguel)))

    def pesquisar_locacoes (self):
        locacao_pesquisar = input ('Insira o código do locatário: ')
        for item in self.lista_de_locacoes:
            if locacao_pesquisar == self.lista_de_locacoes:
                print (item)
                break 
                
    def atualizar_locacoes (self):
        locacao_altuaizar = input('Digite o codigo do Locador que deseja alterar')
        for item in self.lista_de_locadores:
            if locacao_altuaizar == self.lista_de_locacoes:
                print(item)
                print ('Insira as informações a seguir sobre a locacao que deseja atualizar: ')
                imovel = input ('Digite o imovel: ')
                duracao = input ('Duração do contrato: ')
                valorAluguel = input ('Valor do aluguel: ')
                dtPagamento = input ('Data de pagamento: ')
                multaMora = input ('Valor da multa: ')
                locador = input ('Digite o código do locador: ')
                break
