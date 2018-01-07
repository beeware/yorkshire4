# Import:
# * the `random` module so we can generate random numbers,
# * the `math` module so we can perform some 'advanced' mathematical operations
# * `sys` to manipulate the terminal (for the screen clearing function)
import random
import sys

# Here we define a number of 'constants' - these are variables which store values 
# that are used throughout the game, and which don't change. This means we can use
# the variable name, rather than typing in the value each time. This has a couple
# of advantages:
#  * one is that if we typed in everything manually, there is a chance we could
#    mis-type it, and break the code - for example, if we mis-typed the word 
#    'xzanfar' somewhere, it's likely that the playecould never finish the game
#  * another is that if there is a spelling mistake, or we want to change a word,
#    we only need to change it in one place, and it takes effect everywhere. For
#    example, we could easily change 'xzanfar' to 'abracadabra'

# These are the objects/items in the game
OBJ_AXE = 'axe'
OBJ_SHOVEL = 'shovel'
OBJ_ROPE = 'rope'
OBJ_MATCHES = 'matches'
OBJ_SCROLL = 'scroll'
OBJ_COINS = 'coins'
OBJ_VACUUM = 'vacuum'
OBJ_BATTERIES = 'batteries'
OBJ_STATUE = 'statue'
OBJ_MAGICSPELLS = 'magic spells'
OBJ_RING = 'ring'
OBJ_CANDLESTICK = 'candlestick'
OBJ_CANDLE = 'candle'
OBJ_PAINTING = 'painting'
OBJ_BOAT = 'boat'
OBJ_GOBLET = 'goblet'
OBJ_AEROSOL = 'aerosol'
OBJ_KEY = 'key'
OBJ_DOOR = 'door'
OBJ_BATS = 'bats'
OBJ_GHOSTS = 'ghosts'
OBJ_DRAWER = 'drawer'
OBJ_DESK = 'desk'
OBJ_COAT = 'coat'
OBJ_RUBBISH = 'rubbish'
OBJ_COFFIN = 'coffin'
OBJ_BOOKS = 'books'
OBJ_XZANFAR = 'xzanfar'
OBJ_WALLS = 'walls'
OBJ_SPELLS = 'spells'

# These are the verbs/commands the player can use in the game
VERB_HELP = 'help'
VERB_CARRYING = 'carrying?'
VERB_GO = 'go'
VERB_N = 'n'
VERB_S = 's'
VERB_W = 'w'
VERB_E = 'e'
VERB_U = 'u'
VERB_D = 'd'
VERB_GET = 'get'
VERB_TAKE = 'take'
VERB_OPEN = 'open'
VERB_EXAMINE = 'examine'
VERB_READ = 'read'
VERB_SAY = 'say'
VERB_DIG = 'dig'
VERB_SWING = 'swing'
VERB_CLIMB = 'climb'
VERB_LIGHT = 'light'
VERB_UNLIGHT = 'unlight'
VERB_SPRAY = 'spray'
VERB_USE = 'use'
VERB_UNLOCK = 'unlock'
VERB_LEAVE = 'leave'
VERB_SCORE = 'score'

# these are special 'flags', which are used to keep track of whether
# something has happened (or is active) or not
FLAG_LIT_CANDLE = 'lit candle'

# these are the directions
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'

# this next part is quite large and defines the the game map
# the map is on an 8 x 8 grid (8 rows, and 8 columns)
GAME_MAP_ROWS = 8
GAME_MAP_COLS = GAME_MAP_ROWS

# The Game Map:
#                          NORTH
#
#           0    1    2    3    4    5    6    7
#         +----+----+----+----+----+----+----+----+
#         |                                       |
#      0  | 0    1    2    3    4    5    6    7  |
#         |                                       |
#         +    +----+----+    +----+----+         +
#         |    |              |         |         |
#      1  | 8  | 9    10   11 | 12   13 | 14   15 |
#         |    |              |         |         |
#         +    +    +----+----+VVVV+----+----+    +
#         |    |    |         <    |         |    |
#      2  | 16 | 17 | 18   19 < 20 | 21   22 | 23 |
#         |    |    |         <    |         |    |
#         +    +    +    +----+----+    +VVVV+    +
#         |    |    |                   |    $    |
#      3  | 24 | 25 | 26   27   28   29 | 30 $ 31 |
#         |    |    |                   |    $    |
# WEST    +----+    +    +----+%%%%+    +    +    +    EAST
#         |    |         |    |^^^^|    |    |    |
#      4  | 32 | 33   34 | 35 | 36 | 37 | 38 | 39 |
#         |    |         |    |    |    |    |    |
#         +    +    +    +====+    +----+----+    +
#         |         |                        |    |
#      5  | 40   41 | 42   43   44   45   46 | 47 |
#         |         |                        |    |
#         +----+    +----+----+    +----+----+    +
#         |         |              |              |
#      6  | 48   49 | 50   51   52 | 53   54   55 |
#         |         |              |              |
#         |         +----+----+----+              +
#         |                                       |
#      7  | 56   57   58   59   60   61   62   63 |
#         |                                       |
#         +----+----+----+----+----+----+----+----+
#
#                          SOUTH
#
# LEGEND:
#     ====      - false wall
#
#     %%%%      - locked door
#
#        $
#        $      - barred window
#        $
#
#     ^^^^      - downward exit (in direction of arrows)
#
#     VVVV      - downward exit (in direction of arrows)
#
#     <
#     <         - downward exit (in direction of arrows)
#     <
#
#     >
#     >         - downward exit (in direction of arrows)
#     >
#
#
# Note that some exits are up or down (rooms 20, 22 and 36), but these are 
# translated into north, south, east or west directions by the game if the 
# player uses  one of those exits so that it makes sense on the map.
#
# This array defines all the rooms in the map, including the objects they contain
# and what exits are available. Note that while this is defined as a 'constant'
# it will actually be modified occasionally during the game as the player picks 
# up and  leaves objects, or events occur which may change the description of 
# the room, or even what exits are available (if the player unlocks a door, 
# for example)
GAME_MAP = [
    # row 0
    [
        # Rooms 0 - 7
        {'description': 'Dark Corner', 'objects': set(), 'exits': 'se'},
        {'description': 'Overgrown Garden', 'objects': set(), 'exits': 'we'},
        {'description': 'By Large Woodpile', 'objects': {OBJ_AXE,}, 'exits': 'we'},
        {'description': 'Yard by Rubbish', 'objects': set(), 'exits': 'swe'},
        {'description': 'Weedpatch', 'objects': {OBJ_SHOVEL,}, 'exits': 'we'},
        {'description': 'Forest', 'objects': set(), 'exits,}': 'we'},
        {'description': 'Thick Forest', 'objects': set(), 'exits': 'swe'},
        {'description': 'Blasted Tree', 'objects': {OBJ_ROPE,}, 'exits': 'ws'},
    ],
    # row 1
    [
        # Rooms 8 - 15
        {'description': 'Corner of House', 'objects': set(), 'exits': 'ns'},
        {'description': 'Entrance to Kitchen', 'objects': set(), 'exits': 'se'},
        {'description': 'Kutchen & Grimy Cooker', 'objects': {OBJ_MATCHES,}, 'exits': 'we'},
        {'description': 'Scullery Door', 'objects': set(), 'exits': 'nw'},
        {'description': 'Room with Inches of Dust', 'objects': set(), 'exits': 'se'},
        {'description': 'Rear Turret Room', 'objects': {OBJ_SCROLL,}, 'exits': 'w'},
        {'description': 'Clearing by House', 'objects': set(), 'exits': 'ne'},
        {'description': 'Path', 'objects': set(), 'exits': 'nsw'},
    ],
    # row 2
    [
        # Rooms 16 - 23
        {'description': 'Side of House', 'objects': set(), 'exits': 'ns'},
        {'description': 'Back of Hallway', 'objects': set(), 'exits': 'ns'},
        {'description': 'Dark Alcove', 'objects': {OBJ_COINS,}, 'exits': 'se'},
        {'description': 'Small Dark Room', 'objects': set(), 'exits': 'we'},
        {'description': 'Bottom of Spiral Staircase', 'objects': set(), 'exits': 'nwud'},
        {'description': 'Wide Passage', 'objects': set(), 'exits': 'sw'},
        {'description': 'Slippery Steps', 'objects': set(), 'exits': 'wsud'},
        {'description': 'Clifftop', 'objects': set(), 'exits': 'ns'},
    ],
    # row 3
    [
        # Rooms 24 - 31
        {'description': 'Near Crumbling Wall', 'objects': set(), 'exits': 'n'},
        {'description': 'Gloomy Passage', 'objects': {OBJ_VACUUM,}, 'exits': 'ns'},
        {'description': 'Pool of Light', 'objects': {OBJ_BATTERIES,}, 'exits': 'nse'},
        {'description': 'Impressive Vaulted Hallway', 'objects': set(), 'exits': 'we'},
        {'description': 'Hall By Thick Wooden Door', 'objects': {OBJ_STATUE,}, 'exits': 'we'},
        {'description': 'Trophy Room', 'objects': set(), 'exits': 'nsw'},
        {'description': 'Cellar with Barred Window', 'objects': set(), 'exits': 'ns'},
        {'description': 'Cliff Path', 'objects': set(), 'exits': 'ns'},
    ],
    # row 4
    [
        # Rooms 32 - 39
        {'description': 'Cupboard with Hanging Coat', 'objects': set(), 'exits': 's'}, # there is a hidden key in the coat
        {'description': 'Front Hall', 'objects': set(), 'exits': 'nse'},
        {'description': 'Sitting Room', 'objects': set(), 'exits': 'nsw'},
        {'description': 'Secret Room', 'objects': {OBJ_MAGICSPELLS,}, 'exits': 's'},
        {'description': 'Steep Marble Stairs', 'objects': set(), 'exits': 'nsud'},
        {'description': 'Dining Room', 'objects': set(), 'exits': 'n'},
        {'description': 'Deep Cellar with Coffin', 'objects': {OBJ_RING,}, 'exits': 'n'},
        {'description': 'Cliff Path', 'objects': set(), 'exits': 'ns'},
    ],
    # row 5
    [
        # Rooms 40 - 47
        {'description': 'Closet', 'objects': set(), 'exits': 'ne'},
        {'description': 'Front Lobby', 'objects': set(), 'exits': 'nw'},
        {'description': 'Library of Evil Books', 'objects': {OBJ_CANDLESTICK,}, 'exits': 'ne'},
        {'description': 'Study with Desk & Hole in Wall', 'objects': {OBJ_CANDLE,}, 'exits': 'w'},
        {'description': 'Weird Cobwebby Room', 'objects': set(), 'exits': 'nse'},
        {'description': 'Very Cold Chamber', 'objects': set(), 'exits': 'we'},
        {'description': 'Spooky Room', 'objects': {OBJ_PAINTING,}, 'exits': 'w'},
        {'description': 'Cliff Path by Marsh', 'objects': {OBJ_BOAT,}, 'exits': 'ns'},
    ],
    # row 6
    [
        # Rooms 48 - 55
        {'description': 'Rubble Strewn Verandah', 'objects': set(), 'exits': 'se'},
        {'description': 'Front Porch', 'objects': set(), 'exits': 'nsw'},
        {'description': 'Front Tower', 'objects': {OBJ_GOBLET,}, 'exits': 'e'},
        {'description': 'Sloping Corridor', 'objects': set(), 'exits': 'we'},
        {'description': 'Upper Gallery', 'objects': set(), 'exits': 'nw'},
        {'description': 'Marsh by Wall', 'objects': set(), 'exits': 's'},
        {'description': 'Marsh', 'objects': set(), 'exits': 'sw'},
        {'description': 'Soggy Path', 'objects': set(), 'exits': 'nw'},
    ],
    # row 7
    [
        # Rooms 56 - 63
        {'description': 'By Twisted Railing', 'objects': set(), 'exits': 'ne'},
        {'description': 'Path Through Iron Gate', 'objects': set(), 'exits': 'nwe'},
        {'description': 'By Railings', 'objects': set(), 'exits': 'we'},
        {'description': 'Beneath Front Tower', 'objects': set(), 'exits': 'we'},
        {'description': 'Debris from Crumbling Facade', 'objects': {OBJ_AEROSOL,}, 'exits': 'we'},
        {'description': 'Large Fallen Brickwork', 'objects': set(), 'exits': 'nwe'},
        {'description': 'Rotting Stone Arch', 'objects': set(), 'exits': 'nwe'},
        {'description': 'Crumbling Clifftop', 'objects': set(), 'exits': 'w'},
    ]
]

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

# Utility method to join a list of words using commas and an "and". For example:
#        and_join(['banana','apple','pear']) ==> 'banana, apple and pear'
def and_join(words):
    return join(words, 'and')


# Utility method to join a list of words using commas and an "or". For example:
#    or_join(['banana','apple','pear']) ==> 'banana, apple or pear'
def or_join(words):
    return join(words, 'or')


# Utility method to join a list of words using commas and a joining word. For example:
#    _join(['banana','apple','pear', 'or']) ==> 'banana, apple or pear'
def join(words, joiner):
    if not words:
        return ''
    # strip leading and/or trailing spaces from words, and remove any empty strings from the list
    try:
        words = [str(x) for x in words]
        words = [x.strip() for x in words if len(x.strip()) > 0]
        if not words:
            return ''
        return words[0] if len(words) == 1 else (' {} '.format(joiner)).join((', '.join(words[0:-1]), words[-1]))
    except TypeError:
        # words is not an iterable object
        pass
    return ''

# Defines a utility method to check if the room coordinates match
# the given location
def is_in_room(room_coords, location):
    return room_coords[0] == location[0] and room_coords[1] == location[1]


# Defines a utility method to "get" the room definition for
# the given map coordinates
def get_room(map_coords):
    try:
        row = map_coords[0]
        col = map_coords[1]
        return GAME_MAP[row][col]
    except IndexError:
        return None


# Defines a utility method to get the room exits for
# the given room definition
def get_room_exits(room):
    return room.get('exits', '')


# Defines a utility method to change the room exits for
# the given room definition
def update_room_exits(room, exits):
    room['exits'] = exits


# Defines a utility method to get the room description for
# the given room definition
def get_room_description(room):
    return room.get('description', '')


# Defines a utility method to change the room description for
# the given room definition
def update_room_description(room, description):
    room['description'] = description


# Defines a utility method to get the contents for the
# given room definition
def get_room_contents(room):
    return room.get('objects', set())


# Defines a utility method to check if the given room
# definition currently contains the given object
def room_contains(room, obj):
    return obj in get_room_contents(room)


# Defines a utility method to add an object to the given
# room's contents
def add_object_to_room(room, obj):
    get_room_contents(room).add(obj)


# Defines a utility method to remove an object from the given
# room's contents
def remove_object_from_room(room, obj):
    get_room_contents(room).remove(obj)


# Defines a utility method to check if a given game flag is
# currently active
def is_active(flag):
    return game_flags.get(flag, False)


# Defines a utility method to set a given game flag to
# active or inactive
def set_flag_state(flag, is_active):
    game_flags[flag] = True


# Defines a utility method to activate a given game flag. Note
# that this actually just calls set_flag_state(True), but makes
# the code a bit easier to read
def activate_flag(flag):
    set_flag_state(flag, True)


# Defines a utility method to deactivate a given game flag. Note
# that this actually just calls set_flag_state(False), but makes
# the code a bit easier to read
def deactivate_flag(flag):
    set_flag_state(flag, False)


# Defines a utility method to check if the player is holding the
# given object
def is_holding(obj):
    return obj in inventory


# Defines a utility method to 'drop' the given object into the room
def drop_item(obj, room):
    # you can only drop something if you have it!
    if is_holding(obj):
        inventory.remove(obj)
        add_object_to_room(room, obj)


# Defines a utility method to 'take' the given object from the room
def take_item(obj, room):
    # you can only take if the room contains it!
    if room_contains(room, obj):
        remove_object_from_room(room, obj)
        inventory.add(obj)


# Defines a utility method to update the given location by the given
# displacement
def move(current_location, displacement):
    new_row = current_location[0] + displacement[0]
    new_col = current_location[1] + displacement[1]
    new_row = min(GAME_MAP_ROWS - 1, max(0, new_row))
    new_col = min(GAME_MAP_COLS - 1, max(0, new_col))
    current_location[0] = new_row
    current_location[1] = new_col


# The handler function for the verb 'help'
def verb_help(verb, current_location, obj=None):
    return 'Words I know: ' + or_join(VERB_HANDLERS.keys())


# The handler function for the verb 'carrying?'
def verb_carrying(verb, current_location, obj=None):
    if not inventory:
        return 'You are carrying nothing.'
    return 'You are carrying: '+ and_join(inventory)


# The handler function for the verbs 'go', 'n', 's', 'w', w', 'u' and 'd'
def verb_go(verb, current_location, obj=None):
    room = get_room(current_location)
    room_exits = get_room_exits(room)
    direction = verb if obj is None else obj[0]
    message = 'OK'
    if direction not in room_exits:
        message = 'You can\'t go that way'
    else:
        # special handling for up and down conversion to the 2D map
        # for certain rooms - note that though some rooms have 'up '
        # and DOWN exits available, they actually translate to
        # n/s/e/w directions on the map
        if direction == 'u' or direction == 'd':
            # going up or down?
            if is_in_room((2, 4), current_location):
                # Room 20 - spiral staircase
                # UP is actually a NORTH move on the map
                direction = 'n' if direction == 'u' else direction
                # DOWN is actually a WEST move on the map
                direction = 'w' if direction == 'd' else direction
            elif is_in_room((2, 6), current_location):
                # Room 22 - slippery steps
                # UP is actually a WEST move on the map
                direction = 'w' if direction == 'u' else direction
                # DOWN is actually a SOUTH move on the map
                direction = 's' if direction == 'd' else direction
            elif is_in_room((4, 4), current_location):
                # Room 36 - steep marble steps
                # UP is actually a SOUTH move on the map
                direction = 's' if direction == 'u' else direction
                # DOWN is actually a NORTH move on the map
                direction = 'n' if direction == 'd' else direction
        # special handling for 'activated' circumstances in rooms
        if is_holding(OBJ_ROPE):
            message = 'Crash! you fell out of the tree!'
            inventory.remove(OBJ_ROPE)
        elif is_in_room((6, 4), current_location) and is_active(OBJ_GHOSTS):
            # Room 52 - upper gallery
            message = 'Ghosts will not let you move.'
        elif is_in_room((5, 6), current_location) and is_holding(OBJ_PAINTING) and not is_active(OBJ_XZANFAR):
            # Room 45 - very cold chamber - you need the painting
            message = 'A magical barrier to the west.'
        elif is_in_room((3, 2), current_location) and not is_active(FLAG_LIT_CANDLE) and direction in 'ne':
            # Room 26 - pool of light - can't go north or east without a light
            message = 'You need a light.'
        elif is_in_room((3, 2), current_location) and not is_holding(OBJ_BOAT):
            # Room 54 - marsh, no boat in inventory
            message = 'You\'re stuck!'
        elif is_holding(OBJ_BOAT) and (
                is_in_room((6, 5), current_location) or
                is_in_room((6, 6), current_location) or
                is_in_room((6, 7), current_location) or
                is_in_room((5, 7), current_location)
        ):
            # not one of Rooms 53 (marsh by wall), 54 (marsh), 55 (soggy path) or
            # 47 (cliff path by marsh), and boat is in inventory
            message = 'You can\'t carry a {}!'.format(OBJ_BOAT)
        elif (
                (current_location[0] == 3 and current_location[1] >= 2 and current_location[1] <= 6)
        ):
            # rooms 26 - 30 (pool of light, impressive vaulted hallway, hall by thick wooden door,
            # trophy room, cellar with barred window)
            message = 'Too dark to move'
        else:
            displacement_lookup = {
                'n':(-1, 0),
                's':(1, 0),
                'w':(0, -1),
                'e':(0, 1),
            }
            displacement = displacement_lookup.get(direction, 0)
            move(current_location, displacement)

            if is_in_room((5, 1), current_location) and is_active(UP):
                # room 41 - front lobby and door is open
                room = get_room(current_location)
                update_room_exits(room, 'nw') # south exit (front door) is no longer available
                deactivate_flag(UP) # flag that the door is shut
                message = 'The door slams shut!'
    return message

# The handler function for the verb 'get'
def verb_get(verb, current_location, obj=None):
    message = 'I don\'t know what ' + obj + ' is.'
    if is_holding(obj):
        message = 'You already have it.'
    elif obj in adventure_nouns:
        room = get_room(current_location)
        if not room_contains(room, obj):
            message = 'It isn\'t here.'
        else:
            take_item(obj, room)
            message = 'You have the ' + obj
    return message

# The handler function for the verb 'open'
def verb_open(verb, current_location, obj=None):
    if is_in_room((5, 3), current_location) and obj in (OBJ_DRAWER, OBJ_DESK):
        # Room 43 - Study with Desk & Hole in Wall
        deactivate_flag(OBJ_CANDLE)  # TODO -is this flag correct...?
        message = 'The {} is open'.format(OBJ_DRAWER)
    elif is_in_room((3, 4), current_location) and obj == OBJ_DOOR:
        # Room 28 - hall by thick wooden door
        message = 'It\'s locked'
    elif is_in_room((3, 4), current_location) and obj == OBJ_COFFIN:
        # Room 38 - Deep Cellar with Coffin
        message = 'That\'s creepy!'
    else:
        message = 'You can\'t {} that'.format(verb)
    return message

# The handler function for the verb 'examine'
def verb_examine(verb, current_location, obj=None):
    if obj == OBJ_COFFIN:
        # delegate to VERB_OPEN handler
        message = verb_open(verb, obj)
    elif obj in (OBJ_BOOKS, OBJ_SCROLL):
        # delegate to VERB_READ handler
        message = verb_read(verb, obj)
    elif is_in_room((4, 0), current_location) and obj == OBJ_COAT:
        # Room 32 - Cupboard with Hanging Coat - the coat has a key in it
        # which is found upon examination
        if is_active(OBJ_KEY):
            message = 'It\'s just a {}'.format(OBJ_COAT)
        else:
            room = get_room(current_location)
            add_object_to_room(room, OBJ_KEY)
            activate_flag(OBJ_KEY)
            message = 'There\'s something here!'
    elif obj == OBJ_RUBBISH:
        message = 'That\'s disgusting!'
    elif obj in (OBJ_DESK, OBJ_DRAWER):
        message = 'There\'s a drawer'
    elif is_in_room((5, 3), current_location) and obj == OBJ_WALLS:
        # Room 43 - Study with Desk & Hole in Wall
        message = 'There is something beyond...'
    elif not obj:
        message = 'What should I {}?'.format(verb)
    else:
        message = 'I don\'t know how to {} that...'.format(verb)
    return message

# The handler function for the verb 'read'
def verb_read(verb, current_location, obj=None):
    if is_in_room((5, 2), current_location) and obj == OBJ_BOOKS:
        # Room 42 - Library of Evil Books
        message = 'They are demonic works'
    elif obj in (OBJ_SPELLS, OBJ_MAGICSPELLS) and is_holding(OBJ_MAGICSPELLS) and not is_active(OBJ_XZANFAR):
        # Room 42 - Library of Evil Books
        message = 'Use this word with care: "{}".'.format(OBJ_XZANFAR)
    elif obj == OBJ_SCROLL and is_holding(OBJ_SCROLL):
        message = 'The script is in an alien tongue.'
    elif not obj:
        message = 'What should I {}?'.format(verb)
    else:
        message = 'I don\'t know how to {} that...'.format(verb)
    return message

# The handler function for the verb 'say'
def verb_say(verb, current_location, obj=None):
    if not obj:
        message = 'Say... what, exactly?'
    else:    
        message = 'OK: "{}"!'.format(obj)
        if obj == OBJ_XZANFAR and is_holding(OBJ_MAGICSPELLS):
            message = '* Magic Occurs *'
            if is_in_room((5, 5), current_location):
                # if we are in room 45 - Very Cold Chamber OBJ_XZANFAR spell is effective
                activate_flag(OBJ_XZANFAR)
            else:
                # otherwise the OBJ_XZANFAR spell moves the player to a random room
                current_location[0] = random.randint(0,GAME_MAP_ROWS - 1)
                current_location[1] = random.randint(0,GAME_MAP_COLS - 1)
    return message

# The handler function for the verb 'dig'
def verb_dig(verb, current_location, obj=None):
    if is_holding(OBJ_SHOVEL):
        message = 'You made a hole'
        if is_in_room((3, 4), current_location):
            # if we are in room 45 - Cellar with Barred Window
            room = get_room(current_location)
            update_room_exits(room, 'nse') # east exit becomes available
    else:
        message = 'You seriously expect me to to {} with my bare hands...?!?'.format(verb)
    return message

# The handler function for the verb 'swing'
def verb_swing(verb, current_location, obj=None):
    if not is_holding(OBJ_ROPE) and is_in_room((0,7), current_location):
        message = 'This is no time to play games'
        message = 'You don\'t have ' + obj
    elif obj == OBJ_ROPE and is_holding(OBJ_ROPE):
        message = 'You swung it'
    elif obj == OBJ_AXE and is_holding(OBJ_AXE):
        message = 'Whoosh!'
        if is_in_room((0, 7), current_location):
            # Room 43 - Study with Desk & Hole in Wall
            room = get_room(current_location)
            update_room_exits(room, 'wn') # north exit becomes available
            update_room_description(room, 'Study with a Secret Room')
            message = 'You broke through a thin wall.'
    elif obj is None:
        message = 'What should I {}?'.format(verb)
    else:
        message = 'I\'m not sure what swinging that would achieve...'
    return message

# The handler function for the verb 'climb'
def verb_climb(verb, current_location, obj=None):
    if obj == OBJ_ROPE:
        if is_holding(OBJ_ROPE):
            message = 'It isn\'t attached to anything'
        elif is_in_room((0, 7), current_location):
            if is_active(OBJ_ROPE):
                message = 'Going down!'
                deactivate_flag(OBJ_ROPE)
            else:
                message = 'You see a thick forest and a cliff south.'
                activate_flag(OBJ_ROPE)
    elif obj is None:
        message = 'What should I {}?'.format(verb)
    else:
        message = 'I\'m not sure what climbing that would achieve...'
    return message

# The handler function for the verb 'light'
def verb_light(verb, current_location, obj=None):
    if obj == OBJ_CANDLE:
        if not is_holding(OBJ_CANDLE):        
            message = 'You don\'t have a ' + obj
        else:
            if not is_holding(OBJ_CANDLESTICK):
                message = 'It will burn your hands.'
            else:
                if not is_holding(OBJ_MATCHES):
                    message = 'You have nothing to light it with.'
                else:
                    message = 'It casts a flickering light'
                    activate_flag(FLAG_LIT_CANDLE)
    elif obj is None:
        message = 'What should I {}?'.format(verb)
    else:
        message = 'I\'m not sure what setting that on fire that would achieve...'
    return message

# The handler function for the verb 'unlight'
def verb_unlight(verb, current_location, obj=None):
    if is_active(FLAG_LIT_CANDLE):
        message = 'Extinguished.'
    elif obj is None:
        message = 'What should I {}?'.format(verb)
    else:
        message = 'I can\'t extinguish that...'
    return message

# The handler function for the verb 'spray'
def verb_spray(verb, current_location, obj=None):
    if obj in (OBJ_BATS, OBJ_AEROSOL) and is_holding(OBJ_AEROSOL):
        if is_active(OBJ_BATS):
            message = 'Pffft! Got those pesky bats!'
            deactivate_flag(OBJ_BATS)
        else:
            message = 'Hisssss...'
    elif obj is None:
        message = 'What should I {}?'.format(verb)
    else:
        message = 'I can\'t {} that...'.format(verb)
    return message

# The handler function for the verb 'use'
def verb_use(verb, current_location, obj=None):
    if obj == OBJ_VACUUM and is_holding(OBJ_VACUUM) and is_holding(OBJ_BATTERIES):
        message = 'Switched on.'
        activate_flag(OBJ_VACUUM)
        if is_active(OBJ_GHOSTS):
            message = 'Whizz - sucked the ghosts up!'
            deactivate_flag(OBJ_GHOSTS)
    elif obj is None:
        message = 'What should I {}?'.format(verb)
    else:
        message = 'I\'m not sure how to {} that...'.format(verb)
    return message

# The handler function for the verb 'unlock'
def verb_unlock(verb, current_location, obj=None):
    if is_in_room((5, 3), current_location) and obj in (OBJ_DRAWER, OBJ_DESK):
        # Room 43 - Study with Desk & Hole in Wall - delegate to VERB_OPEN handler
        message = verb_open(verb, obj)
    elif is_in_room((3, 4), current_location) and not is_active(OBJ_DOOR) and is_holding(OBJ_KEY):
        # Room 28 - Hall By Thick Wooden Door
        activate_flag(OBJ_DOOR)
        room = get_room(current_location)
        update_room_exits('sew') # south exit becomes available
        update_room_description(room, 'Huge Open Door')
        message = 'The key turns...!'
    elif obj is None:
        message = 'What should I {}?'.format(verb)
    else:
        message = 'I\'m not sure how I could {} that...'.format(verb)
    return message

# The handler function for the verb 'leave'
def verb_leave(verb, current_location, obj=None):
    if obj is None:
        message = 'What should I {}?'.format(verb)
    elif not is_holding(obj):
        message = 'You\'re not carrying that.'
    else:
        room = get_room(current_location)
        drop_item(obj, room)
        message = 'Done.'
    return message

# The handler function for the verb 'score'
def verb_score(verb, current_location, obj=None):
    score = len(inventory)
    if score == 17 and not is_holding(OBJ_BOAT):
        if is_in_room((7, 1), current_location):
            # in room 57 - Path Through Iron Gate
            message = 'Double score for reaching here!'
            score *= 2
        else:
            message = 'You have everything - return to the gate for your final score.'
    return message

# The following is a dictionary object which allows us to 'look up' the
# appropriate handler function for the verbs that the play might use.
VERB_HANDLERS = {
    VERB_HELP: verb_help,
    VERB_CARRYING: verb_carrying,
    VERB_GO: verb_go,
    'n': verb_go,
    's': verb_go,
    'w': verb_go,
    'e': verb_go,
    'u': verb_go,
    'd': verb_go,
    VERB_GET: verb_get,
    VERB_TAKE: verb_get,
    VERB_OPEN: verb_open,
    VERB_EXAMINE: verb_examine,
    VERB_READ: verb_read,
    VERB_SAY:verb_say,
    VERB_DIG: verb_dig,
    VERB_SWING: verb_swing,
    VERB_CLIMB: verb_climb,
    VERB_LIGHT: verb_light,
    VERB_UNLIGHT: verb_unlight,
    VERB_SPRAY: verb_spray,
    VERB_USE: verb_use,
    VERB_UNLOCK:verb_unlock,
    VERB_LEAVE: verb_leave,
    VERB_SCORE: verb_score,
}

OBJECTS = [
    # These 18 objects are 'gettable'
    OBJ_PAINTING, OBJ_RING, OBJ_MAGICSPELLS, OBJ_GOBLET, OBJ_SCROLL, OBJ_COINS, OBJ_STATUE, OBJ_CANDLESTICK,
    OBJ_MATCHES, OBJ_VACUUM, OBJ_BATTERIES, OBJ_SHOVEL, OBJ_AXE, OBJ_ROPE, OBJ_BOAT, OBJ_AEROSOL, OBJ_CANDLE, OBJ_KEY,
    # These 19 objects are not 'gettable' - note that they are not all actually 'objects'
    # but this is how the parsing is set up to work
    NORTH, SOUTH, EAST, WEST, UP, DOWN,
    OBJ_DOOR, OBJ_BATS, OBJ_GHOSTS, OBJ_DRAWER, OBJ_DESK, OBJ_COAT, OBJ_RUBBISH,
    OBJ_COFFIN, OBJ_BOOKS, OBJ_XZANFAR, OBJ_WALLS, OBJ_SPELLS,
]

# initialize the game flags
game_flags = dict(zip(OBJECTS, [False,] * len(OBJECTS)))
for x in [OBJ_RING, OBJ_CANDLE, UP, OBJ_BATS, OBJ_DRAWER]:
    activate_flag(x)

# initialize the game nouns
adventure_nouns = set()
for row in GAME_MAP:
    for room in row:
        room_contents = get_room_contents(room)
        adventure_nouns.update(room_contents)
adventure_nouns.update(
    [
        NORTH, SOUTH, EAST, WEST, UP, DOWN,
        OBJ_KEY,
        OBJ_DOOR, OBJ_BATS, OBJ_GHOSTS, OBJ_DRAWER, OBJ_DESK, OBJ_COAT, OBJ_RUBBISH,
        OBJ_COFFIN, OBJ_BOOKS, OBJ_XZANFAR, OBJ_WALLS, OBJ_SPELLS
    ]
)

# initialise the inventory (empty to start with)
inventory = set()

# initialise the candlelight counter (so we can make the candle "run out"
# when it is lit)
candlelight_counter = 0

# the starting location for the player is Room #57 - Path Through Iron Gate
current_location = [7, 1]

# Now we can start the actual game.
clear_screen()
print('Haunted House')
print('-------------')
while True:
    message = 'OK'
    print('Your location:')
    room = get_room(current_location)
    print(get_room_description(room))
    print('Exits:')
    print(or_join([x for x in get_room_exits(room)]))
    room_objects = get_room_contents(room)
    if room_objects:
        print('You can see ' + and_join(room_objects) + ' here')
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
            message = verb_handler(verb, current_location, obj=obj)
        else:
            message = 'There is no ' + obj

    print(message)

    if is_active(OBJ_BATS) and is_in_room((1, 5), current_location) and not verb == VERB_SPRAY and random.randint(1, 3) is not 3:
        # bats are active in Room 13 - Rear Turret Room
        activate_flag(OBJ_BATS)
        message = 'BATS ATTACKING!!'
        print(message)
    elif is_in_room((5, 4), current_location) and not is_active(DOWN) and random.randint(1, 2) is 1:
        activate_flag(OBJ_GHOSTS)

    if is_active(FLAG_LIT_CANDLE):
        candlelight_counter -= 1
        if candlelight_counter < 10:
            message = 'Your {} is waning...'.format(OBJ_CANDLE)
            if candlelight_counter < 1:
                deactivate_flag(FLAG_LIT_CANDLE)
                message = 'Your {} is out!'.format(OBJ_CANDLE)
        print(message)

    print()
