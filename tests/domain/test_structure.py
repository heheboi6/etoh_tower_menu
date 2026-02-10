import unittest

from domain.structure import Structure


class TestStructure(unittest.TestCase):
    def setUp(self):
        self.__structure_test_1 = Structure("Tower of Infinity Gauntlet","Ring 1")
        self.__structure_test_2 = Structure("Citadel of Green Stuff","Zone 2")
        self.__structure_test_3 = Structure("Is This A Tower?","Time-Lost Plain")
        self.__structure_test_4 = Structure("Tower of Wacky Progression(Monthly)","Time-Lost Clockwork")
        self.__structure_test_5 = Structure("Steeple of Pumpkin Panic(Halloween 2020)","Forsaken Manor")
        self.__structure_test_6 = Structure("Steeple of Gears Locked Up Because It's Cold(April Fools 2023)","Something Otherwordly...")
    def test_init_structure(self):
        self.assertEqual(self.__structure_test_1.get_name(),"Tower of Infinity Gauntlet")
        self.assertEqual(self.__structure_test_2.get_area(),"Zone 2")
        self.assertEqual(self.__structure_test_3.get_name(),"Is This A Tower?")
    def test_get_acronym(self):
        self.assertEqual(self.__structure_test_1.get_acronym(),"ToIG")
        self.assertEqual(self.__structure_test_2.get_acronym(),"CoGS")
        self.assertEqual(self.__structure_test_4.get_acronym(),"ToWP(M)")
        self.assertEqual(self.__structure_test_5.get_acronym(),"SoPP(H2020)")
        self.assertEqual(self.__structure_test_6.get_acronym(),"SoGLUBIC(AF2023)")
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