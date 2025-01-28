def input_int(question):
    '''this function takes inputs and makes sure they are integers'''
    user_input = ""
    while not user_input.isdigit():
        user_input = input(f'{question}:')
        if not user_input.isdigit():
            print("Invalid input try a integer")
    return int(user_input)
def problem1():
    def average(num1, num2, num3):
        '''this function returns the average of num1 and num2 and num3'''
        return (num1 + num2 + num3)/3
    print (average(7, 5, 9))
    print (average(6, 6, 7))
def problem2():
    print (average(7, 5, 9))
    print (average(6, 6, 7))
    def average(num1, num2, num3):
        '''this function returns the average of num1 and num2 and num3'''
        return (num1 + num2 + num3)/3
    #this will not run because the function we try to use in the first half has not been defined.
def problem3():
    def average(num1, num2, num3):
        return (num1 + num2 + num3) / 3

    print(average(7, 5, 9))
    print(average(6, 6, 7))
    print(num1)
    #this will not run because the value num1 is only defined inside the function "average"
def problem4():
    dogsage = input_int("please enter dog's age in years")
    print(f'{dogsage} years in dog years is equivalent to {24+ (dogsage-2)*4}')
def problem5():
    years_since_purchase = input_int("please enter years since purchase")
    car_cost = float(input("please enter car's cost in US dollars with out the $"))
    car_type = input("please enter a 1,2 or 3 for German Japanese or Italian respectively:")
    if car_type == "1":
        print(f'The value of your German car will be ${car_cost*(1-0.05)**years_since_purchase} after {years_since_purchase} years.')
    elif car_type == "2":
        print(f'The value of your German car will be ${car_cost * (1 - 0.07) ** years_since_purchase} after {years_since_purchase} years.')
    elif car_type == "3":
        print(f'The value of your German car will be ${car_cost * (1 + 0.05) ** years_since_purchase} after {years_since_purchase} years.')
def problem6():
    def dogs_age_calculator():
        dogs_name = input("please enter your dog's name")
        dogs_age = float(input("please enter your dog's age in years"))
        age_in_human_years = 24+ (dogs_age-2)*4
        return age_in_human_years
        return dogs_name
    print(f'your {dogs_name} is {age_in_human_years}'