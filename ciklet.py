

"""
n=0
while n <= 10: 
    print(n)
    n = n + 1

m = 1
while m <= 10:
    print(m)
    m = m+2




a = True
while a: 
    pesha = int(input("Vendos peshen"))
    if pesha == 60:
        print("Pesh optimale")
        a = True      
    else:
        print("Error")
        a = False


# Shkruaj nje program ne python ku te ruani te dhenat e klientit
# Te dhenat jane emer mbiemr gjinia

fillo_ciklin = True
while fillo_ciklin:
    emer = input("Vendos emrin ")
    mbiemer = input("vendos mbiemrin ")
    gjinia = input("Vendos gjinin ")
    print(f'Emri i klientit {emer}\nMbiemri i klientit {mbiemer}\nGjinia {gjinia}\n')
    kontrollo_ciklin = input('Shkruaj r per te rifilluar ose e per te dal nga cikli ')
    if kontrollo_ciklin == 'r':
        fillo_ciklin = fillo_ciklin
    elif kontrollo_ciklin == 'e':
        fillo_ciklin = False
    else: 
        break


for i in range(0,10):
    print(i)

"""

a = [1,2,3,4]
for i in a:
    print(i)


{
 
 'objektin1': 'tekst',
 'objekti2': ['test1', 'test2'],
 'objekti3': {
    'objektin1': 'tekst',
    'objekti2': 6,
 }

}






















