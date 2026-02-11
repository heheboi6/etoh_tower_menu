import unittest

from domain.roulette_structure import RouletteStructure
from repo.base_repo import InvalidDataException
from repo.roulette_structure_repo import RouletteStructureRepo
from repo.structure_repo import StructureNotFoundException


class TestRouletteStructureRepo(unittest.TestCase):
    def setUp(self):
        self.__roulette_repo = RouletteStructureRepo()
        self.__roulette_repo.add_element(RouletteStructure("Tower of Infinity Gauntlet","Ring 1",8.23,"Tower"))
        self.__roulette_repo.add_element(RouletteStructure("Citadel of Green Stuff","Zone 2",6.39,"Citadel",times_beaten=1,beat_limit=3))
        self.__roulette_repo.add_element(RouletteStructure("Is This A Tower?","Time-Lost Plain",5.81,"Mini Tower",times_beaten=2,beat_limit=2))
    def test_str(self):
        self.assertEqual(str(self.__roulette_repo), "Tower of Infinity Gauntlet, from Ring 1, with the difficulty Low Insane(8.23), you didn't beat this tower yet, and you need to beat it once to eliminate it.\nCitadel of Green Stuff, from Zone 2, with the difficulty Low-Mid Intense(6.39), you beat this citadel once, and you need to beat it 3 times to eliminate it.\nIs This A Tower?, from Time-Lost Plain, with the difficulty High-Peak Challenging(5.81), you have beaten this mini tower enough so that it can be eliminated from the roulette.\n")
    def test_find_roulette_structure_by_acronym(self):
        self.assertEqual(self.__roulette_repo.find_roulette_structure_by_acronym("ITAT").get_area(), "Time-Lost Plain")
        self.assertEqual(None,self.__roulette_repo.find_roulette_structure_by_acronym("ToTaS"))
    def test_remove_roulette_structure(self):
        self.__roulette_repo.remove_element(RouletteStructure("Citadel of Green Stuff","Zone 2",6.39,"Citadel",times_beaten=1,beat_limit=3))
        self.assertEqual(len(self.__roulette_repo),2)
        self.assertEqual(self.__roulette_repo.get_element_from_position(1).get_name(),"Is This A Tower?")
        self.assertRaises(InvalidDataException,self.__roulette_repo.remove_element,"wow")
if __name__ == '__main__':
    unittest.main()