# binary search
def binary_search(array, key):
    start = 0
    end = len(array) - 1
    middle = start + (end - start)//2

    while start <= end:
        if key == array[middle]:
            print(middle)
            break

        if key > array[middle]:
            start = middle+1

        else:
            end = middle-1
        middle = start + (end - start)//2
    return -1


binary_search([1, 2, 3, 5, 5, 5, 8, 9, 10], 5)
