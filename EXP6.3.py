MAX_A = 4
MAX_B = 3

def generate_graph():
    graph = {}
    for a in range(MAX_A + 1):
        for b in range(MAX_B + 1):
            state = (a, b)
            neighbors = []

            if a < MAX_A:
                neighbors.append((MAX_A, b))
            if b < MAX_B:
                neighbors.append((a, MAX_B))
            if a > 0:
                neighbors.append((0, b))
            if b > 0:
                neighbors.append((a, 0))

            pour = min(a, MAX_B - b)
            if pour > 0:
                neighbors.append((a - pour, b + pour))
            pour = min(b, MAX_A - a)
            if pour > 0:
                neighbors.append((a + pour, b - pour))

            graph[state] = neighbors
    return graph

def get_rule(current, next):
    a1, b1 = current
    a2, b2 = next

    if a2 > a1 and b1 == b2:
        return "FILL JUG A"
    elif b2 > b1 and a1 == a2:
        return "FILL JUG B"
    elif a2 < a1 and b1 == b2 and a2 == 0:
        return "EMPTY JUG A"
    elif b2 < b1 and a1 == a2 and b2 == 0:
        return "EMPTY JUG B"
    elif a2 < a1 and b2 > b1:
        return "POUR A TO B"
    elif b2 < b1 and a2 > a1:
        return "POUR B TO A"
    return "UNKNOWN RULE"

def get_path(goal, parent):
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]
    return list(reversed(path))

def dfs(source, goal_states, graph):
    open_list = [source]  # stack for DFS
    closed_list = []
    parent = {source: None}
    step = 0

    print("\n--- WATER JUG PROBLEM USING DFS TRAVERSAL ---\n")

    while open_list:
        current = open_list.pop()  # stack behavior
        if current in closed_list:
            continue
        closed_list.append(current)
        step += 1

        print(f"STEP {step}: VISITED {current} | JUG A: {current[0]}L, JUG B: {current[1]}L")

        if current in goal_states:
            print(f"\nGOAL STATE {current} REACHED!\n")
            path = get_path(current, parent)
            print("PATH TO GOAL:")
            for p in path:
                print(f"  - {p} | JUG A: {p[0]}L, JUG B: {p[1]}L")
            break

        for neighbor in reversed(graph[current]):  # reverse for correct DFS order
            if neighbor not in closed_list and neighbor not in open_list:
                open_list.append(neighbor)
                parent[neighbor] = current
                rule = get_rule(current, neighbor)
                print(f"  ↳ TRANSITION TO {neighbor} | RULE: {rule}")

    else:
        print("\nGOAL NOT REACHABLE FROM SOURCE.")

    print("\n--- GRAPH (KEY-VALUE PAIRS) ---")
    for state in graph:
        print(f"{state} → {graph[state]}")

if __name__ == "__main__":
    source = (0, 0)
    goal_states = [(2, 0), (0, 2), (4, 2), (2, 3)]
    graph = generate_graph()
    dfs(source, goal_states, graph)
