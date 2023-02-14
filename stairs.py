#!/usr/bin/env python3

def num_of_paths(n):

    if n < 0:
        return 0

    if n == 0 or n == 1:
        return 1

    return num_of_paths(n - 1) + num_of_paths(n - 2) + num_of_paths(n - 3)

print(num_of_paths(11))
