# i = int(input("Rows - "))
# j = int(input("Columns - "))

#pehle 0 the saare
# array = [[0 for _ in range(3)] for _ in range(3)]

# #entering values
# for rows in range(j):
#     for columns in range(i):
#         array_2d[rows][columns] = int(input("Enter - "))

# print(array_2d)

# for row in array_2d:
#     for element in row:
#         print(element, end=" ")



# array[2][2] = [1,2,3,4,5,6,7,8,9]

# for rows in range(3):
#     for columns in range(3):
#         print(array[rows][columns], end=" ")



#another method

def change(arr):

    rows = len(arr)
    columns = len(arr[0])

    for i in range(rows):
        sum = 0
        for j in range(columns-1,-1,-1):
            temp = arr[i][j]
            arr[i]
            sum += temp

    return arr






