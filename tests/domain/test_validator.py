import unittest

from domain.validator import Validator, ValidationException


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.__validator = Validator()
    def test_validate_sorting_parameters(self):
        self.assertRaises(ValidationException, self.__validator.validate_sorting_parameters,"name","Frue")
        self.assertRaises(ValidationException, self.__validator.validate_sorting_parameters,"cheese","True")
        self.assertEqual(self.__validator.validate_sorting_parameters("name","True"),["name",True])
        self.assertEqual(self.__validator.validate_sorting_parameters("area","False"),["area",False])
if __name__ == '__main__':
    unittest.main()