from domain.structure import Structure
from repo.base_repo import BaseRepo
class StructureRepo(BaseRepo):
    def __init__(self):
        self.__structure_list = []
        super().__init__(Structure, self.__structure_list)
    def __str__(self):
        string = ""
        for structure in self.__structure_list:
            string += str(structure) + '\n'
        return string