# Initialize empty graph, path and traversal list
graph = {}         # To store the graph structure (adjacency list)
path = []          # To store the path from source to goal if found
traversal = []     # To record the order in which nodes are visited

def add_edges(vertex, neighbors):
    """
    Adds edges to the graph for a given vertex and its neighbors.
    """
    graph[vertex] = neighbors  # Add the vertex and its neighbors to the graph

def bfs(source, goals):
    """
    Performs BFS to find any goal state, calculates path and distance (number of nodes).
    """
    open_list = [source]               # Queue for BFS; starts with the source node
    parent = {source: None}            # Dictionary to track how we reached each node
    distances = {source: 0}            # Stores distance from source to each node

    while open_list:                   # Continue until queue is empty
        current = open_list.pop(0)     # Remove the first node from the queue
        traversal.append(current)      # Add current node to traversal list (visited order)

        if current in goals:           # If the current node is a goal
            distance = distances[current]  # Get the distance to this goal
            while current is not None:     # Trace the path back to source
                path.append(current)       # Add node to path
                current = parent[current]  # Move to parent node
            path.reverse()                 # Reverse to get path from source to goal
            return f"Goal Found! Path: {' -> '.join(path)}, Distance: {distance} nodes"

        for neighbor in graph.get(current, []):  # Loop through all neighbors of current node
            if neighbor not in distances:        # If neighbor not visited yet
                open_list.append(neighbor)       # Add to queue
                parent[neighbor] = current       # Set its parent
                distances[neighbor] = distances[current] + 1  # Set its distance

    return "No goal found."  # If queue is empty and no goal was found

def get_input():
    """
    Takes input to construct the graph, source, and goals, then runs BFS.
    """
    n = int(input("Enter the number of vertices: "))  # Number of vertices to input
    for _ in range(n):
        vertex = input("Vertex: ").strip()  # Get the vertex name
        neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").strip().split()
        add_edges(vertex, neighbors)        # Add edges to the graph

    source = input("Enter the source node: ").strip()  # Get source node
    goals = input("Enter goal nodes (space-separated): ").strip().split()  # Get goal nodes

    result = bfs(source, goals)  # Call BFS with the input source and goal(s)
    print(result)  # Print the result of BFS
    print("Traversal of the graph:", " -> ".join(traversal))  # Show the traversal order

get_input()  # Run the whole program
