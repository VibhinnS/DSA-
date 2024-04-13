from collections import deque
def shortest_path(grid, start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows = len(grid)
    cols = len(grid[0])

    start = (0,0) #abhi 0,0 le rhe - kuch bhi ho skta hai

    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        current_pos, distance = queue.popleft()
        row, col = current_pos

        if current_pos == end:
            return distance
        
        for dx, dy in directions:
            new_row, new_col = row+dx, col+dy

            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != 'unwanted':
                neighbor = (new_row, new_col)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

    return -1
