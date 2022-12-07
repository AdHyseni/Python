while True:
    import random
    yeslist = ['yes', 'y', 'Yes', 'Yeah']
    guessesTaken = 0

    print('Hello! What is your name?')
    myname = input()

    number = random.random(1, 3)

    print('Well, ' + myname + ', I am thinking of a number between 1 and 20.')
    while guessesTaken < 5:
        print('Take a guess')
        guess = input()
        guess = int(guess)

        guessesTaken = guessesTaken + 1

        if abs(guess - number) >= 3 :
            print('You are too far')
        
        elif abs(number - guess) == 0:
            print('Winner!!')
        
        elif abs(number - guess) < 3:
            print('You are so close. ')

        

        if guess == number:
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job,' + myname + ' ! You guessed my number in ' + guessesTaken +' guesses!')

    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number)

    print("Do you want to restart ? Yes or No")
    response = input()
    if not response in yeslist:
        break