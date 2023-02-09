#!/usr/bin/env python3

def find_x(string):

    if string[n] == 'x':
        return n 

    return ( find_x( string[n+1:len(string)]) )


print( find_x('abcdxefgh') )
