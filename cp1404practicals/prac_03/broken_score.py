"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
while score < 0 or score > 100: # Changed to while loop, added or > 100.
    print("Invalid score")
    score = float(input("Enter score: ")) # Added an escape to the while loop
if score > 90: # Ordered them properly
    print("Your grade is excellent!")
elif score > 50:
    print("Your grade is passable")
else:
    print("You have failed.")
