
# Import 'random' so we can generate random numbers.
import random

# Initialy the score is 300
score = 300

# List of comments for making the game a more fun!
comments = [
        "** MICROS RULE! **", "*PEOPLE ARE SUPID*",
        "+A ROBOT FOR PRESIDENT!", "!COMPUTERS ARE GREAT!",
        "*I'M BETTER THAN YOU!*"
        ]

# Loop while the score is not above 500 i.e you have won,
# or less than 0 means you have lost the game
while score > 0 and score < 500:
    # Number that will be appeared on screen
    number = random.randint(1, 9)
    print("   %d" % (number))
    print("                     %d" % (score))

    if random.randint(1, 9) > 5:
        print(comments[int(score/100)])

    else:
        if score < 60:
            print("THERE IS NO HOPE")
        elif score > 440:
            print("URK! HELP!!")

    print("ENTER THE ANSWER")
    answer = int(input())
    # If you have guessed right increase the score
    if answer == number:
        score = score + number * 2

    else:
        score = score - 10


if score < 0:
    print("YOU'RE NOW MY SLAVE")

else:
    print("OKAY! YOU WIN (THIS TIME)")
