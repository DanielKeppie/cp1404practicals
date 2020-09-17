"""
Prac_06 - Daniel Keppie
Guitar Test
"""

from prac_06.guitar import Guitar

Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
Another = Guitar("Bad Guitar", 2019, 10)
print("{}, age = {}, expected {}".format(Another.name,
                                         Another.get_age(), 1))
print("{}, age = {}, expected {}".format(Gibson.name,
                                         Gibson.get_age(), 98))
print("{}, vintage = {}, expected {}".format(Another.name,
                                             Another.is_vintage(), False))
print("{}, vintage = {}, expected {}".format(Gibson.name,
                                             Gibson.is_vintage(), True))
