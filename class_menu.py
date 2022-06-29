from class_storage import *
from class_shopping import *
from class_move import *

class Menu:
    def __init__(self):
        itens = Storage()
        buyl = Shop()
        buyl.entry = itens

        #iniciar menu
        while True:
            elo = input('Você é um cliente ou funcionario?\nSe cliente, digite (C)\nSe fúncionario digite (F):\n')
            if elo == 'F':
                entryp = input('Informe a opção desejada\n1 - Adicionar Produto\n2 - listar Produtos\n3 - Alterar Produtos\n0 - SAIR\n')

                if entryp == '1':
                    itens.save_products()

                elif entryp == '2':
                    itens.list()

                elif entryp == '0':
                    break
                elif entryp == '3':
                    itens.change_product()

                else:
                    print('Opção Inválida!')

            elif elo == 'C':
                entrypu = input('Deseja comprar um produto ou ir ao ''shopping''?\n1 - Comprar um produto\n2 - Shopping\n')
                if entrypu == '1':
                    buyl.buy()
