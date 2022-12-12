

#Metoda e pare
f = open('./file/text.txt', 'r')
print(f)

count = 0
for line in f:
    count +=1
print('Line Count metoda 1:', count)
f.close()


#Metoda 2
with open('./file/text.txt', 'r') as f:
    count = 0
    for line in f:
        count +=1
print('Line Count metoda 2:', count)

#Metoda 3
try:
    f = open('./file/text.txt', 'r')
    count = 0
    for line in f:
        count +=1
    print('Line Count metoda 3:', count)
except:
    print("Erro")
finally:
    f.close()

with open('./file/text.txt', 'r') as f:
     lorem = []
     for ln in f:
        if ln.startswith('Lorem'):
            lorem.append(ln)
print(lorem)

