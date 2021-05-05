"""Programming Languages class"""


class ProgrammingLanguage:
    """Intialise a language instance"""

    def __init__(self, name, reflection, typing, year):
        self.name = name
        self.reflection = reflection
        self.typing = typing
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.reflection, self.typing, self.year)


