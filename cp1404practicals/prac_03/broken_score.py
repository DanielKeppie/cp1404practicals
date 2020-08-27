"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
import random


def main():
    score = get_valid_score() #or score = random_score()
    statement = calculate_result(score)
    print(statement.format(score))


def calculate_result(score):
    if score > 90:  # Ordered them properly
        return("With your score of {} you have received an excellent grade")
    elif score > 50:
        return("With your score of {} you have received a pass ")
    else:
        return("With our score of {} you have failed")


def get_valid_score():
    score = int(input("What was your score? "))
    while score < 0 or score > 100:  # Changed to while loop, added or > 100.
        print("Invalid score")
        score = float(input("Enter score: "))  # Added an escape to the while loop
    return score


def random_score():
    rand_score = random.randint(0,100)
    return rand_score


main()