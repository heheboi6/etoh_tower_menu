from domain.structure import Structure
from repo.structure_file_repo import StructureFileRepo
from service.general_use_functions import GeneralUseFunctions


class StructureService:
    def __init__(self, structure_repo : StructureFileRepo):
        self.__structure_repo = structure_repo
        self.__useful_functions = GeneralUseFunctions()
    def show_all_structures(self) -> list[Structure]:
        return self.__structure_repo.get_list()
    def sort_by_parameter(self, *, key = "name", reverse = False):
        actual_key = eval(f"lambda x:x.get_{key}()")
        self.__useful_functions.true_merge_sort(self.__structure_repo.get_list(),key=actual_key,reverse=reverse)
        return self.show_all_structures()