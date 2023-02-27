#!/usr/bin/env python3

def partition(left_pointer, right_pointer):

    pivot_index = right_pointer
    pivot = array[pivot_index]
    
    right_pointer -= 1
    
    while(1):

        while (array[left_pointer] < pivot):
            left_pointer += 1

        while (array[right_pointer] > pivot):
            right_pointer -= 1
        
        if (left_pointer >= right_pointer):
            break
        else:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
            left_pointer += 1

    array[left_pointer], array[pivot_index] = array[pivot_index], array[left_pointer]

    return left_pointer


def quicksort(left_index, right_index):

    if (right_index - left_index <= 0):
        return
    
    pivot_index = partition(left_index, right_index)

    quicksort(left_index, pivot_index - 1)
    quicksort(pivot_index + 1, right_index)


array = [8,0,5,2,1,6,3]
quicksort(0, len(array) - 1)
print(array)


