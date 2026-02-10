from domain.roulette_structure import RouletteStructure
from repo.base_repo import InvalidDataException
from repo.roulette_structure_repo import RouletteStructureRepo
from repo.structure_file_repo import CorruptedFileException, StructureFileRepo
from repo.structure_repo import StructureNotFoundException


class RouletteStructureFileRepo(RouletteStructureRepo):
    def __init__(self, structure_repo : StructureFileRepo, *, file_name=""):
        super().__init__()
        self.__file_name = file_name
        self.__structure_repo = structure_repo
        self.__last_structure = None
    def load_from_file(self):
        if self.__file_name == "":
            raise CorruptedFileException("This file does not exist!")
        super().__init__()
        with open(self.__file_name, "r") as file:
            total_data = file.readlines()
            for index in range(len(total_data)-1):
                line = total_data[index]
                data = line.split(" ")
                try:
                    acronym = data[0]
                    beat_data = data[1].split("/")
                    beat_count = int(beat_data[0])
                    beat_limit = int(beat_data[1])
                    acronym_structure = self.__structure_repo.search_by_acronym(acronym)
                    new_structure = RouletteStructure(acronym_structure.get_name(),acronym_structure.get_area(),times_beaten=beat_count,beat_limit=beat_limit)
                    self.add_element(new_structure)
                except (IndexError, ValueError, StructureNotFoundException, InvalidDataException):
                    raise CorruptedFileException("The file does not contain correct or complete structure data!")
            last_acronym = total_data[-1]
            if last_acronym == "@":
                self.__last_structure = None
            else:
                self.__last_structure = self.find_roulette_structure_by_acronym(last_acronym)
            file.close()
    def store_into_file(self, *, save_file_name = ""):
        old_file = ""
        if save_file_name != "":
            old_file = self.__file_name
            self.__file_name = save_file_name
        with open(self.__file_name, "w") as file:
            for index in range(len(self)):
                current_roulette_structure = self.get_element_from_position(index)
                file.write(current_roulette_structure.get_acronym() + " " + current_roulette_structure.show_fraction() + "\n")
            if self.__last_structure is not None:
                file.write(self.__last_structure.get_acronym())
            else:
                file.write("@")
            file.close()
        if save_file_name != "":
            self.__file_name = old_file
    def set_last_structure(self, new_structure : RouletteStructure) -> None:
        self.__last_structure = new_structure
    def get_last_structure(self) -> RouletteStructure:
        return self.__last_structure
    def set_file_name(self, file_name : str):
        self.__file_name = file_name
    def get_file_name(self) -> str:
        return self.__file_name