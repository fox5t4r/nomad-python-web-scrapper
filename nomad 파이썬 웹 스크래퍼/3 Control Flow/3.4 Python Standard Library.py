from random import randint

user_choice = int(input('choose number : '))

computer_choice = randint(1,10)

if user_choice == computer_choice:
    print('correct!')

elif user_choice < computer_choice:
    print('lower! computer :', computer_choice)

elif user_choice > computer_choice:
    print('higher! computer :', computer_choice)