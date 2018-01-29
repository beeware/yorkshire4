import copy

from tkinter import *


class OldSchoolScreen:
    """
    Emulates a screen from the olden days
    """
    def __init__(self, tk, full_screen_size, screen_size, character_size,
                 colors, default_border_color, default_screen_color, default_text_color,
                 font,
                 text_to_character_mapper=None,
                 scale=2):
        """
        Initialise the screen
        :param tk the TKinter instance, as constructed with tkinter.Tk()
        :param full_screen_size: the resolution of the 'full' screen, to the edges of the CRT,
               including any border, as (WIDTH, HEIGHT) in pixels
        :param screen_size:  the resolution of the 'addressable' screen (i.e., the area of the
               screen which the user can actually display things on), as (WIDTH, HEIGHT) in pixels
        :param character_size: the size of characters on the display, as (WIDTH, HEIGHT) in pixels
        :param colors: the colors for the display as a list of hex RGB values in the form '#RRGGBB'
        :param default_border_color: the color to use for the border area when the screen starts
        :param default_screen_color: the color to use for the screen area when the screen starts
        :param default_text_color:  the color to use for the text when the screen starts
        :param font: the bytes which define the bitmap font for the display
        :param text_to_character_mapper: some old school machines had some oddities in how they
               mapped text to character codes (i.e., they did not use a straight ASCII conversion).
               If necessary, a function which takes a string as arguments should be provided here.
               The function must return a list of character codes which correspond to the
               characters in the text on the old school screen being emulated. As a rather silly
               example:

                   def my_mapper(text):
                        char_codes = [(255 - ord(char)) for char in text]
                        return char_codes

        :param scale: the scaling factor (as an integer) - modern displays are usually too high a
               resolution to make the original 'native' display size useful, so this allows it to
               be scaled up
        """
        self.tk = tk
        self.screen_width, self.screen_height = full_screen_size[0], full_screen_size[1]
        self.main_width, self.main_height = screen_size[0], screen_size[1]
        self.char_width, self.char_height = character_size[0], character_size[1]
        self.colors = colors
        self.text_to_character_mapper = text_to_character_mapper
        self.font = font
        self.scale = scale

        # calculate the coordinates of the top left (0, 0) pixel of the addressable screen
        self.main_x0 = int(((self.screen_width - self.main_width) / 2.0) * self.scale)
        self.main_y0 = int(((self.screen_height - self.main_height) / 2.0) * self.scale)

        # work out how many characters the screen can show horizontally and vertically
        self.char_cols = int(self.main_width / self.char_width)
        self.char_rows = int(self.main_height / self.char_height)

        # initialise the screen character memory - fill with spaces (ASCII 32)
        # to be *really* old school we should probably use bytes here rather than integers, but...
        self.screen_char_memory = [32, ] * (self.char_cols * self.char_rows)
        self.last_rendered_screen_char_memory = None
        # initialise the screen color memory
        # again, to be *really* old school we should probably use bytes here rather than
        # integers, and even combine the two colors into a single byte using the first 4 bits for
        # foreground and the last 4 bits for the background, but...
        fg_color = default_text_color
        bg_color = default_screen_color
        self.screen_color_memory = []
        for x in range(self.char_cols * self.char_rows):
            self.screen_color_memory.append([fg_color, bg_color])
        self.last_rendered_screen_color_memory = None
        # initialise the cursor position (at the top left of the screen)
        self.cursor_position = [0, 0]

        # initialise the TK canvas
        self.screen = Canvas(tk,
                             width=self.screen_width * self.scale,
                             height=self.screen_height * self.scale)
        self.screen.pack()

        # set the border and screen colours
        self.set_border_color(default_border_color)
        self.set_screen_color(default_screen_color)
        # clear the screen
        self.clear_screen()

    def bind_event_handler(self, sequence=None, func=None, add=None):
        """
        Bind an event handler to the screen (to handle key presses, for example). This is actually
        just a wrapper around the Tkinter `bind_all(...)` function which is applied to the screen
        canvas instance - please refer to Tkinter documentation for further details.
        """
        self.screen.bind_all(sequence, func, add)

    def unbind_event_handler(self, sequence):
        """
        Unbind an event handler from the screen (to stop handling key presses, for example). This
        is actually just a wrapper around the Tkinter `unbind_all(...)` function which is applied
        to the screen canvas instance - please refer to Tkinter documentation for further details.
        """
        self.screen.unbind_all(sequence)

    def get_screen_size(self):
        """
        Obtain the full screen resolution to the edges of the CRT, including any non-addressable
        border area
        :return: the resolution of the 'full' screen, to the edges of the CRT, including any
                 non-addressable border, as (WIDTH, HEIGHT) in pixels
        """
        return self.screen_width, self.screen_height

    def get_resolution(self):
        """
        Obtain the 'addressable' screen resolution
        :return: the 'addressable' screen resolution as (WIDTH, HEIGHT) in pixels
        """
        return self.main_width, self.main_height

    def get_char_resolution(self):
        """
        Obtain the character size
        :return: the character size (WIDTH, HEIGHT) in pixels
        """
        return self.char_cols, self.char_rows

    def get_colors(self):
        """
        Obtain the colors available to the display  as a list of hex RGB values in the form
        '#RRGGBB'
        :return: the colors available to the display  as a list of hex RGB values in the form
                 '#RRGGBB'
        """
        return self.colors.copy()

    def get_color(self, color):
        """
        Obtain the color at the given index in the form '#RRGGBB'
        :return: the color at the given index in the form '#RRGGBB'
        """
        if type(color) == int:
            return self.colors[0] if (color < 0 or color >= len(self.colors)) else self.colors[color]
        return self.colors[0]

    def constrain_char_coords(self, col, row):
        """
        A utility method to constrain coordinates to the screen boundaries
        :param col: the column coordinate to constrain
        :param row: the row coordinate to constrain
        :return: the constrained coordinates (guarantted to be within the screen boundaries)
        """
        return max(0, min(self.char_cols - 1, col)), max(0, min(self.char_rows - 1, row))

    def get_char(self, col, row):
        """
        Obtain the character currently in screen memory at the given coordinates
        :param col: the column coordinate
        :param row: the row coordinate
        :return: the character at the given coordinates
        """
        col, row = self.constrain_char_coords(col, row)
        screen_memory_offset = self.get_char_memory_offset(col, row)
        return self.screen_char_memory[screen_memory_offset]

    def get_char_colors(self, col, row):
        """
        Obtain the foreground and background colors in color memory at the given coordinates
        :param col: the column coordinate
        :param row: the row coordinate
        :return: the foreground and background colors at the given coordinates
        """
        col, row = self.constrain_char_coords(col, row)
        screen_memory_offset = self.get_char_memory_offset(col, row)
        return copy.deepcopy(self.screen_color_memory[screen_memory_offset])

    def set_char_colors(self, col, row, fg_color=None, bg_color=None):
        """
        Set the foreground and/or background colors in color memory at the given coordinates
        :param col: the column coordinate
        :param row: the row coordinate
        :param fg_color: the foreground color to use
        :param bg_color: the background color to use
        """
        if fg_color is not None or bg_color is not None:
            col, row = self.constrain_char_coords(col, row)
            screen_memory_offset = self.get_char_memory_offset(col, row)
            screen_color = self.screen_color_memory[screen_memory_offset]
            if fg_color is not None:
                screen_color[0] = fg_color
            if bg_color is not None:
                screen_color[1] = bg_color
        return self

    def set_border_color(self, color):
        """
        Set the color to use for the screen border. Updates immediately.
        :param color: the border color to use
        """
        color = self.get_color(color)
        # top rectangle
        self.screen.create_rectangle(
            0, 0,
            (self.screen_width * self.scale), self.main_y0 - 1,
            fill=color, outline=color
        )
        # bottom rectangle
        self.screen.create_rectangle(
            0, self.main_y0 + (self.main_height * self.scale),
            (self.screen_width * self.scale), (self.screen_height * self.scale),
            fill=color, outline=color
        )
        # left rectangle
        self.screen.create_rectangle(
            0, self.main_y0,
            self.main_x0 - 1, self.main_y0 + (self.screen_height * self.scale),
            fill=color, outline=color
        )
        # right rectangle
        self.screen.create_rectangle(
            self.main_x0 + (self.main_width * self.scale), self.main_y0,
            (self.screen_width * self.scale), self.main_y0 + (self.screen_height * self.scale),
            fill=color, outline=color
        )
        return self

    def set_screen_color(self, color, render=True):
        """
        Set the color to use for the main screen area . Updates immediately.
        :param color:
        :param render: if True (default), re-render the screen immediately, otherwise only prepare
               the screen without rendering (may be rendered later)
        :return:
        """
        for offset in range(0, self.char_cols * self.char_rows):
            self.screen_color_memory[offset][1] = color
        if render:
            self.render()
        return self

    def clear_screen(self, render=True, cursor_to_home=True):
        """
        Clear the screen
        :param render: if True (default), re-render the screen immediately, otherwise only prepare
               the screen without rendering (may be rendered later)
        :param cursor_to_home: if True (default), the cursor will be moved to the top left position,
               otherwise it will be left in it's current location
        """
        self.screen_char_memory = [32, ] * (self.char_cols * self.char_rows)
        if cursor_to_home:
            self.move_cursor_to(0, 0)
        if render:
            self.render()
        return self

    def coord_convert(self, x, y):
        """
        Utility method to convert pixel coordinates to rendering coordinates on the addressable
        screen with scaling applied. For example, given (0, 0), the returned coordinates will be
        the *actual* top left coordinates of the screen in the rendered TK canvas
        :param x: the x coordinate
        :param y: the y coordinate
        :return: the converted coordinates
        """
        return round(self.main_x0 + (x * self.scale)), round(self.main_y0 + (y * self.scale))

    def get_char_memory_offset(self, col, row):
        """
        A utility method to obtain the offset from the start of screen memory of a given character
        column and row
        :param col: the column coordinate
        :param row: the row coordinate
        :return: the screen memory offset
        """
        col, row = self.constrain_char_coords(col, row)
        return row * self.char_cols + col

    def get_color_memory_offset(self, col, row):
        """
        A utility method to obtain the offset from the start of color memory of a given character
        column and row.
        NOTE: this actually just calls get_char_memory_offset(...) as desired result is the same
        :param col: the column coordinate
        :param row: the row coordinate
        :return: the color memory offset
        """
        return self.get_char_memory_offset(col, row)

    def define_custom_characters(self, start_charcode, character_defs):
        """
        Override the default font character bytes with customised bytes
        :param start_charcode: the character code at which to begin overwriting
        :param character_defs: the custom character definitions as arrays of integers (bytes)
        :return: the *original* character definitions which were overwritten, in case they need to
               be restored
        """
        old_character_defs = []
        for charcode, character_def in enumerate(character_defs):
            old_character_defs.append(self.font[charcode])
            self.font[start_charcode + charcode] = character_def
        return old_character_defs

    def print(self, text='',
              fg_color=None, bg_color=None,
              newline=True, inverse=False, render=True):
        """
        Print text on the screen, starting at the current cursor location
        :param text: the text to print
        :param fg_color: optionally define the foreground color to use - if unspecified the
               existing color memory at the location of the printing of each character will be used.
        :param bg_color: optionally define the background color to use - if unspecified the
               existing color memory at the location of the printing of each character will be used.
        :param newline: if True (default) put a newline at the end of the text (i.e., move the
               cursor to the next line down), otherwise the cursor position will remain at the end
               of the printed text
        :param inverse: print inverted characters (i.e., swap foreground and background - NOTE:
               relies in Commodore 64 inverse definitions)
        :param render: if True (default) update the screen immediately, otherwise only prepare
               the screen without rendering (may be rendered later)
        """
        if text:
            # just in case they pass in a numeric rather than a string, force string conversion now
            text = str(text)

        if self.text_to_character_mapper:
            # a specific text to character code mapper has been provided - use that to convert
            # the characters in the text to character codes first
            char_codes = self.text_to_character_mapper(text)
        else:
            # get the character codes for each letter in the string (normalising for the number
            # of characters in the font so we don't get index out of bounds issues for fonts with
            # weird numbers of characters in them
            font_char_count = len(self.font)
            char_codes = [(ord(c) % font_char_count) for c in text]

        if inverse:
            fg_color, bg_color = bg_color, fg_color

        # delegate to printing raw character codes at this point
        return self.print_charcodes(char_codes, fg_color, bg_color, newline, render)

    def print_charcodes(self, char_codes=None,
                        fg_color=None, bg_color=None,
                        newline=True, render=True):
        """
        Print text on the screen using 'raw' character codes, starting at the current cursor
        location
        :param char_codes: the character codes to print as a list
        :param fg_color: optionally define the foreground color to use - if unspecified the
               existing color memory at the location of the printing of each character will be used.
        :param bg_color: optionally define the background color to use - if unspecified the
               existing color memory at the location of the printing of each character will be used.
        :param newline: if True (default) put a newline at the end of the text (i.e., move the
               cursor to the next line down), otherwise the cursor position will remain at the end
               of the printed text
        :param render: if True (default) update the screen immediately, otherwise only prepare
               the screen without rendering (may be rendered later)
        """
        cx, cy = self.get_cursor_pos()
        cursor_min_x, cursor_min_y = cx, cy
        cursor_max_x, cursor_max_y = cx, cy
        scrolled = False
        if char_codes:
            for char_code in char_codes:
                cx, cy = self.get_cursor_pos()
                cursor_min_x, cursor_min_y = min(cursor_min_x, cx), min(cursor_min_y, cy)
                cursor_max_x, cursor_max_y = max(cursor_max_x, cx), max(cursor_max_y, cy)

                self.put_character(char_code, cx, cy, fg_color=fg_color, bg_color=bg_color)

                scrolled = self.move_cursor_right()
                if scrolled:
                    cursor_min_y = max(0, cursor_min_y - 1)
        if newline:
            scrolled = self.do_newline()
            if scrolled:
                cursor_min_y = max(0, cursor_min_y - 1)
        if render and (char_codes or newline):
            if scrolled:
                self.render()
            else:
                # just render the area of the screen which was modified
                self.render_area(cursor_min_x, cursor_min_y, cursor_max_x, cursor_max_y)
        return self

    def scroll_up(self):
        """
        Scroll the screen up, as happens when a newline is printed when the cursor is on the bottom
        row of the screen

        NOTE: does not render the updated screen! This must be done manually
        """
        # scroll up character memory, insert blank line (fill with space characters)
        self.screen_char_memory = self.screen_char_memory[self.char_cols:]
        self.screen_char_memory.extend([32, ] * self.char_cols)
        # scroll up color memory, copy last row values onto end
        self.screen_color_memory = self.screen_color_memory[self.char_cols:]
        self.screen_color_memory.extend(copy.deepcopy(self.screen_color_memory[-self.char_cols:]))
        return self

    def get_cursor_pos(self):
        """
        Obtain the current cursor position as (col, row)
        :return: the (col, row) coordinates of the cursor
        """
        return self.cursor_position[0], self.cursor_position[1]

    def move_cursor_to(self, col, row):
        """
        Reposition the cursor (used for printing)
        :param col: the column coordinate to move the cursor to
        :param row: the row coordinate to move the cursor to
        """
        col, row = self.constrain_char_coords(col, row)
        self.cursor_position[0] = col
        self.cursor_position[1] = row
        return self

    def move_cursor_up(self):
        """
        Move the cursor 'up' from its current location - if the cursor is in the top row this will
        have no effect.
        """
        self.cursor_position[1] = max(0, self.cursor_position[1] - 1)
        return self

    def move_cursor_left(self):
        """
        Move the cursor 'left' from its current location, unless it is in the HOME (0,0) position,
        in which case there is nowhere to go. If the cursor is already in the left most column, it
        will 'wrap' to the right hand side of the screen and move up a row.
        """
        if not (self.cursor_position[0] == 0 and self.cursor_position[1] == 0):
            self.cursor_position[0] -= 1
            if self.cursor_position[0] < 0:
                self.cursor_position[0] = self.char_cols - 1
                self.cursor_position[1] -= 1
                if self.cursor_position[1] < 0:
                    self.cursor_position[1] = 0
        return self

    def move_cursor_down(self):
        """
        Move the cursor 'down' from its current location. This may cause the screen to scroll up
        if the cursor is already on the bottom row.

        :return: True if the screen scrolled up as a result of the cursor moving down, False
                 otherwise
        """
        scrolled = False
        self.cursor_position[1] += 1
        if self.cursor_position[1] >= self.char_rows:
            self.cursor_position[1] = self.char_rows - 1
            self.scroll_up()
            scrolled = True
        return scrolled

    def move_cursor_right(self):
        """
        Move the cursor 'right' from its current location. If the cursor is already in the right
        most column, it will 'wrap' to the left hand side of the screen and move down a row. This
        may cause the screen to scroll up if the cursor is in the right most column of the bottom
        row (i.e., bottom right hand corner of the screen) when this method is called.

        :return: True if the screen scrolled up as a result of the cursor moving right, False
                 otherwise
        """
        scrolled = False
        self.cursor_position[0] += 1
        if self.cursor_position[0] >= self.char_cols:
            self.cursor_position[0] = 0
            self.cursor_position[1] += 1
            if self.cursor_position[1] >= self.char_rows:
                self.cursor_position[1] = self.char_rows - 1
                self.scroll_up()
                scrolled = True
        return scrolled

    def do_newline(self):
        """
        Insert a newline. This may cause the screen to scroll up if the cursor is already on the
        bottom row.

        :return: True if the screen scrolled up as a result of the newline, False otherwise
        """
        self.cursor_position[0] = 0
        return self.move_cursor_down()

    def put_character(self, char_code, col, row, fg_color=None, bg_color=None):
        """
        Put the given character into screen memory at the given location

        NOTE: Does not update/re-render the screen - rendering must be done manually to see changes
              after this method call.

        :param char_code: the character code to insert
        :param col: the column coordinate for the character
        :param row: the row coordinate for the character
        :param fg_color: optionally specify the foreground color
        :param bg_color: optionally specify the background color
        """
        screen_mem_offset = self.get_char_memory_offset(col, row)
        self.screen_char_memory[screen_mem_offset] = char_code
        screen_color = self.screen_color_memory[screen_mem_offset]

        if fg_color is not None:
            screen_color[0] = fg_color
        if bg_color is not None:
            screen_color[1] = bg_color

        return self

    def put_characters(self, char_codes, col, row, fg_color=None, bg_color=None):
        """
        Put the given characters into screen memory starting at the given location

        NOTE: Does not update/re-render the screen - rendering must be done manually to see changes
              after this method call.

        :param char_codes: the character codes to insert
        :param col: the column coordinate for the first character
        :param row: the row coordinate for the first character
        :param fg_color: optionally specify the foreground color
        :param bg_color: optionally specify the background color
        """
        screen_mem_offset = self.get_char_memory_offset(col, row)

        for idx, char_code in enumerate(char_codes):
            current_mem_offset = screen_mem_offset + idx
            self.screen_char_memory[current_mem_offset] = char_code
            screen_color = self.screen_color_memory[current_mem_offset]

            if fg_color is not None:
                screen_color[0] = fg_color
            if bg_color is not None:
                screen_color[1] = bg_color

        return self

    def plot(self, x, y, color):
        """
        Draw a single 'pixel' on the screen (with respect to the resolution of the 'old school
        screen' and scaling
        :param x: the x coordinate
        :param y: the y coordinate
        :param color: the color to plot
        """
        # delegates to the `rect(...)` method
        return self.rect(x, y, x+1, y+1, color)

    def rect(self, x1, y1, x2, y2, color):
        """
        Draw a (filled) rectangle on the screen (with respect to the resolution of the 'old school
        screen' and scaling
        :param x1: the top left x coordinate
        :param y1: the top left y coordinate
        :param x2: the bottom right x coordinate
        :param y2: the bottom right y coordinate
        :param color: the color to draw the rectangle
        """
        color = self.get_color(color)
        x1, y1 = self.coord_convert(x1, y1)
        x2, y2 = self.coord_convert(x2, y2)
        self.screen.create_rectangle(
            x1, y1, x2 - 1, y2 - 1,
            fill=color, outline=color
        )
        return self

    def draw_character(self, char_code, col, row, fg_color=None, bg_color=None):
        """
        This method carries out the hard work of actually rendering a character onto the screen. It
        uses the bytes defined in the font array to render the bitmap for each character

        TODO - There **has** to be a better way of doing this than actually plotting rectangles;
               It should be possible to use the bytes directly onto a TK image instance scale/color
               the result (without any anti-aliasing, of course!) and the blat it to the main
               canvas at the correct location. It's probably debatable whether this would be more
               or less 'educational' than the implementation below, but in any case I am currently
               lacking in time to chase this up further.

        :param char_code: the character code to render
        :param col: the column coordinate at which to render the character
        :param row: the row coordinate at which to render the character
        :param fg_color: optionally specify the foreground color to use when rendering the
               character, if unspecifed color memory will be referred to when rendering.
        :param bg_color: optionally specify the bacground color to use when rendering the
               character, if unspecifed color memory will be referred to when rendering.
        """
        if fg_color is None or bg_color is None:
            current_fg, current_bg = self.get_char_colors(col, row)
            fg_color = current_fg if fg_color is None else fg_color
            bg_color = current_bg if bg_color is None else bg_color

        # work out top left coordinate for the character
        top_x = col * self.char_width
        top_y = row * self.char_height

        # clear the character square using the background color
        self.rect(top_x, top_y, top_x + self.char_width, top_y + self.char_height, bg_color)

        # get the character/font bytes to render
        character_def = self.font[char_code % len(self.font)]
        # render each row of the character
        for line_idx, value in enumerate(character_def):
            y1 = top_y + line_idx
            y2 = y1 + 1
            if value == 255:
                # all bits are on - shortcut!
                self.rect(top_x, y1, top_x + self.char_width, y2, fg_color)
            elif value > 0:
                # some bits are on - render
                # we could just render every 'pixel' individually (which would massively simplify
                # the following code), but this tries to minimise draw calls by...
                #
                #  - drawing single rectangles for horizontally adjacent pixels which are active
                #    (instead of one square per 'on' pixel), and
                #  - only processes as far as the rightmost 'on' pixel, skipping processing of
                #    'trailing' pixels which are off.
                #
                # For example:
                #
                #          Draw in this direction
                #          |======>
                # Byte     Bits
                # 184  =   10111000
                #          * ***
                #          ^ ^  ^
                #          | |  L these three pixels are skipped, because there are no more 'on'
                #          | |    pixels to the right of them, so there is nothing else to draw for
                #          | |    this byte.
                #          | |
                #          | L draw these three adjacent 'on' pixels as one single rectangle
                #          |
                #          L draw this pixel as a single rectangle - there are no adjacent 'on'
                #            pixels, so we can't avoid this.
                #
                first_on_idx = None
                bit_is_set = None
                bit_idx = 0
                for bit_idx, bit_value in enumerate([128, 64, 32, 16, 8, 4, 2, 1]):
                    if value > 0 or bit_is_set:
                        bit_is_set = value & bit_value
                        if bit_is_set:
                            # this bit is on
                            if first_on_idx is None:
                                # change of state to 'on' - record this index
                                first_on_idx = bit_idx
                            # by doing this we can stop drawing at the rightmost 'on' pixel,
                            # skipping 'trailing' off pixels to the right of the last 'on' pixel
                            value -= bit_value
                        else:
                            # this bit is off
                            if first_on_idx is not None:
                                # change of state to 'off' - draw the rectangle now
                                self.rect(top_x + first_on_idx, y1,
                                          top_x + bit_idx, y2,
                                          fg_color)
                                # we don't know where the next 'on' will be
                                first_on_idx = None
                # if we finished with an 'on' bit and a first on
                if bit_is_set and first_on_idx:
                    self.rect(top_x + first_on_idx, y1,
                              top_x + bit_idx + 1, y2,
                              fg_color)
        # update screen memory
        self.put_character(char_code, col, row, fg_color, bg_color)

        return self

    def render(self, force_all=False):
        """
        Renders the whole screen. This is optimised to attempt to render only areas of the screen
        which have changed since the last render occurred, skipping anything else.
        :param force_all: optionally force the rendering of *everything* on the screen, skipping
               the optimisations to avoid re-rendering anything which has not changed.
        """
        screen_mem_offset = 0
        for row in range(0, self.char_rows):
            for col in range(0, self.char_cols):
                current_char = self.screen_char_memory[screen_mem_offset]
                current_fg_color, current_bg_color = self.screen_color_memory[screen_mem_offset]
                if force_all:
                    has_changed = True
                elif self.last_rendered_screen_char_memory is None or\
                     self.last_rendered_screen_color_memory is None:
                    has_changed = True
                else:
                    last_char = self.last_rendered_screen_char_memory[screen_mem_offset]
                    last_fg_color, last_bg_color = self.last_rendered_screen_color_memory[screen_mem_offset]
                    has_changed = last_char != current_char or \
                                  last_fg_color != current_fg_color or \
                                  last_bg_color != current_bg_color
                if has_changed:
                    self.draw_character(current_char, col, row, current_fg_color, current_bg_color)
                screen_mem_offset += 1

        self.last_rendered_screen_char_memory = self.screen_char_memory.copy()
        self.last_rendered_screen_color_memory = copy.deepcopy(self.screen_color_memory)

        return self

    def render_area(self, col0, row0, col1, row1, force_all=False):
        """
        Renders a portion of the screen. This is optimised to attempt to render only the parts of
        the area which have changed since the last render occurred, skipping anything else.
        :param col0: the top left column of the area to render
        :param row0: the top left row of the area to render
        :param col1: the bottom right column of the area to render
        :param row1: the bottom right row of the area to render
        :param force_all: optionally force the rendering of *everything* in the area, skipping
               the optimisations to avoid re-rendering anything which has not changed.
        """
        col0, row0 = self.constrain_char_coords(col0, row0)
        col1, row1 = self.constrain_char_coords(col1, row1)
        col0, col1 = min(col0, col1), max(col0, col1)
        row0, row1 = min(row0, row1), max(row0, row1)
        if col0 == 0 and row0 == 0 and col1 >= self.char_cols - 1 and row1 >= self.char_rows - 1:
            # full screen re-render
            self.render(force_all=force_all)
        else:
            for col in range(col0, col1 + 1):
                for row in range(row0, row1 + 1):
                    self.render_char(col, row)

        return self

    def render_char(self, col, row, force=False):
        """
        Render the col/row location as it is currently defined in screen memory. This is optimised
        to render only if the screen and/or color memory at the location has changed since the last
        render occurred, skipping otherwise.
        :param col: the column to render
        :param row: the row to render
        :param force: optionally force the rendering of the character, skipping
               the optimisations to avoid re-rendering it if it has not changed.
        """
        screen_mem_offset = self.get_char_memory_offset(col, row)
        current_char = self.screen_char_memory[screen_mem_offset]
        current_fg_color, current_bg_color = self.screen_color_memory[screen_mem_offset]
        if force:
            has_changed = True
        elif self.last_rendered_screen_char_memory is None or \
             self.last_rendered_screen_color_memory is None:
            has_changed = True
        else:
            last_char = self.last_rendered_screen_char_memory[screen_mem_offset]
            last_fg_color, last_bg_color = self.last_rendered_screen_color_memory[screen_mem_offset]
            has_changed = last_char != current_char or \
                          last_fg_color != current_fg_color or \
                          last_bg_color != current_bg_color
        if has_changed:
            self.draw_character(current_char, col, row, current_fg_color, current_bg_color)

            if self.last_rendered_screen_char_memory is None:
                self.last_rendered_screen_char_memory = self.screen_char_memory.copy()
            else:
                self.last_rendered_screen_char_memory[screen_mem_offset] = self.screen_char_memory[screen_mem_offset]

            if self.last_rendered_screen_color_memory is None:
                self.last_rendered_screen_color_memory = copy.deepcopy(self.screen_color_memory)
            else:
                self.last_rendered_screen_color_memory[screen_mem_offset] = copy.deepcopy(self.screen_color_memory[screen_mem_offset])

        return self
