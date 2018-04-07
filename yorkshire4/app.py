import asyncio

import toga

from .widgets import BitmapView


class OldSchoolTerminal(toga.App):
    def __init__(self, profile):
        self.profile = profile
        super().__init__(self.profile.__name__, 'org.beeware.yorkshire4')

    def clear(self):
        self.cursor_on = True
        with self.screen as screen:
            for x in range(0, self.profile.full_screen_size[0]):
                for y in range(0, self.profile.full_screen_size[1]):
                    if y < self.border_size[1]:
                        color = self.border_color
                    elif y < self.border_size[1] + self.profile.screen_size[1]:
                        if x < self.border_size[0]:
                            color = self.border_color
                        elif x < self.border_size[0] + self.profile.screen_size[0]:
                            color = self.background_color
                        else:
                            color = self.border_color
                    else:
                        color = self.border_color
                    screen.set(x, y, color)

        self.cursor_position = (0, 0)

    def draw_char(self, pos, char):
        """Draw a single character at the given cursor position"""
        with self.screen as screen:
            for bx in range(0, self.profile.character_size[0]):
                bitmap = self.profile.font[ord(char)]
                for by in range(0, self.profile.character_size[1]):
                    if bitmap[by] & (1 << (self.profile.character_size[0] - bx - 1)):
                        color = self.foreground_color
                    else:
                        color = self.background_color

                    screen.set(
                        self.border_size[0] + self.profile.character_size[0] * pos[0] + bx,
                        self.border_size[1] + self.profile.character_size[1] * pos[1] + by,
                        color
                    )

    def print(self, text):
        for char in text:
            if char == '\n':
                self.cursor_position = (0, self.cursor_position[1] + 1)
            else:
                self.draw_char(self.cursor_position, char)
                self.cursor_position = (
                    self.cursor_position[0] + 1,
                    self.cursor_position[1]
                )

    def keypress(self, widget, key=None, modifiers=None):
        if key == toga.Key.ENTER:
            self.print('\n')
        elif key == toga.Key.BACKSPACE:
            self.cursor_position = (
                max(0, self.cursor_position[0] - 1),
                self.cursor_position[1]
            )
        elif key.is_printable():
            if toga.Key.CONTROL in modifiers:
                self.print('^{}'.format(key.value.upper()))
            elif toga.Key.SHIFT in modifiers:
                self.print(key.value.upper())
            else:
                self.print(key.value)

    async def blink_cursor(self):
        while True:
            with self.screen as screen:
                for bx in range(0, self.profile.character_size[0]):
                    bitmap = self.profile.font[self.profile.cursor_char]
                    for by in range(0, self.profile.character_size[1]):
                        if bitmap[by] & (1 << (self.profile.character_size[0] - bx - 1)):
                            if self.cursor_on:
                                color = self.foreground_color
                            else:
                                color = self.background_color
                        else:
                            if self.cursor_on:
                                color = self.background_color
                            else:
                                color = self.foreground_color

                        screen.set(
                            self.border_size[0] + self.profile.character_size[0] * self.cursor_position[0] + bx,
                            self.border_size[1] + self.profile.character_size[1] * self.cursor_position[1] + by,
                            color
                        )

            self.cursor_on = not self.cursor_on
            await asyncio.sleep(self.profile.cursor_blink_delay / 1000)

    def open_document(self, url):
        # This is needed to avoid errors with command line invocation
        pass

    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(
            title=self.name, size=(800, 600)
        )

        self.screen = BitmapView(
            size=self.profile.full_screen_size,
            on_key_press=self.keypress
        )

        self.main_window.content = self.screen

        # Pre-cache some useful properties
        self.border_color = self.profile.colors[self.profile.default_border_color]
        self.background_color = self.profile.colors[self.profile.default_screen_color]
        self.foreground_color = self.profile.colors[self.profile.default_text_color]

        self.border_size = [
            (self.profile.full_screen_size[0] - self.profile.screen_size[0]) // 2,
            (self.profile.full_screen_size[1] - self.profile.screen_size[1]) // 2
        ]

        self.clear()
        self.print(self.profile.boot_text)

        asyncio.ensure_future(self.blink_cursor())

        # Show the main window
        self.main_window.show()


def main():
    from yorkshire4.profiles import commodore64
    return OldSchoolTerminal(commodore64)


def c64():
    from yorkshire4.profiles import commodore64
    return OldSchoolTerminal(commodore64).main_loop()


def microbee():
    from yorkshire4.profiles import microbee
    return OldSchoolTerminal(microbee).main_loop()


def zxspectrum():
    from yorkshire4.profiles import zxspectrum
    return OldSchoolTerminal(zxspectrum).main_loop()
