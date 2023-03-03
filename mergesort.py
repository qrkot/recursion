#!/usr/bin/env python3

import random

def split(array):

    if len(array) == 1:
        return array

    mid_point = len(array) // 2

    left_array = split(array[ : mid_point])
    right_array = split(array[mid_point : ])

    return merge(left_array, right_array)


def merge(left, right):

    output = []
    i = j = 0

    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i : ])
    output.extend(right[j : ])

    return output


array = [ random.randint(1, 100) for x in range(100) ]
print(array)
print(split(array))
