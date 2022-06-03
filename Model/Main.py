from Locatario import Locatario
from Locador import Locador
from Pessoa import Pessoa
from Locacao import Locacao
from Imovel import Imovel
from Model.Apartamento import Apartamento
from Casa import Casa



casa1 = Casa(11, 'R Primavera 22', 10, 60, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 'Sim', 'Sim' )
apartamento1 = Apartamento(22, 'R Professora 10', 80, 50, 3, 1, 1, 1, 1, 1, 0, 0, 'Sim', 6, 'Sim', 4, 2, 45, 'B', 'Sim', 'Sim', 'Sim')
locador1 = Locador('Daniela', 'R Pitangueiras 10', '111.111.111.11', '000000000', 'Solteira', 'Ass. Administrativo', 'Brasileira', '24/07/1994', '33', [])
casa2 = Casa(11, 'R Primavera 30', 10, 60, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 'Sim', 'Sim' )
apartamento2 = Apartamento(22, 'R Professora 15', 80, 50, 3, 1, 1, 1, 1, 1, 0, 0, 'Sim', 6, 'Sim', 4, 2, 45, 'B', 'Sim', 'Sim', 'Sim')

lista_de_imoveis = [casa1, casa2, apartamento1, apartamento2]

locador2 = Locador('Grazieli', 'R de casa', '22222222222', '2232222', 'casada', 'atendente', 'brasileira', '03/05/1996', 20, lista_de_imoveis)





print(locador2.lista_de_imoveis)
print(casa1)
print(apartamento1)
print(locador1)

imovel1 = Imovel(2010, 'R tal', 20, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(imovel1.codigo_imovel)
imovel1.codigo_imovel = 2011
print(imovel1.codigo_imovel)

locatario1 = Locatario('Joao', 'R teste', '5555554', '5454451', 'Solteiro', 'teste', 'brasileiro', '20/06/1994', 2017)
print(locatario1._endereco)


