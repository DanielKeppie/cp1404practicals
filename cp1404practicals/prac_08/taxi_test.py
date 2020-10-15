"""
CP1404 - Daniel Keppie
"""

from prac_08.taxi import Taxi


def main():
    prius = Taxi("Prius 1", 100)
    prius.drive(40)
    print("{}, (${})".format(prius.__str__(), prius.get_fare()))
    prius.start_fare()
    prius.drive(100)
    print("{}, (${})".format(prius.__str__(), prius.get_fare()))


main()
