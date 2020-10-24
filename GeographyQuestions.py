def geography_round():
    score = 0
    print("Geography")
    user_choice = int(input("How many countries are there in the world? "))
    if user_choice == (195):
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")
    user_choice = (
        input("After Brazil what is the largest country in South America? "))
    if user_choice == ("Argentina"):
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")

    return score