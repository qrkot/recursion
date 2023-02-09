#!/usr/bin/env python3
#
# Count total number of chars in a string array.
#

import sys

def number_of_chars(strings):

    if len(strings) == 0:
        return 0

    return len(strings[0]) + number_of_chars(strings[1:len(strings)])



print(number_of_chars(['ab', 'c', 'def', 'ghij']))
