"""
Loops.py
"""

# for i in range(1, 21, 2):
#     print(i, end=" ")
# print()

# a.
# for i in range(0, 110, 10):
#     print(i, end=" ")
# print()

# b.
# for i in range(20, 0, -1):
#     print(i, end=" ")
# print()

# c.
# number_of_stars = int(input("Number of stars: "))
# stars = "*"
# print(stars*number_of_stars)

# d.
number_of_stars = int(input("Number of stars: "))
stars = "*"
while number_of_stars <= 0:
    number_of_stars = int(input("What is that!? \nNumber of stars: "))
for i in range(1, number_of_stars + 1):
    print(stars*i)