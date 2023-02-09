#!/usr/bin/env python3
#
# Find even numbers in an array.
#

def even(arr):
    
    if len(arr) == 0:
        return([])

    if arr[0] % 2 == 0:
        return [arr[0]] + even( arr[1:len(arr)] )
    else:
        return even( arr[1:len(arr)] )



print( even([1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]) )
