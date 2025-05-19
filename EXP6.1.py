def display_jugs(jug_a, jug_b):
    print("\n" + "=" * 45)
    print("         W A T E R   J U G   P R O G R A M")
    print("=" * 45)
    print("")

    # Jug visual display
    jug_a_display = f"JUG A: [{jug_a}/4] " + "|" * jug_a + " " * (4 - jug_a)
    jug_b_display = f"JUG B: [{jug_b}/3] " + "|" * jug_b + " " * (3 - jug_b)
    print(f"{jug_a_display:<25} {jug_b_display}")



def menu():
    print("CHOOSE AN ACTION:")
    print("1. FILL JUG A")
    print("2. FILL JUG B")
    print("3. EMPTY JUG A")
    print("4. EMPTY JUG B")
    print("5. POUR JUG A → JUG B")
    print("6. POUR JUG B → JUG A")
    print("7. EXIT")


def play_game():
    jug_a = 0
    jug_b = 0
    goal = 2
    min_steps = 6
    steps_remaining = min_steps

    print("== WATER JUG PROBLEM ==")
    print("GOAL: GET EXACTLY 2 LITERS IN JUG A OR JUG B USING A 4L JUG A AND 3L JUG B.\n")
    display_jugs(jug_a, jug_b)

    while steps_remaining > 0:
        menu()
        print(f"STEPS REMAINING: {steps_remaining}")
        choice = input("ENTER YOUR CHOICE (1-7): ")

        if choice == '1':
            if jug_a == 4:
                print("JUG A IS ALREADY FULL!")
            else:
                jug_a = 4

        elif choice == '2':
            if jug_b == 3:
                print("JUG B IS ALREADY FULL!")
            else:
                jug_b = 3

        elif choice == '3':
            if jug_a == 0:
                print("JUG A IS ALREADY EMPTY!")
            else:
                jug_a = 0

        elif choice == '4':
            if jug_b == 0:
                print("JUG B IS ALREADY EMPTY!")
            else:
                jug_b = 0

        elif choice == '5':
            if jug_a == 0:
                print("JUG A IS EMPTY! NOTHING TO POUR.")
            elif jug_b == 3:
                print("JUG B IS ALREADY FULL! CAN'T POUR INTO IT.")
            else:
                transfer = min(jug_a, 3 - jug_b)
                jug_a -= transfer
                jug_b += transfer

        elif choice == '6':
            if jug_b == 0:
                print("JUG B IS EMPTY! NOTHING TO POUR.")
            elif jug_a == 4:
                print("JUG A IS ALREADY FULL! CAN'T POUR INTO IT.")
            else:
                transfer = min(jug_b, 4 - jug_a)
                jug_b -= transfer
                jug_a += transfer

        elif choice == '7':
            print("EXITING GAME. GOODBYE!")
            return

        else:
            print("INVALID CHOICE. PLEASE ENTER 1-7.")

        steps_remaining -= 1

        display_jugs(jug_a, jug_b)

        if jug_a == goal or jug_b == goal:
            print("CONGRATULATIONS! YOU REACHED THE GOAL STATE.")
            return

    print("OUT OF STEPS! YOU COULDN'T REACH THE GOAL IN 6 MOVES.")
    choice = input("DO YOU WANT TO TRY AGAIN? (Y/N): ").lower()
    if choice == 'y':
        play_game()
    else:
        print("THANKS FOR PLAYING!")


# START THE GAME
play_game()
