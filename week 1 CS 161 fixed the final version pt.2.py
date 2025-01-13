#This first function is used later on to collect inputs form the user and handle the error of them entering a non digit.
def input_int(question):
    user_input = ""
    while not user_input.isdigit():
        user_input = input(f'{question}:')
        if not user_input.isdigit():
            print("Invalid input try a integer")
    return int(user_input)
def problem1():
    pet_type = "dog"
    pet_name = "lucy"
    print(f" I have a {pet_type} and her name is {pet_name}")

def problem2():
    name = input("Enter first name:")
    age_real = input_int('Please Enter your age')
    yearly_savings =input_int('Please enter your yearly savings')

    time_passed = 10
    years_passed = 5
    print(f"""Hello {name}! 
you are {age_real} years old in {time_passed} years you will be {age_real + time_passed} years old.
If you save ${yearly_savings} per year then in {years_passed} years you will have ${yearly_savings * years_passed}.
Your Average savings is ${yearly_savings / 12} per month.""")
def problem3():
    import datetime
    day_1 = datetime.date(2025, 1, 1)
    day_2 = datetime.date(2025, 2, 1)
    day_in_january = day_2 - day_1
    seconds = int(day_in_january.total_seconds())
    print(f'There are {seconds} of seconds in January.')
def problem4():
    eggs =input_int('Plese enter the amount of eggs you have')
    print(f'this makes {eggs//12} dozen eggs with {eggs%12} leftover')

def prompt():
    x = input("please enter a problem number or q to quit: ")
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
        problem4()
        prompt()
    elif x == "q":
        quit()
    else:
        print('please enter a number between 1 and 4')
        prompt()

prompt()


