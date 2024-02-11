import heapq

graph = {
    'S': [('A', 1), ('B', 2), ('C', 5)],
    'A': [('D', 3), ('E', 4)],
    'E': [('H', 7), ('I', 8)],
    'B': [],
    'C': [('F', 6), ('G', 9)],
    'D': [],
    'F': [],
    'H': [],
    'I': [],
    'G': []
}

visited = set()
priority_queue = [(0, 'S', ['S'])]  # Priority queue now stores the cumulative cost, current node, and the path taken to reach it

while priority_queue:
    cost, current_node, path = heapq.heappop(priority_queue)
    print(current_node, end=" ")

    if current_node == 'H':
        print("\nGoal state reached! Path:", ' -> '.join(path))
        break

    visited.add(current_node)

    for neighbour, edge_cost in graph[current_node]:
        if neighbour not in visited:
            visited.add(neighbour)
            heapq.heappush(priority_queue, (cost + edge_cost, neighbour, path + [neighbour]))

else:
    print("\nGoal state not reached.")
