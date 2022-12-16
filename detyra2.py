class Kafshe():
    def __init__(self,emri,ngjyra):
        self.emri = emri
        self.ngjyra = ngjyra

    def ecen(self):
        print('Une eci')
    
class Gjitare(Kafshe):
    def __init__(self,ushqimi,gjymtyret,ngjyra):
        super().__init__("Gjitare")
        super().__init__(ngjyra)
        self.ushqimi = ushqimi
        self.gjymtyret = gjymtyret
    
    def menyra_ushqimit(self,ushqimi):
        self.ushqimi = ushqimi
        print(f'Une jame {ushqimi}')

class Shpendet(Kafshe):
    def __init__(self, emri, ngjyra,krahet):
        super().__init__(emri, ngjyra)
        self.krahet = krahet

    def fluturojn(self):
        print('Une mund te fluturoj')

class Pinguinet(Shpendet):
    def __init__(self, emri, ngjyra, krahet):
        super().__init__(emri, ngjyra, krahet)

        def notojn(self):
            print('Une mund te notoj')

class Zvarraniket(Kafshe):
    def __init__(self, emri, ngjyra):
        super().__init__(emri, ngjyra)

    def riprodhimi_me_veze(self):
        print('Zvarraniket riprodhohen me veze')