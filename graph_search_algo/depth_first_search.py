def dfs(graph, current_vertex, target_value, visited=None):
    if visited is None:
        visited = []

    visited.append(current_vertex)

    if current_vertex == target_value:
        return visited

    # Add your recursive case here:
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, target_value, visited)

            if path:
                return path


the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
}

# Call dfs() below and print the result:
# print(dfs(the_most_dangerous_graph, "crocodiles", "bees"))

graph = {'A': set(['B','C']),
         'B': set(['A', 'E', 'D']),
         'D': set(['B']),
         'C': set(['A','H']),
         'E': set(['B', 'F']),
         'F': set(['E', 'G']),
         'G': set(['F']),
         'H': set(['C'])}

print(dfs(graph, 'A', 'G'))