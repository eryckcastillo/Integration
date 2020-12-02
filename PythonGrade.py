def calculate_grade(score):
    """Description: Calculates grade out of 6 and converts to a letter grade
    _author_Eryck Castillo
    :parameter score the user has at the end of the game
    :return overall grade
    :rtype String
    """

    percent_score = score / 6  # This is a division with the score which is
    # your score out of 6 then divided by 6 to get the percent. I could also
    # substitute this for a floor division which is // to round to the
    # nearest whole number.
    total_percent = percent_score * 100  # This is another numeric operator
    # that is just saying that whatever percent score is and that * 100 to
    # get the percent score.
    if 100 >= total_percent >= 90:  # This is a logical
        # operator that is just showing how to use it and i know that you
        # can chain them together but just to use it i am using it here.
        # What this is doing is just making sure two conditions are met.
        grade = "A"
    elif total_percent >= 80:
        grade = "B"
    elif total_percent >= 70:
        grade = "C"
    elif total_percent >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade
