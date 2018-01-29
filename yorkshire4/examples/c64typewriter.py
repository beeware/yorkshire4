import tkinter

from yorkshire4.core import OldSchoolScreen
from yorkshire4.profiles import COMMODORE_64

# the ASCII code/character ordinal for the space character
SPACE_CHAR = 32
# the delay between cursor 'blink' updates in milliseconds
CURSOR_BLINK_DELAY = 500


class C64TypeWriter:
    """
    A very simple example of how one might go about making a Commodore 64 'typewriter' with the
    OldSchoolScreen class, complete with a blinking cursor.
    """
    def __init__(self, tkinter_root):
        """
        Constructor
        :param tkinter_root: the Tkinter root instance, as obtained with `tkinter.Tk()`
        """
        self.tkinter_root = tkinter_root
        self.cursor_blink_state = True
        self.screen = OldSchoolScreen(tkinter_root, **COMMODORE_64, scale=3)

        # set up ye olde Commodore 64 boot screen for extra nostalgia...
        self.screen.print()
        self.screen.print('    **** COMMODORE 64 BASIC V2 ****')
        self.screen.print()
        self.screen.print(' 64K RAM SYSTEM  38911 BASIC BYTES FREE')
        self.screen.print()
        self.screen.print('READY.')

        # set up an event handler to "react" when keys are pressed by calling
        # the `keypress_handler` callback function
        self.screen.bind_event_handler('<Key>', self.keypress_handler)

        # start blinking the cursor
        self.update_cursor()

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
        self.tkinter_root.after(CURSOR_BLINK_DELAY, self.update_cursor)

    def blink_cursor(self):
        """
        Updates the cursor, making it turn off if it is currently on, or on if it is currently off,
        causing it to "blink"
        """
        # every time we draw the cursor we swap the background/foreground colors at the cursor
        # position to "blink" the cursor
        x, y = self.screen.get_cursor_pos()
        fg, bg = self.screen.get_char_colors(x, y)
        self.screen.set_char_colors(x, y, bg, fg).render_char(x, y)
        # update the current cursor state (on or off)
        self.cursor_blink_state = not self.cursor_blink_state

    def keypress_handler(self, event=None):
        """
        Handle key presses caught by Tkinter via the event handling loop
        :param event: the keypress event which holds information about what key was pressed
        """
        char = event.char
        # some key presses don't contain a printable character (like the cursor keys and so on),
        # so we need to check whether we actually have anything to work with
        if char:
            # we have a character - extract the character code from the key press
            char_code = ord(char)

            # determine the current cursor position
            cursor_x, cursor_y = self.screen.get_cursor_pos()
            # check the cursor state - we need to make sure we reset the cursor position to the
            # "natural" colors otherwise the cursor will leave a trail behind it
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
                # get the updated cursor position and 'blank' the location by putting a space
                # in the screen memory and re-rendering that character location.
                cursor_x, cursor_y = self.screen.get_cursor_pos()
                self.screen.put_character(SPACE_CHAR, cursor_x, cursor_y)
                self.screen.render_char(cursor_x, cursor_y)
            # all other keys are handled here
            else:
                # simply print the character at the new location without a newline at the end
                self.screen.print(char, newline=False)

            # the cursor blink state returns to 'on' after every key press
            self.cursor_blink_state = True
            # update the cursor now
            self.blink_cursor()


# Kick everything off - start by initialising Tkinter...
tkinter_root = tkinter.Tk()

# set up the 'typewriter'
C64TypeWriter(tkinter_root)

# enter the Tkinter main loop
tkinter_root.mainloop()
