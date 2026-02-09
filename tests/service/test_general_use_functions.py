import unittest

from domain.structure import Structure
from service.general_use_functions import GeneralUseFunctions


class TestGeneralUseFunctions(unittest.TestCase):
    def setUp(self):
        self.__functions = GeneralUseFunctions()
        self.__test_list_1 = [1,5,8,3,7,1,6,3,8,6,3]
        self.__structure_test_1 = Structure("Tower of Infinity Gauntlet", "Ring 1")
        self.__structure_test_2 = Structure("Citadel of Green Stuff", "Zone 2")
        self.__structure_test_3 = Structure("Is This A Tower?", "Time-Lost Plain")
        self.__test_list_2 = [self.__structure_test_1,self.__structure_test_2,self.__structure_test_3]
    def test_true_merge_sort(self):
        self.__functions.true_merge_sort(self.__test_list_1)
        self.assertEqual(self.__test_list_1, [1,1,3,3,3,5,6,6,7,8,8])
        self.__functions.true_merge_sort(self.__test_list_2,key=lambda structure: structure.get_acronym())
        self.assertEqual(self.__test_list_2, [self.__structure_test_2,self.__structure_test_3,self.__structure_test_1])
        self.__functions.true_merge_sort(self.__test_list_2,reverse=True,key=lambda structure: structure.get_acronym())
        self.assertEqual(self.__test_list_2,[self.__structure_test_1, self.__structure_test_3, self.__structure_test_2])
        self.__functions.true_merge_sort(self.__test_list_2,sort_function=lambda structure1, structure2: structure1.get_area() > structure2.get_area())
        self.assertEqual(self.__test_list_2, [self.__structure_test_2, self.__structure_test_3,self.__structure_test_1])
if __name__ == '__main__':
    unittest.main()
