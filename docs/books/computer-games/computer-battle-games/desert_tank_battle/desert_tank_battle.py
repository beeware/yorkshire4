# Import:
# * the `random` module so we can generate random numbers,
# * the `math` module so we can perform some basic trigonometry
import random
import math


# Normal terminals are defined a lot like typewriters. They are "line based" -
# they wait for the user to type a full line, then type Enter, and the entire
# line of input is processed.
#
# This is a utility method to get a whole number input from the keyboard which
# must be within a certain range. For example, a number between 1 and 10.
# For example:
#
#     my_guess = get_number('Please enter a guess between 1 and 10', 1, 10)
#
def get_number(prompt, min_value, max_value):
    # we don't know what value the user will type in yet, so start off
    # with "nothing" in the value
    the_number = None
    # get ready to keep asking the user for the number until they give us
    # an actual number that's within the range we need
    while the_number is None:
        # we can use the `input` function to get the user to type something
        # in and press [ENTER], and store it in the variable `user_input`,
        # so this line asks the user for the number with the `prompt` text
        user_input = input(prompt + ' ')
        try:
            # we have the user's input, so now we need to try to convert
            # it to a whole number
            the_number = int(user_input)
            # it's a number, so now we need to check the range
            if the_number > max_value or the_number < min_value:
                # the number is outside the allowed range
                # show the user a message to help them get it right next time
                if the_number > max_value:
                    print('That is more than {} - please try again.'.format(max_value))
                elif the_number < min_value:
                    print('That is less than {} - please try again.'.format(min_value))
                # discard the number we got because it's invalid
                the_number = None
        except (TypeError, ValueError):
            # whatever the user typed in, it wasn't a number
            # show the user a message to help them get it right next time
            print('That is not a number - please try again.')
    # we have a number that's within the range we need - hand the result back
    return the_number


# Here we set up a bunch of things ready to play the game:
# Firstly - where is the enemy stronghold?
# This selects a whole number between -90 and 90 (inclusive) for the
# direction of the enemy stronghold
stronghold_direction = random.randint(-90, 90)
# This selects a fractional number between 0.0 and 1.0 for the
# distance of the enemy stronghold
stronghold_distance = random.random()

# Next, how many missiles does the player get to try to hit the enemy stronghold?
available_missiles = 5
# How many missiles have they used so far? They haven't started yet, so it's zero
used_missiles = 0
# Is the stronghold destroyed? They haven't started yet, so that is false
stronghold_is_destroyed = False

# Now we can start the actual game.
print()
print('Desert Tank Battle')
print()

# continue playing so long as the player has missiles left and the stronghold
# is not yet destroyed
while used_missiles < available_missiles and not stronghold_is_destroyed:
    # Get the guesses for direction and elevation - we store them in
    # the variables `aim_direction` and `aim_elevation_in_degrees`
    aim_direction = get_number('Direction (-90 to 90) ?', -90, 90)
    aim_elevation_in_degrees = get_number('Elevation (0 to 90) ?', 0, 90)

    # increase the count of used missiles
    used_missiles += 1

    # calculate the distance the missile travelled (the answer
    # will be between 0 and 1).
    # First, though, we need to convert the angle the player gave us
    # from degrees to radians so that we can use it in the `sin`
    # function to work out the distance. If you want to know more about
    # radians and degrees for measruring angles, you can read articles here:
    #   https://en.wikipedia.org/wiki/Degree_(angle)
    #   https://en.wikipedia.org/wiki/Radian
    aim_elevation_in_radians = math.radians(aim_elevation_in_degrees)
    # Now we can use the converted angle to work out the distance
    missile_distance = math.sin(aim_elevation_in_radians)

    # check how far away the missile landed from the actual target
    # first we check how many degrees off target the aim was - we use
    # the `abs` function to get the "absolute" difference between the
    # directions, disregarding whether it was left or right
    direction_difference = abs(stronghold_direction - aim_direction)
    # secondly we check how far off the distance was from the target distance
    # again, we use the `abs` function to get the "absolute" difference
    # between the distances, disregarding whether it was to short or too far
    distance_difference = abs(stronghold_distance - missile_distance)

    # if the direction was with 2 degrees of the actual direction, and the
    # distance was within 0.05 of the actual distance, the target was hit
    good_direction = direction_difference <= 2
    good_distance = distance_difference <= 0.05

    if good_direction and good_distance:
        # record that the stronghold has been destroyed!
        stronghold_is_destroyed = True
    else:
        # the player missed the target - create a message to help them
        # aim better the next time around:
        message = 'The missile '

        # give information about the direction, if that was wrong:
        if not good_direction:
            if aim_direction < stronghold_direction:
                message += 'landed to the left'
            else:
                message += 'landed to the right'

        # if the direction and distance were both wrong, we need to
        # put an 'and' in to make the sentence make sense:
        if not good_direction and not good_distance:
            message += ' and '

        # give information about the distance, if that was wrong:
        if not good_distance:
            if missile_distance < stronghold_distance:
                message += 'did not travel far enough'
            else:
                message += 'travelled too far'

        # finish off the message nicely with a period for good punctuation:
        message += '.'

        # show the created message to help the player out:
        print(message)

if stronghold_is_destroyed:
    # the player hit the target - show a congratulatory message
    print()
    print('*KABOOOMMM*')
    print("You've done it")
    print()
else:
    # the player missed the target with all their missiles
    print()
    print('Disaster - you failed.')
    print('Retreat in disgrace.')
    print()
