"""
t = (1,2,3,4)

l = [1, 'hello', True, 1.2, [1,2,3,4], [2.3, 2.2, 3.4,2.9]]


#print(str.upper(l[1][:]))


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


print(len(l))

"""

a = [2,3,4]


shuma = sum(a)
print(f'Shuma eshte {shuma}')


shuma_1 = 0
for element in a:
    shuma_1 =shuma_1 + element
print(f'Shuma_1 eshte {shuma_1}')


shuma_2 = 0
index = 0
while index < len(a):
    shuma_2 += a[index]
    index +=1

print(f'Shuma_2 eshte {shuma_2}')


b = []
print(len(b))
kontrolli = True

while kontrolli:
    tipi = input("Cfare te dhenash doni te ruani ne list? str - per Strin dhe int- per numrat ")
    if tipi == 'str':
        u_input = input("Vendos tekstin ")
        b.append(u_input)
    elif tipi == 'int':
        u_input = int(input("Vendos numrin "))
        b.append(u_input)
    else:
        print("Ju lutem vendosni int ose str")
    repeat = input('Per te vendosur nje te dhene tjeter shkruani r per te fshire f: ')
    if repeat == 'r':
        kontrolli = kontrolli
    elif repeat == 'f':
        print(b)
        elementi_per_te_fshir = input('Shkruani elementin: ')
        for element in b:
            if  elementi_per_te_fshir == str(element):
                b.remove(element)
            else:
                print('Error')
                break
    else:
        kontrolli = False
print(b)


