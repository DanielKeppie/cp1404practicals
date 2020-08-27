"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            temperature = convert_celsius()
            print("Result: {:.2f} F".format(temperature))
        elif choice == "F":
            temperature = convert_fahrenheit()
            print("Result: {:.2f} C".format(temperature))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    temp = (fahrenheit - 32) * (5 / 9)
    return temp


def convert_celsius():
    celsius = float(input("Celsius: "))
    temp = celsius * 9.0 / 5 + 32
    return temp


main()