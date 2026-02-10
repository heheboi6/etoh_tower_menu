import unittest

from domain.structure import Structure
from repo.structure_file_repo import StructureFileRepo
from service.structure_service import StructureService


class TestStructureService(unittest.TestCase):
    def setUp(self):
        with open("tests/structures_test.txt","w") as file:
            file.write("Tower of Infinity Gauntlet;Ring 1;8.23;Tower\n")
            file.write("Citadel of Green Stuff;Zone 2;6.39;Citadel\n")
            file.write("Is This A Tower?;Time-Lost Plain;5.81;Mini Tower\n")
            file.close()
        self.__structure_repo = StructureFileRepo("tests/structures_test.txt")
        self.__structure_service = StructureService(self.__structure_repo)
        self.__structure_test_1 = Structure("Tower of Infinity Gauntlet", "Ring 1",8.23,"Tower")
        self.__structure_test_2 = Structure("Citadel of Green Stuff", "Zone 2",6.39,"Citadel")
        self.__structure_test_3 = Structure("Is This A Tower?", "Time-Lost Plain",5.82,"Mini Tower")
        self.__structure_service.set_sorting_parameters("name","False")
    def test_show_all_structures(self):
        self.assertEqual(self.__structure_service.show_all_structures(), "Tower of Infinity Gauntlet, from Ring 1, with the difficulty Low Insane(8.23)\nCitadel of Green Stuff, from Zone 2, with the difficulty Low-Mid Intense(6.39)\nIs This A Tower?, from Time-Lost Plain, with the difficulty High-Peak Challenging(5.81)\n")
    def test_sort_by_name(self):
        self.__structure_service.sort_by_parameter()
        self.assertEqual(self.__structure_service.show_all_structures(),"Citadel of Green Stuff, from Zone 2, with the difficulty Low-Mid Intense(6.39)\nIs This A Tower?, from Time-Lost Plain, with the difficulty High-Peak Challenging(5.81)\nTower of Infinity Gauntlet, from Ring 1, with the difficulty Low Insane(8.23)\n")
        self.__structure_service.set_sorting_parameters("name","True")
        self.__structure_service.sort_by_parameter()
        self.assertEqual(self.__structure_service.show_all_structures(),"Tower of Infinity Gauntlet, from Ring 1, with the difficulty Low Insane(8.23)\nIs This A Tower?, from Time-Lost Plain, with the difficulty High-Peak Challenging(5.81)\nCitadel of Green Stuff, from Zone 2, with the difficulty Low-Mid Intense(6.39)\n")
        self.__structure_service.set_sorting_parameters("area", "False")
        self.__structure_service.sort_by_parameter()
        self.assertEqual(self.__structure_service.show_all_structures(),"Tower of Infinity Gauntlet, from Ring 1, with the difficulty Low Insane(8.23)\nIs This A Tower?, from Time-Lost Plain, with the difficulty High-Peak Challenging(5.81)\nCitadel of Green Stuff, from Zone 2, with the difficulty Low-Mid Intense(6.39)\n")
    def test_show_sorting_parameters(self):
        self.assertEqual(self.__structure_service.show_sorting_parameters(),"The current sorting will be made using the name of the structure, in normal order.")
        self.__structure_service.set_sorting_parameters("area","True")
        self.assertEqual(self.__structure_service.show_sorting_parameters(),"The current sorting will be made using the area of the structure, in reverse order.")
if __name__ == '__main__':
    unittest.main()