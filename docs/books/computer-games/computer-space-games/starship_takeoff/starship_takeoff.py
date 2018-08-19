# Import the 'random' module, so you can generate random numbers
import random


print('Starship Take-off')
print('-----------------')
print()

# Select 2 random numbers. `random.randrange(X)` picks a number
# between 0 and X, *including* 0, but *not* including X. Adding
# 1 means we get a number between 1 and X, *inclusive*.
gravity = random.randrange(20) + 1
weight = random.randrange(40) + 1

# Compute the required launch force.
required = gravity * weight

# Print the gravity for the planet
print('Gravity =', gravity)

# Start a loop that will run until either there have been
# 10 attempts, or the user entered the correct force.
success = False
c = 0
while c < 10 and not success:
    # On each loop, increment the count of attempts,
    # and prompt the user for a value
    c = c + 1
    force = int(input("Force:"))

    # Compare the value entered with the required value.
    # If they match, set the success flag; otherwise,
    # print an error
    if force > required:
        print('Too high!')
    elif force < required:
        print('Too low!')
    else:
        success = True

    # As long as this isn't the last loop,
    # we can try again
    if c < 10:
        print('Try again.')

print()

# We've either been successful, or we've done 10 loops.
# Tell the user if they've been successful.
if success:
    print('Good take off!!')
else:
    print('You failed - the aliens got you')
