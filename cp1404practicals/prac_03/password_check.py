MINLENGTH = 5

def main():
    number_of_stars = get_password()
    method_name(number_of_stars)


def method_name(stars):
    """Print stars"""
    print(len(stars) * "*")


def get_password():
    """Get a password over a defined length"""
    password = input("Please input a password: ")
    if len(password) < 5:
        print("The password must be at least {} characters long.".format(MINLENGTH))
        password = input("Please input a password: ")
    return password


main()