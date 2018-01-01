''' You are a late-night computer addict and you have
fallen asleep at the keyboard. Suddenly your computer
comes alive and start hurling numbers and abuse at you.
To beat it you have to match the numbers as they appear
on the screen. Your starting score of 300 is increased
if you hit the right number and decreased if you don't.
If you can get your score up to 500 the computer will
give up and you win, but if it goes down 0, you'll become
a slave of your computer. It's a real nightmare! can you stay sane? '''

# Import 'random' so we can generate random numbers.
import random

# Initialy the score is 300
score = 300

# List of comments for making the game a more fun!
comments = [
        "** MICROS RULE! **", "*PEOPLE ARE SUPID",
        "+A ROBOT FOR PReSIDENT!", "!COMPUTERS ARE GREAT!",
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
