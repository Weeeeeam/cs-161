def input_int(question):
    user_input = ""
    while not user_input.isdigit():
        user_input = input(f'{question}:')
        if not user_input.isdigit():
            print("Invalid input try a integer")
    return int(user_input)
def problem1():
    x = float(input('please enter a interger: '))
    #colect a starting number from the user
    while (x>0):
    # repeat until our countown hits zero
        print(x)
    # share with user current number
        x=x-1
    # tick down one at a time
    print('Blastoff')
    #says blast off like a rocket count down
def problem2():
    #the goal of this function is similar to last except this one also tells the user wether or not the number is even or odd
        x = input_int('please enter a interger:')
    #colect a starting number from the user
        while (x>0):
            if (x%2==0):
                print(f'{x} is even')
            else: print(f'{x} is odd')
        # share with user current number and tell them wether or not the number is even by divinging the number by 2 and checking the remainder
            x=x-1
        # tick down one at a time like a count down clock
        print('Blastoff')
        #says blast off like a rocket count down

def problem3():
    #the goal of this function is1similar to last except this one also let's the user decide at what value they want the timer to count down by.
        first_number = int(input('please enter a interger: '))
        Second_number = int(input('please enter the interger you woudl like to count down by: '))
    #colect a starting number from the user
        while (first_number>0):
            if (first_number%2==0):
                print(f'{first_number} is even')
            else: print(f'{first_number} is odd')
        # share with user current number and tell them wether or not the number is even by divinging the number by 2 and checking the remainder
            first_number=first_number-Second_number
        # tick down one at a time like a count down clock
        print('Blastoff')
        #says blast off like a rocket count down

def problem4_1():
    #goal of this function is to take words from the user until they send a word that  is less then 5 charecters long then the code will say goodbye
    word = input('Please enter a word ')
    #the row above takes an input from the user
    while (len(word)>5):
    # this while statment checks if the word has more than 5 charecters using the length command
        print (f'word has {len(word)} letters')
    #print word back
        word=input('please enter another word')
    #asks user for another word
    print('Goodbye!!!')
    # says goodbye when a word under 5 charecters is entered

def problem4_2():
#the purpose of 'problem4_2' is simalar to 'problem4_1' except now it has a limit to the ammount of 
    word= input('please enter a word: ')
#this line takes the first word
    y=0
# 'Y' tracks the number of attempts
    while y <5 and len(word)>=5:
#checks fot the too exit condition
            print(word,'has',len(word),'letters')
# shows the user how many letters there word has
            word = input('enter another word please: ')
# allows the user to enter a new word
            y=y+1
#adds one to the attempt counter    
    if y<5:
        print('Goodbye!!!')
    else:
        print('loser')
#this If ELse statement looks at which reason the while loop ended and sends a message depending on why we exited the loop
    exit


def problem5():

     x= input_int('please enter a starting number')
     while(x<100):
    #this while statemet makes the loop keep running till the  count hits 100 
        print(x)
    #shares x in decimal form with user
        print(hex(x))
    #share x in hexadecimal form with user
        print(bin(x))
    #shares x in binary form with user 
        x = x+1
    #increases x value to prevent an infinite loop
def problem6_1():
#this function prints a star for the number eneter counting down each line
    def starcounteriteration(x):
        while x > 0:
#this while loop keeps gointg till the input hits zero or lower
            print(x*'*')
# shares x ammount of stars with user
            x = x-1
# lowers x by 1
    starcounteriteration(int(input('Starting Number?')))
def problem6_2():
#the function has the same purpose as the one above except now it uses recursion
    def starcounterrecursion(x):
        if x>0:
            print(x*'*')
            starcounterrecursion(x-1)
        else:
            exit
    starcounterrecursion(int(input('Starting Number?')))
def problemselect():
    #the goal of this function is to add a problem select to this project
    x = (input('please enter what problem would you like: 1, 2, 3, 4.1, 4.2, 5, 6.1, 6.2 or quit to exit the function '))
    #asks user what problem they want to see
    if (x == '1'):
    # this line and the ones following will take the user input and compare then run a problem depending on what it asks.
        problem1()
    elif (x == '2'):
         problem2()
    elif (x=='3'):
         problem3()
    elif (x=='4.1'):
         problem4_1()
    elif (x=='4.2'):
        problem4_2()
    elif (x=='5'):
        problem5()
    elif (x=='6.1'):
        problem6_1()
    elif (x=='6.2'):
        problem6_2()
    elif (x== 'quit'):
        quit()
    problemselect()
problemselect()