def math_round():
    score = 0
    print("Math")
    user_choice = int(input("How many sides does a hexagon have? "))
    if user_choice == 6:
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")
    user_choice = int(input("What is 2^4? "))
    if user_choice == 16:
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")

    return score