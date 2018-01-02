# Import 'random' so we can generate random numbers.
# The 'string' module gives us access to string-related utilities
# The 'time' module helps us to wait for some time


import random
import string
import time
print("VITAL MESSAGE")

# Variable to store the difficulty i.e length of string
level_difficulty = 0

# Loop until the right difficulty level is enterred
while level_difficulty < 4 or level_difficulty > 10:
    print("HOW DIFFICULT? (4-10)")
    x = int(input())
    level_difficulty = x

# Function to clear the screen
# This simply clears the screen by printing 64 blank lines


def clrsc():
    print('\n' * 64)


# Variable to store the secret message
message = ""

for i in range(0, level_difficulty):
    message += (random.choice(string.ascii_letters))

print("SEND THIS MESSAGE:")
print(message)

# Displaying the secret message in accordance of the difficulty level
time.sleep(0.5 * level_difficulty)
clrsc()

print("Enter the secret code that need to be transferred")
code = input()

if(code == message):
    print("MESSAGE CORRECT")
    print("THE WAR IS OVER")
else:
    print("YOU GOT IT WRONG")
    print("YOU SHOULD HAVE SENT:")
    print(message)
