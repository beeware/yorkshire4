import tkinter

from oldschoolscreen.core import OldSchoolScreen
from oldschoolscreen.screen_profiles.commodore64 import COMMODORE_64


class C64TypeWriter:
    def __init__(self, master):
        self.screen = OldSchoolScreen(master, **COMMODORE_64, scale=3)
        self.screen.bind_event_handler('<Key>', self.callback)

    def callback(self, event=None):
        char = event.char
        if char:
            char_code = ord(char)
            if char_code == 13:
                # newline
                scrolled = self.screen.do_newline()
                if scrolled:
                    self.screen.render()
            elif char_code == 8:
                # backspace
                self.screen.move_cursor_left()
                x, y = self.screen.get_cursor_pos()
                self.screen.put_character(32, x, y).render_char(x, y)
            else:
                print(char, char_code)
                self.screen.print(char, newline=False)

root = tkinter.Tk()
app = C64TypeWriter(root)
root.mainloop()