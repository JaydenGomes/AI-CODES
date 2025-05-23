graph = {}
path = []
traversal = []

def add_edges(vertex, neighbors):
    """
    Adds edges to the graph for a given vertex and its neighbors.
    """
    graph[vertex] = neighbors

def bfs(source, goals):
    """
    Performs BFS to find any goal state, calculates path and distance (number of nodes).
    """
    open_list = [source]
    parent = {source: None}
    distances = {source: 0}  # Distance from source to each node

    while open_list:
        current = open_list.pop(0)
        traversal.append(current)
        if current in goals:
            # Construct the path
            distance = distances[current]
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return f"Goal Found! Path: {' -> '.join(path)}, Distance: {distance} nodes"

        for neighbor in graph.get(current, []):
            if neighbor not in distances:  # Not visited
                open_list.append(neighbor)
                parent[neighbor] = current
                distances[neighbor] = distances[current] + 1  # Update distance

    return "No goal found."

def get_input():
    """
    Takes input to construct the graph, source, and goals, then runs BFS.
    """
    n = int(input("Enter the number of vertices: "))
    for _ in range(n):
        vertex = input("Vertex: ").strip()
        neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").strip().split()
        add_edges(vertex, neighbors)

    source = input("Enter the source node: ").strip()
    goals = input("Enter goal nodes (space-separated): ").strip().split()

    result = bfs(source, goals)
    print(result)
    print("Traversal of the graph:", " -> ".join(traversal))

get_input()
