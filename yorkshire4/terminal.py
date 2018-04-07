import sys

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
