def has_cycle(graph, node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True
    rec_stack.remove(node)
    return False

# Usage
graph = {'A': ['B', 'C'], 'B': ['C'], 'C': ['A'], 'D': []}  # Cycle: A-B-C-A
visited = set()
rec_stack = set()
print(has_cycle(graph, 'A', visited, rec_stack))  # Output: True


#   A
#  / \
# B---C
#  D
#Adjacency List: {'A': ['B', 'C'], 'B': ['C'], 'C': ['A'], 'D': []}
#Cycle: A→B→C→A