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

start_node = 'S'
goal_node = 'D'

from queue import Queue

visited = set()
queue = Queue()
queue.put((start_node, [start_node]))  # (node, path)

while not queue.empty():
    current_node, path = queue.get()
    print(current_node, end=" ")

    if current_node == goal_node:
        print("\nGoal state reached! Path:", ' -> '.join(path))
        break

    visited.add(current_node)

    for neighbour in graph[current_node]:
        if neighbour not in visited:
            new_path = path + [neighbour]
            queue.put((neighbour, new_path))
else:
    print("\nGoal state not reached.")
