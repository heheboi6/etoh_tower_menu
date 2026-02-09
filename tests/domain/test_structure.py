import unittest

from domain.structure import Structure


class TestStructure(unittest.TestCase):
    def setUp(self):
        self.__structure_test_1 = Structure("Tower of Infinity Gauntlet","Ring 1")
        self.__structure_test_2 = Structure("Citadel of Green Stuff","Zone 2")
        self.__structure_test_3 = Structure("Is This A Tower?","Time-Lost Plain")
    def test_init_structure(self):
        self.assertEqual(self.__structure_test_1.get_name(),"Tower of Infinity Gauntlet")
        self.assertEqual(self.__structure_test_2.get_area(),"Zone 2")
        self.assertEqual(self.__structure_test_3.get_name(),"Is This A Tower?")
    def test_get_acronym(self):
        self.assertEqual(self.__structure_test_1.get_acronym(),"ToIG")
        self.assertEqual(self.__structure_test_2.get_acronym(),"CoGS")
        self.assertEqual(self.__structure_test_3.get_acronym(),"ITAT")
    def test_str(self):
        self.assertEqual(str(self.__structure_test_1), "Tower of Infinity Gauntlet, from Ring 1")
        self.assertEqual(str(self.__structure_test_2), "Citadel of Green Stuff, from Zone 2")
        self.assertEqual(str(self.__structure_test_3), "Is This A Tower?, from Time-Lost Plain")
    def test_eq(self):
        self.assertNotEqual(self.__structure_test_1, 7)
        self.assertNotEqual(self.__structure_test_1, self.__structure_test_2)
        self.assertEqual(self.__structure_test_1, self.__structure_test_1)
        self.assertEqual(self.__structure_test_2, Structure("Citadel of Green Stuff", "Zone 2"))
        self.assertNotEqual(self.__structure_test_3, Structure("Is This A Tower?","Zone 6"))
if __name__ == '__main__':
    unittest.main()