''' bubble sort algorithm '''

def bubble_sort(lst):
    index_len = len(lst) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range (0, index_len):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                sorted = False
        index_len -= 1

    return lst

# ------------------------------- TEST CASE --------------------------------- #
numbers = [2,4,5,3,6,1,9,5,8,2]
print(bubble_sort(numbers))
