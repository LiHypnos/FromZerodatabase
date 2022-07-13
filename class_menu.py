from class_storage import *
from class_face import *
from class_myBank import *
from class_shop import *
import tkinter
from tkinter import *
from m import *



f = Facer()
f.show_menu()


class Menu:
    def __init__(self):
        itens = Storage()
        buyl = Shoper()
        buyl.entry = itens
        coin = Bullet()

        #iniciar menu
        while True:
            elo = input('Você é um cliente ou funcionario?\nSe cliente, digite (C)\nSe fúncionario digite (F):\n')
            if elo == 'F':
                entryp = input('Informe a opção desejada\nA - Indicar Fabricante\nF - Adicionar Fabricante\n1 - Adicionar Produto\n2 - listar Produtos\n3 - Alterar Produtos\n4 - Adicionar estoque de um produto\n5 - Histórico\n0 - SAIR\n')

                if entryp == 'A':
                    factory = int(input('Código do Fabricante:\n'))
                    up = int(input('Código do produto que deseja indicar:\n'))
                    itens.link_factory(factory,up)


                elif entryp == 'F':
                    name = input('Nome da Fábrica:\n')
                    cod = None
                    itens.save_fac(name, cod)

                elif entryp == '1':
                    description=input('Descrição do Produto:\n')
                    unit=int(input('Unidades do produto em estoque:\n'))
                    price=float(input('Preço do produto:\nR$'))
                    factory=int(input('Codigo da Fabrica:\n'))
                    itens.save_products(description,unit,price,factory)

                elif entryp == '2':
                    itens.list()

                elif entryp == '0':
                    break

                elif entryp == '3':
                    itens.change_product()

                elif entryp == '4':
                    itens.add_product()

                elif entryp == '5':
                    itens.history()


                else:
                    print('Opção Inválida!')

            elif elo == 'C':
                entrypu = input('Deseja comprar um produto ou ir ao ''shopping''?\n1 - Comprar um produto\n2 - Shopping\n3 - Historico de Compras\n4 - Conta Báncaria\n5 - SAIR\n')
                if entrypu == '1':
                    buyl.buy()

                elif entrypu == '3':
                    buyl.historyF()

                elif entrypu == '4':
                    lus = input('Deseja adicionar saldo a carteira (1) ou vizualizar seu extrato bancario (2)?')
                    if lus == '1':
                        coin.add()

                    elif lus == '2':
                        coin.extract

                    else:
                        print('Opção inválida\n_________________________________________________________________________')
                        pass


                elif entrypu == '5':
                    break

                else:
                    print('Opção Inválida!')
