#!/usr/bin/env python3

def flatten(array):
    for item in array:
        if isinstance(item, list):
            flatten(item)
        else:
            print(item)


if __name__ == '__main__':
    flatten( [1,2,3,[4,5,6],7,[8,[9,10,11,[12,13,14]]],
            [15,16,17,18,19,[20,21,22,[23,24,25,[26,27,29]],30,31],32],33] )

