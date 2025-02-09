import requests

def problem1():
    x = int(input('please enter a number:'))
    if x%5 == 0:
        print(f'{x} is divisble by five')
    else: print(f'{x} is not divisble by five')

def problem2():
    state = input('please eneter a state')
    if (state == 'Wisconsin'):
        print ('Madison')
    elif (state == 'Colorado'):
        print('Denver')
    else:
        print ('I do not know that one')                  

def problem22():
    x = input('Please enter a state: ')
    state_capitol = {
    "Washington": "Olympia",
    'Oregon': 'Salem',
    'Colorado': 'Denver',
    'Texas' : 'Austin',
    'Tennesee' : 'Nashville',
    'Florida': 'Tallahasse'
    }
    print( state_capitol[(x)] )
def problem23():
    state = input('please enter a state: ')
    match state:
        case 'Washington':
            print('olympia')
        case 'Oregon':
            print('Salem')
        case 'Colorado':
            print('Denver')
        case other: print('No match found')

def problem4():
    def pool_admission(age):
        if(age < 2):
            return 0
        elif (age < 12):
            return 3
        elif (age < 60):
            return 6
        elif (age > 60):
            return 4
    print(pool_admission(int(input('enter your age: '))))

def promblem5():
    x = requests.get('http://coccbobcat.com.')
    print(x.text.count('160'))

problem22()