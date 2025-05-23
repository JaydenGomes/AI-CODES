# Initialize global structures
graph = {}           # Dictionary to hold the graph (adjacency list)
path = []            # To store the final path from source to goal
traversal = []       # To store the order in which nodes are visited

# Function to add a vertex and its neighbors (edges) to the graph
def add_edges(vertex, neighbors):
    """Adds edges to the graph for a given vertex and its neighbors."""
    graph[vertex] = neighbors  # Map the vertex to its list of neighbors

# Function to perform Depth-First Search
def dfs(source, goals):
    """
    Performs DFS to find any goal state, calculates path and distance (number of nodes).
    """
    open_list = [source]     # Stack for DFS (LIFO)
    parent = {source: None}  # Dictionary to remember each node's parent

    while open_list:
        current = open_list.pop()  # Get the last node added (DFS)

        # Skip if already visited
        if current in traversal:
            continue

        traversal.append(current)  # Mark the node as visited

        # Check if goal is found
        if current in goals:
            distance = len(traversal) - 1  # Number of nodes visited before goal
            # Reconstruct the path from goal to source using parent map
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()  # Reverse to get source to goal order

            return f"Goal Found! Path: {' -> '.join(path)}, Distance: {distance} nodes"

        # Add neighbors in reverse order (to preserve left-to-right DFS traversal)
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in traversal:
                open_list.append(neighbor)      # Add to stack
                parent[neighbor] = current      # Set parent for path tracking

    return "No goal found."  # If the loop finishes without finding a goal

# Function to handle user input and run the DFS algorithm
def get_input():
    """
    Takes input to construct the graph, source, and goals, then runs DFS.
    """
    n = int(input("Enter the number of vertices: "))  # Number of nodes
    for _ in range(n):
        vertex = input("Vertex: ").strip()  # Get vertex name
        neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").strip().split()
        add_edges(vertex, neighbors)  # Add to graph

    source = input("Enter the source node: ").strip()               # Input starting node
    goals = input("Enter goal nodes (space-separated): ").strip().split()  # Input goal node(s)

    # Call the DFS function and display the results
    result = dfs(source, goals)
    print(result)
    print("Traversal of the graph:", " -> ".join(traversal))  # Show traversal path

# Start the program
get_input()
