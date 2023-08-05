arr = [64,25,12,22,11]
n = len(arr)
for i in range(n):
    min_element = min(arr[i:])
    index = arr.index(min_element)
    arr[i],arr[index] = arr[index], arr[i]
    
print(arr)

# har traversal mei minimum element dhundh, replace it with first element of the array
# i ki value badhti rhegi, aur array traversal chota hota jaega
