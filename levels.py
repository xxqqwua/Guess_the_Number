import random
import time
import sys
from threading import Thread


# custom level
def custom_level():
    pass


# hard level
def hard_level():
    number_to_guess = random.randint(1, 300)
    numbers_of_tries = 0
    answer = False

    if number_to_guess > 150:
        print('First hint: The number is higher than 150')
    else:
        print('First hint: The number is lower than 150')

    def countdown():
        time.sleep(10)
        if not answer:
            print('Time is up!')
            print('The number was:', number_to_guess)
            sys.exit()


    t = Thread(target=countdown)
    t.start()
    print('You have 10 seconds to answer')
    while numbers_of_tries < 8:
        user_guess = int(input('Enter your guess: '))

        if user_guess < number_to_guess:
            print('Higher')
        elif user_guess > number_to_guess:
            print('Lower')
        else:
            print('You guessed it!')
            answer = True
            break
        numbers_of_tries += 1
        print(f'You have {9 - numbers_of_tries} tries left')

# medium level
def medium_level():
    number_to_guess = random.randint(1, 200)
    numbers_of_tries = 0

    if number_to_guess > 100:
        print('First hint: The number is higher than 100')
    else:
        print('First hint: The number is lower than 100')

    while numbers_of_tries < 10:
        user_guess = int(input('Enter your guess: '))

        if user_guess < number_to_guess:
            print('Higher')
        elif user_guess > number_to_guess:
            print('Lower')
        else:
            print('You guessed it!')
            break
        numbers_of_tries += 1
        print(f'You have {11 - numbers_of_tries} tries left')


# easy level
def easy_level():
    number_to_guess = random.randint(1, 100)

    if number_to_guess > 50:
        print('First hint: The number is higher than 50')
    else:
        print('First hint: The number is lower than 50')

    while True:
        user_guess = int(input('Enter your guess: '))

        if user_guess < number_to_guess:
            print('Higher')
        elif user_guess > number_to_guess:
            print('Lower')
        else:
            print('You guessed it!')
            break