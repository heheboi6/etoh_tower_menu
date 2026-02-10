import unittest

from domain.structure import Structure
from repo.structure_file_repo import StructureFileRepo, CorruptedFileException


class TestStructureFileRepo(unittest.TestCase):
    def setUp(self):
        with open("tests/structures_test.txt","w") as file:
            file.write("Tower of Infinity Gauntlet;Ring 1;8.23;Tower\n")
            file.write("Citadel of Green Stuff;Zone 2;6.39;Citadel\n")
            file.write("Is This A Tower?;Time-Lost Plain;5.81;Mini Tower\n")
            file.close()
        with open("tests/corrupted_structures.txt","w") as file:
            file.write("Tower of Madness\n")
            file.write("Tower of Glory\n")
            file.close()
    def test_load_from_file(self):
        self.__structure_repo = StructureFileRepo("tests/structures_test.txt")
        self.assertEqual(self.__structure_repo.get_element_from_position(1).get_name(), "Citadel of Green Stuff")
        self.assertEqual(self.__structure_repo.get_element_from_position(2).get_area(), "Time-Lost Plain")
        self.assertEqual(self.__structure_repo.get_element_from_position(0).get_area(), "Ring 1")
        self.assertEqual(self.__structure_repo.get_element_from_position(1).get_difficulty(), 6.39)
        self.assertRaises(CorruptedFileException,StructureFileRepo,"tests/corrupted_structures.txt")
    def test_store_into_file(self):
        structure_test = Structure("Tower of True Skill","Ring 1",7.09,"Tower")
        self.__structure_repo = StructureFileRepo("tests/structures_test.txt")
        self.__structure_repo.add_element(structure_test)
        self.assertEqual(len(self.__structure_repo),4)
        self.__structure_repo.store_into_file()
        self.__structure_repo = StructureFileRepo("tests/structures_test.txt")
        self.assertEqual(len(self.__structure_repo),4)
        self.assertEqual(self.__structure_repo.get_element_from_position(-1),structure_test)
        self.assertEqual(self.__structure_repo.get_element_from_position(2).get_area(),"Time-Lost Plain")
if __name__ == '__main__':
    unittest.main()
