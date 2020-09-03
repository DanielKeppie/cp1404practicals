AMOUNT_OF_NUMBERS = 5


def main():
    numbers = get_numbers()
    print(numbers)
    print_outputs(numbers)
    access = validate_user()
    print(access)


def get_numbers():
    """Get a list of numbers from the user"""
    list_of_numbers = []
    for i in range(AMOUNT_OF_NUMBERS):
        number = int(input("Number: "))
        list_of_numbers.append(number)
    return list_of_numbers


def print_outputs(values):
    """Print a variety of outputs based on a numeric list input"""
    print("The first number is {}".format(values[0]))
    print("The last number is {}".format(values[-1]))
    print("The smallest number is {}". format(min(values)))
    print("The largest number is {}".format(max(values)))
    print("The average of the numbers is {}".format(sum(values)/len(values)))


def validate_user():
    """Return if a user has a pre-determined username"""
    valid_usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                       'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                       'bob']
    username = input("Username: ")
    if username in valid_usernames:
        return "Access granted"
    return "Access denied"


main()
