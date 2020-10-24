def sports_round():
    score = 0
    print("Sports")
    user_choice = int(
        input("How many points is a touchdown worth in football? "))
    if user_choice == (6):
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")
    user_choice = int(input("How many team participate in the World Cup? "))
    if user_choice == (32):
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")

    return score