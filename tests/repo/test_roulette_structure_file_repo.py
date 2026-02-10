import unittest

from domain.roulette_structure import RouletteStructure
from repo.roulette_structure_file_repo import RouletteStructureFileRepo
from repo.structure_file_repo import StructureFileRepo, CorruptedFileException


class TestRouletteStructureFileRepo(unittest.TestCase):
    def setUp(self):
        with open("tests/roulette_structures_test.txt", "w") as file:
            file.writelines(["ToIG 0/3\n","CoGS 1/3\n","ITAT 2/3\n","ToIG"])
            file.close()
        with open("tests/corrupted_roulette_structures.txt", "w") as file:
            file.writelines(["ToDAN\n","1/3\n","4\n"])
            file.close()
        with open("tests/structures_test.txt", "w") as file:
            file.write("Tower of Infinity Gauntlet;Ring 1\n")
            file.write("Citadel of Green Stuff;Zone 2\n")
            file.write("Is This A Tower?;Time-Lost Plain\n")
            file.write("Steeple of Wicked Grotto;Silent Abyss")
            file.close()
        self.__file_repo = StructureFileRepo("tests/structures_test.txt")
    def test_load_from_file(self):
        repo_test = RouletteStructureFileRepo(self.__file_repo,file_name="tests/roulette_structures_test.txt")
        repo_test.load_from_file()
        self.assertEqual(repo_test.get_element_from_position(1).get_name(),"Citadel of Green Stuff")
        self.assertEqual(repo_test.get_element_from_position(2).get_area(),"Time-Lost Plain")
        self.assertEqual(repo_test.get_element_from_position(0).get_name(),"Tower of Infinity Gauntlet")
        corrupted_repo = RouletteStructureFileRepo(self.__file_repo,file_name="tests/corrupted_roulette_structures.txt")
        self.assertRaises(CorruptedFileException,corrupted_repo.load_from_file)
        blank_repo = RouletteStructureFileRepo(self.__file_repo)
        self.assertRaises(CorruptedFileException,blank_repo.load_from_file)
    def test_store_into_file(self):
        repo_test = RouletteStructureFileRepo(self.__file_repo,file_name="tests/roulette_structures_test.txt")
        repo_test.load_from_file()
        repo_test.add_element(RouletteStructure("Steeple of Wicked Grotto","Silent Abyss",times_beaten=1,beat_limit=5))
        repo_test.store_into_file()
        repo_test.load_from_file()
        self.assertEqual(len(repo_test),4)
        self.assertEqual(repo_test.get_element_from_position(3).get_name(),"Steeple of Wicked Grotto")
        repo_test.store_into_file(save_file_name="tests/save_test.txt")
        repo_test_2 = RouletteStructureFileRepo(self.__file_repo,file_name="tests/save_test.txt")
        repo_test_2.load_from_file()
        self.assertEqual(len(repo_test_2), 4)
        self.assertEqual(repo_test_2.get_element_from_position(3).get_name(), "Steeple of Wicked Grotto")
if __name__ == "__main__":
    unittest.main()