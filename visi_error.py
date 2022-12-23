class Items():
    def __init__(self,emri, desc,price,viti) -> None:
        self.emri = emri
        self.desc = desc
        self.viti = viti
        self.price = price

class Item_qty():
    def __init__(self,item,qty) -> None:
        self.item = item
        self.qty = qty
       

class Bill():
    def __init__(self,item_qty,data,total) -> None:
        self.item_qty = item_qty
        self.date = data
        self.total= total

class Storag():
    item_storage = {
        1:Item_qty(Items(emri='HP',desc='Laptop',price=300,viti=2010),qty=10),
        2:Item_qty(Items(emri='Xiami',desc='Monitor',price=300,viti=2010),qty=10),
        3:Item_qty(Items(emri='Apple',desc='Iphone',price=390,viti=2010),qty=10),
        4:Item_qty(Items(emri='Boose',desc='Kufje',price=50,viti=2022),qty=10),
        5:Item_qty(Items(emri='Panasonic',desc='Tv',price=3000,viti=2009),qty=10),
        6:Item_qty(Items(emri='Sony',desc='Laptop',price=300,viti=2010),qty=10),
    }

    def show_items(self):
        for key,values in self.item_storage.items():
            print(f'{values.item.emri},{values.item.desc},{values.item.price},{values.item.viti},{values.qty}') # te printojme dhe te dhenat e tjera

    
    def search_item(self):
        input_name=input("Vendos emrin e produktit qe kerkoni")
        counter = 0
        for key,value in self.item_storage.items():
            counter +=1
            if input_name ==value.item.emri:
                print(f'Produkti{value.item.emri}ndodhet ne dyqan dhe ka {value.qty} njesi te mbetura')
                break
            elif counter >= len(self.item_storage.items()):
                print ("Produkti nuk gjendet ne dyqanin tone")

    def add_item(self,emri,desc,price,viti,qty):
        last_key= list(self.item_storage)[-1]
        new_key= last_key+1
        print(new_key)
        self.item_storage[new_key]=Item_qty(Items(emri,desc,price,viti),qty)

    def buy_item(self,emri,qty):
        counter=0
        for key,value in self.item_storage.items():
            counter+=1

            if value.item.emri == emri:
                print(value.item.emri)
                if qty <= value.qty:
                    new_qty = value.qty-qty
                    self.item_storage[key]=Item_qty(Items(emri,value.item.desc,value.item.price,value.item.viti),new_qty)
                    print ('Suksese')
                    return Item_qty(Items(emri,value.item.desc,value.item.price,value.item.viti),qty)
                else:
                    print('Sasia eshte me emadhe se sasia e ruajtur ne magazine')
                    return 0
            elif counter >= len(self.item_storage.items()):
                print ("Produkti nuk ekziston")
                return 0


##storage = Storag()
#storage.buy_item('HP',2)

from datetime import date
class Kasa():
    shporta ={}
    

    def buy(self):
        storage = Storag()# i referohet klases stirage m nga ketu mund te therasim cdo sjellje te Storage
        a =True #kontrollo ciklin
        key =1 #eshte celesei i fjalorit (shporta)
        while a:
            prod_name = input("Shkruaj emrin e produktit")# kerkojme emrin e item
            prod__qty = input("Shkruaj sasine")# sasine qe duam te blejme
            produkti =storage.buy_item(prod_name,int(prod__qty))# ne momentin qe therassim buy_item nga storage ne marrim njeobjekt me te dhenat e item dhe sasine e item
            totali_per_produkt= int(prod__qty)*produkti.item.price
            self.shporta[key]= Bill(produkti,date.today(),totali_per_produkt)
            user_input = input('shkrujan po per te vazhduar dhe cdo gje tjeter per e dale')
            if user_input== 'po':
                a = True
                key+=1
            else:
                a = False
                with open (f'Fatura-{date.today()}.txt','w') as f:
                    totali= 0
                    for k,v in self.shporta.items():
                        totali+= v.total
                    for k,v in self.shporta.items():
                        f.writelines(f'{k}-- Emri i produkti: {v.item_qty.item.emri}---Pershkrim:{v.item_qty.item.desc}--- Totali:{v.total}')
                    f.writelines(f'-----Totali per te paguar eshte :{totali} eu\n')


    def main (self):
        user_input= input('Shkruaj 1 per te pare porduktet\nShkruaj 2 per te kerkuar nje produkt\nShkruaj 3 per te blere nje produkt\n')
        storage = Storag()
        match user_input:
            case'1':
                storage.show_items
            case'2':
                storage.search_item()
            case'3':
                self.buy()
            case _:
                print('Faleminderit qe blete ne dyqanin tone')
kasa = Kasa()
kasa.buy()
