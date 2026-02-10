import unittest

from domain.structure import Structure
from repo.base_repo import InvalidDataException
from repo.structure_repo import StructureRepo, StructureNotFoundException


class TestStructureRepo(unittest.TestCase):
    def setUp(self):
        self.__structure_repo = StructureRepo()
        self.__structure_repo.add_element(Structure("Tower of Infinity Gauntlet","Ring 1",8.23,"Tower"))
        self.__structure_repo.add_element(Structure("Citadel of Green Stuff","Zone 2",6.39,"Citadel"))
        self.__structure_repo.add_element(Structure("Is This A Tower?","Time-Lost Plain",5.81,"Mini Tower"))
    def test_get_element_from_position(self):
        self.assertEqual(self.__structure_repo.get_element_from_position(1).get_name(),"Citadel of Green Stuff")
        self.assertEqual(self.__structure_repo.get_element_from_position(2).get_area(),"Time-Lost Plain")
        self.assertEqual(self.__structure_repo.get_element_from_position(0).get_area(),"Ring 1")
        self.assertEqual(self.__structure_repo.get_element_from_position(-3).get_name(),"Tower of Infinity Gauntlet")
        self.assertRaises(InvalidDataException, self.__structure_repo.get_element_from_position, -4)
        self.assertRaises(InvalidDataException, self.__structure_repo.get_element_from_position, 4)
    def test_add(self):
        self.__test_structure = Structure("Steeple of Descendance","Silent Abyss",5.15,"Steeple")
        self.__structure_repo.add_element(self.__test_structure)
        self.assertEqual(len(self.__structure_repo),4)
        self.assertEqual(self.__structure_repo.get_element_from_position(-1).get_area(),"Silent Abyss")
        self.assertEqual(self.__structure_repo.get_element_from_position(-1).get_name(), "Steeple of Descendance")
        self.assertEqual(self.__structure_repo.get_element_from_position(-1).get_difficulty(),5.15)
        self.assertRaises(InvalidDataException, self.__structure_repo.add_element, self.__test_structure)
        self.assertRaises(InvalidDataException, self.__structure_repo.add_element, 17)
    def test_str(self):
        self.assertEqual(str(self.__structure_repo),"Tower of Infinity Gauntlet, from Ring 1, with the difficulty Low Insane(8.23)\nCitadel of Green Stuff, from Zone 2, with the difficulty Low-Mid Intense(6.39)\nIs This A Tower?, from Time-Lost Plain, with the difficulty High-Peak Challenging(5.81)\n")
    def test_search_by_acronym(self):
        self.assertEqual(self.__structure_repo.search_by_acronym("CoGS"),Structure("Citadel of Green Stuff","Zone 2",6.39,"Citadel"))
        self.assertEqual(self.__structure_repo.search_by_acronym("ITAT"),Structure("Is This A Tower?","Time-Lost Plain",5.81,"Mini Tower"))
        self.assertRaises(StructureNotFoundException,self.__structure_repo.search_by_acronym,"ToZZ")
if __name__ == '__main__':
    unittest.main()