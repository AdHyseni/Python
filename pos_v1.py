class Items():
    def __init__(self,emri, desc, price, viti_prodh) -> None:
        self.emri = emri
        self.desc = desc
        self.price = price
        self.viti_prodh = viti_prodh


class Item_qty():
    def __init__(self,item,qty) -> None:
        self.item = item
        self.qty = qty

    
class Inventory():
    def __init__(self,item_qty, desc,total) -> None:
        self.item_qty = item_qty
        self.desc = desc
        self.total = total
    
class Storag():
    items_storage = {
        1: Item_qty(Items(emri='HP',desc='Laptop',price=300,viti_prodh=2010),qty=10),
        2: Item_qty(Items(emri='Xiaomi',desc='Monitor',price=200,viti_prodh=2020),qty=10),
        3: Item_qty(Items(emri='Apple',desc='Iphone',price=1300,viti_prodh=2021),qty=10),
        4: Item_qty(Items(emri='Boose',desc='Kufje',price=100,viti_prodh=2010),qty=10),
        5: Item_qty(Items(emri='Panasonic',desc='TV',price=330,viti_prodh=2010),qty=10),
        6: Item_qty(Items(emri='Sony',desc='Aparat Fotografik',price=3000,viti_prodh=2021),qty=10)
            }
        
    def show_items(self):
        for key,values in self.items_storage.items():
            print(f'{values.item.emri}, {values.item.price},{values.item.viti_prodh},{values.qty}') # Printoni dhe te dhenat e tjera
    
    
    
    def search_item(self):
        input_name = input("Vendos emrin e produktit qe doni te kontrolloni: ")
        counter = 0
        for key,value in self.items_storage.items():
            counter +=1
            if input_name == value.item.emri:
                print(f'Produkti {value.item.emri} ndodhet ne dyqan dhe ka {value.qty} njesi te mbetura')
                break
            elif counter >= len(self.items_storage.items()): 
                print('Produkti nuk gjendet ne dyqanin tone')
    
    def add_item(self, e, d, p, v,q):
        last_key = list(self.items_storage)[-1]
        new_key = last_key +1
        print(new_key)
        self.items_storage[new_key] = Item_qty(Items(e, d,p,v),q)

    def buy_item(self,name,qty):
        i = 0
        for k,v in self.storage.items():
            i += 1
            if name == v.item.name:
                if qty <= v.qty:
                    new_qty = v.qty - qty
                    self.storage.update({k:Item_qty(Item(name,v.item.desc,v.item.price,v.item.prod_year),new_qty)})
                    return Item_qty(Item(name,v.item.desc,v.item.price,v.item.prod_year),new_qty)
                else:
                    print('Sasia eshte me e madhe se sasia e ruajtur ne magazine')
            elif i >= len(self.storage.items()):
                print('Produkti nuk ekziston')


        
storage = Storag()
storage.show_items()



class Kasa():
    pass
        