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
stack = [('S', ['S'])]  # Stack now stores both the current node and the path taken to reach it

while stack:
    current_node, path = stack.pop()
    print(current_node, end=" ")

    if current_node == 'I':
        print("\nGoal state reached! Path:", ' -> '.join(path))
        break

    visited.add(current_node)

    for neighbour in reversed(graph[current_node]):
        if neighbour not in visited:
            visited.add(neighbour)
            stack.append((neighbour, path + [neighbour]))

else:
    print("\nGoal state not reached.")

