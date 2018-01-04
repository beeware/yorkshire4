# Import 'random' so we can generate random numbers.
# The 'string' module gives us access to string-related utilities
# The 'time' module helps us to wait for some time
import random
import string
import time

print('VITAL MESSAGE')

# Variable to store the difficulty i.e length of string
difficulty = 0

# Loop until the right difficulty level is enterred
while difficulty < 4 or difficulty > 10:
    print('How difficult do you want the game to be? (4-10)')
    x = int(input())
    difficulty = x

# Create the secret message
message = ''.join(
    random.choice(string.ascii_letters)
    for i in range(0, difficulty)
)

print('Send this message:')
print(message)

# Display the secret message in accordance with the difficulty level
time.sleep(0.5 * difficulty)

code = input('Enter the secret code that need to be transferred')

if code == message:
    print('MESSAGE CORRECT')
    print('The war is over!')
else:
    print('YOU GOT IT WRONG')
    print('You should have sent:', message)
