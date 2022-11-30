# While

"""
a = True
b = 'Hello'
while a:
    a = False
    if b == ' ':
        continue
    break
"""

## Perllogarit Mesataren

"""b = input("Nese doni te vendosni nje vlere tjeter shtypni p, nese jo e")
counter = 0
sum = 0
while b == 'p':
    a = int(input("Vendos numrin"))
    if b == 'p':
        sum += a
        counter += 1
        avg = sum/counter
    elif b == 'e':
        print(avg)
        break"""

def gjej_mesataren(x, y):
    return x/y

def vendos_te_dhenat(b,pesha,sum,counter,avg):
     while b: #Infinite loop
        pesha = int(input('Vendos peshen '))
        print(f"Pesha {pesha}")
        sum += pesha
        print(f"Shuma {sum}")
        counter +=1
        print(f"Counter {counter}")
        avg = gjej_mesataren(sum,counter)
        print(f"Mesatarja {avg}")
        c = input("Shkruaj s per te vendosur tjeter vler ose cdo gje tjt per te dal nga loop ")
        if c != 's':
            break

def gjej_mesataren_per(a):
    if a == 'm':
        vendos_te_dhenat(True,0,0,0,0)
   
    elif a == 'f':
        vendos_te_dhenat(True,0,0,0,0)



b = True
while b:
    c = input('Shkruaj s per te vazhduar ose cdo gje tjeter per ndalur ')
    if c == 's':
        a = input("Vendos gjinin ")
        gjej_mesataren_per(a)
    elif c != 's':
        break

   






"""for i in range(0,10):
    pass"""