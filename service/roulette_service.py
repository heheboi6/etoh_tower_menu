import random

from domain.roulette_structure import RouletteStructure
from domain.validator import Validator
from repo.roulette_structure_file_repo import RouletteStructureFileRepo
from repo.structure_file_repo import StructureFileRepo

class RouletteService:
    def __init__(self, structure_repo : StructureFileRepo):
        self.__structure_repo = structure_repo
        self.__roulette_repo = None
        self.__validator = Validator()
    def create_roulette(self, *, beat_limit=1, file_name=""):
        if file_name != "":
            self.__validator.validate_file_name(file_name)
        self.__validator.validate_pozitive_integer(beat_limit)
        if file_name == "":
            self.__roulette_repo = RouletteStructureFileRepo(self.__structure_repo)
            for index in range(len(self.__structure_repo)):
                current_structure = self.__structure_repo.get_element_from_position(index)
                new_structure = RouletteStructure(current_structure.get_name(),current_structure.get_area(),beat_limit=beat_limit)
                self.__roulette_repo.add_element(new_structure)
        else:
            self.__roulette_repo = RouletteStructureFileRepo(self.__structure_repo,file_name=file_name)
            self.__roulette_repo.load_from_file()
    def save_roulette(self, file_name = ""):
        self.__validator.validate_save_file(file_name)
        if self.__roulette_repo.get_file_name() == "":
            self.__roulette_repo.set_file_name(file_name)
        self.__roulette_repo.store_into_file(save_file_name=file_name)
    def __get_real_roulette_list(self) -> list[RouletteStructure]:
        available_structures = []
        for index in range(len(self.__roulette_repo)):
            current_structure = self.__roulette_repo.get_element_from_position(index)
            if not current_structure.get_eliminated():
                available_structures.append(current_structure)
        return available_structures
    def generate_random_structure(self):
        structure_list = self.__get_real_roulette_list()
        random_structure = random.choice(structure_list)
        self.__roulette_repo.set_last_structure(random_structure)
        if self.__roulette_repo.get_file_name() != "":
            self.__roulette_repo.store_into_file()
        return str(random_structure)
    def beat_current_structure(self) -> bool:
        self.__roulette_repo.get_last_structure().beat_structure()
        eliminated = self.__get_last_eliminated()
        self.__roulette_repo.set_last_structure(None)
        if self.__roulette_repo.get_file_name() != "":
            self.__roulette_repo.store_into_file()
        return eliminated
    def get_last_structure(self) -> RouletteStructure:
        return self.__roulette_repo.get_last_structure()
    def show_roulette(self):
        return str(self.__roulette_repo)
    def get_roulette_total(self) -> list[int|int]:
        total_beaten = 0
        total_structures = 0
        for index in range(len(self.__roulette_repo)):
            current_structure = self.__roulette_repo.get_element_from_position(index)
            fraction = current_structure.show_fraction().split("/")
            total_beaten += int(fraction[0])
            total_structures += int(fraction[1])
        return [total_beaten,total_structures]
    def __get_last_eliminated(self) -> bool:
        return self.get_last_structure().get_eliminated()