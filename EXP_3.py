# Initialize global data structures
graph = {}                   # Stores the graph as an adjacency list
path = []                    # Stores the final path from source to goal
traversal = []               # Stores the traversal order of nodes
cost_of_traversal = 0        # Stores the total traversal cost based on heuristics

# Function to add edges to the graph
def add_edges(vertex, neighbors):
    """Adds edges to the graph for a given vertex and its neighbors."""
    graph[vertex] = neighbors  # Map the vertex to its neighbors

# Function to perform Best-First Search (Greedy Search)
def best_first_search(source, goals, heuristic):
    """Performs Best-First Search to find the goal state and calculates the path."""
    
    open_list = [source]          # List of nodes to be explored
    parent = {source: None}       # Track parent nodes for path reconstruction
    visited = set()               # Set of visited nodes to avoid repetition

    # Reset globals before new run
    global cost_of_traversal
    cost_of_traversal = 0
    traversal.clear()
    path.clear()

    while open_list:
        # Select node with the lowest heuristic value from open_list
        current = min(open_list, key=lambda node: heuristic[node])
        open_list.remove(current)          # Remove the selected node
        traversal.append(current)          # Add to traversal path

        # If it's not the source, add heuristic of parent to cost
        if current in parent and parent[current] is not None:
            cost_of_traversal += heuristic[parent[current]]

        # Goal check
        if current in goals:
            # Build path from goal to source using parent dictionary
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()  # Reverse to get source to goal path

            # Collect heuristics of goal nodes
            goal_heuristics = {goal: heuristic[goal] for goal in goals if goal in heuristic}

            return f"Goal Found! Path: {' -> '.join(path)}\n" \
                   f"Goal heuristics: {goal_heuristics}\n" \
                   f"Total traversal cost: {cost_of_traversal}"

        visited.add(current)  # Mark node as visited

        # Add unvisited neighbors to open_list
        for neighbor in graph.get(current, []):
            if neighbor not in visited and neighbor not in open_list:
                open_list.append(neighbor)
                parent[neighbor] = current

    return "No goal found."  # If no goal is found

# Function to handle input and run the algorithm
def get_input():
    """Takes input to construct the graph, source, and goals, then runs Best-First Search."""
    print("\n")
    
    n = int(input("Enter the number of vertices: "))  # Number of vertices in the graph
    for _ in range(n):
        vertex = input("Vertex: ").strip()  # Input vertex
        neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").strip().split()
        add_edges(vertex, neighbors)        # Add edges for this vertex

    source = input("Enter the source node: ").strip()  # Input source
    goals = input("Enter goal nodes (space-separated): ").strip().split()  # Input goal nodes

    # Input heuristic values for each vertex
    heuristic = {}
    for vertex in graph.keys():
        heuristic[vertex] = int(input(f"Enter heuristic for {vertex}: "))

    # Run the Best-First Search algorithm
    result = best_first_search(source, goals, heuristic)
    
    # Display results
    print(result)
    print("Traversal of the graph:", " -> ".join(traversal))
    print(f"Total traversal cost: {cost_of_traversal}")

# Run the program
get_input()
