'''
    GUMX style hints
'''

import typing

Flag = typing.Optional
Hint = typing.TypedDict

class Color(Hint):
    foreground = None
    background = None

class Cursor(Color):
    mode: typing.Literal['blink'] = None












class Confirm(Hint):
    affirmative        : str    = None
    negative           : str    = None
    show_help          : bool   = None
    prompt             : Color  = None
    selected           : Color  = None
    unselected         : Color  = None

class File(Hint):
    height             : int    = None
    cursor             : str    = None
    show_help          : bool   = None
    cursor             : Color  = None
    symlink            : Color  = None
    directory          : Color  = None
    file               : Color  = None
    permissions        : Color  = None
    selected           : Color  = None
    file_size          : Color  = None

class Pager(Hint):
    show_line_numbers  : bool   = None
    help               : Color  = None
    line_number        : Color  = None
    match              : Color  = None
    match_highlight    : Color  = None

class Write(Hint):
    width              : int    = None
    height             : int    = None
    show_cursor_line   : bool   = None
    show_line_numbers  : bool   = None
    show_help          : bool   = None
    base               : Color  = None
    header             : Color  = None
    placeholder        : Color  = None
    prompt             : Color  = None
    end_of_buffer      : Color  = None
    line_number        : Color  = None
    cursor_line_number : Color  = None
    cursor_line        : Color  = None
    cursor             : Cursor = None

class Filter(Hint):
    indicator          : Color  = None
    selected_indicator : Color  = None
    unselected_prefix  : Color  = None
    header             : Color  = None
    text               : Color  = None
    cursor_text        : Color  = None
    match              : Color  = None
    prompt             : Color  = None
    placeholder        : Color  = None

class Input(Hint):
    cursor             : Cursor = None
    width              : int    = None
    show_help          : bool   = None
    prompt             : Color  = None
    placeholder        : Color  = None
    cursor             : Color  = None
    header             : Color  = None

class Spinner(Hint):
    spinner            : Color = None
    title              : Color = None

# EOF