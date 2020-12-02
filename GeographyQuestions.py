def geography_round():
    """Description: Calculates all points in the geography round
    _author_Eryck Castillo
    :return score for geography round
    :rtype int and string
     """
    score = 0
    print("Geography")
    try:
        user_choice = int(input("How many countries are there in the world? "))
        if user_choice == 195:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    except ValueError:
        print("Incorrect, I was expecting a number")
    try:
        user_choice = (
            input("After Brazil what is the largest country in South America? "
                  ))
        if user_choice == "Argentina" or "argentina":  # I am using the or just
            # in case someone puts the right answer but forgets that it
            # needs to be capitalized. The answer is correct but the or just
            # means that it will take in the capitalized or the non
            # capitalized.
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    except ValueError:
        print("Incorrect, I was expecting a string")

    return score
