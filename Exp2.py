graph = {}
path = []
traversal = []

def add_edges(vertex, neighbors):
    """Adds edges to the graph for a given vertex and its neighbors."""
    graph[vertex] = neighbors

def dfs(source, goals):
    """
    Performs DFS to find any goal state, calculates path and distance (number of nodes).
    """
    open_list = [source]  # Stack for DFS
    parent = {source: None}

    while open_list:
        current = open_list.pop()
        if current in traversal:
            continue

        traversal.append(current)

        if current in goals:
            # Construct the path
            distance = len(traversal) - 1
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return f"Goal Found! Path: {' -> '.join(path)}, Distance: {distance} nodes"

        for neighbor in reversed(graph.get(current, [])):  # Reverse for consistent DFS order
            if neighbor not in traversal:
                open_list.append(neighbor)
                parent[neighbor] = current

    return "No goal found."

def get_input():
    """
    Takes input to construct the graph, source, and goals, then runs DFS.
    """
    n = int(input("Enter the number of vertices: "))
    for _ in range(n):
        vertex = input("Vertex: ").strip()
        neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").strip().split()
        add_edges(vertex, neighbors)

    source = input("Enter the source node: ").strip()
    goals = input("Enter goal nodes (space-separated): ").strip().split()

    result = dfs(source, goals)
    print(result)
    print("Traversal of the graph:", " -> ".join(traversal))

get_input()
