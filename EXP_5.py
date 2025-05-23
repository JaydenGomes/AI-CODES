# Function to print the current board with positions of queens
def print_board(positions):
    board = [["." for _ in range(4)] for _ in range(4)]  # Create a 4x4 empty board
    for index, (i, j) in enumerate(positions):           # Place each queen on the board
        board[i][j] = f"Q{index+1}"                      # Label queens as Q1, Q2, ...
    print("\nCURRENT BOARD:")
    print("    1   2   3   4")                           # Column headers
    for row_index, row in enumerate(board):              # Row-wise print
        print(f"{row_index + 1} ", " ".join(f"{cell:>3}" for cell in row))
    print()

# Function to check for conflicts with already placed queens
def is_conflict(new_i, new_j, positions):
    for existing_i, existing_j in positions:
        if new_i == existing_i:
            return "CONFLICT: SAME ROW!"
        if new_j == existing_j:
            return "CONFLICT: SAME COLUMN!"
        if abs(new_i - existing_i) == abs(new_j - existing_j):
            return "CONFLICT: SAME DIAGONAL!"
    return None  # No conflict

# Helper function to check if placing queen at (i, j) is safe
def is_safe(i, j, placed):
    for pi, pj in placed:
        if pi == i or pj == j or abs(pi - i) == abs(pj - j):
            return False
    return True

# Recursive function to check if it's still possible to place all 4 queens
def try_place(placed):
    if len(placed) == 4:
        return True
    for i in range(4):
        for j in range(4):
            if (i, j) not in placed and is_safe(i, j, placed):
                if try_place(placed + [(i, j)]):  # Try placing a queen and go deeper
                    return True
    return False

# Wrapper function to check if solution is still solvable from current state
def is_still_solvable(positions):
    return try_place(positions)

# Asks user if they want to replay the game
def ask_replay():
    response = input("DO YOU WANT TO PLAY AGAIN? (YES/NO): ").strip().lower()
    return response == "yes"

# Main game loop
def play_game():
    while True:
        positions = []           # List to store placed queen positions
        step_counter = 4         # Max 4 steps allowed
        print("\nSTARTING NEW GAME: 4 QUEENS PROBLEM")
        print_board(positions)   # Show empty board

        while step_counter > 0 and len(positions) < 4:
            print(f"STEPS REMAINING: {step_counter}")
            try:
                i = int(input("ENTER ROW (1–4): ")) - 1
                j = int(input("ENTER COLUMN (1–4): ")) - 1
            except ValueError:
                print("INVALID INPUT! PLEASE ENTER NUMERIC VALUES FROM 1 TO 4.")
                continue

            if not (0 <= i <= 3 and 0 <= j <= 3):
                print("VALUES OUT OF RANGE! PLEASE ENTER NUMBERS FROM 1 TO 4.")
                continue

            conflict = is_conflict(i, j, positions)
            step_counter -= 1

            if conflict:
                print(conflict)
                print("GAME OVER! YOU VIOLATED A CONSTRAINT.")
                print_board(positions)
                if ask_replay():
                    break
                else:
                    print("THANKS FOR PLAYING!")
                    return
            else:
                positions.append((i, j))  # Add valid queen position
                print_board(positions)

                if not is_still_solvable(positions):
                    print("NO VALID MOVES LEFT — A SOLUTION IS NO LONGER POSSIBLE FROM THIS STATE.")
                    print("GAME OVER.")
                    print_board(positions)
                    if ask_replay():
                        break
                    else:
                        print("THANKS FOR PLAYING!")
                        return

        if len(positions) == 4:
            print("CONGRATULATIONS! YOU PLACED ALL 4 QUEENS CORRECTLY.")
            if not ask_replay():
                print("THANKS FOR PLAYING!")
                break
        elif step_counter == 0:
            print("OUT OF STEPS! GAME OVER.")
            print_board(positions)
            if not ask_replay():
                print("THANKS FOR PLAYING!")
                break

# START THE GAME
play_game()
