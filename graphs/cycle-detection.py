from collections import deque
from typing import Dict, Set, List


def undirected_cycle_detection_via_bfs(graph: Dict[int, List[int]], start: int, visited: Set[int]) -> bool:
    queue: deque = deque([(start, None)])
    visited.add(start) #start node added in visited set

    while queue:
        current, parent_node = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, current))
            elif neighbor != parent_node:
                return True

    return False



def undirected_cycle_detection_via_dfs(graph):
    visited = set()
    
    def _dfs(node, parent, visited=set()):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if _dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if _dfs(node, None):
                return True
    return False
    
    



print(undirected_cycle_detection_via_bfs({1: [2, 3], 2: [1, 5], 3: [1, 4, 6], 4: [3], 5: [2, 7], 6: [3, 7], 7: [5, 6]}, 1, set()))

print(undirected_cycle_detection_via_dfs({1: [2, 3], 2: [1, 5], 3: [1, 4, 6], 4: [3], 5: [2, 7], 6: [3, 7], 7: [5, 6]}))

