import random as r

pyetjet_dhe_pergjigjet_e_quiz = {
    'Cili eshte shteti me sip me te madhe?':'Rusia',
    'Cili eshte shteti me popullsine me te madhe?':'Kina',
    'A eshte Australia nje kontinent me vete?':'Po',
    'A ndodhet Shqiperia ne kontinentin e Amerikes se Veriut':'Jo'
}

list_alternativa_gjografi = ['USA','Australia','Italia','Spanja','Zvicer', 'Poloni','Rumani']


def pyetsori(fjalori, lista, piket):
    for celes, vlere in fjalori.items(): 
        print(celes)
        l = []
        if str(vlere) == 'Po' or str(vlere)== 'Jo':
            l.append(vlere)
            if vlere =='Po':
                l.append('Jo')
                for i in l:
                    print(i)
                user_input = input("Shkruaj pergjigjen: ")
                if user_input == vlere:
                    piket +=1
                else:
                    piket += 0
            else:
                l.append('Po')
                for i in l:
                    print(i)
                user_input = input("Shkruaj pergjigjen: ")
                if user_input == vlere:
                    piket +=1
                else:
                    piket += 0
        else:
            for i in range(0,4):
                l.append(lista[r.randint(0,6)])
                l.append(vlere)
                seti = set(l)
            for j in seti:
                print(j)
            user_input = input("Shkruaj pergjigjen: ")
            if user_input == vlere:
                piket +=1
            else:
                piket += 0
                
    print(f"Urime ju keni {piket} pike")


pyetsori(pyetjet_dhe_pergjigjet_e_quiz, list_alternativa_gjografi,0)
        