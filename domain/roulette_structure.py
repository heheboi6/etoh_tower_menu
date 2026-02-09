from domain.structure import Structure


class RouletteStructure(Structure):
    def __init__(self, name : str, area : str, *, times_beaten = 0, beat_limit = 1):
        super().__init__(name,area)
        self.__times_beaten = times_beaten
        self.__beat_limit = beat_limit
        if times_beaten >= beat_limit:
            self.__eliminated = True
        else:
            self.__eliminated = False
    def __str__(self):
        str_return = f"{self.get_name()}, from {self.get_area()}"
        if self.__eliminated:
            str_return += ", you have beaten this tower enough so that it can be eliminated from the roulette."
            return str_return
        if self.__times_beaten == 0:
            str_return += ", you didn't beat this tower yet"
        elif self.__times_beaten == 1:
            str_return += ", you beat this tower once"
        else:
            str_return += f", you beat this tower {self.__times_beaten} times"
        if self.__beat_limit == 1:
            str_return += ", and you need to beat it once to eliminate it."
        else:
            str_return += f", and you need to beat it {self.__beat_limit} times to eliminate it."
        return str_return
    def beat_structure(self) -> None:
        self.__times_beaten += 1
        if self.__times_beaten >= self.__beat_limit:
            self.__eliminated = True
    def get_eliminated(self) -> bool:
        return self.__eliminated