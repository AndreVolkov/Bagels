# Bagels Game
from random import randint
t ='''        *** GAME OF BAGELS ********************************************************
        *                                                                         *
        *  I am thinking of a 3-digit number. Try to guess what it is.            * 
        *  Here are some clues:                                                   *
        *  When I say:    That means:                                             *
        *  Pico         One digit is correct but in the wrong position.           *
        *  Fermi        One digit is correct and in the right position.           * 
        *  Bagels       No digit is correct.                                      *
        *                                                                         *
        *  I have thought up a 3-digit number.                                    *
        *  You have 10 guesses to get it right.                                   * 
        *                                                                         *
        ***************************************************************************'''           
print(t)
play = 'yes'
j = 0
n = str(randint(100,999))
print(n)
a = list(map(int, n))
#print(a)
def Bagels(x):
    result = ''
    f = 'Fermi'
    p = 'Pico'
      
    for i in range(0,3):
        if b[i] in a:
            if a[i] == b[i]:
                result = result + f + ' '
            else:
                result = result + p + ' '                  
        
    if result == '':
        result = 'Bagels'
    print(result)
    
while play == 'yes':
    while j != 10:
        j = j + 1
        x = str(int(input('Please enter a 3 digit number:')))
        b = list(map(int, x))
        #print(b)
        if b == a:
            print('You got it!')
            play = str(input('Do you want to play again? (yes or no)'))
            if play == 'no':
                print('Thanks for playing!')
                sys.exit()
            else:
                j = 0
                n = str(randint(100,999))
                #print(n)
                a = list(map(int, n))
                #print(a)
        else:
            Bagels(x)
    print('Game Over','Correct answer:', int(n))
    play = str(input('Do you want to play again? (yes or no)'))
    if play == 'no':
        print('Thanks for playing!')
        break
    else:
        j = 0
        n = str(randint(100,999))
        #print(n)
        a = list(map(int, n))
        #print(a)
     
        


        

