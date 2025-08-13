def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")  # Process node (e.g., print)
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(graph, neighbor, visited)
    return visited

# Usage
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
dfs(graph, 'A')  # Output: A B D C

#Start at A -> Explore B -> Explore D (B's neighbor) -> Backtrack to A -> Explore C -> C's neighbor D already visited -> Done
#Order: A, B, D, C