class Structure:
    def __init__(self, name : str, area : str):
        self.__name = name
        self.__area = area
    def __str__(self):
        return self.__name + ", from "  + self.__area
    def __eq__(self, other):
        if type(other) != Structure:
            return False
        return self.get_name() == other.get_name() and self.get_area() == other.get_area()
    def get_name(self) -> str:
        return self.__name
    def get_area(self) -> str:
        return self.__area
    def get_acronym(self) -> str:
        words = self.get_name().split()
        acronym = ""
        for word in words:
            acronym += word[0]
        return acronym