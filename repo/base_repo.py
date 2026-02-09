class InvalidDataException(Exception):
    def __init__(self, message):
        super().__init__(message)
class BaseRepo:
    def __init__(self, repo_class, repo_list):
        self.__repo_class = repo_class
        self.__repo_list = repo_list
    def __len__(self):
        return len(self.__repo_list)
    def get_element_from_position(self, position : int):
        try:
            returned_element = self.__repo_list[position]
        except IndexError:
            raise InvalidDataException(f"The element at the given position does not exist! The positions must be between {-len(self)} and {len(self)}.")
        return returned_element
    def add_element(self, element):
        if element in self.__repo_list:
            raise InvalidDataException("The element is already in the list!")
        if type(element) != self.__repo_class:
            raise InvalidDataException(f"The element is not from the correct class!")
        self.__repo_list.append(element)
    def get_list(self):
        return self.__repo_list
