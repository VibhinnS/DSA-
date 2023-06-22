array = [1, 2, 3, 4, 5]
# temp = []

# for i in range(len(array)-1):
#     temp.append(array[i] + array[i+1])


def sum_triangle(arr):

    temp = []
    if len(arr) < 1:
        return

    for i in range(len(arr)-1):
        temp.append(arr[i] + arr[i+1])

    sum_triangle(temp)
    print(arr)


sum_triangle(array)
