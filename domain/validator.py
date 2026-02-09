class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)
class Validator:
    __ACCEPTED_PARAMETERS = ("name","area")
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