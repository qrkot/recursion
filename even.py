#!/usr/bin/env python3
#
# Find even numbers in an array.
#

def even(arr, res):
    
    if len(arr) == 0:
        return([])

    if arr[0] % 2 == 0:
        res.append(arr[0])

    even( arr[1:len(arr)], res )

    return(res)


print( even([1, 2, 3, 4, 5, 6 , 7, 8, 9, 10], []) )
