"""
CP1404 Practical
Silver Service Taxi class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    fare_charge = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = float(fanciness)
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.fare_charge

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{} plus flagfall of ${}".format(super().__str__(), self.fare_charge)
