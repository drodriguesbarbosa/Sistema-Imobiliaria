from Main import menus

class Facede():
    
    def exibir_menu():
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
                  menu_locatario (opcao_locatario)
                  opcao_menu = True
            elif opcao == 2:
                  menu_locadores (opcao_locador)
                  opcao_menu = True
            elif opcao ==3:
                  menu_locacoes (opcao_locacoes)
                  opcao_menu = True
            elif opcao == 4:
                  menu_imoveis (opcao_imoveis)
                  opcao_menu = True
            elif opcao == 5:
                  finalizar = input('Você deseja finalizar? (S/N): ')
                  if finalizar == 'S':
                        print('Sistema finalizado! Obrigada por utilizar a Imobiliária Mais1Code!')
                  opcao_menu = True
            else:
                  print('Opção inválida!')
      



