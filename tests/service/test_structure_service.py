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
    def test_show_all_structures(self):
        self.assertEqual(self.__structure_service.show_all_structures(), [self.__structure_test_1, self.__structure_test_2, self.__structure_test_3])
    def test_sort_by_name(self):
        self.assertEqual(self.__structure_service.sort_by_parameter(),[self.__structure_test_2, self.__structure_test_3, self.__structure_test_1])
        self.assertEqual(self.__structure_service.sort_by_parameter(reverse=True),[self.__structure_test_1, self.__structure_test_3, self.__structure_test_2])
        self.assertEqual(self.__structure_service.sort_by_parameter(key="area"),[self.__structure_test_1, self.__structure_test_3, self.__structure_test_2])
if __name__ == '__main__':
    unittest.main()