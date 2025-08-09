def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add neighbors to stack (reverse to mimic recursion order)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

# Usage
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
dfs_iterative(graph, 'A')  # Output: A B D C