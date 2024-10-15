import random
import time
import os
from threading import Thread


def play(max_number, max_tries, max_time):
    number_to_guess = random.randint(1, max_number)
    half_max_number = max_number // 2
    numbers_of_tries = 0
    answer = False

    if number_to_guess > half_max_number:
        print(f'Hint: The number is higher than {half_max_number}')
    else:
        print(f'Hint: The number is lower than {half_max_number}')

    if max_time == 0:
        max_time = 999999999

    if max_tries == 0:
        max_tries = 999999999

    def time_to_answer():
        time.sleep(max_time)
        if not answer:
            print('\nTime is up!')
            print('The number was:', number_to_guess)
            os._exit(0)

    t = Thread(target=time_to_answer)
    t.start()

    if max_time != 999999999:
        print(f'You have {max_time} seconds to say the guessed number')


    while numbers_of_tries < max_tries:
        try:
            user_guess = int(input('Enter your guess: '))
        except ValueError:
            print('Invalid input! Please enter a number.')
            continue

        if user_guess < number_to_guess:
            print('Higher')
        elif user_guess > number_to_guess:
            print('Lower')
        else:
            print('You guessed it!')
            answer = True
            break
        numbers_of_tries += 1

        if max_tries != 999999999:
            print(f'You have {max_tries - numbers_of_tries} tries left')
            if max_tries - numbers_of_tries == 0:
                print('You lost, the number was:', number_to_guess)
                os._exit(0)


# custom level
def custom_level():
    def get_user_input(prompt, input_type=int, default_value=None):
        while True:
            try:
                user_input = input(prompt)
                if user_input == '' and default_value is not None:
                    return default_value
                return input_type(user_input)
            except ValueError:
                print(f'Invalid input! Please enter a number.')

    max_number = get_user_input('Enter the maximum number: ')
    max_tries = get_user_input('Enter the maximum number of tries (0 - infinite): ')
    max_time = get_user_input('Enter the maximum time (0 - infinite): ')
    play(max_number, max_tries, max_time)


# hard level
def hard_level():
    play(300, 8, 15)


# medium level
def medium_level():
    play(200, 10, 0)


# easy level
def easy_level():
    play(100, 0, 0)