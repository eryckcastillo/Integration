# Eryck Castillo My integration project This is a little Trivia Game i made
# that includes all of the concepts we have learned so far.
from GeographyQuestions import geography_round
from MathQuestions import math_round
from PythonGrade import calculate_grade
from SportQuestions import sports_round
"""Description: The program that adds all the categories of questions and 
gives final grade 
_author_Eryck Castillo """
print("Welcome to my", end=" ")  # The end = is just saying that at the end of
print("Integration Project")  # statement then it will add the next print.
print("Trivia Game")

user_wants_to_quit = False
while not user_wants_to_quit:
    print("There will be 3 categories of questions.")
    print("1st Math")
    print("2", "Sports", sep="nd ")  # The sep= is just saying lets put a ",
    # " and then replace it with a what is in the "" in the sep=.
    print("3rd Geography")

    # I set the score = 0 so later in the if else statement then it adds 1
    score = 0
    user_choice = (input("Type start to continue: "))
    if user_choice == "start":
        for x in range(1, 4):
            if x == 1:
                score += math_round()
            elif x == 2:
                score += sports_round()
            else:
                score += geography_round()
    else:
        exit()

    print("Your score was %d out of 6." % score)
    grade = calculate_grade(score)
    print("Your grade is a", grade)
    decision = input("Do you want to try again? " + "Type Y for yes")
    # This is just a demonstration of a + as a string this is just connecting
    # two "".
    if decision != "Y":
        user_wants_to_quit = True
