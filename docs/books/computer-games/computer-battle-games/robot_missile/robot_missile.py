# Import `random` so we can generate random numbers.
# The `string` module gives us access to string-related utilities,
# like a list of lowercase characters.
import random
import string

print('ROBOT MISSILE')
print()
print('Type the correct code letter (A-Z) to defuse the missile.')
print('You have 4 chances.')
print()

# Choose, at random, a lowercase ascii character
code = random.choice(string.ascii_lowercase)

# Loop until we get a match, or we've tried 4 times
guesses = 0
success = False

while not success and guesses < 4:
    # Read a character from the user, and convert it to lower case
    guess = input('What is your guess? ').lower()
    guesses += 1

    # Check to see if the guess is correct. If it is, flag the success;
    # otherwise, print an error message hinting towards the final answer.
    if guess == code:
        success = True
    elif guess < code:
        print('The code is later than %s in the alphabet' % guess)
    elif guess > code:
        print('The code is earlier than %s in the alphabet' % guess)

# The loop has exited. Let the user know if they succeeded or not.
if success:
    print('TICK... FIZZ... CLICK...')
    print('You did it!')
else:
    print('BOOOOOOOOMMM...')
    print('You blew it!')
    print()
    print("The correct code was '%s'." % code)
