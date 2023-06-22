dimensions = input("Dimensions - ").split()


i = int(dimensions[0])
j = int(dimensions[1])


array = [[0 for _ in range(j)] for _ in range(i)]


for rows in range(i):
    for columns in range(j):
        array[rows][columns] = int(input("Enter value - "))


def search_array(element):
    for row in range(i):
        for column in range(j):
            if array[row][column] == element:
                print(row, " ", column)
                print(array)
                return True
    return False


print("\n")
element = int(input("Enter the value to be searched - "))
search_array(element)
