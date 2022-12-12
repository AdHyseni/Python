
import random as r
"""
a = set('abracadabra')
print(a)

b = set('alacazam')
print(b)




lista = ['USA','Australia','Italia','Spanja','Zvicer', 'Poloni','Rumani']
l = [] #temp
seti = {}
for i in range(0,3):
    l.append(lista[r.randint(0,6)])
    seti = set(l)
print("Seti ",seti)
print("Lista ",l)
"""

lista_2 = [1,2,3,4,1,3,4,5]
l_2 = []
seti_2 = {}
for i in range(0,5):
    index= r.randint(0,7)
    #print(index)
    l_2.append(lista_2[index])
seti_2 = set(l_2)
print("Seti :",seti_2)

print("Lista  l_2: ",l_2)

