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

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Example usage:
dfs(visited, graph, 'S')
