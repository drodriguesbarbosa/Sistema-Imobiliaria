from Model.Imovel import Imovel
from Model.Locacao import Locacao
from Model.Locador import Locador
from Model.Locatario import Locatario
from Controller.Controller import Controler

locadorteste = Locador('katy', 'r testando', '55522222222', '8888888', 'teste', 'testando ainda', 'brasileiro', '00/00/0000', 40, 22)
imovelTeste = Imovel(22, 'teste', 22, 11, 1, 1, 1, 1, 1, 1, 1, 1)
locacaoteste = Locacao(22, '2 anos', 'R$ 700,00', '5', 'R$ 20,00', 10)
print(imovelTeste.codigo_imovel)