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
            if char in '\r\n':
                scrolled = self.screen.do_newline()
                if scrolled:
                    self.screen.render()
            else:
                self.screen.print(char, newline=False)

root = tkinter.Tk()
app = C64TypeWriter(root)
root.mainloop()