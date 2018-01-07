VERBS = [
    'help', 'carrying?', 'go', 'n', 's', 'w', 'e', 'u', 'd',
    'get', 'take', 'open', 'examine', 'read', 'say',
    'dig', 'swing', 'climb', 'light', 'unlight', 'spray', 'use', 'unlock', 'leave', 'score'
]
# the descriptions of each of the rooms (8x8 grid)
LOCATIONS = [
    # 0             1                   2                     3
    'Dark Corner', 'Overgrown Garden', 'By Large Woodpile', 'Yard by Rubbish',
    # 4           5         6               7
    'Weedpatch', 'Forest', 'Thick Forest', 'Blasted Tree',

    # 8                 9                      10                        11
    'Corner of House', 'Entrance to Kitchen', 'Kutchen & Grimy Cooker', 'Scullery Door',
    # 12                         13                  14                   15
    'Room with Inches of Dust', 'Rear Turret Room', 'Clearing by House', 'Path',

    # 16              17                  18            19
    'Side of House', 'Back of Hallway', 'Dark Alcove', 'Small Dark Room',
    # 20                           21              22                23
    'Bottom of Spiral Staircase', 'Wide Passage', 'Slippery Steps', 'Clifftop',

    # 24                    25                26               27
    'Near Crumblind Wall', 'Gloomy Passage', 'Pool of Light', 'Impresseive Vaulted Hallway',
    # 28                          29             30                           31
    'Hall By Thick Wooden Door', 'Trophy Room', 'Cellar with Barred Window', 'Cliff Path',

    # 32                           33            34              35
    'Cupboard with Hanging Coat', 'Front Hall', 'Sitting Room', 'Secret Room',
    # 36                           37            38              39
    'Steep Marble Stairs', 'Dining Room', 'Deep Cellar with Coffin', 'Cliff Path',

    # 40       41             42                        43
    'Closet', 'Front Lobby', 'Library of Evil Books', 'Study with Desk & Hole in Wall',
    # 44                    45                   46             47
    'Weird Cobwebby Room', 'Very Cold Chamber', 'Spooky Room', 'Cliff Path by Marsh',

    # 48                       49             50             51
    'Rubble Strewn Verandah', 'Front Porch', 'Front Tower', 'Sloping Corridor',
    # 52              53               54       55
    'Upper Gallery', 'Marsh by Wall', 'Marsh', 'Soggy Path',

    # 56                   57                        58             59
    'By Twisted Railing', 'Path Through Iron Gate', 'By Railings', 'Beneath Front Tower',
    # 60                             61                        62                    63
    'Debris from Crumbling Facade', 'Large Fallen Brickwork', 'Rotting Stone Arch', 'Crumbling Clifftop'
]

# the exits of each of the rooms (8x8 grid)
EXITS = [
    'se', 'we', 'we', 'swe', 'we', 'we', 'swe', 'ws',
    'ns', 'se,' 'we', 'nw', 'se', 'w', 'ne', 'nsw',
    'ns', 'ns', 'se', 'we', 'nwud', 'se', 'wsud', 'ns',
    'n', 'ns', 'nse', 'we', 'we', 'nsw', 'ns', 'ns',
    's', 'nse', 'nsw', 's', 'nsud', 'n', 'n', 'ns',
    'ne', 'nw', 'ne', 'w', 'nse', 'we', 'w', 'ns',
    'se', 'nsw', 'e', 'we', 'nw', 's', 'sw', 'nw',
    'ne', 'nwe', 'we', 'we', 'we', 'nwe', 'nwe', 'w',
]
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
# the indices of the rooms in which the gettable objects are located - corresponds to the
# items in OBJECTS above
# For example, the 'Painting' is located in room at index 46, which is the 'Spooky Room'
GETTABLE_OBJECTS = [
    # Object: Painting, Ring, Magic Spells, Goblet, Scroll, Coins, Statue, Candlestick
    # Room#:  46        38    35            50      13      18     28      42
    46, 38, 35, 50, 13, 18, 28, 42,
    # Object: Matches, Vacuum, Batteries, Shovel, Axe, Rope, Boat, Aerosol, Candle, Key
    # Room#:  10       25      26         4       2    7     47    60       43      32
    10, 25, 26, 4, 2, 7, 47, 60, 43, 32
]
# don't forget this is all 1 indexed in the BASIC version with respect to the objects,
# because index 0 is used as a "special" flag, so the object 'painting' corresponds to
# flag index 1, the object 'ring' corresponds to flag index 2 and so on.
FLAGS = [False, ] * len(OBJECTS)
FLAGS[2] = True  # ring
FLAGS[17] = True  # candle
FLAGS[18] = True  # key
FLAGS[23] = True  # up
FLAGS[26] = True  # bats
FLAGS[28] = True  # drawer

ROOM = 57
MESSAGE = 'OK'


# utility to convert old room indexes to the "modern map" for checking
def old_coord_convert(old_index):
    row = int(old_index / 8)
    col = old_index - (row * 8)
    return 'Room', old_index, 'is at coordinates', row, col
