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
            file.write("Tower of Extraterrestrial Enchantment;Zone 2;6.49;Tower\n")
            file.write("Tower of Annoying Paths(Monthly);Time-Lost Plain;7.08;Tower\n")
            file.write("Tower of Modernistic Design Choices;Pit of Misery;1.84;Tower\n")
            file.write("Zone 2 Tower Rush;Zone 2;8.84;Tower Rush\n")
            file.write("Pit of Misery Tower Rush;Pit of Misery;14.99;Tower Rush\n")
            file.close()
        with open("tests/structures_test_2.txt", "w") as file:
            file.write("Not Even A Tower;Ring 1;1.11;Mini Tower\n")
            file.write("Totally A Tower;Ring 3;6.99;Mini Tower\n")
            file.write("Rings 1-4 Mini Tower Rush;Ring 5;6.99;Tower Rush\n")
            file.close()
        with open("tests/roulette_structures_test.txt", "w") as file:
            file.writelines(["ToIG 0/3\n","CoGS 1/4\n","ITAT 2/3\n","ToAP(M) 1/3\n","ToEE 2/4\n","ToMDC 30/100\n","ToIG\n","progressive False"])
            file.close()
        with open("tests/roulette_structures_test_2.txt", "w") as file:
            file.writelines(["NEAT 1/3\n","TAT 2/3\n","@\n","progressive False"])
            file.close()
        self.__structure_repo = StructureFileRepo("tests/structures_test.txt")
        self.__roulette_service = RouletteService(self.__structure_repo)
    def test_create_roulette(self):
        self.assertRaises(ValidationException,self.__roulette_service.create_roulette,file_name="abcd",beat_limit=2)
        self.assertRaises(ValidationException,self.__roulette_service.create_roulette,file_name="",beat_limit=-1)
        self.__roulette_service.create_roulette()
        self.assertEqual(len(self.__roulette_service.show_roulette().split('\n')),10)
        self.assertEqual(self.__roulette_service.show_roulette().split("\n")[2], "Is This A Tower?, from Time-Lost Plain, with the difficulty High-Peak Challenging(5.81), you didn't beat this mini tower yet, and you need to beat it once to eliminate it.")
        self.assertEqual(self.__roulette_service.show_roulette().split("\n")[0],"Tower of Infinity Gauntlet, from Ring 1, with the difficulty Low Insane(8.23), you didn't beat this tower yet, and you need to beat it once to eliminate it.")
        self.__roulette_service.create_roulette(beat_limit=5)
        self.assertEqual(self.__roulette_service.show_roulette().split("\n")[0],"Tower of Infinity Gauntlet, from Ring 1, with the difficulty Low Insane(8.23), you didn't beat this tower yet, and you need to beat it 5 times to eliminate it.")
        self.__roulette_service.create_roulette(file_name="tests/roulette_structures_test.txt")
        self.assertEqual(self.__roulette_service.show_roulette().split("\n")[1],"Citadel of Green Stuff, from Zone 2, with the difficulty Low-Mid Intense(6.39), you beat this citadel once, and you need to beat it 4 times to eliminate it.")
        self.__roulette_service.create_roulette()
        self.__roulette_service.set_tower_rush_mode("none")
        self.assertEqual(len(self.__roulette_service.show_roulette().split('\n')), 8)
        self.__roulette_service.create_roulette()
        self.__roulette_service.set_include_pomtr(False)
        self.assertEqual(len(self.__roulette_service.show_roulette().split('\n')), 9)
    def test_save_roulette(self):
        self.__roulette_service.create_roulette()
        self.assertRaises(ValidationException,self.__roulette_service.save_roulette,"")
        self.__roulette_service.save_roulette("tests/abcd.txt")
        self.__roulette_service.create_roulette(file_name="tests/abcd.txt")
        self.assertEqual(len(self.__roulette_service.show_roulette().split('\n')), 10)
        self.assertEqual(self.__roulette_service.show_roulette().split("\n")[2],
                         "Is This A Tower?, from Time-Lost Plain, with the difficulty High-Peak Challenging(5.81), you didn't beat this mini tower yet, and you need to beat it once to eliminate it.")
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
        self.assertEqual(self.__roulette_service.get_roulette_total(),[0,9])
        self.__roulette_service.create_roulette(beat_limit=5)
        self.assertEqual(self.__roulette_service.get_roulette_total(), [0,45])
        self.__roulette_service.create_roulette(file_name="tests/roulette_structures_test.txt")
        self.assertEqual(self.__roulette_service.get_roulette_total(), [36,117])
        self.__roulette_service.generate_random_structure()
        self.__roulette_service.beat_current_structure()
        self.assertEqual(self.__roulette_service.get_roulette_total(), [37,117])
    def test_search_for_rushes(self):
        self.__roulette_service.create_roulette(file_name="tests/roulette_structures_test.txt")
        self.assertEqual(self.__roulette_service.update_rushes(),True)
        self.assertEqual(self.__roulette_service.update_rushes(),False)
        self.assertEqual(len(self.__roulette_service.show_roulette().split('\n')), 8)
        self.__roulette_service.create_roulette(file_name="tests/roulette_structures_test.txt")
        self.__roulette_service.set_include_pomtr(True)
        self.assertEqual(self.__roulette_service.update_rushes(),True)
        self.assertEqual(len(self.__roulette_service.show_roulette().split('\n')), 9)
        self.__structure_repo_2 = StructureFileRepo("tests/structures_test_2.txt")
        self.__roulette_service_2 = RouletteService(self.__structure_repo_2)
        self.__roulette_service_2.create_roulette(file_name="tests/roulette_structures_test_2.txt")
        self.assertEqual(self.__roulette_service_2.update_rushes(),False)
    def test_show_area_tower_stats(self):
        self.__roulette_service.create_roulette(file_name="tests/roulette_structures_test.txt")
        print(self.__roulette_service.show_area_tower_stats())
        self.assertEqual(len(self.__roulette_service.show_area_tower_stats().split('\n')),130)