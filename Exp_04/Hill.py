graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E'],
    'E': ['H', 'I'],
    'B': [],
    'C': ['F', 'G'],
    'D': [],
    'F': [],
    'H': [],
    'I': [],
    'G': []
}

from collections import deque

start_node = 'S'
goal_node = 'G'

visited = set()
queue = deque([(start_node, [start_node])])

while queue:
    current_node, path = queue.popleft()
    print(current_node, end=" ")

    if current_node == goal_node:
        print("\nGoal state reached! Path:", ' -> '.join(path))
        break

    visited.add(current_node)

    for neighbour in graph[current_node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append((neighbour, path + [neighbour]))
else:
    print("\nGoal state not reached.")
