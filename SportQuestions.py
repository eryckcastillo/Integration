def sports_round():
    """Description: Calculates all points in the sports round
    _author_Eryck Castillo
    :return score for sports round
    :rtype int
    """
    score = 0
    print("Sports")
    try:
        user_choice = int(
            input("How many points is a touchdown worth in football? "))
        if user_choice == 6:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    except ValueError:
        print("Incorrect, I was expecting a number")
    try:
        user_choice = int(input("How many team participate in the World Cup? "
                                ))
        if user_choice == 32:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    except ValueError:
        print("Incorrect, I was expecting a number")

    return score
