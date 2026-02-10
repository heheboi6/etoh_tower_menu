import unittest

from domain.roulette_structure import RouletteStructure
from domain.structure import Structure


class TestRouletteStructure(unittest.TestCase):
    def setUp(self):
        self.__structure_test_1 = RouletteStructure("Tower of Infinity Gauntlet","Ring 1")
        self.__structure_test_2 = RouletteStructure("Citadel of Green Stuff","Zone 2",times_beaten=1,beat_limit=3)
        self.__structure_test_3 = RouletteStructure("Is This A Tower?","Time-Lost Plain",times_beaten=2,beat_limit=2)
    def test_str(self):
        self.assertEqual(str(self.__structure_test_1),"Tower of Infinity Gauntlet, from Ring 1, you didn't beat this tower yet, and you need to beat it once to eliminate it.")
        self.assertEqual(str(self.__structure_test_2),"Citadel of Green Stuff, from Zone 2, you beat this tower once, and you need to beat it 3 times to eliminate it.")
        self.assertEqual(str(self.__structure_test_3),"Is This A Tower?, from Time-Lost Plain, you have beaten this tower enough so that it can be eliminated from the roulette.")
    def test_eq(self):
        self.assertEqual(self.__structure_test_1,self.__structure_test_1)
        self.assertNotEqual(self.__structure_test_1,self.__structure_test_2)
        self.assertNotEqual(self.__structure_test_1,self.__structure_test_3)
    def test_beat_structure(self):
        self.assertEqual(self.__structure_test_1.get_eliminated(),False)
        self.__structure_test_1.beat_structure()
        self.assertEqual(self.__structure_test_1.get_eliminated(),True)
        self.__structure_test_2.beat_structure()
        self.assertEqual(self.__structure_test_2.get_eliminated(),False)
        self.__structure_test_2.beat_structure()
        self.assertEqual(self.__structure_test_2.get_eliminated(),True)
        self.assertEqual(self.__structure_test_3.get_eliminated(),True)
        self.__structure_test_3.beat_structure()
        self.assertEqual(self.__structure_test_3.get_eliminated(),True)
    def test_show_fraction(self):
        self.assertEqual(self.__structure_test_1.show_fraction(),"0/1")
        self.assertEqual(self.__structure_test_2.show_fraction(),"1/3")
        self.assertEqual(self.__structure_test_3.show_fraction(),"2/2")
if __name__ == '__main__':
    unittest.main()