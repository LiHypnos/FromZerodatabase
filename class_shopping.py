from class_storage import *
from class_myBank import *
import datetime

time=datetime.datetime

class Shop:
    def __init__(self, total=0, preT=0):
        self.aslut = total
        self.limial = preT
        self.entry = Storage()
        self.bull = Bullet()
        self.account = []
        self.shopcar = []
        self.history = []
        self.control = []

    def buy(self):
        wishl = input('Informe o código do produto:\n')
        tryr = str(len(self.account)+1)
        for i in range(len(self.entry.productsList)):
            if wishl == self.entry.productsList[i].cod:
                much = int(input('Quantidade que deseja comprar:\n'))
                limial=self.entry.productsList[i].price*much
                if self.bull.valor<limial:
                    print('Você não tem saldo o suficiente para efetuar essa compra')
                elif self.entry.productsList[i].unit<much:
                    print('Não temos essa quantidade de estoque do produto selecionado disponível!')
                else:
                    self.bull.valor-=limial
                    self.entry.productsList[i].unit -= much
                    print('O valor total da compra foi de: R$',limial)
                    print('Seu saldo é de: R$',self.bull.valor)
                    self.history.append(f'Compra no valor de: R$ {limial} do item: {self.entry.productsList[i].description}!',time)
                    self.entry.saveHistory(f'Venda no valor de: R$ {limial} do item:{self.entry.productsList[i].description}!',time)
                    #self.control.append(Storage(f'Venda no valor de: R$ {limial} do item:{self.entry.productsList[i].description}!'))
                    print('_______________________________________________________________________________________________________')
            else:
                pass

    def shopping(self):
        wilt= str
        aslut = 0
        limial = 0
        wilt = input('Informe o código do produto ou digite (S) para sair ou (C) para confirmar as compras:\n')
        while wilt != 'S':
            for a in range(len(self.entry.productsList)):
                if wilt == self.entry.productsList[a].cod:
                    much = int(input('Quantidade que deseja comprar:\n'))
                    #self.control.append(Storage(f'A quantidade de {much} do produto {self.entry.productsList[a].cod} foi selecionada em um carrinho de compras!'))
                    self.entry.saveHistory(f'A quantidade de {much} do produto {self.entry.productsList[a].cod} foi selecionada em um carrinho de compras!',time)
                    print(type(aslut))
                    print(type(much))
                    aslut += much
                    limial += self.entry.productsList[a].price*much
                    self.entry.productsList[a].unit -= much
                    print('Preço atual das compras: R$',limial)
                    print('_______________________________________________________________________________________________________')
                    self.history.append(f'O item {self.entry.productsList[a].description} Foi adicionado no carrinho com sucesso!',time)
                    #self.control.append(Storage(f'Item reservado no carrinho no valor de: R${limial} do item:{self.entry.productsList[i].description}!'))
                    self.entry.saveHistory(f'Item reservado no carrinho no valor de: R${limial} do item:{self.entry.productsList[a].description}!')
                    wilt = input('Deseja continuar as compras? Se sim, digite o proximo código do produto. *Se deseja confirmar as compras, digite (C)\nSe deseja sair, digite (S)\n',time)
                    if wilt == 'C':
                        if self.bull.valor<limial:
                            print('Você ficará em débito')
                            pass
                        else:
                            self.bull.valor -= limial
                            print('Preço total das compras: R$',limial)
                            print('Seu saldo é de: R$',self.bull.valor)
                            print('___________________________________________________________________________________________________________')
                            self.history.append(f'"SHOPPING", compra realizada no valor de: R${limial} de um total de {aslut}itens!',time)
                            #self.control.append(Storage(f'"SHOPPING" no valor de: R${limial} do item:{self.entry.productsList[i].description}!'))
                            self.entry.saveHistory(f'"SHOPPING" no valor de: R${limial} do item:{self.entry.productsList[a].description}!',time)
                elif wilt == 'S':
                    break

                else:
                    break
                    print('___________________________________________________________________________________________________________')

    def historyF(self):
        for i in range(len(self.history)):
            print(self.history[i])


