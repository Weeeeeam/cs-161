#You might be getting tired of my input int code
def input_int(question):
    user_input = ""
    while not user_input.isdigit():
        user_input = input(f'{question}:')
        if not user_input.isdigit():
            print("Invalid input try a integer")
    return int(user_input)
#the purpose of this first function is to take a lower input x and a higher input Y from the user and thne share all the even numbers between them with 
#the user
def problem1():
#take starting number from user and stores as x
    x = input_int('please enter your lower starting number')
#take final number from user and stores as y
    y = input_int('please enter your higher ending  number')
# this variable s is saved as a buffer to be user later
    s=''
#This is a while loop that goes until x is greater than y
    while x<y:
# this line checks to see if x is even or odd if even it will add two to show the next even number if odd is will add 1 to get to the first next 
# even number, in this while loop the variable is changed constantly so that all even numbers are saved to be shared with user
        if x%2==1:    
            s += ' '+str(x+1)
            x = x+2
        else:
            s += ' '+str(x+2)
            x = x+2  
    print('the even numbers between ' , x , ' and ' ,y, ' are ', s)

def problem2():
    x = input_int('enter your starting number: ')
    y = 1 
    s = ''
    while y<=x:
        if x%y == 0:
            s += " "+str(y)
            y=y+1
        else:
            y= y+1 
    print(s, 'are all the factors of ',x)
# I use the problem 3 just to have every thing broken down into sections
def problem3():
    # Define the alphabet list
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    # this function wil calculate the sum of letter positions
    def sum_name_positions(name):
    # Convert name to lowercase
        name = name.lower()  
        total = 0
        for letter in name:
            if letter in alphabet:
                position = alphabet.index(letter)
                total += position
        return total

    # Get the name from user input
    name = input("Enter a name: ")

    # Calculate and print the result
    result = sum_name_positions(name)
    print(f"The sum of letter positions in '{name}' is: {result}")
def problem4():
    
    def recursion_with_square_things(x,y):
        
        if y<=x:
            print(y*y)
            recursion_with_square_things(x,y+1)
        else:
            exit
    recursion_with_square_things(input_int( 'please enter the number you would like to see all the squares leading up to?'),1)    
#The purpose of this function is to let the user enter a list of numbers then to sort said list of number with the odd on the left accending to
#center and the even starting at the center decending to the left
def problem5():
 #these three lists all play a role later the "unsorted list" stores all numbers the user enters then the odd numbers are added to the "odd list"
 # while the even number are added to the even list  
    unsorted_list = []
    oddlist = []
    evenlist = []
    #This function will sort the unsorted list into the desired Teepee shape with odds on the left and evens on the right 
    def teepeesort():
                i = 0
                while i < len(unsorted_list):
                    if unsorted_list[i]%2:
                        oddlist.insert(1,unsorted_list[i])
                        i = i + 1
                    else:
                        evenlist.insert(1,unsorted_list[i])
                        i=i+1
    #sort odd list ascending to the left 
                oddlist.sort(reverse = False)
    #sort even list decending to the left 
                evenlist.sort(reverse = True)
    # add odd and even list into one teepee sorted list 
                sortedlist= oddlist + evenlist
    #pirnt out now teepee sorted list 
                print(sortedlist)
#this function will let the user make there own custom list 
    def teepeesorter():
        x = input('type "1" to add a number to the list type "2" to see your current list sorted: ')
#this checks user input if one lets them add to their list if two 
        if x == '1':
            unsorted_list.insert(1,input_int('please enter the number you wish to add to the list') )
            teepeesorter()
        elif x == '2':
            teepeesort()
        else:
            print('please enter the number "1" or "2"')
            teepeesorter()
    teepeesorter()
problem5()