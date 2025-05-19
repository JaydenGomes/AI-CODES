def movegen(graph, state):
    return graph.get(state, {}).get("children", [])


def hill_climbing(graph, start, is_maximization):
    current = start
    traversal = [current]
    while True:
        children = movegen(graph, current)
        if not children:
            print("\nLocal", "Maxima" if is_maximization else "Minima", "found at:", current)
            return traversal, current

        children.sort(key=lambda child: graph[child]["heuristic"], reverse=is_maximization)
        best_child = children[0]

        if (is_maximization and graph[best_child]["heuristic"] > graph[current]["heuristic"]) or \
                (not is_maximization and graph[best_child]["heuristic"] < graph[current]["heuristic"]):
            current = best_child
            traversal.append(current)
        else:
            print("\nLocal", "Maxima" if is_maximization else "Minima", "found at:", current)
            return traversal, current


optimization_type = input("Enter optimization type (max/min): ").strip().lower()
is_maximization = optimization_type == "max"

graph = {}
num_states = int(input("Enter the number of states: "))
for _ in range(num_states):
    state_name = input("Enter current state: ")
    heuristic_value = int(input(f"Enter heuristic value for {state_name}: "))
    num_children = int(input(f"How many children for {state_name}? "))
    children = [input(f"Enter child {i + 1}: ") for i in range(num_children)]
    graph[state_name] = {"heuristic": heuristic_value, "children": children}

start = input("Enter start state: ")
traversal, local_extreme = hill_climbing(graph, start, is_maximization)

print("\nTraversal order:")
print(" -> ".join(traversal))
print("\nLocal", "Maxima" if is_maximization else "Minima", "found at:", local_extreme)
