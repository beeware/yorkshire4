import tkinter

from oldschoolscreen.oldschoolscreen import OldSchoolScreen
from oldschoolscreen.screen_profiles.zxspectrum import ZX_SPECTRUM


class ZXSpectrumTypeWriter:
    def __init__(self, master):
        self.screen = OldSchoolScreen(master, **ZX_SPECTRUM, scale=3)
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
app = ZXSpectrumTypeWriter(root)
root.mainloop()