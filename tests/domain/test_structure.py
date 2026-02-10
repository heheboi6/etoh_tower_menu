import unittest

from domain.structure import Structure


class TestStructure(unittest.TestCase):
    def setUp(self):
        self.__structure_test_1 = Structure("Tower of Infinity Gauntlet","Ring 1",8.23,"Tower")
        self.__structure_test_2 = Structure("Citadel of Green Stuff","Zone 2",6.39,"Citadel")
        self.__structure_test_3 = Structure("Is This A Tower?","Time-Lost Plain",5.81,"Mini Tower")
        self.__structure_test_4 = Structure("Tower of Wacky Progression(Monthly)","Time-Lost Clockwork",4.72,"Tower")
        self.__structure_test_5 = Structure("Steeple of Pumpkin Panic(Halloween 2020)","Forsaken Manor",5.92,"Steeple")
        self.__structure_test_6 = Structure("Steeple of Gears Locked Up Because It's Cold(April Fools 2023)","Something Otherwordly...",8.77,"Steeple")
        self.__structure_test_7 = Structure("Tower of Tallying Every Mistake","Lost River",7.00,"Tower")
        self.__structure_test_8 = Structure("Wait of The World","The Doghouse",17.00,"Tower")
    def test_init_structure(self):
        self.assertEqual(self.__structure_test_1.get_name(),"Tower of Infinity Gauntlet")
        self.assertEqual(self.__structure_test_2.get_area(),"Zone 2")
        self.assertEqual(self.__structure_test_3.get_name(),"Is This A Tower?")
        self.assertEqual(self.__structure_test_3.get_tower_type(),"Mini Tower")
        self.assertEqual(self.__structure_test_4.get_difficulty(),4.72)
    def test_get_acronym(self):
        self.assertEqual(self.__structure_test_1.get_acronym(),"ToIG")
        self.assertEqual(self.__structure_test_2.get_acronym(),"CoGS")
        self.assertEqual(self.__structure_test_4.get_acronym(),"ToWP(M)")
        self.assertEqual(self.__structure_test_5.get_acronym(),"SoPP(H2020)")
        self.assertEqual(self.__structure_test_6.get_acronym(),"SoGLUBIC(AF2023)")
    def test_str(self):
        self.assertEqual(str(self.__structure_test_1), "Tower of Infinity Gauntlet, from Ring 1, with the difficulty Low Insane(8.23)")
        self.assertEqual(str(self.__structure_test_2), "Citadel of Green Stuff, from Zone 2, with the difficulty Low-Mid Intense(6.39)")
        self.assertEqual(str(self.__structure_test_3), "Is This A Tower?, from Time-Lost Plain, with the difficulty High-Peak Challenging(5.81)")
    def test_eq(self):
        self.assertNotEqual(self.__structure_test_1, 7)
        self.assertNotEqual(self.__structure_test_1, self.__structure_test_2)
        self.assertEqual(self.__structure_test_1, self.__structure_test_1)
        self.assertEqual(self.__structure_test_2, Structure("Citadel of Green Stuff", "Zone 2",6.39,"Citadel"))
        self.assertNotEqual(self.__structure_test_3, Structure("Is This A Tower?","Zone 6",5.81,"Mini Tower"))
    def test_get_real_difficulty(self):
        self.assertEqual(self.__structure_test_1.get_real_difficulty(),"Low Insane")
        self.assertEqual(self.__structure_test_4.get_real_difficulty(),"High Difficult")
        self.assertEqual(self.__structure_test_5.get_real_difficulty(),"Peak Challenging")
        self.assertEqual(self.__structure_test_2.get_real_difficulty(),"Low-Mid Intense")
        self.assertEqual(self.__structure_test_7.get_real_difficulty(),"Baseline Remorseless")
        self.assertEqual(self.__structure_test_8.get_real_difficulty(),"Sisyphean")
if __name__ == '__main__':
    unittest.main()