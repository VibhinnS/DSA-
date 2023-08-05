def permutations(arr):
    result = []

    if len(arr) == 1:
        return [arr[:]]

    for i in range(len(arr)):
        n = arr[i]
        remaining = arr[:i] + arr[i + 1:]
        perms = permutations(remaining)

        for perm in perms:
            result.append([n] + perm)

    return sorted(result)

final_arr = permutations([1,2,3])
curr = final_arr.index()


# print(final_arr.index(arr))


def find_permutations(string):
    # Convert the string to a list to enable easy manipulation
    chars = list(string)
    
    # Base case: If the string contains only one character, return a list with that character
    if len(chars) == 1:
        return [string]
    
    permutations = []
    
    # Iterate over each character in the string
    for i in range(len(chars)):
        # Extract the current character
        char = chars[i]
        
        # Create a list with the remaining characters by excluding the current one
        remaining_chars = chars[:i] + chars[i+1:]
        
        # Recursively find permutations of the remaining characters
        sub_permutations = find_permutations(''.join(remaining_chars))
        
        # Append the current character to each sub-permutation and add them to the main list
        for sub_permutation in sub_permutations:
            permutations.append(char + sub_permutation)
    
    return permutations

# print(find_permutations("abc"))


