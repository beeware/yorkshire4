# Import random so we can generate random numbers
# Import math to perform mathematics operations like sine cosine etc.

import random
import math

print('Desert Tank Battle')
print('~~~~~~~~~~~~~~~~~~')
# The direction (angle) at which the castle is located,
# The angle is between -90 and 90
castle_direction = int(random.random() * 181) - 90

# Distance of castle from your tank
castle_distance = random.random()
# Checks whether you have destroyed castle or not
flag = 0
# Loop untill either you have destroyed the enemy castle,
# Or you have run out of missiles

for i in range(0, 5):

    print('Commander you have %d missiles left' % (5-i))
    print('Enter the direction (-90 to 90)')
    direction = int(input())

    print('Enter the elevation at which the missile is to be fired (0 to 90)')
    elevation = int(input())

    # Measuring the distance travelled by the missile,
    # According to the elevation chosen in above step
    distance = math.sin(2 * (elevation / 180 * 3.146))

    # You have guessed right direction as well as distance
    if (abs(castle_direction - direction) < 2 and
            abs(castle_distance - distance) < 0.05):
        flag = 1
        break
    # The direction or distance is not accurate to destroy the castle
    print('Missile Landed ', end="")

    if direction < castle_direction:
        print('To the left of enemy ', end="")
    elif direction > castle_direction:
        print('To the right of enemy ', end="")

    if castle_distance - distance > 0.05:
        print('And Not Far Enough ')
    elif distance - castle_distance > 0.05:
        print('And Far Enough')

# The enemy castle is destroyed
if flag == 1:
    print('*Kaboommmm*')
    print('You have destroyed enemy castle')

    # Tank has run out of missiles
else:
    print('Disaster - You Failed')
    print('Retreat in disgrace')
