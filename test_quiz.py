"""
Krijo nje loje ku:
    1 - Te kete kategorite 
        -Gjeografi
        -Matematike
        -Biologji
    2 - Per cdo kategori te kete nga 5 pyetje
    3 - Ne momentin qe user gjen pyetjen e sakte i shtohet nje pike
    4 - Ne fund te programit te printohet:
        Urime "Emri i user", ju keni mbledhur "numri i pikeve"
    BONUS:
     - Nese user ka me pak se 2 pike te printohet
     "Rezultati eshte shume i dobet"
"""
piket =0
kategoria = input("Vendosni kategorine ")



def pyetsori(
    pyetja_1,
    pyetja_2,
    pyetja_3,
    pyetja_4,
    pyetja_5,
    pergjigjet_1,
    pergjigja_e_sakt_1,
    pergjigjet_2,
    pergjigja_e_sakt_2,
    pergjigjet_3,
    pergjigja_e_sakt_3,
    pergjigjet_4,
    pergjigja_e_sakt_4,
    pergjigjet_5,
    pergjigja_e_sakt_5,
    piket
):
      
        print('Pyetja: '+pyetja_1)
        print(pergjigjet_1)
        pergjigja_1_user = input('Jepni pergjigjen tuaj: ')
        if pergjigja_1_user == pergjigja_e_sakt_1:
            piket +=1
        else:
            piket = piket
        print('Pyetja: '+pyetja_2)
        print(pergjigjet_2)
        pergjigja_1_user = input('Jepni pergjigjen tuaj: ')
        if pergjigja_1_user == pergjigja_e_sakt_2:
            piket +=1
        else:
            piket = piket
        print('Pyetja: '+pyetja_3)
        print(pergjigjet_3)
        pergjigja_1_user = input('Jepni pergjigjen tuaj: ')
        if pergjigja_1_user == pergjigja_e_sakt_3:
            piket +=1
        else:
            piket = piket
        print('Pyetja: '+pyetja_4)
        print(pergjigjet_4)
        pergjigja_1_user = input('Jepni pergjigjen tuaj: ')
        if pergjigja_1_user == pergjigja_e_sakt_4:
            piket +=1
        else:
            piket = piket
        print('Pyetja: '+pyetja_5)
        print(pergjigjet_5)
        pergjigja_1_user = input('Jepni pergjigjen tuaj: ')
        if pergjigja_1_user == pergjigja_e_sakt_5:
            piket +=1
        else:
            piket = piket
        print(piket)


match kategoria:
    case 'Gjeografi':
        pyetsori(
            'Sa kontinente ka bota',
            'Cili eshte shteti me siperfaqen me te madhe ?',
            'A egziston Atlantis ne harten e botes ?',
            'Ne cilin kontinent ndodhet Shqiperia ?',
            'A eshte Australia kontinent me vete ?',
            '7\n8\n9\n10\n',
            '7',
            'SHBA\nKina\nRusia\nAustria\n',
            'Rusia',
            'Po\nJo\n',
            'Jo',
            'Azia\nEuropa\nKina\nAmerika Veriore\n',
            'Europa',
            'Po\nJo\n',
            'Po',
             0
        )
    case 'Biologji':
            pyetja_1 = 'Sa kontinente ka bota'
            pyetja_2 = 'Cili eshte shteti me siperfaqen me te madhe ?'
            pyetja_3 = 'A egziston Atlantis ne harten e botes ?'
            pyetja_4 = 'Ne cilin kontinent ndodhet Shqiperia ?'
            pyetja_5 = 'A eshte Australia kontinent me vete ?'

            print('Pyetja: '+pyetja_1)
            print('7\n8\n9\n10\n')
            pergjigja_1 = input('Jepni pergjigjen tuaj: ')
            if pergjigja_1 == '7':
                piket +=1
            else:
                piket = piket
            print('Pyetja: '+pyetja_2)
            print('SHBA\nKina\nRusia\nAustria\n')
            pergjigja_1 = input('Jepni pergjigjen tuaj: ')
            if pergjigja_1 == 'Rusia':
                piket +=1
            else:
                piket = piket
            print('Pyetja: '+pyetja_3)
            print('Po\nJo\n')
            pergjigja_1 = input('Jepni pergjigjen tuaj: ')
            if pergjigja_1 == 'Jo':
                piket +=1
            else:
                piket = piket
            print('Pyetja: '+pyetja_4)
            print('Azia\nEuropa\nKina\nAmerika Veriore\n')
            pergjigja_1 = input('Jepni pergjigjen tuaj: ')
            if pergjigja_1 == 'Europa':
                piket +=1
            else:
                piket = piket
            print('Pyetja: '+pyetja_5)
            print('Po\nJo\n')
            pergjigja_1 = input('Jepni pergjigjen tuaj: ')
            if pergjigja_1 == 'Po':
                piket +=1
            else:
                piket = piket
            print(piket)
    case 'Matematike':
            pyetja_1 = 'Sa kontinente ka bota'
            pyetja_2 = 'Cili eshte shteti me siperfaqen me te madhe ?'
            pyetja_3 = 'A egziston Atlantis ne harten e botes ?'
            pyetja_4 = 'Ne cilin kontinent ndodhet Shqiperia ?'
            pyetja_5 = 'A eshte Australia kontinent me vete ?'

            print('Pyetja: '+pyetja_1)
            print('7\n8\n9\n10\n')
            pergjigja_1 = input('Jepni pergjigjen tuaj: ')
            if pergjigja_1 == '7':
                piket +=1
            else:
                piket = piket
            print('Pyetja: '+pyetja_2)
            print('SHBA\nKina\nRusia\nAustria\n')
            pergjigja_1 = input('Jepni pergjigjen tuaj: ')
            if pergjigja_1 == 'Rusia':
                piket +=1
            else:
                piket = piket
            print('Pyetja: '+pyetja_3)
            print('Po\nJo\n')
            pergjigja_1 = input('Jepni pergjigjen tuaj: ')
            if pergjigja_1 == 'Jo':
                piket +=1
            else:
                piket = piket
            print('Pyetja: '+pyetja_4)
            print('Azia\nEuropa\nKina\nAmerika Veriore\n')
            pergjigja_1 = input('Jepni pergjigjen tuaj: ')
            if pergjigja_1 == 'Europa':
                piket +=1
            else:
                piket = piket
            print('Pyetja: '+pyetja_5)
            print('Po\nJo\n')
            pergjigja_1 = input('Jepni pergjigjen tuaj: ')
            if pergjigja_1 == 'Po':
                piket +=1
            else:
                piket = piket
            print(piket)