method_names = ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
arguments = [[2],[1],[2],[3],[4],[7],[8],[20],[21],[0],[2],[],[],[],[],[]]

output = []

# Initialize the class instance
output.append(f"dinnerplates = DinnerPlates({arguments[0][0]})")

# Iterate through the methods and their arguments
for method, arg in zip(method_names[1:], arguments[1:]):
    if arg:
        output.append(f"dinnerplates.{method}({', '.join(map(str, arg))})")
    else:
        output.append(f"dinnerplates.{method}()")

# Join the output list into a single string with newline characters
formatted_output = '\n'.join(output)
print(formatted_output)
