import random
import string

print('ROBOT MISSILE')
print()
print('Type the correct code letter (A-Z) to defuse the missile.')
print('You have 4 chances.')
print()

code = random.choice(string.ascii_lowercase)

guesses = 0
success = False

while not success and guesses < 4:
    guess = input('What is your guess? ')
    guesses += 1

    if guess.lower() == code:
        success = True
    if guess < code:
        print('The code is later than %s in the alphabet' % guess)
    if guess > code:
        print('The code is earlier than %s in the alphabet' % guess)

if success:
    print('TICK... FIZZ... CLICK...'
          '\nYou did it!')
else:
    print('BOOOOOOOOMMM...'
          '\nYou blew it!'
          '\nThe correct code was \'%s\'.' % code)
