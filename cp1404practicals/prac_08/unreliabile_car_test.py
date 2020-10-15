"""
CP1404 - Daniel Keppie
Unreliable Car Test
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    bad_car = UnreliableCar("Bucket", 100, 5)
    good_car = UnreliableCar("Swell", 100, 95)
    for i in range(1, 10):
        print("{} drove {}km".format(bad_car.name, bad_car.drive(i)))
        print("{} drove {}km".format(good_car.name, good_car.drive(i)))


main()
