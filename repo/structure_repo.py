from domain.structure import Structure
from repo.base_repo import BaseRepo
class StructureNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)
class StructureRepo(BaseRepo):
    def __init__(self):
        self.__structure_list = []
        super().__init__(Structure, self.__structure_list)
    def __str__(self):
        string = ""
        for structure in self.__structure_list:
            string += str(structure) + '\n'
        return string
    def search_by_acronym(self, acronym : str) -> Structure:
        for structure in self.__structure_list:
            if structure.get_acronym() == acronym:
                return structure
        raise StructureNotFoundException("The structure with this acronym was not found!")
    def find_roulette_structure_by_name(self, name : str):
        for structure in self.__structure_list:
            if structure.get_name() == name:
                return structure
        return None