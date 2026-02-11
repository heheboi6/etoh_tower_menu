class Structure:
    __DIFFICULTY_ASSOCIATION = {1 : "Easy", 2 : "Medium", 3 : "Hard", 4 : "Difficult", 5 : "Challenging", 6 : "Intense", 7 : "Remorseless", 8 : "Insane", 9 : "Extreme", 10 : "Terrifying", 11 : "Catastrophic", 12 : "Horrific", 13 : "Unreal", 14 : "Gingerbread", 15 : "Eternal", 16 : "Eschaton",17 : "Sisyphean"}
    __DIFFICULTY_FLAVORS = ("Bottom","Bottom-Low","Low","Low-Mid","Mid","Mid-High","High","High-Peak","Peak")
    def __init__(self, name : str, area : str, difficulty : float, tower_type : str):
        self.__name = name
        self.__area = area
        self.__difficulty = difficulty
        self.__tower_type = tower_type
    def __str__(self):
        return self.__name + ", from "  + self.__area + ", with the difficulty " + self.get_real_difficulty() + "(" + str(self.get_difficulty()) + ")"
    def __eq__(self, other):
        if type(other) != Structure:
            return False
        return self.get_name() == other.get_name() and self.get_area() == other.get_area()
    def get_name(self) -> str:
        return self.__name
    def get_area(self) -> str:
        return self.__area
    def get_difficulty(self) -> float:
        return self.__difficulty
    def get_tower_type(self) -> str:
        return self.__tower_type
    def get_real_difficulty(self) -> str:
        if int(self.__difficulty) == 17:
            return f"{self.__DIFFICULTY_ASSOCIATION[int(self.get_difficulty())]}"
        if int(self.get_difficulty()) == self.get_difficulty():
            return f"Baseline {self.__DIFFICULTY_ASSOCIATION[int(self.get_difficulty())]}"
        else:
            flavor_difficulty = int((self.__difficulty - int(self.get_difficulty()) - 0.01) // 0.11)
            return f"{self.__DIFFICULTY_FLAVORS[flavor_difficulty]} {self.__DIFFICULTY_ASSOCIATION[int(self.get_difficulty())]}"
    def get_acronym(self) -> str:
        acronym = ""
        true_name = self.get_name()
        if "100M" in self.get_name():
            acronym += "100M"
            true_name = self.get_name().replace("100M ", "")
        acronym_char = True
        for character in true_name:
            if acronym_char:
                acronym += character
                acronym_char = False
            elif character == " " or character == "-":
                acronym_char = True
            elif character == "(" or character == ")":
                acronym_char = True
                acronym += character
            elif character.isdigit():
                acronym += character
        return acronym