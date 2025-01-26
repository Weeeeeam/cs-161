def problem1():
    #create function to recall later
    x = input ('what is your name?')
    #take name
    print (f'Hello {x}')
    #say hello to name
def problem2():
    #create function to recall later
    x = int(input ('what is your age?'))
    #take user's age have to make in to integer so the next line can add
    print (f' {x + 5}')
def problem3():
    x = int(input ('what is your age?'))
    #take user's age
    print (f'you are {x} years old in five years you will be {x+5}')
    #tell the user their age and how old they will be in 5 years
def problem4or5():
    x = float(input('how many hours do you work in a week?'))
    #take user's hours worked per week
    y= float(input('Enter your hourly wage, without the$'))
    #take user's hourly wage
    print(f'''your gross pay this week is {x*y}$ 
in a year you should make {50*x*y}$''')
    #tell User's weekly and annual income
def prompt():
    x = input("please enter problem number or q to quit: ")
    if x == "1":
        problem1()
        prompt()
    elif x == "2":
        problem2()
        prompt()
    elif x == "3":
        problem3()
        prompt()
    elif x == "4":
        problem4or5()
        prompt()
    elif x == "5":
        problem4or5()
        prompt()
    elif x == "q":
        quit()
    else:
        print('please enter between 1 and 4')
        prompt()

prompt()