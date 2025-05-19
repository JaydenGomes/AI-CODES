graph = {}
path = []
traversal = []
cost_of_traversal = 0  # Variable to keep track of the traversal cost

def add_edges(vertex, neighbors):
    """Adds edges to the graph for a given vertex and its neighbors."""
    graph[vertex] = neighbors

def best_first_search(source, goals, heuristic):
    """Performs Best-First Search to find the goal state and calculates the path."""
    open_list = [source]
    parent = {source: None}
    visited = set()

    global cost_of_traversal
    cost_of_traversal = 0  # Reset traversal cost
    traversal.clear()
    path.clear()

    while open_list:
        # Select the node with the lowest heuristic value
        current = min(open_list, key=lambda node: heuristic[node])
        open_list.remove(current)
        traversal.append(current)

        if current in parent and parent[current] is not None:
            cost_of_traversal += heuristic[parent[current]]  # Add heuristic cost of moving

        if current in goals:
            # Construct the path from source to goal
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()

            goal_heuristics = {goal: heuristic[goal] for goal in goals if goal in heuristic}
            return f"Goal Found! Path: {' -> '.join(path)}\n" \
                   f"Goal heuristics: {goal_heuristics}\n" \
                   f"Total traversal cost: {cost_of_traversal}"

        visited.add(current)

        # Add neighbors to the open list
        for neighbor in graph.get(current, []):
            if neighbor not in visited and neighbor not in open_list:
                open_list.append(neighbor)
                parent[neighbor] = current

    return "No goal found."

def get_input():
    """Takes input to construct the graph, source, and goals, then runs Best-First Search."""
    print("\n")
    n = int(input("Enter the number of vertices: "))
    for _ in range(n):
        vertex = input("Vertex: ").strip()
        neighbors = input(f"Enter neighbors of {vertex} (space-separated): ").strip().split()
        add_edges(vertex, neighbors)

    source = input("Enter the source node: ").strip()
    goals = input("Enter goal nodes (space-separated): ").strip().split()

    # Getting heuristics for each node
    heuristic = {}
    for vertex in graph.keys():
        heuristic[vertex] = int(input(f"Enter heuristic for {vertex}: "))

    result = best_first_search(source, goals, heuristic)
    print(result)
    print("Traversal of the graph:", " -> ".join(traversal))
    print(f"Total traversal cost: {cost_of_traversal}")

get_input()
