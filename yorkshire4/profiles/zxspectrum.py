from travertino.colors import color


UNPRINTABLE_CHAR = [0, 0, 0, 0, 0, 0, 0, 0]

ZX_SPECTRUM_FONT = [
    # The system font is stored at 0x3D00-0x3FFF in the ROM with
    # each character being represented
    # by 8 sequential bytes (left pixel is high bit)
    # https://damieng.com/blog/2011/02/20/typography-in-8-bits-system-fonts
    # https://web.archive.org/web/20050307204242/http://eclecticsatyr.hostultra.com/speccs.htm
    # https://www.worldofspectrum.org/faq/reference/48kreference.htm
    # 0
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # PRINT
    UNPRINTABLE_CHAR,  # EDIT
    UNPRINTABLE_CHAR,  # CURSOR LEFT
    UNPRINTABLE_CHAR,  # CURSOR RIGHT
    UNPRINTABLE_CHAR,  # CURSOR DOWN
    UNPRINTABLE_CHAR,  # CURSOR UP
    UNPRINTABLE_CHAR,  # DELETE
    UNPRINTABLE_CHAR,  # ENTER
    UNPRINTABLE_CHAR,  # NUMBER
    UNPRINTABLE_CHAR,  # UNDEFINED
    # 16
    UNPRINTABLE_CHAR,  # INK
    UNPRINTABLE_CHAR,  # PAPER
    UNPRINTABLE_CHAR,  # FLASH
    UNPRINTABLE_CHAR,  # BRIGHT
    UNPRINTABLE_CHAR,  # INVERSE
    UNPRINTABLE_CHAR,  # AT
    UNPRINTABLE_CHAR,  # TAB
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    UNPRINTABLE_CHAR,  # UNDEFINED
    # 32
    # [SPACE] ! " # $ % ^ ' ( ) * + , - . /
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 16, 16, 16, 16, 0, 16, 0],
    [0, 36, 36, 0, 0, 0, 0, 0],
    [0, 36, 126, 36, 36, 126, 36, 0],
    [0, 8, 62, 40, 62, 10, 62, 8],
    [0, 98, 100, 8, 16, 38, 70, 0],
    [0, 16, 40, 16, 42, 68, 58, 0],
    [0, 8, 16, 0, 0, 0, 0, 0],
    [0, 4, 8, 8, 8, 8, 4, 0],
    [0, 32, 16, 16, 16, 16, 32, 0],
    [0, 0, 20, 8, 62, 8, 20, 0],
    [0, 0, 8, 8, 62, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 8, 16],
    [0, 0, 0, 0, 62, 0, 0, 0],
    [0, 0, 0, 0, 0, 24, 24, 0],
    [0, 0, 2, 4, 8, 16, 32, 0],
    # 48
    # 0 1 2 3 4 5 6 7 8 9 : ; < = > ?
    [0, 60, 70, 74, 82, 98, 60, 0],
    [0, 24, 40, 8, 8, 8, 62, 0],
    [0, 60, 66, 2, 60, 64, 126, 0],
    [0, 60, 66, 12, 2, 66, 60, 0],
    [0, 8, 24, 40, 72, 126, 8, 0],
    [0, 126, 64, 124, 2, 66, 60, 0],
    [0, 60, 64, 124, 66, 66, 60, 0],
    [0, 126, 2, 4, 8, 16, 16, 0],
    [0, 60, 66, 60, 66, 66, 60, 0],
    [0, 60, 66, 66, 62, 2, 60, 0],
    [0, 0, 0, 16, 0, 0, 16, 0],
    [0, 0, 16, 0, 0, 16, 16, 32],
    [0, 0, 4, 8, 16, 8, 4, 0],
    [0, 0, 0, 62, 0, 62, 0, 0],
    [0, 0, 16, 8, 4, 8, 16, 0],
    [0, 60, 66, 4, 8, 0, 8, 0],
    # 64
    # @ a b c d e f g h i j k l m n o
    [0, 60, 74, 86, 94, 64, 60, 0],
    [0, 60, 66, 66, 126, 66, 66, 0],
    [0, 124, 66, 124, 66, 66, 124, 0],
    [0, 60, 66, 64, 64, 66, 60, 0],
    [0, 120, 68, 66, 66, 68, 120, 0],
    [0, 126, 64, 124, 64, 64, 126, 0],
    [0, 126, 64, 124, 64, 64, 64, 0],
    [0, 60, 66, 64, 78, 66, 60, 0],
    [0, 66, 66, 126, 66, 66, 66, 0],
    [0, 62, 8, 8, 8, 8, 62, 0],
    [0, 2, 2, 2, 66, 66, 60, 0],
    [0, 68, 72, 112, 72, 68, 66, 0],
    [0, 64, 64, 64, 64, 64, 126, 0],
    [0, 66, 102, 90, 66, 66, 66, 0],
    [0, 66, 98, 82, 74, 70, 66, 0],
    [0, 60, 66, 66, 66, 66, 60, 0],
    # 80
    # p q r s t u v w x y z [ £ ] ↑ ←
    [0, 124, 66, 66, 124, 64, 64, 0],
    [0, 60, 66, 66, 82, 74, 60, 0],
    [0, 124, 66, 66, 124, 68, 66, 0],
    [0, 60, 64, 60, 2, 66, 60, 0],
    [0, 254, 16, 16, 16, 16, 16, 0],
    [0, 66, 66, 66, 66, 66, 60, 0],
    [0, 66, 66, 66, 66, 36, 24, 0],
    [0, 66, 66, 66, 66, 90, 36, 0],
    [0, 66, 36, 24, 24, 36, 66, 0],
    [0, 130, 68, 40, 16, 16, 16, 0],
    [0, 126, 4, 8, 16, 32, 126, 0],
    [0, 14, 8, 8, 8, 8, 14, 0],
    [0, 0, 64, 32, 16, 8, 4, 0],
    [0, 112, 16, 16, 16, 16, 112, 0],
    [0, 16, 56, 84, 16, 16, 16, 0],
    [0, 0, 0, 0, 0, 0, 0, 255],
    # 96
    #   A B C D E F G H I J K L M N O
    [0, 28, 34, 120, 32, 32, 126, 0],
    [0, 0, 56, 4, 60, 68, 60, 0],
    [0, 32, 32, 60, 34, 34, 60, 0],
    [0, 0, 28, 32, 32, 32, 28, 0],
    [0, 4, 4, 60, 68, 68, 60, 0],
    [0, 0, 56, 68, 120, 64, 60, 0],
    [0, 12, 16, 24, 16, 16, 16, 0],
    [0, 0, 60, 68, 68, 60, 4, 56],
    [0, 64, 64, 120, 68, 68, 68, 0],
    [0, 16, 0, 48, 16, 16, 56, 0],
    [0, 4, 0, 4, 4, 4, 36, 24],
    [0, 32, 40, 48, 48, 40, 36, 0],
    [0, 16, 16, 16, 16, 16, 12, 0],
    [0, 0, 104, 84, 84, 84, 84, 0],
    [0, 0, 120, 68, 68, 68, 68, 0],
    [0, 0, 56, 68, 68, 68, 56, 0],
    # 112
    # P Q R S T U V W X Y Z
    [0, 0, 120, 68, 68, 120, 64, 64],
    [0, 0, 60, 68, 68, 60, 4, 6],
    [0, 0, 28, 32, 32, 32, 32, 0],
    [0, 0, 56, 64, 56, 4, 120, 0],
    [0, 16, 56, 16, 16, 16, 12, 0],
    [0, 0, 68, 68, 68, 68, 56, 0],
    [0, 0, 68, 68, 40, 40, 16, 0],
    [0, 0, 68, 84, 84, 84, 40, 0],
    [0, 0, 68, 40, 16, 40, 68, 0],
    [0, 0, 68, 68, 68, 60, 4, 56],
    [0, 0, 124, 8, 16, 32, 124, 0],
    [0, 14, 8, 48, 8, 8, 14, 0],
    [0, 8, 8, 8, 8, 8, 8, 0],
    [0, 112, 16, 12, 16, 16, 112, 0],
    [0, 20, 40, 0, 0, 0, 0, 0],
    [60, 66, 153, 161, 161, 153, 66, 60],
    # 128
    # graphics characters
    [0, 0, 0, 0, 0, 0, 0, 0],
    [15, 15, 15, 15, 0, 0, 0, 0],
    [240, 240, 240, 240, 0, 0, 0, 0],
    [255, 255, 255, 255, 0, 0, 0, 0],
    [0, 0, 0, 0, 15, 15, 15, 15],
    [15, 15, 15, 15, 15, 15, 15, 15],
    [240, 240, 240, 240, 15, 15, 15, 15],
    [255, 255, 255, 255, 15, 15, 15, 15],
    [0, 0, 0, 0, 240, 240, 240, 240],
    [15, 15, 15, 15, 240, 240, 240, 240],
    [240, 240, 240, 240, 240, 240, 240, 240],
    [255, 255, 255, 255, 240, 240, 240, 240],
    [0, 0, 0, 0, 255, 255, 255, 255],
    [15, 15, 15, 15, 255, 255, 255, 255],
    [240, 240, 240, 240, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255, 255],
    # 144
    UNPRINTABLE_CHAR,  # GR-A
    UNPRINTABLE_CHAR,  # GR-B
    UNPRINTABLE_CHAR,  # GR-C
    UNPRINTABLE_CHAR,  # GR-D
    UNPRINTABLE_CHAR,  # GR-E
    UNPRINTABLE_CHAR,  # GR-F
    UNPRINTABLE_CHAR,  # GR-G
    UNPRINTABLE_CHAR,  # GR-H
    UNPRINTABLE_CHAR,  # GR-I
    UNPRINTABLE_CHAR,  # GR-J
    UNPRINTABLE_CHAR,  # GR-K
    UNPRINTABLE_CHAR,  # GR-L
    UNPRINTABLE_CHAR,  # GR-M
    UNPRINTABLE_CHAR,  # GR-N
    UNPRINTABLE_CHAR,  # GR-O
    UNPRINTABLE_CHAR,  # GR-P
    # 160
    UNPRINTABLE_CHAR,  # GR-Q
    UNPRINTABLE_CHAR,  # GR-R
    UNPRINTABLE_CHAR,  # GR-S
    UNPRINTABLE_CHAR,  # GR-T
    UNPRINTABLE_CHAR,  # GR-U
    UNPRINTABLE_CHAR,  # RND
    UNPRINTABLE_CHAR,  # INKEY$
    UNPRINTABLE_CHAR,  # PI
    UNPRINTABLE_CHAR,  # FN
    UNPRINTABLE_CHAR,  # POINT
    UNPRINTABLE_CHAR,  # SCREEN$
    UNPRINTABLE_CHAR,  # ATTR
    UNPRINTABLE_CHAR,  # AT
    UNPRINTABLE_CHAR,  # TAB
    UNPRINTABLE_CHAR,  # VAL$
    UNPRINTABLE_CHAR,  # CODE
    # 176
    UNPRINTABLE_CHAR,  # VAL
    UNPRINTABLE_CHAR,  # LEN
    UNPRINTABLE_CHAR,  # SIN
    UNPRINTABLE_CHAR,  # COS
    UNPRINTABLE_CHAR,  # TAN
    UNPRINTABLE_CHAR,  # ASN
    UNPRINTABLE_CHAR,  # ACS
    UNPRINTABLE_CHAR,  # ATN
    UNPRINTABLE_CHAR,  # LN
    UNPRINTABLE_CHAR,  # EXP
    UNPRINTABLE_CHAR,  # INT
    UNPRINTABLE_CHAR,  # SQR
    UNPRINTABLE_CHAR,  # SGN
    UNPRINTABLE_CHAR,  # ABS
    UNPRINTABLE_CHAR,  # PEEK
    UNPRINTABLE_CHAR,  # IN
    # 192
    UNPRINTABLE_CHAR,  # USR
    UNPRINTABLE_CHAR,  # STR$
    UNPRINTABLE_CHAR,  # CHR$
    UNPRINTABLE_CHAR,  # NOT
    UNPRINTABLE_CHAR,  # BIN
    UNPRINTABLE_CHAR,  # OR
    UNPRINTABLE_CHAR,  # AND
    UNPRINTABLE_CHAR,  # <=
    UNPRINTABLE_CHAR,  # >=
    UNPRINTABLE_CHAR,  # <>
    UNPRINTABLE_CHAR,  # LINE
    UNPRINTABLE_CHAR,  # THEN
    UNPRINTABLE_CHAR,  # TO
    UNPRINTABLE_CHAR,  # STEP
    UNPRINTABLE_CHAR,  # DEF FN
    UNPRINTABLE_CHAR,  # CAT
    # 208
    UNPRINTABLE_CHAR,  # FORMAT
    UNPRINTABLE_CHAR,  # MOVE
    UNPRINTABLE_CHAR,  # ERASE
    UNPRINTABLE_CHAR,  # OPEN#
    UNPRINTABLE_CHAR,  # CLOSE#
    UNPRINTABLE_CHAR,  # MERGE
    UNPRINTABLE_CHAR,  # VERIFY
    UNPRINTABLE_CHAR,  # BEEP
    UNPRINTABLE_CHAR,  # CIRCLE
    UNPRINTABLE_CHAR,  # INK
    UNPRINTABLE_CHAR,  # PAPER
    UNPRINTABLE_CHAR,  # FLASH
    UNPRINTABLE_CHAR,  # BRIGHT
    UNPRINTABLE_CHAR,  # INVERSE
    UNPRINTABLE_CHAR,  # OVER
    UNPRINTABLE_CHAR,  # OUT
    # 224
    UNPRINTABLE_CHAR,  # LPRINT
    UNPRINTABLE_CHAR,  # LLIST
    UNPRINTABLE_CHAR,  # STOP
    UNPRINTABLE_CHAR,  # READ
    UNPRINTABLE_CHAR,  # DATA
    UNPRINTABLE_CHAR,  # RESTORE
    UNPRINTABLE_CHAR,  # NEW
    UNPRINTABLE_CHAR,  # BORDER
    UNPRINTABLE_CHAR,  # CONTINUE
    UNPRINTABLE_CHAR,  # DIM
    UNPRINTABLE_CHAR,  # REM
    UNPRINTABLE_CHAR,  # FOR
    UNPRINTABLE_CHAR,  # GOTO
    UNPRINTABLE_CHAR,  # GO SUB
    UNPRINTABLE_CHAR,  # INPUT
    UNPRINTABLE_CHAR,  # LOAD
    # 240
    # LIST LET PAUSE NEXT POKE PRINT PLOT RUN SAVE
    # RANDOMIZE IF CLS DRAW CLEAR RETURN COPY
    UNPRINTABLE_CHAR,  # LIST
    UNPRINTABLE_CHAR,  # LET
    UNPRINTABLE_CHAR,  # PAUSE
    UNPRINTABLE_CHAR,  # NEXT
    UNPRINTABLE_CHAR,  # POKE
    UNPRINTABLE_CHAR,  # PRINT
    UNPRINTABLE_CHAR,  # PLOT
    UNPRINTABLE_CHAR,  # RUN
    UNPRINTABLE_CHAR,  # SAVE
    UNPRINTABLE_CHAR,  # RANDOMIZE
    UNPRINTABLE_CHAR,  # IF
    UNPRINTABLE_CHAR,  # CLS
    UNPRINTABLE_CHAR,  # DRAW
    UNPRINTABLE_CHAR,  # CLEAR
    UNPRINTABLE_CHAR,  # RETURN
    UNPRINTABLE_CHAR,  # COPY
]

# ZX Spectrum screen profile

__name__ = 'ZX Spectrum'

# ZX Spectrum 'full screen' is 403 pixels wide x 312 pixels high,
# including the border area
full_screen_size = (352, 312)

# ZX Spectrum 'addressable' screen area - 256 pixels wide x 192 pixels high
screen_size = (256, 192)

# ZX Spectrum text characters are 8 pixels wide x 8 pixels high
character_size = (8, 8)

# ZX Spectrum  colors
colors = [
    # dark
    color('#000000'),  # black
    color('#0000D7'),  # blue
    color('#D70000'),  # red
    color('#D700D7'),  # magenta
    color('#00D700'),  # green
    color('#00D7D7'),  # cyan
    color('#D7D700'),  # yellow
    color('#D7D7D7'),  # white
    # bright
    color('#000000'),  # black
    color('#0000FF'),  # blue
    color('#FF0000'),  # red
    color('#FF00FF'),  # magenta
    color('#00FF00'),  # green
    color('#00FFFF'),  # cyan
    color('#FFFF00'),  # yellow
    color('#FFFFFF'),  # white
]

default_border_color = 0  # black
default_screen_color = 7  # white
default_text_color = 0  # black

font = ZX_SPECTRUM_FONT

# The character code to use for the cursor (' ')
cursor_char = 32

# Cursor blink delay (in ms)
cursor_blink_delay = 500

boot_text = ''
