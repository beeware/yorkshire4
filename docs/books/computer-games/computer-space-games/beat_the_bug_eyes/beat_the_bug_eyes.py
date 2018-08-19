# Import:
# * the `random` module so we can generate random numbers,
# * `time` so we can sleep
import random
import time

from yorkshire4.terminal import *


# Start by hiding the cursor
hide_cursor()

score = 0

# Do 10 iterations of showing bug eyes
for t in range(10):
    clear_screen()

    # random.random() returns a floating point number in the range 0 -> 1
    # Add 0.5 to get a number between 0.5 and 1.5. That's how long we'll
    # sleep before displaying some eyes.
    time.sleep(random.random() + 0.5)

    # Pick a random zone in which to display the eyes.
    zone = random.randrange(4) + 1

    # The zone gives us the x,y offset
    if zone == 1:
        x_offset = 0
        y_offset = 0
    elif zone == 2:
        x_offset = 38
        y_offset = 0
    elif zone == 3:
        x_offset = 0
        y_offset = 12
    elif zone == 4:
        x_offset = 38
        y_offset = 12

    # Combine the offsets and a random number to postion the cursor
    # and print eyes. We can just print newlines to set the y (vertical)
    # position, then print spaces to set the x (horizontal) position.
    for y in range(random.randrange(12) + y_offset):
        print()

    print(' ' * (random.randrange(38) + x_offset) + '* *')

    # Wait up to a second for the player to respond.
    try:
        selected = int(getch(timeout=1))
    except TypeError:
        # If the user doesn't press a character, or they press something
        # other than a number, the call to int() will raise a ValueError.
        # Regardless, we know they didn't pick a zone; set the zone to None
        selected = None

    if selected == zone:
        score = score + 1

# Clear the screen, and re-show the cursor.
clear_screen()
show_cursor()

# Last of all, print the user's score.
print('You blasted %s bugs' % score)
