from collections import deque

def find_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None  # No path found

# Usage
graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
print(find_path(graph, 'A', 'D'))  # Output: ['A', 'B', 'D']


#  A
 # / \
# B   C
#  \ /
#   D
#Path from A to D: A→B→D (or A→C→D)




#Problem to be solved later
#Write a truth table for $ P ↔ (Q ∧ ¬R) $.
#Calculate $ C(5,3) $ and $ P(5,3) $.
#Implement a function to find all paths between two nodes.