from repo.structure_file_repo import StructureFileRepo
from service.general_use_functions import GeneralUseFunctions
from domain.validator import Validator


class StructureService:
    def __init__(self, structure_repo : StructureFileRepo):
        self.__structure_repo = structure_repo
        self.__useful_functions = GeneralUseFunctions()
        self.__sorting_parameters = ["name",False]
        self.__validator = Validator()
    def show_all_structures(self) -> str:
        return str(self.__structure_repo)
    def sort_by_parameter(self) -> None:
        key = self.__sorting_parameters[0]
        reverse = self.__sorting_parameters[1]
        actual_key = eval(f"lambda x:x.get_{key}()")
        self.__useful_functions.true_merge_sort(self.__structure_repo.get_list(),key=actual_key,reverse=reverse)
    def set_sorting_parameters(self, new_key : str, new_reverse : str) -> None:
        parameters = self.__validator.validate_sorting_parameters(new_key, new_reverse)
        self.__sorting_parameters = parameters
    def show_sorting_parameters(self) -> str:
        if self.__sorting_parameters[1] == False:
            return f"The current sorting will be made using the {self.__sorting_parameters[0]} of the structure, in normal order."
        else:
            return f"The current sorting will be made using the {self.__sorting_parameters[0]} of the structure, in reverse order."