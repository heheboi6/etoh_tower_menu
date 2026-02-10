import os
class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)
class Validator:
    __ACCEPTED_PARAMETERS = ("name","area","difficulty","tower_type")
    __BOOL_VALUES = ("True","False")
    @staticmethod
    def validate_sorting_parameters(key : str, reverse : str) -> list[str|bool]:
        errors = []
        if key not in Validator.__ACCEPTED_PARAMETERS:
            errors.append(f"The introduced key is not valid! The accepted values are {",".join(Validator.__ACCEPTED_PARAMETERS)}.")
        if reverse not in Validator.__BOOL_VALUES:
            errors.append(f"You did not introduce a True or False value for reversing the sorting order!")
        if len(errors) > 0:
            raise ValidationException("\n".join(errors))
        if reverse == "True":
            return [key,True]
        return [key,False]
    @staticmethod
    def validate_pozitive_integer(number : int):
        if number <= 0:
            raise ValidationException("The number must be greater than 0!")
    @staticmethod
    def validate_file_name(file_name : str):
        if not os.path.exists(file_name):
            raise ValidationException(f"The file {file_name} does not exist!")
        return
    @staticmethod
    def validate_save_file(string : str):
        if string == "":
            raise ValidationException("The string cannot be an empty string!")
        extension_split = string.split(".")
        if len(extension_split) != 2:
            raise ValidationException(f"The save file must have an extension!")
        if extension_split[1] != "txt":
            raise ValidationException(f"The save file must be a text file(with the extension .txt)!")
        return