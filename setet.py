t = (1,2,3,4)

l = [1, 'hello', True, 1.2, [1,2,3,4], [2.3, 2.2, 3.4,2.9]]


#print(str.upper(l[1][:]))
"""

for i in l:
    if type(i) == bool:
        print(i)

for i in l:
    if type(i) == list:
        print(i)

a = 0 
while a < len(l):
    print(f'Elementi me indexin {a} eshte {l[a]}')
    a +=1
"""


#print(f'Printo gjatesin e hello {len(l[1])}')

lista_1 = [1,5,7]
lista_2 = [2,3,4,6]

lista_3 = lista_1+lista_2

#print(lista_3[0:3]) # 0, 1, 2, ---3 jo
#print(lista_3[1:3]) # 0, 1, 2, 3
lista_1.extend([2])
t = ['d', 'c', 'e', 'b', 'a']
x = len(t)
for i in range(0,x):
    t.pop(0)
print(t)




#print(lista_3)

"""
print(len(l))

"""