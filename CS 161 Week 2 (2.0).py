from string import digits


def input_int(question):
    user_input = ""
    while not user_input.isdigit():
        user_input = input(f'{question}:')
        if not user_input.isdigit():
            print("Invalid input try a integer")
    return int(user_input)
def problem1():
    x = 31
#using a number such as 1.825 you get the error "TypeError: 'float' object cannot be interpreted as an integer"  because a integer can not have any fractions or decimal points

    y=0b1001
    z=0xA3
    print(y,z)


    w = x + y + z
    print('the sum is', w)
def problem2():
    original_size = input_int("original size: ")
    dictionary_size = input_int("dictionary size: ")
    compressed_text_size = input_int("compressed text size: ")
    Percentofcompression = (f"{((1-((((compressed_text_size+dictionary_size))/original_size)))*100)}")
    will_ = round((float(Percentofcompression)), 2)
    print(f'''compressed text size:{compressed_text_size}
  original text size:{dictionary_size}
               total:{compressed_text_size + dictionary_size}
     dictionary size:{dictionary_size}
        compression :{will_}%''')

problem2()
