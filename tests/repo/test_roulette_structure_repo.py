import unittest

from domain.roulette_structure import RouletteStructure
from repo.roulette_structure_repo import RouletteStructureRepo
from repo.structure_repo import StructureNotFoundException


class TestRouletteStructureRepo(unittest.TestCase):
    def setUp(self):
        self.__roulette_repo = RouletteStructureRepo()
        self.__roulette_repo.add_element(RouletteStructure("Tower of Infinity Gauntlet","Ring 1"))
        self.__roulette_repo.add_element(RouletteStructure("Citadel of Green Stuff","Zone 2",times_beaten=1,beat_limit=3))
        self.__roulette_repo.add_element(RouletteStructure("Is This A Tower?","Time-Lost Plain",times_beaten=2,beat_limit=2))
    def test_str(self):
        self.assertEqual(str(self.__roulette_repo), "Tower of Infinity Gauntlet, from Ring 1, you didn't beat this tower yet, and you need to beat it once to eliminate it.\nCitadel of Green Stuff, from Zone 2, you beat this tower once, and you need to beat it 3 times to eliminate it.\nIs This A Tower?, from Time-Lost Plain, you have beaten this tower enough so that it can be eliminated from the roulette.\n")
    def test_find_roulette_structure_by_acronym(self):
        self.assertEqual(self.__roulette_repo.find_roulette_structure_by_acronym("ITAT").get_area(), "Time-Lost Plain")
        self.assertRaises(StructureNotFoundException,self.__roulette_repo.find_roulette_structure_by_acronym,"ToTaS")
if __name__ == '__main__':
    unittest.main()