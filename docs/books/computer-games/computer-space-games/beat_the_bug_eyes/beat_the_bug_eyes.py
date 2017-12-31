# Import:
# * the `random` module so we can generate random numbers,
# * `select`, `sys`, `termios` and `tty` to manipulate the terminal
# * `time` so we can sleep
import random
import select
import sys
import termios
import time
import tty


# Normal terminals are defined a lot like typewriters. They are "line based" -
# they wait for the user to type a full line, then type Enter, and the entire
# line of input is processed. To be able to read a single character (without
# typing Enter), you need to put the terminal (or tty - short for TeleTYpe)
# into "raw" mode.
#
# However, putting a terminal into "raw" mode leaves the terminal in an unusual
# state, so it's good to clean up after yourself. We use the termios module
# to record the initial state of the terminal (using `tcgetattr`), and restore
# the state of the terminal (using `tcsetattr`) after you're done.

try:
    # sys.stdin is the "standard input" pipe - that is, the keyboard.
    fd = sys.stdin.fileno()

    # Record the initial settings of the input pipe
    old_settings = termios.tcgetattr(fd)

    # Set the input pipe to be in raw mode
    tty.setraw(fd)

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

    # Another utility method - this time, to get a single character from
    # the keyboard.
    #
    # But though we're in "raw" mode, we can't answer the question "has the
    # user typed
    # key or not?" To do *that*, you need to use an operating system call called
    # `select`. Select is a method used to inspect the status of "pipes" of content
    # to determine if any content is ready. The keyboard in an "input pipe"; the
    # screen is an "output pipe". Select waits until a specific pipe has content
    # available; you also provide a timeout which is the maximum length of time
    # that the select call will wait until content is available. This timeout can
    # be "0 seconds", or it can be as long as you're willing to wait.

    def getch(timeout=None):
        # If we aren't using a timeout, we can just read from the input pipe.
        # If we *do* have a timeout, use the select call to wait until input
        # is availble, or the timeout expires.
        if timeout is None or select.select([sys.stdin], [], [], timeout)[0]:
            ch = sys.stdin.read(1)
        else:
            ch = None

        # Return the character that was read - or None, if no character was pressed.
        return ch

    # Now we can start the actual game.

    # Use the ?25l ANSI escape code to hide the cursor, and ?12h to turn off
    # local echo. This means we won't be able to see what keys we type.
    print('\033[?25l\033[?12h')

    score = 0

    # Do 10 iterations of showing bug eyes
    for t in range(10):
        clear_screen()

        # random.random() returns a floating point number in the range 0 -> 1
        # Add 0.5 to get a number between 0.5 and 1.5. That's how long we'll sleep
        # before displaying some eyes.
        time.sleep(random.random() + 0.5)

        # Pick a random zone in which to display the eyes.
        zone = random.randrange(4) + 1

        # The zone gives us the x,y offset
        if zone == 1:
            x_offset = 0
            y_offset = 0
        elif zone == 2:
            x_offset = 38
            y_offset = 0
        elif zone == 3:
            x_offset = 0
            y_offset = 12
        elif zone == 4:
            x_offset = 38
            y_offset = 12

        # Combine the offsets and a random number to postion the cursor
        # and print eyes. We can just print newlines to set the y (vertical)
        # position, then print spaces to set the x (horizontal) position.
        for y in range(random.randrange(12) + y_offset):
            print()

        print(' ' * (random.randrange(38) + x_offset) + '* *')

        # Wait up to a second for the player to respond.
        try:
            selected = int(getch(timeout=1))
        except TypeError:
            # If the user doesn't press a character, or they press something
            # other than a number, the call to int() will raise a ValueError.
            # Regardless, we know they didn't pick a zone; set the zone to None
            selected = None

        if selected == zone:
            score = score + 1

    # Clear the screen
    clear_screen()

finally:
    # No matter what happens, clean up after yourself.

    # Use the ?25h ANSI escape code to restore the cursor, and ?12l to turn on local echo
    print('\033[?25h\033[?12l')

    # No matter what happens, drain the input pipe, and restore to
    # it's original state.
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# Last of all, print the user's score.
# We do this *after* restoring the terminal settings so that the output
# behaves the way we'd expect a normal terminal to behave.
print('You blasted %s bugs' % score)
