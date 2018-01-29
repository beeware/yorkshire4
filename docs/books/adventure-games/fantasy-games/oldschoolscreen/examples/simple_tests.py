from tkinter import *

from oldschoolscreen.core import OldSchoolScreen
from oldschoolscreen.screen_profiles.commodore64 import COMMODORE_64

"""
This is intended as a simple example to show how to use the basic functions of the 
`OldSchoolScreen`. It is left as an exercise to the reader to explore the remaining methods,
functionality, and to extend and/or improve it!
"""

# These are the byte values for 13 custom characters 1 byte (or 8 bits) wide by 8 bytes tall (so
# basically an 8x8 grid of pixels which are either 'on' or 'off'), which we use later in the
# example.
custom_characters = [
    [255, 255, 255, 255, 255, 255, 255, 255],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [85, 170, 85, 170, 85, 170, 85, 170],
    [0, 60, 24, 60,126, 126, 126, 60],
    [0, 56, 100, 114, 95, 73, 41, 31],
    [20, 42, 20, 20, 93, 93, 62, 99],
    [60, 126, 255, 255, 255, 253, 255, 255],
    [60, 102, 195, 129, 129, 129, 133, 129],
    [129, 66, 36, 0, 0, 36, 66, 129],
    [0, 60, 66, 66, 66, 66, 60, 0],
    [76, 158, 170, 190, 84, 30, 37, 88],
    [0, 56, 84, 124, 56, 44, 68, 102],
    [0, 8, 28, 42, 127, 85, 65, 34],
]

# Initialise the screen using a "profile"; COMMODORE_64, in this case . Try some of the other
# example screen profiles provided, or make one of your own! The TRS-80 anyone...?
#     http://www.kreativekorp.com/software/fonts/trs80.shtml
crt_screen = OldSchoolScreen(Tk(), **COMMODORE_64, scale=3)

# clear the screen
crt_screen.clear_screen()

# Here we test some of the basic functionality.
# Print some stuff to the screen so that we know it's working - this can be useful as some of the
# older machines only had an upper case character set, and/or a limited set of non-alphanumerics
# (i.e., punctuation etc) available. Note that the `print()` function will automatically cause the
# screen to re-render the appropriate areas to update the screen.
crt_screen.print('abcdefghijklmnopqrstuvwxyz')
crt_screen.print('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
crt_screen.print('0123456789')
crt_screen.print('!"#$%&\'()*+,-./')
crt_screen.print(':;<>?')
crt_screen.print('@^[]')
crt_screen.print('The rain in spain stays mainly on the plain!')
# You could also test all available characters with something like...
'''
step = 32
for x in range(0, len(c64_screen.font), step):
    c64_screen.print_charcodes(range(x, x+step))
'''

# Try changing the screen and border colors to red and yellow respectively (note that these are
# color values 2 and 7 respectively on the Commodore 64, which use to be set by directly altering
# specific memory addresses with POKE statements, like so...
#   POKE 53281, 2
#   POKE 53280, 7
# Again, like the `print()` function, `set_screen_color` and `set_border_color` will automatically
# cause the screen to update itself. Side note: how ugly were those colors? We thought they were
# amazing, though...
crt_screen.set_screen_color(2)
crt_screen.set_border_color(7)

# Try setting the screen color memory at a specific location - note that this requires a 'manual'
# update of the screen afterwards. This is because you probably want to do more than just update a
# single color memory item, and so it would be a waste of resources to re-render the screen after
# every single update (though on the actual Commodore 64 this would be an instantaneous change
# because of the way the hardware worked). On the original machine, this would have been done by
# directly setting a memory address with a POKE statement
crt_screen.set_char_colors(0, 0, fg_color=1, bg_color=0)
crt_screen.render()

# we can also re-render a single character 'square' if we want to really optimise stuff...
crt_screen.render_char(0, 0)

# ...or render a particular area we know has been changed...
crt_screen.set_char_colors(0, 0, 2)
crt_screen.set_char_colors(1, 0, 3)
crt_screen.set_char_colors(0, 1, 5)
crt_screen.set_char_colors(1, 1, 7)
crt_screen.render_area(0, 0, 2, 2)

# ...or force a *complete* re-render of the entire screen (skipping all optimisation) for areas
# that haven't changed since the last render.
crt_screen.render(force_all=True)

# Finally, let's test defining some custom characters by modifying the "character memory" with new
# bytes - we'll redefine starting at character 65 with the bytes defined in `custom_characters`:
crt_screen.define_custom_characters(65, custom_characters)
# print the characters to the screen, but don't update (i.e., render) the screen just yet
crt_screen.print('abcdefghijklm', render=False)
# force a re-render of the whole screen so that the other characters already on the screen that fall
# into the range of the custom characters also update (which is what would have happened on the
# original machine - once you change that character memory, *everything* changes, even what you
# already had on the screen before the change was made:
crt_screen.render(force_all=True)

mainloop()
