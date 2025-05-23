# Function to generate next possible states (children) of a given state
def movegen(graph, state):
    return graph.get(state, {}).get("children", [])

# Hill Climbing algorithm function
def hill_climbing(graph, start, is_maximization):
    current = start                # Start from the initial state
    traversal = [current]          # Keep track of traversal path

    while True:
        children = movegen(graph, current)  # Get children of current state

        # If no children, we are at a local maxima or minima
        if not children:
            print("\nLocal", "Maxima" if is_maximization else "Minima", "found at:", current)
            return traversal, current

        # Sort children by heuristic value
        # Descending for maximization, Ascending for minimization
        children.sort(key=lambda child: graph[child]["heuristic"], reverse=is_maximization)
        best_child = children[0]  # Best child based on heuristic

        # Check if the best child improves over the current state
        if (is_maximization and graph[best_child]["heuristic"] > graph[current]["heuristic"]) or \
           (not is_maximization and graph[best_child]["heuristic"] < graph[current]["heuristic"]):
            current = best_child
            traversal.append(current)
        else:
            # No improvement possible → Local extrema found
            print("\nLocal", "Maxima" if is_maximization else "Minima", "found at:", current)
            return traversal, current


# Get user input: Type of optimization (max/min)
optimization_type = input("Enter optimization type (max/min): ").strip().lower()
is_maximization = optimization_type == "max"  # Boolean flag

# Build the graph from user input
graph = {}
num_states = int(input("Enter the number of states: "))
for _ in range(num_states):
    state_name = input("Enter current state: ")
    heuristic_value = int(input(f"Enter heuristic value for {state_name}: "))
    num_children = int(input(f"How many children for {state_name}? "))
    children = [input(f"Enter child {i + 1}: ") for i in range(num_children)]
    # Store heuristic and children for each state
    graph[state_name] = {"heuristic": heuristic_value, "children": children}

# Get the start state from user
start = input("Enter start state: ")

# Run the hill climbing algorithm
traversal, local_extreme = hill_climbing(graph, start, is_maximization)

# Output the results
print("\nTraversal order:")
print(" -> ".join(traversal))
print("\nLocal", "Maxima" if is_maximization else "Minima", "found at:", local_extreme)
