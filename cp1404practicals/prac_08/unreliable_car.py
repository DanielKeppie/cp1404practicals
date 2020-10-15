"""
CP1404/CP5632 Practical
Unreliable Car class
"""

from prac_08.car import Car
import random


class UnreliableCar(Car):
    """an unreliable brand of car"""

    def __init__(self, name, fuel, reliability):
        super().__init__(self, name)
        self.reliability = reliability
        self.fuel = fuel
        self.name = name

    def drive(self, distance):
        if random.randint(1, 100) < int(self.reliability):
            # Only drives if random number is above the reliability
            return super().drive(distance)
        else:
            return super().drive(0)

    def __str__(self):
        """Return a string representation of a Car object."""
        return ""

