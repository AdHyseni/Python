# Sintaksa e nje liste 
lista = []

# Tipet e vlerave qe permban nje list 
lista = [1,'text',1.0,True, ['list'], ('tuple'),{'key':1}]

#Operimet me listat 
lista_1 = [1,2,3]
lista_2 = [4,5,6]
lista_3 = lista_1+lista_2

lista_4 = lista_1*2

#Si te marrim te dhenat nga nje liste 

#Kemi parasysh qe numerimi fillon nga 0

lista = [1,2,3] # 0,1,2
print(lista[0]) # index 0 = 0

#nese duam te printojme te gjithe elementet perdorom ciklet
for element in lista:
    print(element)

a =0 # fillojm nga index 0
while a <len(lista): #len tregon gjatesine e listes
    print(lista[a])
    a +=1 #incrementojme a ne menyre qe te marrim elementet e tjere

# ndrysimi i vlerave 
lista[0]= 0
print(lista[0])

#metodat e listave
x = len(lista) #tregon gjatesine e listes
max = max(lista) #shpreh vleren me te madhe
min = min(lista) #shpreh vleren me te vogel
sum = sum(lista) #shpreh vleren me te shumen


list_unsorted = [332, 34,22,64,355,3,66]
list_unsorted.sort(reverse=False) # ne momentin qe thrasim sort lista renditet
print(list_unsorted)

#prerja e listave ose slice 

lista_a = [1,2,3,4,5,6,7,8]
lista_b = lista_a[:5] # kjo list permbane t elementet e listes a me index 0 deri ne 4
lista_c = lista_a[2:5] # elementet me index 2,3,4 do jene pjese e listes c 

# listat dhe strings
string_1 = 'Happy new year'
list_string = string_1.split() # krijon nje liste me fjalet ne string
string_2 = ''
string_2.join(list_string) # krijon nje string me fjalet ne list