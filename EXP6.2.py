from collections import deque

# CAPACITIES OF JUG A AND JUG B
JUG_A = 4
JUG_B = 3

# GOAL STATE (YOU CAN CHANGE THIS)
GOAL = (2, 3)

# FUNCTION TO CHECK IF A STATE IS VALID
def is_valid(state):
    a, b = state
    return 0 <= a <= JUG_A and 0 <= b <= JUG_B

# FUNCTION TO GET NEXT POSSIBLE STATES FROM CURRENT STATE
def get_next_states(state):
    a, b = state
    return [
        (JUG_A, b),          # FILL JUG A
        (a, JUG_B),          # FILL JUG B
        (0, b),              # EMPTY JUG A
        (a, 0),              # EMPTY JUG B
        (a - min(a, JUG_B - b), b + min(a, JUG_B - b)),  # POUR A TO B
        (a + min(b, JUG_A - a), b - min(b, JUG_A - a))   # POUR B TO A
    ]

# BFS FUNCTION
def bfs(start, goal):
    visited = set()
    queue = deque([(start, [])])
    graph = {}

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        graph[state] = get_next_states(state)

        print(f"VISITED {state} | JUG A: {state[0]}L, JUG B: {state[1]}L".upper())

        if state == goal:
            print("\nGOAL STATE REACHED!".upper())
            return path + [state], graph

        for next_state in get_next_states(state):
            if is_valid(next_state) and next_state not in visited:
                queue.append((next_state, path + [state]))
                print(f"  ↳ TRANSITION TO {next_state} | RULE: {get_rule(state, next_state)}".upper())

    return None, graph

# FUNCTION TO DESCRIBE THE TRANSITION RULE
def get_rule(state, next_state):
    a1, b1 = state
    a2, b2 = next_state
    if a1 != a2 and b1 == b2:
        if a2 == 0:
            return "EMPTY JUG A"
        elif a2 == JUG_A:
            return "FILL JUG A"
    elif b1 != b2 and a1 == a2:
        if b2 == 0:
            return "EMPTY JUG B"
        elif b2 == JUG_B:
            return "FILL JUG B"
    elif a1 > a2 and b1 < b2:
        return "POUR A TO B"
    elif b1 > b2 and a1 < a2:
        return "POUR B TO A"
    return "UNKNOWN"

# MAIN FUNCTION
def main():
    print("--- WATER JUG PROBLEM USING BFS TRAVERSAL ---\n".upper())
    path, graph = bfs((0, 0), GOAL)

    if path:
        print("\nSHORTEST PATH:".upper())
        for state in path:
            print(f"  - {state} | JUG A: {state[0]}L, JUG B: {state[1]}L".upper())
    else:
        print("NO SOLUTION FOUND.".upper())

    print("\n--- GRAPH (KEY-VALUE PAIRS) ---".upper())
    for k, v in graph.items():
        print(f"{k} → {v}".upper())

# RUNNING MAIN
if __name__ == "__main__":
    main()
