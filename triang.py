#!/usr/bin/env python3

def get_n(n):
    
    if n == 0:
        return 0

    if n == 1:
        return 1

    return n + get_n(n-1)


if __name__ == '__main__':
    print( get_n(7) )
