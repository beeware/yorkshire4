# Import:
# * the `random` module so we can generate random numbers,
# * the `math` module so we can perform some 'advanced' mathematical operations
# * `select`, `sys`, `termios` and `tty` to manipulate the terminal
import random
import sys

# Define a utility method to clear the screen.
# This uses "ANSI Escape Sequences" - special combinations of
# characters that are understood by the terminal, but are difficult
# (or impossible) to type on a keyboard. `\033[` is the
# "escape sequence"; the characters after the escape sequnce are
# interpreted as commands. In this case, we're using:
#   2J - clear screen; and
#   H - move the cursor to the Home position (top left corner)
#
# For more details about ANSI escape sequences, see:
#     https://en.wikipedia.org/wiki/ANSI_escape_code
#
def clear_screen():
    print('\033[2J\033[H', end='')
    sys.stdout.flush()


ADVENTURE_MAP = [
    # row 0
    [
        # Rooms 0 - 7
        {'description': 'Dark Corner', 'objects': set(), 'exits': 'se'},
        {'description': 'Overgrown Garden', 'objects': set(), 'exits': 'we'},
        {'description': 'By Large Woodpile', 'objects': {'axe',}, 'exits': 'we'},
        {'description': 'Yard by Rubbish', 'objects': set(), 'exits': 'swe'},
        {'description': 'Weedpatch', 'objects': {'shovel',}, 'exits': 'we'},
        {'description': 'Forest', 'objects': set(), 'exits,}': 'we'},
        {'description': 'Thick Forest', 'objects': set(), 'exits': 'swe'},
        {'description': 'Blasted Tree', 'objects': {'rope',}, 'exits': 'ws'},
    ],
    # row 1
    [
        # Rooms 0 - 7
        {'description': 'Corner of House', 'objects': set(), 'exits': 'ns'},
        {'description': 'Entrance to Kitchen', 'objects': set(), 'exits': 'se'},
        {'description': 'Kutchen & Grimy Cooker', 'objects': {'matches',}, 'exits': 'we'},
        {'description': 'Scullery Door', 'objects': set(), 'exits': 'nw'},
        {'description': 'Room with Inches of Dust', 'objects': set(), 'exits': 'se'},
        {'description': 'Rear Turret Room', 'objects': {'scroll',}, 'exits': 'w'},
        {'description': 'Clearing by House', 'objects': set(), 'exits': 'ne'},
        {'description': 'Path', 'objects': set(), 'exits': 'nsw'},
    ],
    # row 2
    [
        # Rooms 0 - 7
        {'description': 'Side of House', 'objects': set(), 'exits': 'ns'},
        {'description': 'Back of Hallway', 'objects': set(), 'exits': 'ns'},
        {'description': 'Dark Alcove', 'objects': {'coins',}, 'exits': 'se'},
        {'description': 'Small Dark Room', 'objects': set(), 'exits': 'we'},
        {'description': 'Bottom of Spiral Staircase', 'objects': set(), 'exits': 'nwud'},
        {'description': 'Wide Passage', 'objects': set(), 'exits': 'sw'},
        {'description': 'Slippery Steps', 'objects': set(), 'exits': 'wsud'},
        {'description': 'Clifftop', 'objects': set(), 'exits': 'ns'},
    ],
    # row 3
    [
        # Rooms 0 - 7
        {'description': 'Near Crumbling Wall', 'objects': set(), 'exits': 'n'},
        {'description': 'Gloomy Passage', 'objects': {'vacuum',}, 'exits': 'ns'},
        {'description': 'Pool of Light', 'objects': {'batteries',}, 'exits': 'nse'},
        {'description': 'Impressive Vaulted Hallway', 'objects': set(), 'exits': 'we'},
        {'description': 'Hall By Thick Wooden Door', 'objects': {'statue',}, 'exits': 'we'},
        {'description': 'Trophy Room', 'objects': set(), 'exits': 'nsw'},
        {'description': 'Cellar with Barred Window', 'objects': set(), 'exits': 'ns'},
        {'description': 'Cliff Path', 'objects': set(), 'exits': 'ns'},
    ],
    # row 4
    [
        # Rooms 0 - 7
        {'description': 'Cupboard with Hanging Coat', 'objects': set(), 'exits': 's'}, # there is a hidden key in the coat
        {'description': 'Front Hall', 'objects': set(), 'exits': 'nse'},
        {'description': 'Sitting Room', 'objects': set(), 'exits': 'nsw'},
        {'description': 'Secret Room', 'objects': {'magic spells',}, 'exits': 's'},
        {'description': 'Steep Marble Stairs', 'objects': set(), 'exits': 'nsud'},
        {'description': 'Dining Room', 'objects': set(), 'exits': 'n'},
        {'description': 'Deep Cellar with Coffin', 'objects': {'ring',}, 'exits': 'n'},
        {'description': 'Cliff Path', 'objects': set(), 'exits': 'ns'},
    ],
    # row 5
    [
        # Rooms 0 - 7
        {'description': 'Closet', 'objects': set(), 'exits': 'ne'},
        {'description': 'Front Lobby', 'objects': set(), 'exits': 'nw'},
        {'description': 'Library of Evil Books', 'objects': {'candlestick',}, 'exits': 'ne'},
        {'description': 'Study with Desk & Hole in Wall', 'objects': {'candle',}, 'exits': 'w'},
        {'description': 'Weird Cobwebby Room', 'objects': set(), 'exits': 'nse'},
        {'description': 'Very Cold Chamber', 'objects': set(), 'exits': 'we'},
        {'description': 'Spooky Room', 'objects': {'painting',}, 'exits': 'w'},
        {'description': 'Cliff Path by Marsh', 'objects': {'boat',}, 'exits': 'ns'},
    ],
    # row 6
    [
        # Rooms 0 - 7
        {'description': 'Rubble Strewn Verandah', 'objects': set(), 'exits': 'se'},
        {'description': 'Front Porch', 'objects': set(), 'exits': 'nsw'},
        {'description': 'Front Tower', 'objects': {'goblet',}, 'exits': 'e'},
        {'description': 'Sloping Corridor', 'objects': set(), 'exits': 'we'},
        {'description': 'Upper Gallery', 'objects': set(), 'exits': 'nw'},
        {'description': 'Marsh by Wall', 'objects': set(), 'exits': 's'},
        {'description': 'Marsh', 'objects': set(), 'exits': 'sw'},
        {'description': 'Soggy Path', 'objects': set(), 'exits': 'nw'},
    ],
    # row 7
    [
        # Rooms 0 - 7
        {'description': 'By Twisted Railing', 'objects': set(), 'exits': 'ne'},
        {'description': 'Path Through Iron Gate', 'objects': set(), 'exits': 'nwe'},
        {'description': 'By Railings', 'objects': set(), 'exits': 'we'},
        {'description': 'Beneath Front Tower', 'objects': set(), 'exits': 'we'},
        {'description': 'Debris from Crumbling Facade', 'objects': {'aerosol',}, 'exits': 'we'},
        {'description': 'Large Fallen Brickwork', 'objects': set(), 'exits': 'nwe'},
        {'description': 'Rotting Stone Arch', 'objects': set(), 'exits': 'nwe'},
        {'description': 'Crumbling Clifftop', 'objects': set(), 'exits': 'w'},
    ]
]

def get_room(room_coords):
    try:
        row = room_coords[0]
        col = room_coords[1]
        return ADVENTURE_MAP[row][col]
    except IndexError:
        return None


def is_in_room(room_coords, current_location):
    return room_coords[0] == current_location[0] and room_coords[1] == current_location[1]


def move_north(current_location):
    current_location[0] = max(0, current_location[0] - 1)


def move_south(current_location):
    current_location[0] = min(MAP_ROWS - 1, current_location[0] + 1)


def move_east(current_location):
    current_location[1] = min(MAP_COLS - 1, current_location[1] + 1)


def move_west(current_location):
    current_location[1] = max(0, current_location[1] - 1)


def verb_help(verb=None, obj=None):
    return 'Words I know: ' + ', '.join(VERB_HANDLERS.keys())


def verb_carrying(verb=None, obj=None):
    if not inventory:
        return 'You are carrying nothing.'
    return 'You are carrying: '+ ', '.join([item for item in inventory])


def verb_go(verb=None, obj=None):
    room = get_room(current_location)
    room_exits = room.get('exits', '')
    lookup_key = verb if obj is None else obj[0]
    message = 'OK'
    if lookup_key not in room_exits:
        message = 'You can\'t go that way'
    else:
        # direction is n=1, s=2, w=3, e=4, u=5 and d=5, so...
        direction_lookup = {'n': 1, 's': 2, 'w': 3, 'e': 4, 'u': 5, 'd': 6}
        direction = 0
        direction  = direction_lookup.get(lookup_key, 0)

        # special handling for up and down conversion to the 2D map
        # for certain rooms - note that though some rooms have 'up '
        # and 'down' exits available, they actually translate to
        # n/s/e/w directions on the map
        if direction == 5 or direction == 6:
            # going up or down?
            if current_location[0] == 2 and current_location[1] == 4:
                # Room 20 - spiral staircase
                direction = 1 if direction == 5 else direction
                direction = 3 if direction == 6 else direction
            elif current_location[0] == 2 and current_location[1] == 6:
                # Room 22 - slippery steps
                direction = 3 if direction == 5 else direction
                direction = 2 if direction == 6 else direction
            elif current_location[0] == 4 and current_location[1] == 4:
                # Room 36 - steep marble steps
                direction = 2 if direction == 5 else direction
                direction = 1 if direction == 6 else direction
        # special handling for 'activated' circumstances in rooms
        if 'rope' in inventory:
            message = 'Crash! you fell out of the tree!'
            inventory.remove('rope')
        elif current_location[0] == 6 and current_location[1] == 4 and adventure_flags.get('ghosts', False):
            # Room 52 - upper gallery
            message = 'Ghosts will not let you move.'
        elif current_location[0] == 5 and current_location[1] == 5 and 'painting' in inventory and not adventure_flags.get('xzanfar', False):
            # Room 45 - very cold chamber - you need the painting
            message = 'A magical barrier to the west.'
        elif current_location[0] == 3 and current_location[1] == 2 and not adventure_flags.get('lit candle', False) and direction in (1, 4):
            # Room 26 - pool of light - can't go north or east without a light
            message = 'You need a light.'
        elif not 'boat' in inventory and current_location[0] == 3 and current_location[1] == 2:
            # Room 54 - marsh, no boat in inventory TODO
            message = 'You\'re stuck!'
        elif 'boat' in inventory and (
                (current_location[0] == 6 and current_location[1] == 5) or
                (current_location[0] == 6 and current_location[1] == 6) or
                (current_location[0] == 6 and current_location[1] == 7) or
                (current_location[0] == 5 and current_location[1] == 7)
        ):
            # not one of Rooms 53 (marsh by wall), 54 (marsh), 55 (soggy path) or 
            # 47 (cliff path by marsh), and boat is in inventory
            message = 'You can\'t carry a boat!'
        elif (
                (current_location[0] == 3 and current_location[1] >= 2 and current_location[1] <= 6)
        ):
            # rooms 26 - 30 (pool of light, impressive vaulted hallway, hall by thick wooden door,
            # trophy room, cellar with barred window)
            message = 'Too dark to move'
        else:
            if direction == 1:
                move_north(current_location)
            elif direction == 2:
                move_south(current_location)
            elif direction == 3:
                move_west(current_location)
            elif direction == 4:
                move_east(current_location)
            else:
                message = 'You can\'t move that way.'
            if is_in_room((5, 1), current_location) and adventure_flags['up']:
                # room 41 - front lobby and door is open
                room = ADVENTURE_MAP[5][1]
                room['exits'] = 'nw' # south exit (front door) is no longer available
                adventure_flags['up'] = False # flag that the door is shut
                message = 'The door slams shut!'
    return message


def verb_get(verb=None, obj=None):
    message = 'I don\'t know what ' + obj + ' is.'
    if obj in inventory:
        message = 'You already have it.'
    elif obj in adventure_nouns:
        room = get_room(current_location)
        room_objects = room.get('objects', None)
        if obj not in room_objects:
            message = 'It isn\'t here.'
        else:
            inventory.add(obj)
            room_objects.remove(obj)
            message = 'You have the ' + obj
    return message


def verb_open(verb=None, obj=None):
    if is_in_room((5, 3), current_location) and obj in ('drawer', 'desk'):
        # Room 43 - Study with Desk & Hole in Wall
        adventure_flags['candle'] = False  # TODO -is this flag correct...?
        message = 'The drawer is open'
    elif is_in_room((3, 4), current_location) and obj == 'door':
        # Room 28 - hall by thick wooden door
        message = 'It\'s locked'
    elif is_in_room((3, 4), current_location) and obj == 'coffin':
        # Room 38 - Deep Cellar with Coffin
        message = 'That\'s creepy!'
    else:
        message = 'You can\'t open that'
    return message

def verb_examine(verb=None, obj=None):
    if obj == 'coffin':
        # delegate to 'open' handler
        message = verb_open(verb, obj)
    elif obj in ('books', 'scroll'):
        # delegate to 'read' handler
        message = verb_read(verb, obj)
    elif is_in_room((4, 0), current_location) and obj == 'coat':
        # Room 32 - Cupboard with Hanging Coat - the coat has a key in it
        # which is found upon examination
        if adventure_flags.get('key', False):
            message = 'It\'s just a coat'
        else:
            room = get_room(current_location)
            room['objects'].add('key')
            adventure_flags['key'] = True
            message = 'There\'s something here!'
    elif obj == 'rubbish':
        message = 'That\'s disgusting!'
    elif obj in ('desk', 'drawer'):
        message = 'There\'s a drawer'
    elif is_in_room((5, 3), current_location) and obj == 'walls':
        # Room 43 - Study with Desk & Hole in Wall
        message = 'There is something beyond...'
    elif not obj:
        message = 'What should I examine?'
    else:
        message = 'I don\'t know how to examine that...'
    return message

def verb_read(verb=None, obj=None):
    if is_in_room((5, 2), current_location) and obj == 'books':
        # Room 42 - Library of Evil Books
        message = 'They are demonic works'
    elif obj in ('spells', 'magic spells') and 'magic spells' in inventory and not adventure_flags.get('xzanfar', False):
        # Room 42 - Library of Evil Books
        message = 'Use this word with care: "xzanfar".'
    elif 'scroll' in inventory and obj == 'scroll':
        message = 'The script is in an alien tongue.'
    elif not obj:
        message = 'What should I read?'
    else:
        message = 'I don\'t know how to read that...'
    return message

def verb_say(verb=None, obj=None):
    if not obj:
        message = 'Say... what, exactly?'
    else:    
        message = 'OK: "{}"!'.format(obj)
        if 'magic spells' in inventory and obj == 'xzanfar':
            message = '* Magic Occurs *'
            if is_in_room((5,5), current_location):
                # if we are in room 45 - Very Cold Chamber 'xzanfar' spell is effective
                adventure_flags['xzanfar'] = True
            else:
                # otherwise the 'xzanfar' spell moves the player to a random room
                current_location = [random.randint(0,MAP_ROWS), random.randint(0,MAP_COLS)]
    return message

def verb_dig(verb=None, obj=None):
    if 'shovel' in inventory:
        message = 'You made a hole'
        if is_in_room((3,4), current_location):
            # if we are in room 45 - Cellar with Barred Window
            room = get_room(current_location)
            room['exits'] = 'nse' # east exit becomes available
    else:
        message = 'I don\'t have anything to dig with...'
    return message

def verb_swing(verb=None, obj=None):
    if 'rope' not in inventory and is_in_room((0,7), current_location):
        message = 'This is no time to play games'
        message = 'You don\'t have ' + obj
    elif obj == 'rope' and 'rope' in inventory:
        message = 'You swung it'
    elif obj == 'axe' and 'axe' in inventory:
        message = 'Whoosh!'
        if is_in_room((0,7), current_location):
            # Room 43 - Study with Desk & Hole in Wall
            room = get_room(current_location)
            room['exits'] = 'wn' # north exit becomes available
            room['description'] = 'Study with a Secret Room'
            message = 'You broke through a thin wall'
    elif obj is None:
        message = 'What should I swing?'
    else:
        message = 'I\'m not sure what swinging that would achieve...'
    return message

def verb_climb(verb=None, obj=None):
    if obj == 'rope':
        if 'rope' in inventory:
            message = 'It isn\'t attached to anything'
        elif is_in_room((0,7), current_location):
            if adventure_flags.get('rope', False):
                message = 'Going down!'
                adventure_flags['rope'] = False
            else:
                message = 'You see a thick forest and a cliff south.'
                adventure_flags['rope'] = True
    elif obj is None:
        message = 'What should I climb?'
    else:
        message = 'I\'m not sure what climbing that would achieve...'
    return message

def verb_light(verb=None, obj=None):
    if obj == 'candle':
        if not 'candle' in inventory:        
            message = 'You don\'t have a ' + obj
        else:
            if not 'candlestick' in inventory:
                message = 'It will burn your hands.'
            else:
                if not 'matches' in inventory:
                    message = 'You have nothing to light it with.'
                else:
                    message = 'It casts a flickering light'
                    adventure_flags['lit candle'] = True
    elif obj is None:
        message = 'What should I light?'
    else:
        message = 'I\'m not sure what setting that on fire that would achieve...'
    return message

def verb_unlight(verb=None, obj=None):
    if adventure_flags.get('lit candle', False):
        message = 'Extinguished.'
    elif obj is None:
        message = 'What should I unlight?'
    else:
        message = 'I can\'t extinguish that...'
    return message

def verb_spray(verb=None, obj=None):
    if obj in ('bats', 'aerosol') and 'aerosol' in inventory:
        if adventure_flags.get('bats', False):
            message = 'Pffft! Got those pesky bats!'
            adventure_flags['bats'] = False
        else:
            message = 'Hisssss...'
    elif obj is None:
        message = 'What should I spray?'
    else:
        message = 'I can\'t spray that...'
    return message

def verb_use(verb=None, obj=None):
    if obj == 'vacuum' and 'vacuum' in inventory and 'vacuum' in inventory:
        message = 'Switched on.'
        adventure_flags['vacuum'] = True
        if adventure_flags.get('ghosts', False):
            message = 'Whizz - vacuumed the ghosts up!'
            adventure_flags['ghosts'] = False
    elif obj is None:
        message = 'What should I use?'
    else:
        message = 'I\'m not sure how to use that...'
    return message

def verb_unlock(verb=None, obj=None):
    if is_in_room((5,3), current_location) and obj in ('drawer', 'desk'):
        # Room 43 - Study with Desk & Hole in Wall - delegate to 'open' handler
        message = verb_open(verb, obj)
    elif is_in_room((3,4), current_location) and not adventure_flags.get('door', False) and 'key' in inventory:
        # Room 28 - Hall By Thick Wooden Door
        adventure_flags['door'] = True
        room = get_room(current_location)
        room['exits'] = 'sew' # south exit becomes available
        room['description'] = 'Huge Open Door'
        message = 'The key turns...!'
    elif obj is None:
        message = 'What should I unlock?'
    else:
        message = 'I\'m not sure how I could unlock that...'
    return message

def verb_leave(verb=None, obj=None):
    if obj is None:
        message = 'What should I leave?'
    if obj in inventory:
        inventory.remove(obj)
        room = get_room(current_location)
        room['objects'].add(obj)
        message = 'Done.'
    else:
        message = 'You\'re not carrying that.'
    return message

def verb_score(verb=None, obj=None):
    score = len(inventory)
    if score == 17 and not 'boat' in inventory:
        if is_in_room((7,1), current_location):
            # in room 57 - Path Through Iron Gate
            message = 'Double score for reaching here!'
            score *= 2
        else:
            message = 'You have everything - return to the gate for your final score.'
    return message


VERB_HANDLERS = {
    'help': verb_help,
    'carrying?': verb_carrying,
    'go': verb_go,
    'n': verb_go,
    's': verb_go,
    'w': verb_go,
    'e': verb_go,
    'u': verb_go,
    'd': verb_go,
    'get': verb_get,
    'take': verb_get,
    'open': verb_open,
    'examine': verb_examine,
    'read': verb_read,
    'say':verb_say,
    'dig': verb_dig,
    'swing': verb_swing,
    'climb': verb_climb,
    'light': verb_light,
    'unlight': verb_unlight,
    'spray': verb_spray,
    'use': verb_use,
    'unlock':verb_unlock,
    'leave': verb_leave,
    'score': None,
}

OBJECTS = [
    # These 18 objects are 'gettable'
    'painting', 'ring', 'magic spells', 'goblet', 'scroll', 'coins', 'statue', 'candlestick',
    'matches', 'vacuum', 'batteries', 'shovel', 'axe', 'rope', 'boat', 'aerosol', 'candle', 'key',
    # These 19 objects are not 'gettable' - note that they are not all actually 'objects'
    # but this is how the parsing is set up to work
    'north', 'south', 'east', 'west', 'up', 'down',
    'door', 'bats', 'ghosts', 'drawer', 'desk', 'coat', 'rubbish',
    'coffin', 'books', 'xzanfar', 'walls', 'spells',
]

adventure_flags = dict(zip(OBJECTS, [False,] * len(OBJECTS)))
for x in ['ring', 'candle', 'up', 'bats', 'drawer']:
    adventure_flags[x] = True

MAP_ROWS = 8
MAP_COLS = MAP_ROWS

adventure_nouns = set()
for row in ADVENTURE_MAP:
    for room in row:
        room_objects = room.get('objects', set())
        adventure_nouns.update(room_objects)

adventure_nouns.update(['north', 'south', 'east', 'west', 'up', 'down',
    'key',
    'door', 'bats', 'ghosts', 'drawer', 'desk', 'coat', 'rubbish',
    'coffin', 'books', 'xzanfar', 'walls', 'spells'])
inventory = set()

candlelight_counter = 0
current_location = [7,1] # Room #57 - Path Through Iron Gate
message = 'OK'

# Now we can start the actual game.
clear_screen()
print('Haunted House')
print('-------------')
while True:
    print('Your location:')
    room = ADVENTURE_MAP[current_location[0]][current_location[1]]
    print(room.get('description'))
    print('Exits:')
    print(', '.join(x.upper() for x in room.get('exits')))
    room_objects = room.get('objects')
    if room_objects:
        print('You can see ' + ', '.join(room_objects) + ' here')
    print('='*20)
    print(message)
    message = 'What?'
    user_input = input('What will you do now? ')
    words = user_input.split(' ')
    word_count = len(words)
    if len(words) > 1:
        verb, obj = words[0].lower(), ' '.join(words[1:]).lower()
    else:
        verb = words[0].lower()
        obj = None

    verb_handler = VERB_HANDLERS.get(verb, None)
    if verb_handler is None:
        message = 'I don\'t understand.'
    else:
        if len(words) == 1 or (obj and obj in adventure_nouns):
            message = verb_handler(verb, obj)
        else:
            message = 'There is no ' + obj

    if adventure_flags.get('bats', False) and is_in_room((1, 5), current_location) and not verb is 'spray' and random.randint(1, 3) is not 3:
        # bats are active in Room 13 - Rear Turret Room
        adventure_flags['bats'] = True
        message = 'BATS ATTACKING!!'
    elif is_in_room((5, 4), current_location) and not adventure_flags.get('down', False) and random.randint(1,2) is 1:
        adventure_flags['ghosts'] = True

    print(message)

    if adventure_flags.get('lit candle', False):
        candlelight_counter -= 1
        if candlelight_counter < 10:
            message = 'Your candle is waning...'
            if candlelight_counter < 1:
                adventure_flags['lit candle'] = False
                message = 'Your candle is out!'
        print(message)

    print()
