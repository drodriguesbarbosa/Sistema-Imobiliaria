from Locatario import Locatario
from Locador import Locador
from Pessoa import Pessoa
from Locacao import Locacao
from Imovel import Imovel
from Apartamento import Apartamento
from Casa import Casa

casa1 = Casa(11, 'R Primavera 22', 10, 60, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 'Sim', 'Sim' )
apartamento1 = Apartamento(22, 'R Professora 10', 80, 50, 3, 1, 1, 0, 1, 1, 1, 0, 0, 'Sim', 6, 'Sim', 4, 2, 45, 'B', 'Sim', 'Sim', 'Sim')
locador1 = Locador('Daniela', 'R Pitangueiras 10', '111.111.111.11', '000000000', 'Solteira', 'Ass. Administrativo', 'Brasileira', '24/07/1994', '33')

print(casa1)
print(apartamento1)
print(locador1)



