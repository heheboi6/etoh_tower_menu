from domain.roulette_structure import RouletteStructure
from repo.base_repo import BaseRepo
from repo.structure_repo import StructureNotFoundException


class RouletteStructureRepo(BaseRepo):
    def __init__(self):
        self.__roulette_structure_list = []
        super().__init__(RouletteStructure, self.__roulette_structure_list)
    def __str__(self):
        string = ""
        for roulette_structure in self.__roulette_structure_list:
            string += str(roulette_structure) + '\n'
        return string
    def find_roulette_structure_by_acronym(self, acronym : str) -> RouletteStructure:
        for roulette_structure in self.__roulette_structure_list:
            if roulette_structure.get_acronym() == acronym:
                return roulette_structure
        raise StructureNotFoundException("The structure with this acronym does not exist in the roulette!")