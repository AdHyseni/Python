"""
print("Ushtrimi i zgjidhur i if statement\n\n")
a=3
b=4 
c=5 
d= 10


if a > d:
    print("If eshte i vertet")
elif b != c:
    print("Elif eshte OK")
elif d>a:
    print("Elif 2 i vertet")
else:
    print("Else i gabuar")

print("Shembull  i zgjidhur i if statement\n\n")
#Ekuacionet e fuqis se dyte

a = int(input("a eshte "))
b = int(input("b eshte "))
c = int(input("f eshte "))

d = b*b - 4*a*c

if d == 0:
    x = -b/2*a
    print(f'd eshte {d} dhe x eshte {x}')
elif d>0:
    x1 = (-b + 4*c)/2*a
    x2 = (-b - 4*c)/2*a
    print(f'd eshte {d} dhe x1 eshte {x1} dhe x2 eshte {x2}')
else:
    print(f'd eshte {d} kjo vlere eshte me e vogel se 0')

## Kompania
print("Shembull i if statement\n\n")
str = input("Vendos deparatamentin ")

if str == 'it' or str == 'dig' or str == 'admin':
    print("Ju keni akses ne katin e pare")
    str2 = input("Vendos departamentin ")
    if str2 == 'crm':
        print('Ju keni akses ne deren me nr 2')
    elif str2 == 'dev':
        print('Ju keni akses ne deren me nr 1')
    else:
        print('Ju keni akses ne te dy departamentet')

elif str == 'it' and str == 'fin':
    print("Ju keni akses ne katin e dyte")
elif str == 'it' and str == 'mark':
    print("Ju keni akses ne katin e trete")
elif str == 'it' and str == 'admin':
    print("Ju keni akses ne katin e katert")
else:
    print("Ju nuk keni akses ")

print("Ushtrimi i zgjidhur i if statement\n\n")
## Shkruaj nje program ku: 
## Te printoni rrogen mujore te punonjsit
## Nese oret e punes jane me shume se 40 athere shumzojini me 1.5 ato. 
## Gjeni rrogen
oret = int(input('Vendosni oret e ketij muaji '))
paga = int(input('Vendosini pagen per ore'))
if oret > 40:
    print(f'Rroga juaj per kete muaj eshte {(oret*1.5)*paga}')
else:
    print(f'Rroga juaj per kete muaj eshte {oret*paga}')


## Shkruani nje program ku:
### Te gjeni siperfaqen e Trekendshit. 
### Nese kendi eshte me i vogel se 90 ateher formula eshte (b*h)/2 
### dhe nese eshte me i vogel se 90 por me i madhe se 0 formula eshte rrenja katrore e gjysem perimetrit 
### i trekendshit qe shumzon diferencen midis tij dhe tre brinjeve te trekendshit
### dhe nese kendi eshte me i madhe se 90 por me i vogel se 180 athere formula eshte baze her lartesi shumzuar me sinusin e kendit
### nese kendi nuk i permbush kushtet shfaq nje error sipas deshires.
print("Ushtrimi i zgjidhur if statement \n\n")
import math # Nga python importojme librarin e funksioneve matematikore

kendi = int(input("Vendos kendin e trekendshit "))

if kendi == 90:
    b = int(input("Vendos bazen "))
    h = int(input('Vendos lartesin'))
    a = (b*h)/2
    print('Siperfaqa eshte {a} njesi katror')
elif kendi <90 and kendi>0:
    a = int(input("Vendos a "))
    b = int(input("Vendos b "))
    c = int(input("Vendos c "))
    s = (a+b+c)/2 #Gjysem Perimetri
    siperfaqa = math.sqrt(s*(s-a)*(s-b)*(s-c)) #nga funksioni i math therrasim sqrt qe perfaqson rrenjen katrore
    print(f'Siperfaqa eshte {siperfaqa} njesi katror')
elif kendi >90 and kendi<180:
    b = int(input("Vendos bazen "))
    h = int(input('Vendos lartesin'))
    a = (b*h)/2*math.sin(kendi) # nga math therrasim sin e kendit.
    print(f'Siperfaqa eshte {a} njesi katror')
else:
    print('Nuk mund te gjejm siperfaqen kendi nuk eshte i sakte')



### Shkruaj nje program i cili ne baze te komandes m jep listen e kengeve te fundit 
### dhe kur vendos komanden f liston filmat e fundit

print("Ushtrimi i zgjidhur i match statement\n\n")
user_input = input('Shkruaj m per te listuar kenget e fundit, shkruaj f per te listuar filmat e fundit ne treg ')
            
match user_input:
    case 'm':
        print(  'Anti-HeroTaylor Swift.\n'+
                'Unholy (feat. Kim Petras)Sam Smith, Kim Petras.\n'+
                'CUFF ITBeyoncé\n'+
                'As It WasHarry Styles.\n'+
                'Calm Down (with Selena Gomez)Rema, Selena Gomez.\n'+
                'Rich FlexDrake,21 Savage.\n'
                'Miss YouOliver Tree, Robin Schulz.\n'
                'I\'m Good (Blue)David Guetta, Bebe Rexha.\n')
    case 'f':
        print(  '#1. Black Panther: Wakanda Forever (2022) 84% 85% #1. ...'+
                '' Test'+ 
                '#2. The Menu (2022) 89% 77% #2. ...\n'+
                '#3. The Wonder (2022) 87% 71% #3. ...\n'+
                '#4. Stutz (2022) 100% 97% #4. ...\n'+
                '#5. Disenchanted (2022) 39% 56% #5. ...\n'+
                '#6. Spirited (2022) 68% 82% #6. ...\n'+
                '#7. Black Adam (2022) 39% 90% #7. ...\n'+
                '#8. The Fabelmans (2022) 93% 79% #8.\n')
    case _:
        print('Faleminderit kthehuni perseri!')

"""

## Perseritje

"""
    Shkruaj nje program ne python ku: 
    Te marri vlerat nga user per gjinin, moshen dhe peshen.

    Pesha optimale eshte 60
    1- Nese pesha eshte me e madhe se 60kg ateher printoni "Pesha juaj eshte optimale"
    2- Nese pesha eshte me e vogel se 60kg, printoni "Kini kujdes, duhet te ushqeheni me mire"
    3- Nese pesha eshte me e madhe se 60kg dhe me vogel se 120, printoni "Kini kujdes me peshen"
    4- Nese pesha eshte me e madhe se 120kg , printoni "Kini kujdes keni tejkaluar limitin"
"""

gjinia = input("Vendos gjinin")
mosha = int(input("Vendos moshen "))
pesha = float(input("Vendos peshen "))
if gjinia == 'f':
    if mosha > 20:
        if pesha == 60:
            print('Pesha juaj eshte optimale ')
        elif pesha < 60:
            print("Kini kujdes, duhet te ushqeheni me mire")
        elif pesha > 60 and pesha < 120:
            print("Kini kujdes me peshen")
        elif pesha >=120:
            print("Kujdes keni tejkaluar limitin")
        else:
            print("Error")
elif gjinia == 'm':













    

