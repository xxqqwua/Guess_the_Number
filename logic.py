import random


number_to_guess = random.randint(1, 100)


# print rules
print('-'*30 + '\nRules:' + '\n' + '\n')
print('The programme guesses a number, by answering the programme Higher or Lower, in N number of tries you have to guess '
      'the number' + '\n' + '-'*30 + '\n')


def hard_level():
    pass


def medium_level():
    pass


def easy_level():
    while True:
        user_guess = int(input('Enter your guess: '))

        if user_guess < number_to_guess:
            print('Higher')
        elif user_guess > number_to_guess:
            print('Lower')
        else:
            print('You guessed it!')
            break


#  Choose difficulty
user_level = input('Choose a difficulty. Type "easy", "hard" or "medium": ').lower()
print(user_level)
if user_level == 'easy':
    easy_level()
elif user_level == 'hard':
    hard_level()
elif user_level == 'medium':
    medium_level()
else:
    print('Invalid input')
