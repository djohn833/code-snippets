#!/usr/bin/env python

import re
from regex_helpers import escape_for_charset


def binary_search_with_compare(c):
    low, high = 0x20, 0x7e
    while low < high:
        guess = (low + high + 1) // 2
        if chr(guess) <= c:
            low = guess
        else:
            high = guess - 1
        print(low, high, guess)
    return chr(low)


def binary_search_with_regex(c):
    low, high = 0x20, 0x7e
    while low < high:
        guess = (low + high + 1) // 2
        # Iff guess <= c, then c matches [guess-high]
        if re.fullmatch('[' + escape_for_charset(chr(guess)) + '-' + escape_for_charset(chr(high)) + ']', c):
            low = guess
        else:
            high = guess - 1
        print(low, high, guess)
    return chr(low)
