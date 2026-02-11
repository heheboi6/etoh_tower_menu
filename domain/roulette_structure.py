from domain.structure import Structure


class RouletteStructure(Structure):
    def __init__(self, name : str, area : str, difficulty : float, tower_type : str, *, times_beaten = 0, beat_limit = 1):
        super().__init__(name,area,difficulty,tower_type)
        self.__times_beaten = times_beaten
        self.__beat_limit = beat_limit
        if times_beaten >= beat_limit:
            self.__eliminated = True
        else:
            self.__eliminated = False
    def __str__(self):
        str_return = super().__str__()
        if self.__eliminated:
            str_return += f", you have beaten this {self.get_tower_type().lower()} enough so that it can be eliminated from the roulette."
            return str_return
        if self.__times_beaten == 0:
            str_return += f", you didn't beat this {self.get_tower_type().lower()} yet"
        elif self.__times_beaten == 1:
            str_return += f", you beat this {self.get_tower_type().lower()} once"
        else:
            str_return += f", you beat this {self.get_tower_type().lower()} {self.__times_beaten} times"
        if self.__beat_limit == 1:
            str_return += ", and you need to beat it once to eliminate it."
        else:
            str_return += f", and you need to beat it {self.__beat_limit} times to eliminate it."
        return str_return
    def __eq__(self, other):
        if type(other) is not RouletteStructure:
            return False
        return self.get_acronym() == other.get_acronym()
    def beat_structure(self) -> None:
        self.__times_beaten += 1
        if self.__times_beaten >= self.__beat_limit:
            self.__eliminated = True
    def get_eliminated(self) -> bool:
        return self.__eliminated
    def show_fraction(self) -> str:
        return str(self.__times_beaten) + "/" + str(self.__beat_limit)
    def set_beat_limit(self, beat_limit : int):
        self.__beat_limit = beat_limit
        if self.__times_beaten < self.__beat_limit:
            self.__eliminated = False
        else:
            self.__eliminated = True
    def get_beat_limit(self) -> int:
        return self.__beat_limit