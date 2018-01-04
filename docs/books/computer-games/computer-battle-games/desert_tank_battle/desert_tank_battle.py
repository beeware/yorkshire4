import random

print('Desert Tank Battle')
# The direction (angle) at which the enemy is hiding
enemy_direction = int(random.rand * 181) - 90

# Distance of enemy from your tank
enemy_distance = random.rand

for i in range(1, 5):
    print('Enter the direction (-90 to 90)')
    direction = int(input())

    print('Enter the elevation at which the missile is to be fired (0 to 90)')
    elevaion = int(input())
    # measuring the distance travelled by the missile according to the elevation chosen in above step
    distance = sin(2 * (elavation / 180 * 3.146))

    if abs((enemy_direction - direction) < 2 and abs(enemy_distance - distance) < 0.5:
        print('Kaboom ***')
        print('You have done it!')
        print('Enemy killed')
        break

    print('Missile Landed')

    if direction < enemy_direction:
           print('To the left of enemy')
    elif direction > enemy_direction:
           print('To the right of enemy')

    if abs(enemy_distane-distance) > 0.5 and abs 

