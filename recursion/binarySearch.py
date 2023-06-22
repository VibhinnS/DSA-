# Binary Search with recursion
def binary_search(array, start, end, target):
    if (start > end):
        return -1

    middle = start + (end - start)//2
    if (target == array[middle]):
        return middle
    elif (target < array[middle]):
        return binary_search(array, start, middle-1, target)
    else:
        return binary_search(array, middle+1, end, target)


array = [1, 2, 3, 36, 46, 55, 66, 78, 587, 3456]
array.sort()
target = 36
print(binary_search(array, 0, len(array)-1, target))
