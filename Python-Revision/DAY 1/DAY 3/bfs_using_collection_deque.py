from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")  # Process node
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

# Usage
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
bfs(graph, 'A')  # Output: A B C D

#Start at A -> Explore neighbors B, C -> Explore B's neighbor D, C's neighbor D (already queued) -> Done
#Order: A, B, C, D (level by level)