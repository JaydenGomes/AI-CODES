left_m = 3
left_c = 3
right_m = 0
right_c = 0
boat = 'left'
moves_left = 15

def is_valid(m_left, c_left, m_right, c_right):
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0):
        return False
    if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
        return False
    return True

def print_state():
    print("\n-----------------------------------------")
    print(f"LEFT SIDE:  {left_m} MISSIONARIES, {left_c} CANNIBALS")
    print(f"RIGHT SIDE: {right_m} MISSIONARIES, {right_c} CANNIBALS")
    print(f"BOAT IS ON THE {'LEFT' if boat == 'left' else 'RIGHT'} SIDE")
    print(f"MOVES LEFT: {moves_left}")
    print("-----------------------------------------")

def move(m, c):
    global left_m, left_c, right_m, right_c, boat

    if m + c > 2 or m + c == 0:
        print("YOU CAN ONLY MOVE 1 OR 2 PEOPLE.")
        return False

    if boat == 'left':
        if left_m < m or left_c < c:
            print("NOT ENOUGH PEOPLE ON THE LEFT TO MAKE THIS MOVE.")
            return False
        left_m -= m
        left_c -= c
        right_m += m
        right_c += c
        boat = 'right'
    else:
        if right_m < m or right_c < c:
            print("NOT ENOUGH PEOPLE ON THE RIGHT TO MAKE THIS MOVE.")
            return False
        right_m -= m
        right_c -= c
        left_m += m
        left_c += c
        boat = 'left'

    if not is_valid(left_m, left_c, right_m, right_c):
        print("OH NO! THE MISSIONARIES GOT EATEN!")
        return "lose"

    return True

print("---------- RIVER CROSSING GAME ----------")
while moves_left > 0:
    print_state()

    if right_m == 3 and right_c == 3:
        print("\n🎉 CONGRATULATIONS! YOU GOT EVERYONE ACROSS SAFELY!")
        break

    print("\nCHOOSE YOUR MOVE:")
    print("1. MOVE 1 MISSIONARY AND 1 CANNIBAL")
    print("2. MOVE 2 MISSIONARIES")
    print("3. MOVE 2 CANNIBALS")
    print("4. MOVE 1 MISSIONARY")
    print("5. MOVE 1 CANNIBAL")

    choice = input("---> ENTER YOUR CHOICE (1-5): ")

    if choice == '1':
        result = move(1, 1)
    elif choice == '2':
        result = move(2, 0)
    elif choice == '3':
        result = move(0, 2)
    elif choice == '4':
        result = move(1, 0)
    elif choice == '5':
        result = move(0, 1)
    else:
        print("INVALID CHOICE.")
        continue

    if result == "lose":
        print("\n💀 GAME OVER! YOU LOST.")
        break
    elif result:
        moves_left -= 1

else:
    print("\n OUT OF MOVES! YOU FAILED TO SOLVE THE PUZZLE.")
