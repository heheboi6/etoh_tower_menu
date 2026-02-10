from domain.structure import Structure
from repo.base_repo import InvalidDataException
from repo.structure_repo import StructureRepo

class CorruptedFileException(Exception):
    def __init__(self, message):
        super().__init__(message)
class StructureFileRepo(StructureRepo):
    def __init__(self, file_name : str):
        super().__init__()
        self.__file_name = file_name
        self.__load_from_file()
    def __load_from_file(self):
        with open(self.__file_name, "r") as file:
            content = file.readlines()
            for line in content:
                data = line.split(";")
                try:
                    data[-1] = data[-1].replace("\n", "")
                    name = data[0]
                    area = data[1]
                    difficulty = float(data[2])
                    tower_type = data[3]
                    new_structure = Structure(name, area, difficulty, tower_type)
                    self.add_element(new_structure)
                except (IndexError,InvalidDataException):
                    raise CorruptedFileException("The file does not contain correct or complete structure data!")
            file.close()
    def store_into_file(self):
        with open(self.__file_name, "w") as file:
            for index in range(len(self)):
                current_structure = self.get_element_from_position(index)
                file.write(current_structure.get_name() + ";" + current_structure.get_area() + ";" + str(current_structure.get_difficulty()) + ";" + current_structure.get_tower_type() + "\n")
            file.close()