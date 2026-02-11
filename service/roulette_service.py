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
    @staticmethod
    def __is_tower_rush(structure : RouletteStructure) -> bool:
        if "Tower Rush" in structure.get_name():
            return True
        else:
            return False
    def __eliminate_tower_rushes(self):
        index = 0
        while index < len(self.__roulette_repo):
            current_structure = self.__roulette_repo.get_element_from_position(index)
            if self.__is_tower_rush(current_structure) and self.get_tower_rush_mode() != "from start":
                self.__roulette_repo.remove_element(current_structure)
                index -= 1
            if self.get_tower_rush_mode() == "from start" and current_structure.get_name() == "Pit of Misery Tower Rush" and not self.__get_include_pomtr():
                self.__roulette_repo.remove_element(current_structure)
                index -= 1
            index += 1
    def __get_tower_rush_minimum_from_areas(self) -> dict:
        zone_dict = {}
        for index in range(len(self.__roulette_repo)):
            current_structure = self.__roulette_repo.get_element_from_position(index)
            if (current_structure.get_difficulty() < 8 or current_structure.get_difficulty() >= 14) and current_structure.get_tower_type() in ("Tower","Citadel","Steeple") and (current_structure.get_area() != "Pit of Misery" or self.__get_include_pomtr()):
                fraction = current_structure.show_fraction().split("/")
                times_beaten = int(fraction[0])
                if current_structure.get_area() not in zone_dict.keys():
                    zone_dict[current_structure.get_area()] = times_beaten
                elif zone_dict[current_structure.get_area()] > times_beaten:
                    zone_dict[current_structure.get_area()] = times_beaten
        return zone_dict
    def update_rushes(self) -> bool:
        warning = False
        if self.get_tower_rush_mode() != "progressive":
            return False
        tower_rush_indicator = self.__get_tower_rush_minimum_from_areas()
        mini_tower_rush_list = ("NEAT","MAT","TAT","WBAT")
        minimum = -1
        for mini_tower in mini_tower_rush_list:
            current_structure = self.__roulette_repo.find_roulette_structure_by_acronym(mini_tower)
            if current_structure is not None:
                fraction = current_structure.show_fraction().split("/")
                times_beaten = int(fraction[0])
                if minimum == -1:
                    minimum = times_beaten
                elif times_beaten < minimum:
                    minimum = times_beaten
            else:
                minimum = -2
        if minimum > 0:
            tower_rush_indicator["Rings 1-4 Mini"] = minimum
        for pair in tower_rush_indicator.items():
            if pair[1] > 0:
                tower_rush_name = pair[0] + " Tower Rush"
                tower_rush = self.__structure_repo.find_roulette_structure_by_name(tower_rush_name)
                if tower_rush is not None:
                    roulette_rush = self.__roulette_repo.find_roulette_structure_by_acronym(tower_rush.get_acronym())
                    if roulette_rush is None:
                        self.__roulette_repo.add_element(RouletteStructure(tower_rush.get_name(),tower_rush.get_area(),tower_rush.get_difficulty(),"Tower Rush",beat_limit=pair[1]))
                        warning = True
                    else:
                        if int(roulette_rush.show_fraction().split("/")[1]) != pair[1]:
                            warning = True
                        roulette_rush.set_beat_limit(pair[1])
        if self.__roulette_repo.get_file_name() != "":
            self.__roulette_repo.store_into_file()
        return warning
    def create_roulette(self, *, beat_limit=1, file_name=""):
        if file_name != "":
            self.__validator.validate_file_name(file_name)
        self.__validator.validate_pozitive_integer(beat_limit)
        if file_name == "":
            self.__roulette_repo = RouletteStructureFileRepo(self.__structure_repo)
            for index in range(len(self.__structure_repo)):
                current_structure = self.__structure_repo.get_element_from_position(index)
                new_structure = RouletteStructure(current_structure.get_name(),current_structure.get_area(),current_structure.get_difficulty(),current_structure.get_tower_type(),beat_limit=beat_limit)
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
    def update_when_skip(self):
        self.__roulette_repo.set_last_structure(None)
        if self.__roulette_repo.get_file_name() != "":
            self.__roulette_repo.store_into_file()
    def __get_last_eliminated(self) -> bool:
        return self.get_last_structure().get_eliminated()
    def set_tower_rush_mode(self, new_mode : str):
        self.__roulette_repo.set_tower_rush_mode(new_mode)
        self.__eliminate_tower_rushes()
    def get_tower_rush_mode(self) -> str:
        return self.__roulette_repo.get_tower_rush_mode()
    def set_include_pomtr(self, include_pomtr : bool):
        self.__roulette_repo.set_include_pomtr(include_pomtr)
        self.__eliminate_tower_rushes()
    def __get_include_pomtr(self) -> bool:
        return self.__roulette_repo.get_include_pomtr()
    def show_area_tower_stats(self):
        zone_total_dict = {}
        zone_total_tr_dict = {}
        zone_dict = {}
        zone_tr_dict = {}
        check_mini_tr = False
        for index in range(len(self.__roulette_repo)):
            current_structure = self.__roulette_repo.get_element_from_position(index)
            if current_structure.get_area() not in zone_total_dict.keys():
                zone_total_dict[current_structure.get_area()] = 1
            else:
                zone_total_dict[current_structure.get_area()] += 1
            fraction = current_structure.show_fraction().split("/")
            times_beaten = int(fraction[0])
            beat_total = int(fraction[1])
            if current_structure.get_area() not in zone_dict.keys():
                zone_dict[current_structure.get_area()] = [0] * beat_total
                for dict_index in range(times_beaten):
                    zone_dict[current_structure.get_area()][dict_index] += 1
            else:
                while beat_total > len(zone_dict[current_structure.get_area()]):
                    zone_dict[current_structure.get_area()].append(0)
                for dict_index in range(times_beaten):
                    zone_dict[current_structure.get_area()][dict_index] += 1
            if self.get_tower_rush_mode() == "progressive" and (current_structure.get_difficulty() < 8 or current_structure.get_difficulty() >= 14) and current_structure.get_tower_type() in ("Tower","Citadel","Steeple") and (self.__get_include_pomtr() or current_structure.get_area() != "Pit of Misery"):
                tower_rush_name = current_structure.get_area() + " Tower Rush"
                tower_rush_test = self.__structure_repo.find_roulette_structure_by_name(tower_rush_name)
                if tower_rush_test is not None:
                    if current_structure.get_area() not in zone_total_tr_dict.keys():
                        zone_total_tr_dict[current_structure.get_area()] = 1
                    else:
                        zone_total_tr_dict[current_structure.get_area()] += 1
                    if current_structure.get_area() not in zone_tr_dict.keys():
                        zone_tr_dict[current_structure.get_area()] = [0] * beat_total
                        for dict_index in range(times_beaten):
                            zone_tr_dict[current_structure.get_area()][dict_index] += 1
                    else:
                        while beat_total > len(zone_dict[current_structure.get_area()]):
                            zone_tr_dict[current_structure.get_area()].append(0)
                        for dict_index in range(times_beaten):
                            zone_tr_dict[current_structure.get_area()][dict_index] += 1
        if self.get_tower_rush_mode() == "progressive":
            mini_tower_rush_list = ("NEAT", "MAT", "TAT", "WBAT")
            tower_sum = 0
            mini_tower_tr_list = []
            for mini_tower in mini_tower_rush_list:
                current_structure = self.__roulette_repo.find_roulette_structure_by_acronym(mini_tower)
                if current_structure is not None:
                    fraction = current_structure.show_fraction().split("/")
                    times_beaten = int(fraction[0])
                    beat_total = int(fraction[1])
                    tower_sum += 1
                    if len(mini_tower_tr_list) == 0:
                        mini_tower_tr_list = [0] * beat_total
                        for dict_index in range(times_beaten):
                            mini_tower_tr_list[dict_index] += 1
                    else:
                        while beat_total > len(mini_tower_tr_list):
                            mini_tower_tr_list.append(0)
                        for dict_index in range(times_beaten):
                            mini_tower_tr_list[dict_index] += 1
            if tower_sum == 4:
                zone_total_tr_dict["Rings 1-4 Mini Tower Rush"] = 4
                zone_tr_dict["Rings 1-4 Mini Tower Rush"] = mini_tower_tr_list
                check_mini_tr = True
        str_show = ""
        for area in zone_total_dict.keys():
            str_show += f"\nYour statistics in {area} are:\n\n"
            total_structures = zone_total_dict[area]
            normal_list = zone_dict[area]
            for index in range(len(normal_list)):
                current_counter = normal_list[index]
                if index == 0:
                    spelling = "time"
                else:
                    spelling = "times"
                str_show += f"You beat {current_counter}/{total_structures} towers {index+1} {spelling} in this area.\n"
            if self.get_tower_rush_mode() == "progressive" and area in zone_total_tr_dict.keys():
                str_show += "\nAlso, your tower rush progress in the area looks like this:\n\n"
                tr_structures = zone_total_tr_dict[area]
                tr_list = zone_tr_dict[area]
                for index in range(len(tr_list)):
                    current_counter = tr_list[index]
                    if index == 0:
                        spelling = "time"
                    else:
                        spelling = "times"
                    str_show += f"You beat {current_counter}/{tr_structures} towers needed for this tower rush {index + 1} {spelling} in this area.\n"
        if check_mini_tr:
            str_show += "\nAnd at last, your tower rush progress for the Rings 1-4 Mini Tower Rush looks like this:\n\n"
            tr_structures = zone_total_tr_dict["Rings 1-4 Mini Tower Rush"]
            tr_list = zone_tr_dict["Rings 1-4 Mini Tower Rush"]
            for index in range(len(tr_list)):
                current_counter = tr_list[index]
                if index == 0:
                    spelling = "time"
                else:
                    spelling = "times"
                str_show += f"You beat {current_counter}/{tr_structures} mini towers needed for this tower rush {index + 1} {spelling} in this area.\n"
        return str_show
