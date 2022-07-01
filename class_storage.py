import datetime
from class_product import *
from datetime
from class_factory import *

now = datetime.time
time = datetime.datetime

class Storage:
    def __init__(self):
        self.factoryList= []
        self.productsList= []
        self.his= []
        self.control= []
        self.productsList.append(Product(cod='1', description="Bolacha", factory="Maria", unit=100, price=5))
        self.factoryList.append(Factory(cod='1', descPro="bolacha", name='Maria'))
        self.factoryList.append(Factory(cod='2', descPro="Lapís de Cor", name='FaberCastle'))
        self.productsList.append(Product(cod='2', description="Lapís de Cor", factory="FaberCastle", unit=100, price=12))



    def save_products(self):

        codE = str(len(self.productsList)+1)
        descryptionE = input('Informe  o nome:\n')
        factoryE = input('Informe o fabricante:\n')
        unitE = int(input('Informe a quantia do produto:\n'))
        priceE = float(input('Valor do produto:\n'))
        self.factoryList.append(Factory(name=factoryE, cod=codE, descPro=descryptionE))
        Fac=self.factoryList
        self.productsList.append(Product(cod=codE, description=descryptionE, factory=Fac, unit=unitE,price=priceE))
        print('O código do produto é:',codE,'*')
        print('Produto Adicionado!')
        print('_______________________________________________________________________________________________________')

    def list(self):
        choose = input('Desejo listar todos (A)\nDesejo listar um produto esppecifico (B)\n')
        if choose == 'A' or 'a':
            for i in range(len(self.productsList)):
                print('Código:',self.productsList[i].cod,'/',
                    'Descrição:',self.productsList[i].description,'/',
                    'Fabricante:',self.productsList[i].factory,'/',
                    'Unidades:',self.productsList[i].unit,'/',
                    'Preço: R$',self.productsList[i].price)
                print('___________________________________________________________________________________________________')
        elif choose == 'B' or 'b':
            entry = input('Informe o código do produto:\n')
            for i in range(len(self.productsList)):
                if entry == self.productsList[i].cod:
                    print(self.productsList[i])
                    print('___________________________________________________________________________________________________')
                else:
                    limo += 1
                if limo == len(self.productsList):
                    print('Código não existente')

    def change_product(self):
        wish = input ('Deseja mudar todos os dados do produto ou um dado em específico?\nSe todos digite (A)\nSe específico digite (E)\n')
        if wish == 'A':
            wishl = input('Informe o código do produto:\n')
            for i in range(len(self.productsList)):
                if wishl == self.productsList[i].cod:
                    self.productsList[i].descryption = input('Nova descrição:\n')
                    self.his.append(f'Descrição do produto {self.productsList[i].cod} alterada!',time)
                    print('_______________________________________________________________________________________________________')
                    self.productsList[i].factory = input('Novo nome de fabricante:\n')
                    self.his.append(f'Nome do fabricante do produto {self.productsList[i].cod} alterado!',time)
                    print('_______________________________________________________________________________________________________')
                    self.productsList[i].price = input('Novo preço:\nR$')
                    self.his.append(f'Preço do produto {self.productsList[i].cod} alterado!',time)
                    print('_______________________________________________________________________________________________________')
                else:
                    cont += 1
                if cont == len(self.productsList):
                    print('Código não existente')
                print('_______________________________________________________________________________________________________')
        elif wish == 'E':
            wishl = input('Informe o código do produto:\n')
            for i in range(len(self.productsList)):
                if wishl == self.productsList[i].cod:
                    will = input ('Deseja mudar a descrição ou o nome de fabricante do produto?\nSe descrição, digite (D)\nSe fabricante, digite (F)\nSe preço, digite (P)\n')
                    if will == 'D':
                        self.productsList[i].descryption = input('Nova descrição:\n')
                        self.his.append(f'Descrição do produto {self.productsList[i].cod} alterada!',time)
                        print('_______________________________________________________________________________________________________')
                    elif will == 'F':
                        self.productsList[i].factory = input('Novo nome de fabricante:\n')
                        self.his.append(f'Nome do fabricante do produto {self.productsList[i].cod} alterado!',time)
                        print('_______________________________________________________________________________________________________')
                    elif will == 'P':
                        self.productsList[i].price = input('Novo preço:\nR$')
                        self.his.append(f'Preço do produto {self.productsList[i].cod} alterado!',time)
                        print('_______________________________________________________________________________________________________')
                else:
                    lont += 1
                if lont == len(self.productsList):
                    print('Código não existente')
                print('_______________________________________________________________________________________________________')
    def add_product(self):
        lup = input('Digite o código do produto que você deseja adicionar mais unidades\n')
        for i in range(len(self.productsList)):
            if lup == self.productsList[i].cod:
                luple = int(input('Quantidade que deseja adicionar\n'))
                self.productsList[i].unit += luple
                self.his.append(f'Adicionado ao estoque do produto {self.productsList[i].cod} uma quantia de: {luple}',time)
                print('Quantidade de',luple,'Adicionado ao estoque do produto com sucesso!!')

    def saveHistory(self,valor):
        self.his.append(valor)


    def history(self):
        for i in range(len(self.his)):
            print(self.his[i])









