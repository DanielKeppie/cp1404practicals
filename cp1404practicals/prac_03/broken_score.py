"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

def main():
    score = get_valid_score()
    grade = calculate_result(score)
    print("With our score of {} you have received a {} ".format(score, grade))


def calculate_result(score):
    if score > 90:  # Ordered them properly
        print("excellent mark")
    elif score > 50:
        return("pass")
    else:
        return("fail")


def get_valid_score():
    score = int(input("What was your score? "))
    while score < 0 or score > 100:  # Changed to while loop, added or > 100.
        print("Invalid score")
        score = float(input("Enter score: "))  # Added an escape to the while loop
    return score


main()