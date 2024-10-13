import random

number_to_guess = random.randint(1, 100)

print('-'*30 + '\nRules:' + '\n' + '\n') # print rules
print('The programme guesses a number, by answering the programme Higher or Lower, in N number of tries you have to guess '
      'the number' + '\n' + '-'*30 + '\n')


while True:
      user_guess = int(input('Enter your guess: '))

      if user_guess < number_to_guess:
          print('Higher')
      elif user_guess > number_to_guess:
          print('Lower')
      else:
          print('You guessed it!')
          break
