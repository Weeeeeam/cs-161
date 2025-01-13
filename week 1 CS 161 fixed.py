def problem1():
    pet_type = "dog"
    pet_name = "lucy"
    print(f" I have a {pet_type} and her name is {pet_name}")

def problem2():
    name = input("Enter first name:")
    age= ""
    while not age.isdigit():
        age = input('Enter your age:')
        if not age.isdigit():
            print("Invalid input try a integer")
    age_real = int(age)

    yearly_savings = ""
    while not yearly_savings.isdigit():
        yearly_savings = input('Enter your yearly savings:')
        if not yearly_savings.isdigit():
            print("Invalid input try a integer")

    money_saved_per_year = int(yearly_savings)
    time_passed = 10
    years_passed = 5
    print(f"""Hello {name}! 
you are {age_real} years old in {time_passed} years you will be {age_real + time_passed} years old.
If you save ${money_saved_per_year} per year then in {years_passed} years you will have ${money_saved_per_year * years_passed}.
Your Average savings is ${money_saved_per_year / 12} per month.""")
def problem3():
    days_in_month = 31
    seconds_in_day = 60 * 60 * 24
    print(f" there are {days_in_month * seconds_in_day} seconds in the month of January")
def problem4():
    eggs =int(input("enter number of eggs: "))
    print(f'this makes {eggs//12} dozen eggs with {eggs%12} leftover')

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
        problem4()
        prompt()
    elif x == "q":
        quit()
    else:
        print('please enter between 1 and 4')
        prompt()

prompt()


