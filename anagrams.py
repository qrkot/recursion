#!/usr/bin/env python3
#
# Print anagrams of a given string.
#

import sys

def anagrams_of(string):

    if len(string) == 1:
        return [string[0]]

    collection = []

    substring_anagrams = anagrams_of(string[1 : len(string)])

    for substring_anagram in substring_anagrams:
        for index in range(len(substring_anagram) + 1):
            collection.append(substring_anagram[:index]+string[0]+substring_anagram[index:])

    return collection
        

if __name__ == '__main__':
    print( anagrams_of( sys.argv[1] if len(sys.argv) > 1 else '123' ) )
