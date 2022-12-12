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

"""
b = []
print(f'Lista ka gjatesine : {len(b)}')
kontrolli = True

while kontrolli:
    tipi = input("Cfare te dhenash doni te ruani ne list? str - per Strin dhe int- per numrat ")
    if tipi == 'str':
        u_input = input("Vendos tekstin ")
        b.append(u_input)
    elif tipi == 'int':
        u_input = int(input("Vendos numrin "))
        b.append(u_input)
    elif tipi == 'bool':
        u_input = int(input("Vendos numrin 0 per false ose 1 per True"))
        if u_input ==1:
            b.append(True)
        elif u_input == 0:
            b.append(False)
        else:
            print("Duhet te vendosni numrin 0 per false ose 1 per True")
    else:
        print("Ju lutem vendosni int, str ose bool")
    repeat = input('Per te vendosur nje te dhene tjeter shkruani r per te fshire f: ')
    if repeat == 'r':
        kontrolli = kontrolli #True
    elif repeat == 'f': #Me poshte eshte operacioni i fshirjes se nje te dhene
        print(b)
        elementi_per_te_fshir = input('Shkruani elementin qe doni te fshini: ')
        print(f"Ke shkruar: {elementi_per_te_fshir}")
        # Hym ne cikel per te lexuar elementet e listes
        index = 0 #Pika e fillimit
        while index < len(b): # Ekzekutohu persa kohe kushti eshte True  
            #Nese elementi ne index eshte i barabart me elementin qe duam te fshime athere fshije
            #Fillimisht elementet jane pershtatur(konvertuar ne string), pasi input = str
            if  elementi_per_te_fshir == str(b[index]): 
                print(f'Eshte fshire: {b[index]}') #test
                del b[index]
                break
            #Nese jo inkremento index dhe kalo perseri ne cikel
            else:
                #print(b[index])
                #print(type(elementi_per_te_fshir))
                print(type(b[index]))
                print('Error')  
                index +=1
                continue       
    else:
        with open('./file/set_list.txt', 'w') as f:
            for i in b:
                f.writelines(i)
        kontrolli = False
print(b)


