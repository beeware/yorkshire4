import select
import sys
import termios
import tty

# Define some methods to do screen cursor moves.
# These use "ANSI Escape Sequences" - special combinations of
# characters that are understood by the terminal, but are difficult
# (or impossible) to type on a keyboard. `\033[` is the
# "escape sequence"; the characters after the escape sequnce are
# interpreted as commands.
#
# For more details about ANSI escape sequences, see:
#     https://en.wikipedia.org/wiki/ANSI_escape_code


# Use the 2J code to clear the screen, and H to move the cursor to the
# Home position (top left corner)
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


def getch(timeout=None):
    """Get a single character from the keyboard (without pressing enter)

    Normal terminals are defined a lot like typewriters. They are "line based" -
    they wait for the user to type a full line, then type Enter, and the entire
    line of input is processed. To be able to read a single character (without
    typing Enter), you need to put the terminal (or tty - short for TeleTYpe)
    into "raw" mode.

    However, putting a terminal into "raw" mode leaves the terminal in an unusual
    state, so it's good to clean up after yourself. We use the termios module
    to record the initial state of the terminal (using `tcgetattr`), and restore
    the state of the terminal (using `tcsetattr`) after you're done.

    The 'timeout' argument lets you configure how long you wait before
    """
    try:
        # sys.stdin is the "standard input" pipe - that is, the keyboard.
        fd = sys.stdin.fileno()

        # Record the initial settings of the input pipe
        old_settings = termios.tcgetattr(fd)

        tty.setraw(fd)

        # If we aren't using a timeout, we can just read from the input pipe.
        # If we *do* have a timeout, use the select call to wait until input
        # is availble, or the timeout expires.
        if timeout is None or select.select([sys.stdin], [], [], timeout)[0]:
            ch = sys.stdin.read(1)
        else:
            ch = None

        # Return the character that was read
        # - or None, if no character was pressed.
    finally:
        # No matter what happens, drain the input pipe, and restore to
        # it's original state.
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch
