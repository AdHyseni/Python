"""
Python eshte nje gjuhe programimi e bazuar ne ideologjin e OOP(Object oriented programiming)
Kjo ideologji krijon objekte dhe i riperdor keto objekte athere kur duhen
Klasat jane blueprint ose plan projekt i objekteve
Klasat shpesh karakterizohen nga properties and methods ose ne Shqip, me karakteristikat dhe sjelljen
Pra cfar karakteristikash ka nje produkt dhe cfar sjelljesh ka ky produkt kur merre inpute

"""

#Kjo eshte nje klass
class Klasa(): # Emri i klases gjithmon duhet te jete me te medha per te ber diferenc nga metoda
    x = 'Ky eshte nje string nga klasa'


class Grupi_python:
    x= 'Geri'

o1 = Grupi_python()
print(o1.x)




o_1 = Klasa() # Ky eshte nje objekt.
print(o_1.x)

# funksioni __init__ . Ky funksion therritet per te treguar karakteristikat e klases 

class Animal():
    def __init__(animal,ngjyra, gjatesia):
        animal.ngjyra = ngjyra
        animal.gjatesia = gjatesia

animal_1 = Animal('e bardhe', 110) # objekti i pare 
animal_2 = Animal('e kuqe', 120) # objekti i dyte

print(animal_1.gjatesia)
print(animal_1.gjatesia)

"""
Objekti i pare dhe i dyte nuk kane asnje lidhje me njeri tjetri. 
Ata veprojne si objekte te pavaruara
Gjeja e vetme qe i lidhe eshte sepse kane te njejten planimetri(klas)
"""


# metoda __str__. Kjo metode kthen nje string me karakteristikat qe do te printosh nese klasa thirret

class Person():
    def __init__(self, emer, mbiemer):
        self.emer = emer
        self.mbiemer = mbiemer


    def __str__(self) -> str:
        return f'{self.emer} {self.mbiemer}'

pers = Person(True, 1) #objekti person
print(pers) #printo objektin


# metodat dhe klasa

class Klasa_me_metod():
    def __init__(self,var_1,var_2) -> None:
        self.var_1 = var_1
        self.var_2 = var_2
    #Sjellja/ method
    def printo_var1_var_2(self):
        print(f'Var 1 eshte {self.var_1} dhe var 2 eshte {self.var_2}')



okm = Klasa_me_metod(1,2)
okm.printo_var1_var_2()

# Parametri self i referohet vete klases. Pra nese duam te therrasim metoda ose varibla te cilat ndodhen ne klase duhet te shkruajm self.var/meth
# Nuk eshte e thene qe duhet te perdoret patjeter self mund te perdorim dhe emerime te tjera, por self eshte me 
# e pershtashme se fjalet e tjera... gjithashtu eshte nje fjale e rezervuar 

"""
Polimofizmi dhe Inheritanca jane dy konceptet baze te OOP

Polimorfizmi lejon qe klasa te ndryshme te kene funksione me te njejtin emer
"""

from math import pi


class Forma:
    def __init__(self, name):
        self.name = name

    def siperfaqa(self):
        pass

    def faktet(self):
        return "Form 2D."

    def __str__(self):
        return self.name


class Katrori(Forma):
    def __init__(self, length):
        super().__init__("Katror")
        self.length = length

    def siperfaqa(self):
        return self.length**2

    def faktet(self):
        return "Cdo kende eshte 90 grade."


class Rrethi(Forma):
    def __init__(self, radius):
        super().__init__("Rreth")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

class Trapez(Forma):
    def __init__(self, bazM,bazV,h):
        super().__init__("Trapez")
        self.bazM = bazM
        self.bazV = bazV
        self.h = h

    def area(self):
        return (self.bazM+self.bazV)*self.h/2





a = Katrori(4)
b = Rrethi(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())


