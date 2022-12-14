from datetime import date

class Invoice():
    def __init__(self,item_qty,date,total) -> None:
        self.item_qty = item_qty
        self.date = date
        self.total = total

class Item():
    def __init__(self,name,desc,price,prod_year) -> None:
        self.name = name
        self.desc = desc
        self.price = price
        self.prod_year = prod_year

class Item_qty():
    def __init__(self,item,qty) -> None:
        self.item = item
        self.qty = qty

class Storage():
    storage ={
        1: Item_qty(Item('HP notebook','Laptop',300,2010),10),
        2: Item_qty(Item('Lenovo','Laptop',230,2009),10),
        3: Item_qty(Item('HP','PC',300,2010),10),
        4: Item_qty(Item('Apple','Laptop',3000,2022),10),
        5: Item_qty(Item('Xiaomi','Monitor',300,2020),10)
    }
    def show_all(self):
        for k,v in self.storage.items():
            print(f'Produkti {k} me emer {v.item.name} dhe cmim {v.item.price}')

    def add(self,name,desc,price,year,qty):
        last_key = list(self.storage)[-1]
        next_key = last_key +1
        self.storage[next_key] = Item_qty(Item(name,desc,price,year),qty)
    
    def get_item(self):
        search = input("Shkruaj emrin e produktit ")
        i =0
        for k,v in self.storage.items():
            i += 1
            if search == v.item.name:
                print(f'Produkti me emer {v.item.name} ekziston dhe ka {v.qty} njesi')
                break
            elif i >= len(self.storage.items()):
                print('Produkti nuk ekziston')

    def buy_item(self,name,qty):
        i = 0
        for k,v in self.storage.items():
            i += 1
            if name == v.item.name:
                if qty <= v.qty:
                    new_qty = v.qty - qty
                    self.storage.update({k:Item_qty(Item(name,v.item.desc,v.item.price,v.item.prod_year),new_qty)})
                    return Item_qty(Item(name,v.item.desc,v.item.price,v.item.prod_year),qty)
                else:
                    print('Sasia eshte me e madhe se sasia e ruajtur ne magazine')
            elif i >= len(self.storage.items()):
                print('Produkti nuk ekziston')
        

class Kasa():
    shporta = {}

    def buy(self):
        a = True
        counter =0
        while a:
            item_name = input('Shkruaj emrin e produktit: ')
            item_qyt = int(input('Shkruaj sasine e produktit '))
            storage = Storage()
            item = storage.buy_item(item_name,item_qyt)
            total_price = item.item.price * item_qyt
            self.shporta[counter] = Invoice(Item_qty(Item(item.item.name,item.item.desc,item.item.price,item.item.prod_year),item_qyt),f'{date.today()}',total_price)
            user_in = input('Doni te shtoni produkt tjeter ? Nese po ather shkruani po ose cdo gje tjeter per te dale. ')
            if user_in == 'po':
                a = True
                counter += 1
            else:
                total_price_inv = 0
                for k,v in self.shporta.items():
                    total_price_inv += v.total
                    print(f'Totali eshte {v.total}')
                with open(f'./file/invoice{date.today()}.txt','w') as invoice:
                    for k,v in self.shporta.items():
                        invoice.writelines(f'{k+1} -- Produkti {v.item_qty.item.name}, {v.item_qty.item.desc}, viti i prodhimit {v.item_qty.item.prod_year} me sasine {v.item_qty.qty} i blere me date {v.date} cmimin total {v.total}\n')
                    invoice.writelines(f'------------Totali i fatures eshte: {total_price_inv} ALL------------------------')
                a = False 


    def main(self):
        user_input = input('Shkruaj\n1 Per te pare listen e produkteve\n2 Per te kerkuar nje Produkt\n3 Per te blere nje produkt ')
        match user_input:
            case '1':
                storage = Storage()
                storage.show_all()
            case '2':
                storage = Storage()
                storage.get_item()
            case '3':
                self.buy()
            case _:
                print('Faliminderit qe blet ne dyqanin tone')

kasa = Kasa()
kasa.main()



    