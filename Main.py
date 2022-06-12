from typing_extensions import Self
from Controller.Controller import Controler

class menus():

    def menu_locatario (opcao_locatario):
        try:
            if opcao_locatario == 1:
                cadastro_de_locatarios(self)
            elif opcao_locatario == 2:
                mostrar_todos_locatarios(self)
            elif opcao_locatario == 3:
                pesquisar_locatarios(self)  
            elif opcao_locatario == 4:
                atualizar_locatario(self)
            elif opcao_locatario == 5:
                exibir_menu()
            elif opcao_locatario == 6:
                print('Sistema Finalizado!')
            else:
                print('Opção inválida')
            return True
        except Exception as ex:
            print('Erro durante seleção de opções: ' + str(ex))
            return False   
        
    def menu_locadores (opcao_locador):
        try:
            if opcao_locador == 1:
                cadastro_de_locadores(self)
            elif opcao_locador == 2:
                mostrar_todos_locadores(self)
            elif opcao_locador == 3:
                pesquisar_locadores(self)  
            elif opcao_locador == 4:
                atualizar_locadores(self)
            elif opcao_locador == 5:
                exibir_menu()
            elif opcao_locador == 6:
                print('Sistema Finalizado!')
            else:
                print('Opção inválida')
            return True
        except Exception as ex:
            print('Erro durante seleção de opções: ' + str(ex))
            return False   
            
    def menu_locacoes (opcao_locacoes):
        try:
            if opcao_locacoes == 1:
                cadastro_de_locacoes(self)
            elif opcao_locacoes == 2:
                mostrar_todas_locacoes(self)
            elif opcao_locacoes == 3:
                pesquisar_locacoes(self)  
            elif opcao_locacoes == 4:
                atualizar_locacoes(self)
            elif opcao_locacoes == 5:
                exibir_menu()
            elif opcao_locacoes == 6:
                print('Sistema Finalizado!')
            else:
                print('Opção inválida')
            return True
        except Exception as ex:
            print('Erro durante seleção de opções: ' + str(ex))
            return False 
            
    def menu_imoveis (opcao_imoveis):
        try:
            if opcao_imoveis == 1:
                cadastro_de_imoveis(self)
            elif opcao_imoveis == 2:
                mostrar_todos_imoveis(self)
            elif opcao_imoveis == 3:
                pesquisar_imoveis(self)  
            elif opcao_imoveis == 4:
                atualizar_imoveis(self)
            elif opcao_imoveis == 5:
                exibir_menu()
            elif opcao_imoveis == 6:
                print('Sistema Finalizado!')
            else:
                print('Opção inválida')
            return True
        except Exception as ex:
            print('Erro durante seleção de opções: ' + str(ex))
            return False 

