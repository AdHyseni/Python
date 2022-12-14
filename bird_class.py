class Bird():
    ##Vetite
    #konstruktor
    def __init__(self,ngjyre, gjatsi, sqep):
        self.ngjyre = ngjyre
        self.gjatsi = gjatsi
        self.sqep = sqep
    
    # Pershkrues
    def __str__(self) -> str:
        return f'Shpendi me ngjyre {self.ngjyre} dhe gjatsi {self.gjatsi} e ka sqepin {self.sqep}'


    ##sjelljen
    def fluturon(self):
        print("Ky shpend fluturon")
    
    def ecen(self):
        print("Ky shpend ecen")

    
        
shpendi_1 = Bird('e verdh', 30, 'vogel')
print(shpendi_1)