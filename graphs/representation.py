input:list[list[int]] = [[0,1],[0,2],[0,3],[0,4],[1,3],[2,3],[2,4],[2,5],[3,5]]
n:int = 6 #number of nodes

#adjacency matrix
"""
Space Complexity: O(n^2)
"""
mg = [[0 for _ in range(n)] for _ in range(n)]
for (u,v) in input:
    mg[u][v] = 1
    mg[v][u] = 1
for row in mg:
    print(row)
print("\n")

# adjacency list
"""
Space Complexity: O(2e)  ->  better for storing the adjacent neighbours of the nodes.
"""
graph:dict[int,list[int]] = {}
for (u,v) in input:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)
    
for element in graph:
    print(f"{element}: {graph[element]}")
