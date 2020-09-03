import random

POSSIBLE_NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                    27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]


def main():
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        usable_numbers = POSSIBLE_NUMBERS
        quick_pick = get_quick_pick(usable_numbers)
        print_quick_pick(quick_pick)


def print_quick_pick(quick_pick):
    for number in quick_pick:
        print("{:2}".format(number), end=" ")
    print("")


def get_quick_pick(usable_numbers):
    temp_list = []
    for j in range(6):
        chosen_number = random.randint(0, len(usable_numbers) - 1)
        temp_list.append(usable_numbers.pop(chosen_number))
    return temp_list


main()
