# Eryck Castillo
# My integration project
#This is a little Trivia Game and at the end just a demonation that i know
#how to use the numeric operators. I did not show all of them but the concept is
#still there all the same but just different symbols.
from GeographyQuestions import geography_round
from MathQuestions import math_round
from PythonGrade import calculate_grade
from SportQuestions import sports_round

print("Welcome to my Integration Project")
print("Trivia Game")

user_wants_to_quit = False
while not user_wants_to_quit:
    print("There will be 3 categories of questions.")
    print("1st Math")
    print("2nd Sports")
    print("3rd Geography")

    #I set the score = 0 so later in the if else statement then it adds 1
    score = 0
    user_choice = (input("Type start to continue: "))
    #Simple if else statement that if the input is start then it prints something
    #if not then it prints the else statement
    if user_choice == ("start"):
        for x in range(1,4):
            if x == 1:
                score += math_round()
            elif x == 2:
                score += sports_round()
            else:
                score += geography_round()
    else:
        exit()

    print("Your score was %d out of 6." %(score))
    grade = calculate_grade(score)
    print("Your grade is a", grade)
    decision = input("Do you want to try again? Type Y for yes")
    if decision != "Y":
        user_wants_to_quit = True

