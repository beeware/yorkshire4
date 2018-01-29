import sys

from yorkshire4.core import OldSchoolScreen
from yorkshire4.profiles import COMMODORE_64, MICROBEE, ZX_SPECTRUM

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


# Use the ?25l ANSI escape code to hide the cursor, and ?12h to turn off
# local echo. This means we won't be able to see what keys we type.
def hide_cursor():
    print('\033[?25l\033[?12h')
    sys.stdout.flush()


# Use the ?25h ANSI escape code to restore the cursor,
# and ?12l to turn on local echo
def show_cursor():
    print('\033[?25h\033[?12l')
    sys.stdout.flush()



class Terminal:
    # the ASCII code/character ordinal for the space character
    SPACE_CHAR = 32

    """
    A very simple example of how one might go about making a Commodore 64
    'terminal' with the OldSchoolScreen class, complete with a blinking cursor.
    """
    def __init__(self, profile, tkinter_root=None):
        """
        Constructor
        :param tkinter_root: the Tkinter root instance, as obtained with `tkinter.Tk()`
        """
        import tkinter

        # Kick everything off - start by initialising Tkinter...
        if tkinter_root:
            self.tkinter_root = tkinter_root
        else:
            self.tkinter_root = tkinter.Tk()

        self.cursor_blink_state = True
        self.screen = OldSchoolScreen(tkinter_root, **profile, scale=3)

        self.boot()

        # set up an event handler to "react" when keys are pressed by calling
        # the `keypress_handler` callback function
        self.screen.bind_event_handler('<Key>', self.keypress_handler)

        # start blinking the cursor
        self.update_cursor()

    def run(self):
        # enter the Tkinter main loop
        self.tkinter_root.mainloop()

    def boot(self):
        pass

    def update_cursor(self):
        """
        This method is periodically called to update the appearance of the cursor, making
        it "blink"
        """
        # blink the cursor
        self.blink_cursor()
        # schedule Tkinter to automatically call this method again after
        # half a second (500 milliseconds), making the cursor run through
        # an on/off blink cycle once every second
        self.tkinter_root.after(self.CURSOR_BLINK_DELAY, self.update_cursor)

    def blink_cursor(self):
        """
        Updates the cursor, making it turn off if it is currently on, or on
        if it is currently off,causing it to "blink"
        """
        # every time we draw the cursor we swap the background/foreground
        # colors at the cursor position to "blink" the cursor
        x, y = self.screen.get_cursor_pos()
        fg, bg = self.screen.get_char_colors(x, y)
        self.screen.set_char_colors(x, y, bg, fg).render_char(x, y)

        # update the current cursor state (on or off)
        self.cursor_blink_state = not self.cursor_blink_state

    def keypress_handler(self, event=None):
        """
        Handle key presses caught by Tkinter via the event handling loop
        :param event: the keypress event which holds information about what key
        was pressed
        """
        char = event.char
        # some key presses don't contain a printable character (like the
        # cursor keys and so on), so we need to check whether we actually
        # have anything to work with
        if char:
            # we have a character - extract the character code
            # from the key press
            char_code = ord(char)

            # determine the current cursor position
            cursor_x, cursor_y = self.screen.get_cursor_pos()
            # check the cursor state - we need to make sure we reset
            # the cursor position to the "natural" colors otherwise the
            # cursor will leave a trail behind it
            if not self.cursor_blink_state:
                # cursor is on - need to reset the colors to normal
                fg, bg = self.screen.get_char_colors(cursor_x, cursor_y)
                self.screen.set_char_colors(cursor_x, cursor_y, bg, fg)
                self.screen.render_char(cursor_x, cursor_y)

            # special handling for [RETURN] key
            if char_code == 13:
                # newline
                scrolled = self.screen.do_newline()
                if scrolled:
                    self.screen.render()
            # special handling for [BACKSPACE] key
            elif char_code == 8:
                # move the cursor left
                self.screen.move_cursor_left()
                # get the updated cursor position and 'blank' the location
                # by putting a space in the screen memory and re-rendering
                # that character location.
                cursor_x, cursor_y = self.screen.get_cursor_pos()
                self.screen.put_character(self.SPACE_CHAR, cursor_x, cursor_y)
                self.screen.render_char(cursor_x, cursor_y)
            # all other keys are handled here
            else:
                # simply print the character at the new location without a
                # newline at the end
                self.screen.print(char, newline=False)

            # the cursor blink state returns to 'on' after every key press
            self.cursor_blink_state = True
            # update the cursor now
            self.blink_cursor()


class C64Terminal(Terminal):
    # the ASCII code/character ordinal for the space character
    CURSOR_CHAR = 32

    # the delay between cursor 'blink' updates in milliseconds
    CURSOR_BLINK_DELAY = 500

    def __init__(self):
        super().__init__(COMMODORE_64)

    def boot(self):
        self.screen.print()
        self.screen.print('    **** COMMODORE 64 BASIC V2 ****')
        self.screen.print()
        self.screen.print(' 64K RAM SYSTEM  38911 BASIC BYTES FREE')
        self.screen.print()
        self.screen.print('READY.')


def c64():
    C64Terminal().run()


class Microbee(Terminal):
    # the ASCII code/character ordinal for the _ character
    CURSOR_CHAR = 95

    # the delay between cursor 'blink' updates in milliseconds
    CURSOR_BLINK_DELAY = 500

    def __init__(self):
        super().__init__(MICROBEE)

    def boot(self):
        self.screen.print('Applied Technology MicroBee Colour Basic. Ver 6.00')
        self.screen.print()
        self.screen.print('>', newline=False)


def microbee():
    Microbee().run()


class ZXSpectrum(Terminal):
    # the ASCII code/character ordinal for the space character
    CURSOR_CHAR = 32

    # the delay between cursor 'blink' updates in milliseconds
    CURSOR_BLINK_DELAY = 500

    def __init__(self):
        super().__init__(ZX_SPECTRUM)


def zxspectrum():
    # set up the 'typewriter'
    ZXSpectrum().run()
