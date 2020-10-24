def calculate_grade(score):
    percent_score = score / 6
    total_percent = percent_score * 100
    if total_percent >= 90:
        grade = ("A")
    elif total_percent >= 80:
        grade = ("B")
    elif total_percent >= 70:
        grade = ("C")
    elif total_percent >= 60:
        grade = ("D")
    else:
        grade = ("F")

    return grade