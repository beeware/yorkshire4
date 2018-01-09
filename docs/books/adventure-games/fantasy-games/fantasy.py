from tkinter import *

from oldschoolscreen import OldSchoolScreen
from screen_profiles import COMMODORE_64

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

c64_screen = OldSchoolScreen(**COMMODORE_64, scale=3)
c64_screen.clear_screen()
c64_screen.print('abcdefghijklmnopqrstuvwxyz')
c64_screen.print('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
c64_screen.print('0123456789')
c64_screen.print('!"#$%&\'()*+,-./')
c64_screen.print(':;<>?')
c64_screen.print('@^[]')
c64_screen.print('The rain in spain stays mainly on the plain!')
c64_screen.render()
# c64_screen.set_screen_color(2)
# for x in range(0, 255, 16):
#    c64_screen.print_charcodes(range(x, x+16))
# c64_screen.set_screen_color(0)
# c64_screen.set_char_colors(0, 0, 1)
# c64_screen.render_char(0, 0)
# c64_screen.set_char_colors(0, 0, 2)
# c64_screen.set_char_colors(1, 0, 3)
# c64_screen.set_char_colors(0, 1, 5)
# c64_screen.set_char_colors(1, 1, 7)
# c64_screen.render_area(0, 0, 2, 2)
c64_screen.define_custom_characters(65, custom_characters)
c64_screen.print('ABC', render=False)
c64_screen.put_character(64, 0, 0, bg_color=2)
c64_screen.render(force_all=True)

mainloop()