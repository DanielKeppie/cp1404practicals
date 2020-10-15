"""
CP1404 - Daniel Keppie
Silver Service Taxi test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)
    print(hummer.__str__()+", with a total fare of ${}0".format(hummer.get_fare()))


main()
