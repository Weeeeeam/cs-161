def problem1():
    pet_type = "dog"
    pet_name = "lucy"
    print(f" I have a {pet_type} and her name is {pet_name}")

def problem2():


    name = input("Enter first name:")
    age = int( input("Enter your current age:"))
    Money_saved_per_year = int( input('Enter your yearly savings:'))
    time_passed = 10
    years_passed = 5
    print(f" hello {name}! you are {age} years old in {time_passed} years you will be {age + time_passed} years old. If you save ${Money_saved_per_year} per year then in {years_passed} years you will have ${Money_saved_per_year * years_passed}. Your Average savings is ${Money_saved_per_year / 12} per month.")
def problem3():
    days_in_month = 31
    seconds_in_day = 60 * 60 * 24
    print(f" there are {days_in_month * seconds_in_day} seconds in the month of January")
def problem4():
    eggs =int(input("enter number of eggs"))
    print(f'this makes {eggs//12} dozen eggs with {eggs%12} leftover')


