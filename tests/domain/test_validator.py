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
    def test_validate_pozitive_number(self):
        self.assertRaises(ValidationException,self.__validator.validate_pozitive_integer,-1)
        self.assertRaises(ValidationException,self.__validator.validate_pozitive_integer,0)
        self.assertEqual(self.__validator.validate_pozitive_integer(1),None)
    def test_validate_file_name(self):
        self.assertRaises(ValidationException,self.__validator.validate_file_name,"alabala")
        self.assertEqual(self.__validator.validate_file_name("tests/structures_test.txt"),None)
    def test_validate_string(self):
        self.assertRaises(ValidationException,self.__validator.validate_save_file,"")
        self.assertRaises(ValidationException,self.__validator.validate_save_file,"alabala")
        self.assertRaises(ValidationException, self.__validator.validate_save_file, "alabala.pog")
        self.assertEqual(self.__validator.validate_save_file("fire and flame.txt"),None)
if __name__ == '__main__':
    unittest.main()