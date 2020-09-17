"""
Prac_06 - Daniel Keppie
Guitars
"""

from prac_06.guitar import Guitar


def main():
    guitars = []
    name = "default"
    while name != "":
        name = input("Name:")
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40)) # Test inputs
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Strat", 2014, 765.4))
    for i, guitar in enumerate(guitars):
        vintage_string = " (vintage)" if guitar.is_vintage() is True else ""
        print("Guitar {}: {:>02} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


main()
