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
        self.__tower_rush_mode = "from start"
        self.__include_pomtr = True
    def load_from_file(self):
        if self.__file_name == "":
            raise CorruptedFileException("This file does not exist!")
        super().__init__()
        with open(self.__file_name, "r") as file:
            total_data = file.readlines()
            for index in range(len(total_data)-2):
                line = total_data[index]
                data = line.split(" ")
                try:
                    acronym = data[0]
                    beat_data = data[1].split("/")
                    beat_count = int(beat_data[0])
                    beat_limit = int(beat_data[1])
                    acronym_structure = self.__structure_repo.search_by_acronym(acronym)
                    new_structure = RouletteStructure(acronym_structure.get_name(),acronym_structure.get_area(),acronym_structure.get_difficulty(),acronym_structure.get_tower_type(),times_beaten=beat_count,beat_limit=beat_limit)
                    self.add_element(new_structure)
                except (IndexError, ValueError, StructureNotFoundException, InvalidDataException):
                    raise CorruptedFileException("The file does not contain correct or complete structure data!")
            last_acronym = total_data[-2].replace("\n","")
            if last_acronym == "@":
                self.__last_structure = None
            else:
                self.__last_structure = self.find_roulette_structure_by_acronym(last_acronym)
            tower_rush_info = total_data[-1].split(" ")
            if tower_rush_info[0] == "none":
                self.__tower_rush_mode = "none"
            else:
                self.__tower_rush_mode = tower_rush_info[0]
                if tower_rush_info[1] == "True":
                    self.__include_pomtr = True
                else:
                    self.__include_pomtr = False
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
                file.write(self.__last_structure.get_acronym() + "\n")
            else:
                file.write("@\n")
            tower_rush_str = self.__tower_rush_mode
            if tower_rush_str != "none":
                tower_rush_str += " " + str(self.__include_pomtr)
            file.write(tower_rush_str)
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
    def get_tower_rush_mode(self) -> str:
        return self.__tower_rush_mode
    def set_tower_rush_mode(self, tower_rush_mode : str):
        self.__tower_rush_mode = tower_rush_mode
    def get_include_pomtr(self) -> bool:
        return self.__include_pomtr
    def set_include_pomtr(self, include_pomtr : bool):
        self.__include_pomtr = include_pomtr