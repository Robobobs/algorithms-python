'''Binary search algorithm'''
from math import floor

def binary_search(list, value):
    '''Binary search algorithm for returning index position of value(s)'''
    left = 0
    right = len(list) - 1
    indices = []

    while left <= right:
        middle = floor((left + right) / 2)
        if list[middle] == value:
            indices.append(middle)

            prev_idx = middle - 1
            while prev_idx >= 0:
                prev_value = list[prev_idx]
                
                if prev_value == value: # Performs linear search to the left
                    indices.insert(0, prev_idx)
                    prev_idx = prev_idx - 1
                    prev_value = list[prev_idx]
                else:
                    break

            next_idx = middle + 1
            while next_idx <= len(list)-1:
                next_value = list[next_idx]
                
                if next_value == value: # Performs linear search to the right
                    indices.append(next_idx)
                    if next_idx+1 == len(list):
                        break
                    else:
                        next_idx = next_idx + 1
                        next_value = list[next_idx]
                else:
                    break

            return indices

        elif value < list[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return False


# ------------------------------- TEST CASE --------------------------------- #

if __name__ == '__main__':
        #idx  0  1  2  3  4  5  6  7  8  9  10 11 12  13  14  15, 16
    list_1 = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 15, 15]
    target_1 = 9
    target_2 = 15
    target_3 = 5
    target_4 = 1

    print(binary_search(list_1, target_1)) # should return index 11
    print(binary_search(list_1, target_2)) # should return indices 15 and 16
    print(binary_search(list_1, target_3)) # should return indices 5, 6 and 7
    print(binary_search(list_1, target_4)) # should return indices 0 and 1


'''
# --------------------------------- NOTES ----------------------------------- #

A fast searching algorithm, used to find the location(s) of a value in an array.

Binary search algorithm can only be be performed on a sorted array. If the array
is not sorted, a sorting algorithm must be run first before running the binary search.

Works via a 'decrease-and-conquer' method (i.e. reduces the problem instance into a
smaller instance of the same problem. There is only ever one problem to solve throughout.)

If the array length is odd, use floor division to round down.

'''
