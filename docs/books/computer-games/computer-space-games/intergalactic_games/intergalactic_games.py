# import randint, so we can get a random integer
# import atan and pi, so we can calculate the correct angle
# import sqrt, so we can calculate the correct speed
from random import randint
from math import atan, pi
from math import sqrt


# Set up the number of guesses we're going to get
guesses = 8

# Create a flag to keep track if we've won
won_game = False

print("INTERGALACTIC GAMES")

# Chooses the height to which you must launch your satellite,
# puts the value in height, and prints it.
height = randint(1, 100)
print("You must launch a satellite to a height of", height)

# As long as we have guesses left and haven't won yet, we'll keep trying
while guesses:
    guesses -= 1

    # Asks you for an angle and puts it in angle
    angle = int(input("Enter an angle (0-90): "))

    # Asks you for a speed and puts it in speed
    speed = int(input("Enter a speed (0-40000): "))

    # Subtracts the correct angle from your guess to determine
    # how close you were and stores the value in angle_diff
    angle_diff = angle - (atan(height / 3) * 180 / pi)

    # Subtracts the correct speed from your guess to determine
    # how close you were and stores the value in speed_diff
    speed_diff = speed - (3000 * sqrt(height + 1 / height))

    # Checks if you were close enough to win
    if abs(angle_diff) < 2 and abs(speed_diff) < 100:
        won_game = True
        break

    # Prints appropriate messages to help you with your next guess
    if angle_diff < -2:
        print("Too shallow.")
    elif angle_diff > 2:
        print("Too steep.")

    if speed_diff < -100:
        print("Too slow.")
    elif speed_diff > 100:
        print("Too fast.")
    print()

if won_game:
    print("You've done it!")
    print("NCTV WINS--thanks to you!")
else:
    print("You've failed.")
    print("You're fired!")
