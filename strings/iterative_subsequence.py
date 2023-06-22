def iterative_subsequence(array):
    output_array = [[]]
    for nums in array:
        n = len(output_array)
        for i in range (n):
            internal_array = output_array[i].copy()
            internal_array.append(nums)
            output_array.append(internal_array)
    return output_array


print(iterative_subsequence([1,2,3]))
