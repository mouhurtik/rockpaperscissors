import random
a = 0
b = 'n'
print('''
Rock 👊 Paper 📄 Scissors ✂, Virtual Game
     by Mouhurtik Ray\n''')

mn = random.randrange(1, 4)
mc = 'default'

def user_choice(uc):
    uc = uc.capitalize()
    if uc == 'R':
        print('You choose Rock')
        return uc
    elif uc == 'P':
        print('You choose Paper')
        return uc
    elif uc == 'S':
        print('You choose Scissors')
        return uc
    else:
        print('Wrong input, Please Try Again!')

def machine_choice(mn):
    if mn == 1:
        print('Machine Choose Rock')
        return 'R'
    elif mn == 2:
        print('Machine Choose Paper')
        return 'P'
    else:
        print('Machine Choose Scissors')
        return 'S'

def game_over():
    if uc == mn:
        print(f"Ohh Your choices matched, it's a Tie! ")
    elif uc == 'R' and mn == 'P':
        print('\n Congrats! You Won : ) ')
    elif uc == 'R' and mn == 'S':
        print('\n Congrats! You Won : ) ')
    elif uc == 'P' and mn == 'S':
        print('\n Ohhno, You Lost : ( ')
    elif uc == 'P' and mn == 'R':
        print('\n Congrats! You Won : ) ')
    elif uc == 'S' and mn == 'R':
        print('\n Ohhno, You Lost : ( ')
    elif uc== 'S' and mn == 'P':
        print('\n Congrats! You Won : ) ')
    else:
        print(f'''Encountered an exception, user choose {user_choice(uc)}
              and machine choose {machine_choice(mn)} ''')


uc = input('''Enter R for Rock, P for Paper,
        S for Scissors\n''')

uc = user_choice(uc)
mn = machine_choice(mn)
game_over()










