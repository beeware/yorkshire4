# Import:
# * random so we can generate random numbers,
# * sys to manipulate the terminal
import sys, random

# Includes some yorkshire4 terminal utilities, too
from yorkshire4.terminal import clear_screen


clear_screen()

# This chooses a number between 1 and 100 for the frequency of the Robots.
frequency = random.randint(1,100)

# These are used if you go too low or too high.
low = False
high = False

won = False
lost = False

# This is the beginning of a loop hich allows you to have 5 turns.
for turn in range(5):
    guess = int(input('What is your guess? '))

    # Checks if your guess is within 5 of the frequency.
    # If it is, it sets the won variable to True.
    if abs(frequency - guess) < 5:
        won = True
        break
    # Checks if your guess is so low it is less than the frequency by more than 40.
    # If it is, check that a low guess hasn't already been made, if it hasn't, print a warning.
    # If it isn't, the program tells you that you have lost.
    elif frequency - guess > 40:
        if not low:
            print('Too low... the building rumbles, careful...')
            low = True
        else:
            print('The building collapsed!')
            lost = True
            break
    # Checks if your guess is so high it is more than the frequency by more than 40.
    # If it is, check that a high guess hasn't already been made, if it hasn't, print a warning.
    # If it isn't, the program tells you that you have lost.
    elif guess - frequency > 40:
        if not high:
            print('Too high... ouch!')
            high = True
        else:
            print('Your head aches - you have to give up.')
            lost = True
            break
    else:
        print('No visible effect.')

# Checks what happened in the loop, if the game was won, print YOU'VE DONE IT.
# If not, check that there weren't too many low or high guesses before printing a message.
if won:
    print('YOU\'VE DONE IT!')
elif not lost:
    print('You took too long!')
    print('The frequency was %d.' % frequency)
