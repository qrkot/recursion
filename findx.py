#!/usr/bin/env python3

def find_x(string, n = 0):

    if string[n] == 'x':
        return n 

    return ( find_x( string, n + 1) )

print( find_x('abcdefxgh') )
