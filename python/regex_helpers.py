#!/usr/bin/env python

def escape_for_charset(c):
    """Escape a character to include it in a character set in a regex.

    Characters with special meanings inside a character set (e.g., \, ^, \, and -)
    must be escaped with a slash for them to be included in the character set
    instead of having their special meaning.

    ] is used to mark the end of the character set.
    - is used to specify a range between two characters (e.g., [a-z]).
    ^ is used to negate the character set when it is the first character.
    \ is used to escape other characters, so it must be escaped itself.
    
    Args:
        c: The character to escape

    Returns:
        A string that contains c, escaped if needed.

    """
    if c == ']' or c == '^' or c == '\\' or c == '-':
        return '\\' + c
    return c
