from levels import *


# print rules
print('-'*30 + '\nRules:' + '\n' + '\n')
print('The programme guesses a number, by answering the programme Higher or Lower, in N number of tries you have to guess '
      'the number' + '\n' + '-'*30 + '\n')


#  Choose difficulty
def choose_difficulty():
    while True:
        user_level = input('Choose a difficulty. Type "easy", "medium", "hard" or "custom": ').lower()
        if user_level == 'easy':
            easy_level()
        elif user_level == 'hard':
            hard_level()
        elif user_level == 'medium':
            medium_level()
        elif user_level == 'custom':
            custom_level()
        else:
            print('Invalid input')
            continue
