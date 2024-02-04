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

def bfs(graph, start, goal):
    queue = [(start, [start])]  # Queue now stores both the current node and the path taken to reach it

    while queue:
        current_node, path = queue.pop(0)
        print(current_node, end=" ")

        if current_node == goal:
            print("\nGoal state reached! Path:", ' -> '.join(path))
            return

        visited.add(current_node)

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    print("\nGoal state not reached.")

# Example usage for BFS with start state 'S' and goal state 'G':
bfs(graph, 'S', 'G')
