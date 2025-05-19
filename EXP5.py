def print_board(positions):
    board = [["." for _ in range(4)] for _ in range(4)]
    for index, (i, j) in enumerate(positions):
        board[i][j] = f"Q{index+1}"
    print("\nCURRENT BOARD:")
    print("    1   2   3   4")
    for row_index, row in enumerate(board):
        print(f"{row_index + 1} ", " ".join(f"{cell:>3}" for cell in row))
    print()

def is_conflict(new_i, new_j, positions):
    for existing_i, existing_j in positions:
        if new_i == existing_i:
            return "CONFLICT: SAME ROW!"
        if new_j == existing_j:
            return "CONFLICT: SAME COLUMN!"
        if abs(new_i - existing_i) == abs(new_j - existing_j):
            return "CONFLICT: SAME DIAGONAL!"
    return None

def is_safe(i, j, placed):
    for pi, pj in placed:
        if pi == i or pj == j or abs(pi - i) == abs(pj - j):
            return False
    return True

def try_place(placed):
    if len(placed) == 4:
        return True
    for i in range(4):
        for j in range(4):
            if (i, j) not in placed and is_safe(i, j, placed):
                if try_place(placed + [(i, j)]):
                    return True
    return False

def is_still_solvable(positions):
    return try_place(positions)

def ask_replay():
    response = input("DO YOU WANT TO PLAY AGAIN? (YES/NO): ").strip().lower()
    return response == "yes"

def play_game():
    while True:
        positions = []
        step_counter = 4
        print("\nSTARTING NEW GAME: 4 QUEENS PROBLEM")
        print_board(positions)

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
                positions.append((i, j))
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