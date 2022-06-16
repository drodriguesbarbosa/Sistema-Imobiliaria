from Controller import Controller as ct


class Faced():
    def __init__(self):
      self.id = 1
      
    def menu_locatario (self,opcao_locatario):
        try:
            if opcao_locatario == 1:
                ct.cadastro_de_locatarios()
            elif opcao_locatario == 2:
                ct.mostrar_todos_locatarios()
            elif opcao_locatario == 3:
                ct.pesquisar_locatarios()  
            elif opcao_locatario == 4:
                ct.atualizar_locatario()
            elif opcao_locatario == 5:
                ct.exibir_menu()
            elif opcao_locatario == 6:
                print('Sistema Finalizado!')
            else:
                print('Opção inválida')
            return True
        except Exception as ex:
            print('Erro durante seleção de opções: ' + str(ex))
            return False   
        
    def menu_locadores (self,opcao_locador):
        try:
            if opcao_locador == 1:
                ct.cadastro_de_locadores()
            elif opcao_locador == 2:
                ct.mostrar_todos_locadores()
            elif opcao_locador == 3:
                ct.pesquisar_locadores()  
            elif opcao_locador == 4:
                ct.atualizar_locadores()
            elif opcao_locador == 5:
                ct.exibir_menu()
            elif opcao_locador == 6:
                print('Sistema Finalizado!')
            else:
                print('Opção inválida')
            return True
        except Exception as ex:
            print('Erro durante seleção de opções: ' + str(ex))
            return False   
            
    def menu_locacoes (self,opcao_locacoes):
        try:
            if opcao_locacoes == 1:
                ct.cadastro_de_locacoes()
            elif opcao_locacoes == 2:
                ct.mostrar_todas_locacoes()
            elif opcao_locacoes == 3:
                ct.pesquisar_locacoes()  
            elif opcao_locacoes == 4:
                ct.atualizar_locacoes()
            elif opcao_locacoes == 5:
                ct.exibir_menu()
            elif opcao_locacoes == 6:
                print('Sistema Finalizado!')
            else:
                print('Opção inválida')
            return True
        except Exception as ex:
            print('Erro durante seleção de opções: ' + str(ex))
            return False 
            
    def menu_imoveis (self,opcao_imoveis):
        try:
            if opcao_imoveis == 1:
                ct.cadastro_de_imoveis()
            elif opcao_imoveis == 2:
                ct.mostrar_todos_imoveis()
            elif opcao_imoveis == 3:
                ct.pesquisar_imoveis()  
            elif opcao_imoveis == 4:
                ct.atualizar_imoveis()
            elif opcao_imoveis == 5:
                ct.exibir_menu()
            elif opcao_imoveis == 6:
                print('Sistema Finalizado!')
            else:
                print('Opção inválida')
            return True
        except Exception as ex:
            print('Erro durante seleção de opções: ' + str(ex))
            return False 



    def exibir_menu(self):
        opcao_menu = False 
        opcao = 0
        while opcao_menu == False:
            opcao = int(input("""
***************************************************
Imobiliária Mais1Code - Sistema de gerenciamento.

Selecione uma das opções para prosseguir:
1 - Cadastrar, mostrar, pesquisar e atualizar Locatários.
2 - Cadastrar, mostrar, pesquisar e atualizar Locadores.
3 - Cadastrar, mostrar, pesquisar e atualizar Locações.
4 - Cadastrar, mostrar, pesquisar e atualizar Imóveis. 
5 - Finalizar sistema.
***************************************************
"""))
            if opcao == 1:
                  self.menu_locatario(opcao)
                  opcao_menu = True
            elif opcao == 2:
                  self.menu_locadores (opcao)
                  opcao_menu = True
            elif opcao ==3:
                  self.menu_locacoes (opcao)
                  opcao_menu = True
            elif opcao == 4:
                  self.menu_imoveis (opcao)
                  opcao_menu = True
            elif opcao == 5:
                  finalizar = input('Você deseja finalizar? (S/N): ')
                  if finalizar == 'S':
                        print("""
***************************************************
Imobiliária Mais1Code - Sistema de gerenciamento.

Sistema finalizado! Obrigada por utilizar a Imobiliária Mais1Code!

***************************************************
""")
                        opcao_menu = True
                  elif finalizar == 'N':
                        opcao_menu = False
            else:
                  print('Opção inválida!')
      



