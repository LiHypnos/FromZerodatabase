import datetime
from class_product import *
from class_factory import *
from datetime import datetime

#print(datetime.today().strftime('%Y-%m-%d %H:%M'))
#databank link
#_______________________________________________________________________________________________________________________
import mysql.connector
#_______________________________________________________________________________________________________________________


class Shoper:
    def __init__(self):

        self.conex = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='lojinha'
        )
        self.my_c = self.conex.cursor()

    def buy(self):
        wip = int(input('Informe o Codigo do Produto:\n'))
        wop = int(input('Deseja comprar quantas unidades do produto?\n'))
        comandd_sql = f'insert into Sell ' \
                      f'(IDs,codP,unitB,priceT) ' \
                      f' value ' \
                      f'({wop},{priceT})'\
                      f' where codP = {wip}'

        self.my_c.execute(comandd_sql)
        self.conex.commit()
        print('Produto Comprado!')
        print('_______________________________________________________________________________________________________')

    #def shopping(self):

