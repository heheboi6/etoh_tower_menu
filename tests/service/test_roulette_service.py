import unittest

from domain.validator import ValidationException
from repo.structure_file_repo import StructureFileRepo
from service.roulette_service import RouletteService


class TestRouletteService(unittest.TestCase):
    def setUp(self):
        with open("tests/structures_test.txt", "w") as file:
            file.write("Tower of Infinity Gauntlet;Ring 1;8.23;Tower\n")
            file.write("Citadel of Green Stuff;Zone 2;6.39;Citadel\n")
            file.write("Is This A Tower?;Time-Lost Plain;5.81;Mini Tower\n")
            file.write("Steeple of Wicked Grotto;Silent Abyss;6.02;Steeple\n")
            file.write("Ring 1 Tower Rush;Ring 1;7.83;Tower Rush\n")
            file.write("Pit of Misery Tower Rush;Pit of Misery;14.99;Tower Rush\n")
            file.close()
        with open("tests/roulette_structures_test.txt", "w") as file:
            file.writelines(["ToIG 0/3\n","CoGS 1/4\n","ITAT 2/3\n","ToIG\n","progressive False"])
            file.close()
        self.__structure_repo = StructureFileRepo("tests/structures_test.txt")
        self.__roulette_service = RouletteService(self.__structure_repo)
    def test_create_roulette(self):
        self.assertRaises(ValidationException,self.__roulette_service.create_roulette,file_name="abcd",beat_limit=2)
        self.assertRaises(ValidationException,self.__roulette_service.create_roulette,file_name="",beat_limit=-1)
        self.__roulette_service.create_roulette()
        self.assertEqual(len(self.__roulette_service.show_roulette().split('\n')),7)
        self.assertEqual(self.__roulette_service.show_roulette().split("\n")[2], "Is This A Tower?, from Time-Lost Plain, with the difficulty High-Peak Challenging(5.81), you didn't beat this tower yet, and you need to beat it once to eliminate it.")
        self.assertEqual(self.__roulette_service.show_roulette().split("\n")[0],"Tower of Infinity Gauntlet, from Ring 1, with the difficulty Low Insane(8.23), you didn't beat this tower yet, and you need to beat it once to eliminate it.")
        self.__roulette_service.create_roulette(beat_limit=5)
        self.assertEqual(self.__roulette_service.show_roulette().split("\n")[0],"Tower of Infinity Gauntlet, from Ring 1, with the difficulty Low Insane(8.23), you didn't beat this tower yet, and you need to beat it 5 times to eliminate it.")
        self.__roulette_service.create_roulette(file_name="tests/roulette_structures_test.txt")
        self.assertEqual(self.__roulette_service.show_roulette().split("\n")[1],"Citadel of Green Stuff, from Zone 2, with the difficulty Low-Mid Intense(6.39), you beat this tower once, and you need to beat it 4 times to eliminate it.")
        self.__roulette_service.create_roulette()
        self.__roulette_service.set_tower_rush_mode("none")
        self.assertEqual(len(self.__roulette_service.show_roulette().split('\n')), 5)
        self.__roulette_service.create_roulette()
        self.__roulette_service.set_include_pomtr(False)
        self.assertEqual(len(self.__roulette_service.show_roulette().split('\n')), 6)
    def test_save_roulette(self):
        self.__roulette_service.create_roulette()
        self.assertRaises(ValidationException,self.__roulette_service.save_roulette,"")
        self.__roulette_service.save_roulette("tests/abcd.txt")
        self.__roulette_service.create_roulette(file_name="tests/abcd.txt")
        self.assertEqual(len(self.__roulette_service.show_roulette().split('\n')), 7)
        self.assertEqual(self.__roulette_service.show_roulette().split("\n")[2],
                         "Is This A Tower?, from Time-Lost Plain, with the difficulty High-Peak Challenging(5.81), you didn't beat this tower yet, and you need to beat it once to eliminate it.")
        self.assertEqual(self.__roulette_service.show_roulette().split("\n")[0],
                         "Tower of Infinity Gauntlet, from Ring 1, with the difficulty Low Insane(8.23), you didn't beat this tower yet, and you need to beat it once to eliminate it.")
    def test_generate_random_structure(self):
        self.__roulette_service.create_roulette()
        random_structure = self.__roulette_service.generate_random_structure()
        self.assertTrue(random_structure in self.__roulette_service.show_roulette())
    def test_beat_structure(self):
        self.__roulette_service.create_roulette(file_name="tests/roulette_structures_test.txt")
        self.__roulette_service.generate_random_structure()
        self.__roulette_service.beat_current_structure()
        self.__roulette_service.create_roulette()
        self.__roulette_service.generate_random_structure()
        self.assertEqual(self.__roulette_service.beat_current_structure(),True)
        self.__roulette_service.create_roulette(beat_limit = 5)
        self.__roulette_service.generate_random_structure()
        self.assertEqual(self.__roulette_service.beat_current_structure(), False)
    def test_get_roulette_total(self):
        self.__roulette_service.create_roulette()
        self.assertEqual(self.__roulette_service.get_roulette_total(),[0,6])
        self.__roulette_service.create_roulette(beat_limit=5)
        self.assertEqual(self.__roulette_service.get_roulette_total(), [0,30])
        self.__roulette_service.create_roulette(file_name="tests/roulette_structures_test.txt")
        self.assertEqual(self.__roulette_service.get_roulette_total(), [3,10])
        self.__roulette_service.generate_random_structure()
        self.__roulette_service.beat_current_structure()
        self.assertEqual(self.__roulette_service.get_roulette_total(), [4,10])
