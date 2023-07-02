def permutations(arr):
    result = []
    
    if len(arr) == 1:
        return [arr[:]]

    for i in range(len(arr)):
        n = arr[0]
        arr = arr[1:]
        perms = permutations(arr)
        
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        arr.append(n)
    return sorted(result)

# print(permutations([2,3,1]))



def find_permutations(string):
    if len(string) == 1:
        return [string]
    
    permutations = []
    
    for i in range(len(string)):
        char = string[i]
        remaining_string = string[:i] + string[i+1:]
        
        sub_permutations = find_permutations(remaining_string)
        
        for sub_permutation in sub_permutations:
            permutations.append(char + sub_permutation)
    
    return permutations

print(find_permutations("abc"))

