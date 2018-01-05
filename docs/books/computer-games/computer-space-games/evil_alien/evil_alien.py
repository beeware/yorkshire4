# Import:
# * the `random` module so we can generate random numbers,
from random import randint

print("EVIL ALIEN")

# set the size of the grid
size = 10

# set the size of the goes
goes = 4

# Create a flag to keep track if we've won
won_game = False

# Elron's position is fixed by these lines, 
# which select 3 numbers between 0 and the size of the grid
x = randint(0, size)
y = randint(0, size)
d = randint(0, size)

# start of a loop which tells the computer to repeat the 
# next lines G times
for i in range(goes):
    
    # this section asks you for your 3 numbers and stores them in x1, y1 and d1
    x1 = int(input("X position (0 to 9): "))
    y1 = int(input("Y position (0 to 9): "))
    d1 = int(input("D position (0 to 9): "))
    
    # checks if you were right and jumps to 300 if you were
    if x== x1 and y == y1 and d == d1:
        won_game = True
        break
    
    # your guesses are compared with Elron's position and a report printed
    print('SHOT WAS ')
    if y1 > y:
        print('NORTH')
    if y1 < y:
        print('SOUTH')
    if x1 > x:
        print('EAST')
    if x1 < x:
        print('WEST')

    print()
    
    if d1 > x:
        print('TOO FAR')
    if d1 < x:
        print('NOT FAR ENOUGH')
    # end of loop. returns for another go until 'goes' remain.
    
# prints if you've used up all your goes
if not won_game:
    print('YOUR TIME HAS RUN OUT!!')
else:
    print('*BOOM* YOU GOT HIM!')
