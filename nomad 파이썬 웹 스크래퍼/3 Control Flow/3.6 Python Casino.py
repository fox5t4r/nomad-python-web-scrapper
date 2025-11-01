from random import randint

print('welcome to python casino!')

computer_choice = randint(1,10)

playing = True

while playing:
    user_choice = int(input('choose number (1~10) : '))
    if user_choice == computer_choice:
        print('correct!')
        playing = False

    elif user_choice < computer_choice:
        print('lower!')

    elif user_choice > computer_choice:
        print('higher!')