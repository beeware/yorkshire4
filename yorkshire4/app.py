import asyncio

import toga

from .widgets import BitmapView


class Cursor:
    def __init__(self, app, position):
        self.app = app
        self.position = position
        self.on = True

    def toggle(self):
        self.on = not self.on

    async def blink(self):
        while self == self.app.cursor:
            with self.app.screen as screen:
                origin_x = (
                    self.app.border_size[0]
                    + self.app.profile.character_size[0] * self.position[0]
                )
                origin_y = (
                    self.app.border_size[1]
                    + self.app.profile.character_size[1] * self.position[1]
                )
                for x in range(0, self.app.profile.character_size[0]):
                    for y in range(0, self.app.profile.character_size[1]):
                        if self.on:
                            color = self.app.foreground_color
                        else:
                            color = self.app.background_color

                        screen.set(origin_x + x, origin_y + y, color)
            self.toggle()
            await asyncio.sleep(self.app.profile.cursor_blink_delay / 1000)


class OldSchoolTerminal(toga.App):
    def __init__(self, profile):
        self.profile = profile
        super().__init__(self.profile.__name__, 'org.beeware.yorkshire4')

    def clear(self):
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

        self.start_cursor()

    def draw_char(self, pos, char):
        """Draw a single character at the given cursor position"""
        with self.screen as screen:
            origin_x = (
                self.border_size[0] + self.profile.character_size[0] * pos[0]
            )
            origin_y = (
                self.border_size[1] + self.profile.character_size[1] * pos[1]
            )
            for x in range(0, self.profile.character_size[0]):
                bitmap = self.profile.font[ord(char)]
                for y in range(0, self.profile.character_size[1]):
                    if bitmap[y] & (1 << (self.profile.character_size[0] - x - 1)):
                        color = self.foreground_color
                    else:
                        color = self.background_color

                    screen.set(origin_x + x, origin_y + y, color)

    def print(self, text):
        position = self.cursor.position
        for char in text:
            if char == '\n':
                position = (0, position[1] + 1)
            else:
                self.draw_char(position, char)
                position = (position[0] + 1, position[1])

        # Restart the cursor blinking
        self.start_cursor(position)

    def keypress(self, widget, key=None, modifiers=None):
        if key == toga.Key.ENTER:
            self.draw_char(self.cursor.position, ' ')
            self.print('\n')
        elif key == toga.Key.BACKSPACE:
            self.draw_char(self.cursor.position, ' ')
            self.start_cursor((
                max(0, self.cursor.position[0] - 1),
                self.cursor.position[1]
            ))
        elif key.is_printable():
            if toga.Key.CONTROL in modifiers:
                self.print('^{}'.format(key.value.upper()))
            elif toga.Key.SHIFT in modifiers:
                self.print(key.value.upper())
            else:
                self.print(key.value)

    def start_cursor(self, position=(0, 0)):
        """Start a new cursor at the given position

        This turns off the cursor
        """
        self.cursor = Cursor(self, position)
        asyncio.ensure_future(self.cursor.blink())

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
