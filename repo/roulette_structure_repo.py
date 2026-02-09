from domain.roulette_structure import RouletteStructure
from repo.base_repo import BaseRepo


class RouletteStructureRepo(BaseRepo):
    def __init__(self):
        self.__roulette_structure_list = []
        super().__init__(RouletteStructure, self.__roulette_structure_list)
    def __str__(self):
        string = ""
        for roulette_structure in self.__roulette_structure_list:
            string += str(roulette_structure) + '\n'
        return string