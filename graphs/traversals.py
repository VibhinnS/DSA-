# bfs
from collections import deque
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            print(current_node)  

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                        

def dfs(visited, graph, root):
    if root in visited:
        return
    visited.add(root)
    print(root)
    neighbours = graph[root]
    for next_node in neighbours:
        dfs(visited, graph, next_node)
    


if __name__ == "__main__":
    graph = {1:[2,8], 2:[1,3], 3:[2,4,5,6], 4:[3,8,7], 5:[3,6], 6:[5,3,7], 7: [4,6], 8: [1,4]}
    visited :set[str] = set()
    dfs(visited, graph, 1)
