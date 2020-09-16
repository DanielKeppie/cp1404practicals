"""
Prac_06 - Daniel Keppie
Programming Language
"""


class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=True, year=1900):
        """Initialise ProgrammingLanguage"""
        self.name = name.title()
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.reflection, self.year )
