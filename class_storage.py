import datetime
from class_product import *
from class_factory import *
from datetime import datetime

#print(datetime.today().strftime('%Y-%m-%d %H:%M'))
#databank link
#_______________________________________________________________________________________________________________________
import mysql.connector

#listpp = my_cursor.fetchall()
#for i in listpp
    #print(i)
    #CRUD
    #create
    #Read
    #Update
    #Delete
#print(conexão)
#_______________________________________________________________________________________________________________________


class Storage:
    def __init__(self):

        self.conex = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='lojinha'
        )
        self.my_c = self.conex.cursor()

    def save_fac(self, name, cod):
        objef = Factory(name, cod)
        comand_sql = f'insert into Factory ' \
                     f'(namee) ' \
                     f'value ' \
                     f'("{objef.name}")'

        self.my_c.execute(comand_sql)
        self.conex.commit()
        print('Fábrica Adicionada!')
        print('_______________________________________________________________________________________________________')

    def save_products(self, description, unit, price,factory):
        objec = Product( description, unit, price,factory)
        comandd_sql = f'insert into Storag (descriptionn,unit,price,FactoryCode) values ("{description}",{unit},{price},{factory})'
        self.my_c.execute(comandd_sql)
        self.conex.commit()
        print('Produto Adicionado!')
        print('______________________________________________________________________________________________________')

    def link_factory(self,factory,up):
        comandder_sql = f'insert into Storag ' \
                        f'(FactoryCode) ' \
                        f' (select cod from Factory where cod = {factory} where cod = {up}'
        self.my_c.execute(comandder_sql)
        self.conex.commit()
        print('______________________________________________________________________________________________________')


    def list(self):
        choose = input('Desejo listar todos (A)\nDesejo listar um produto especifico (B)\n')
        if choose == 'A':
            comand_sql = 'select * from Storag'
            self.my_c.execute(comand_sql)
            list = self.my_c.fetchall()
            for i in list:
                print(i)
                print('___________________________________________________________________________________________________')
        elif choose == 'B':
            pm = int(input('Digite o Código do produto:\n'))
            comand_sql = f'select * from Storag where {pm} = Cod'
            self.my_c.execute(comand_sql)
            list = self.my_c.fetchall()
            for i in list:
                print(i)
                print('___________________________________________________________________________________________________')
        else:
            print('Comando Inválido!')

    def change_product(self):
        cod = int(input('Informe o código do produto:\n'))
        conf = input('Deseja mudar qual coluna? Cod[],descriptionn[],unit[],price[]\n')
        new = input('Nova informação:\n')
        comand_sql = f'update Storag set "{conf}" = "{new}" where id = {cod}'
        comand_sqls = f'insert into HistoryT '\
                      f'(describ,datar) '\
                      f'value '\
                      f'(Item alterado na seguinte posição: "{conf}" where CodP = {cod})'
        print('Atualizado com Sucesso!')
        print('_____________________________________________________________________________________________________')
        self.my_c.execute(comand_sql)
        self.my_c.execute(comand_sqls)
        self.conex.commit()

    def add_product(self):
        lup = input('Digite o código do produto que você deseja adicionar mais unidades\n')
        salko = int(input('Digite a quantidade que deseja adicionar ao estoque do produto\n'))
        comand_sql = f'update Storag set {unit} = unit+{salko} where id = {lup}'
        slk = datetime.today().strftime('%Y-%m-%d %H:%M')
        comand_sqls = f'insert into HistoryT ' \
                      f'(describ,datar) ' \
                      f'value ' \
                      f'("Item alterado na seguinte posição: "{unit}" where CodP = {cod})",("{slk}")'
        self.my_c.execute(comand_sql)
        self.my_c.execute(comand_sqls)
        self.conex.commit()



    #def saveHistory(self,valor):
        #self.append(valor)


    def history(self):
            comand_sql = 'select * from HistoryT '
            self.my_c.execute(comand_sql)
            list = self.my_c.fetchall()
            for i in list:
                print(i)
                print('___________________________________________________________________________________________________')









