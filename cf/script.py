def generate_subsets(nums):
    def backtrack(start, subset):
        subsets.append(subset[:])  # Append a copy of the current subset to the list of subsets
        for i in range(start, len(nums)):
            subset.append(nums[i])  # Include the current number in the subset
            backtrack(i + 1, subset)  # Recur for the next index with the updated subset
            subset.pop()  # Backtrack: remove the current number from the subset

    subsets = []
    backtrack(0, [])
    return subsets

# Example usage:
nums = [1, 2, 3]
all_subsets = generate_subsets(nums)
for subset in all_subsets:
    print(subset)
