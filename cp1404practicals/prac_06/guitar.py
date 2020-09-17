"""
Prac_06 - Daniel Keppie
Guitar
"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name.title()
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.cost, self.year)

    def get_age(self):
        current_year = 2020
        age = current_year - self.year
        return age

    def is_vintage(self):
        vintage = True if self.get_age() >= 50 else False
        return vintage