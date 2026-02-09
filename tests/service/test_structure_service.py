import unittest

from domain.structure import Structure
from repo.structure_file_repo import StructureFileRepo
from service.structure_service import StructureService


class TestStructureService(unittest.TestCase):
    def setUp(self):
        with open("tests/structures_test.txt","w") as file:
            file.write("Tower of Infinity Gauntlet;Ring 1\n")
            file.write("Citadel of Green Stuff;Zone 2\n")
            file.write("Is This A Tower?;Time-Lost Plain\n")
            file.close()
        self.__structure_repo = StructureFileRepo("tests/structures_test.txt")
        self.__structure_service = StructureService(self.__structure_repo)
        self.__structure_test_1 = Structure("Tower of Infinity Gauntlet", "Ring 1")
        self.__structure_test_2 = Structure("Citadel of Green Stuff", "Zone 2")
        self.__structure_test_3 = Structure("Is This A Tower?", "Time-Lost Plain")
        self.__structure_service.set_sorting_parameters("name","False")
    def test_show_all_structures(self):
        self.assertEqual(self.__structure_service.show_all_structures(), "Tower of Infinity Gauntlet, from Ring 1\nCitadel of Green Stuff, from Zone 2\nIs This A Tower?, from Time-Lost Plain\n")
    def test_sort_by_name(self):
        self.__structure_service.sort_by_parameter()
        self.assertEqual(self.__structure_service.show_all_structures(),"Citadel of Green Stuff, from Zone 2\nIs This A Tower?, from Time-Lost Plain\nTower of Infinity Gauntlet, from Ring 1\n")
        self.__structure_service.set_sorting_parameters("name","True")
        self.__structure_service.sort_by_parameter()
        self.assertEqual(self.__structure_service.show_all_structures(),"Tower of Infinity Gauntlet, from Ring 1\nIs This A Tower?, from Time-Lost Plain\nCitadel of Green Stuff, from Zone 2\n")
        self.__structure_service.set_sorting_parameters("area", "False")
        self.__structure_service.sort_by_parameter()
        self.assertEqual(self.__structure_service.show_all_structures(),"Tower of Infinity Gauntlet, from Ring 1\nIs This A Tower?, from Time-Lost Plain\nCitadel of Green Stuff, from Zone 2\n")
    def test_show_sorting_parameters(self):
        self.assertEqual(self.__structure_service.show_sorting_parameters(),"The current sorting will be made using the name of the structure, in normal order.")
        self.__structure_service.set_sorting_parameters("area","True")
        self.assertEqual(self.__structure_service.show_sorting_parameters(),"The current sorting will be made using the area of the structure, in reverse order.")
if __name__ == '__main__':
    unittest.main()