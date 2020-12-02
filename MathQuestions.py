def math_round():
    """Description: Calculates all points in the math round
    _author_Eryck Castillo
    :return score for math round
    :rtype int
    """
    score = 0
    print("Math")
    try:
        user_choice = int(input("What is the remainder of 3/5? "))
        if user_choice == 3 % 5:  # Modulus operator just gives the remainder.
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    except ValueError:
        print("Incorrect, I was expecting a number")
    try:
        user_choice = int(input("What is (2^4)-5? "))
        if user_choice == (2 ** 4) - 5:  # Numeric operator that means to
            # the power of so we read 2 to the power of 4 and we are
            # subtracting that by 5.
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    except ValueError:
        print("Incorrect, I was expecting a number")

    return score
