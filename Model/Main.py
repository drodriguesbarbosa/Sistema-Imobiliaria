from Locatario import Locatario
from Locador import Locador
from Pessoa import Pessoa
from Locacao import Locacao
from Imovel import Imovel
from Apartamento import Apartamento
from Casa import Casa


#Casas
casa1 = Casa(11, 'R Primavera, 11', 60, 60, 2, 1, 1, 1, 2, 1, 1, 1, 2, 'Manual', 'Sim', 'Sim' )
casa2 = Casa(22, 'Rua das Marias, 22', 80, 60, 2, 1, 1, 1, 2, 1, 1, 1, 2,'Manual', 'Sim', 'Sim' )
casa3 = Casa(33, 'Rua teste, 33', 70, 2, 1, 1, 2, 3, 2, 1, 0, 1, 'Elétrico', 'Sim', 'Sim', 'Sim')

#Apartamentos
apartamento1 = Apartamento(44, 'Rua Professora, 10', 80, 2, 3, 1, 1, 1, 1, 1, 0, 'Sim', 'Sim', 8, 'Sim', 4, 2, 185, 'C', 'Sim', 'Sim', 'Sim')
apartamento2 = Apartamento(55, 'Rua Professora, 15', 80, 3, 3, 1, 1, 1, 1, 1, 0, 'sim', 'Sim', 4, 'Sim', 4, 2, 145, 'A', 'Sim', 'Sim', 'Sim')
apartamento3 = Apartamento(66, 'Rua Professora, 20', 70, 2, 1, 1, 1, 2, 2, 1, 1, 'Não', 'Sim', 6, 'Sim', 6, 3, 168, 'B', 'Sim', 'Sim', 'Sim')

lista_de_imoveis = [casa1, casa2, casa3, apartamento1, apartamento2, apartamento3]

#Locadores
locador1 = Locador('Grazieli', 'Rua professora, 10', '111.111.111-11', '1111111-1', 'Casada', 'Atendente', 'Brasileira', '03/05/1996', '111', lista_de_imoveis)
locador2 = Locador('Michelle', 'Rua Professora, 15', '222.222.222-33', '2222222-2', 'Solteira', 'Assistente Adm.', 'Brasileira', '10/05/1982', '222', lista_de_imoveis )
locador3 = Locador('Mario', 'Rua das Marias, 22', '333.333.333-33', '33333333-3', 'Solteiro', 'Motorista', 'Brasileiro', '22/08/2000', '333', lista_de_imoveis)

lista_de_locadores = [locador1, locador2, locador3]

#Locatários
locatario1 = Locatario('Joao', 'Rua teste, 11', '444.444.444-44', '44444444-4', 'Solteiro', 'Corretor', 'brasileiro', '20/06/1994', 444)
locatario2 = Locatario('Laura', 'Rua teste, 22', '555.555.555-55', '5555555-5', 'Casado', 'Gerente', 'Brasileira', '18/02/1997', 555)
locatario3 = Locatario('Maria', 'Rua teste 33', '666.666.666-6', '66666666-6', 'Solteira', 'Vendedora', 'Brasileira', '03/07/1983', 666)

lista_de_locatarios = [locatario1, locatario2, locatario3]

#Locações
locacao1 = Locacao(11, '2 anos', 'R$ 900,00', '05', 'R$ 50,00', 111)
locacao2 = Locacao(66, '3 anos', 'R$ 1500,00', '01', 'R$ 100,00', 66)
locacao3 = Locacao(44, '2 anos', 'R$ 1000,00', '10', 'R$ 60,00', 444)

listade_locacoes = [locacao1, locacao2, locacao3]

print(locador2._lista_de_imoveis)
print(casa1.endereco)
print(apartamento1.apPorAndar)
print(locador1.codigo_do_locador)

#imovel1 = Imovel(2010, 'R tal', 20, 1, 1, 1, 1, 1, 1, 1, 1, 1)
#print(imovel1.codigo_imovel)
#imovel1.codigo_imovel = 2011
#print(imovel1.codigo_imovel)

print(locatario1._endereco)


locatario1._endereco = ('testando de novo')
print (locatario1._endereco)
