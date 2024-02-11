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
visited = set()

queue = [('S', ['S'])]  # Queue now stores both the current node and the path taken to reach it

while queue:
    current_node, path = queue.pop(0)
    print(current_node, end=" ")

    if current_node == 'I':
        print("\nGoal state reached! Path:", ' -> '.join(path))
        break

    visited.add(current_node)

    for neighbour in graph[current_node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append((neighbour, path + [neighbour]))

print("\nGoal state not reached.")
