from collections import defaultdict
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]

#template for LeetCode Topological Sort
def template():
    degree = {key: 0 for key in input}
    graph = defaultdict(list)

    for node_depend,node in input:
        graph[node].append(node_depend)
        degree[node] += 1
        
    lst_no_dep = [ node for node in input if degree[node] == 0]

    stk = []
    while lst_no_dep:
        node = lst_no_dep.pop()
        stk.append(node)
        for node_depend in graph[node]:
            degree[node_depend] -= 1
            if degree[node_depend] == 0:
                lst_no_dep.append(node_depend)
    return stk


graph = {1:[2,8], 2:[1,3], 3:[2,4,5,6], 4:[3,8,7], 5:[3,6], 6:[5,3,7], 7: [4,6], 8: [1,4]}

print(topological_sort(graph))
