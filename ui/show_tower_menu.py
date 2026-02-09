from colorama import Fore, Style

from domain.validator import ValidationException
from service.structure_service import StructureService

class ShowTowerMenu:
    def __init__(self, structure_service : StructureService):
        self.__structure_service = structure_service
    @staticmethod
    def __print_menu():
        print("Choose an option from the menu:")
        print("1. Change the sorting method;")
        print("2. Show all of the structures in a sorted order;")
        print("3. Exit")
    def run(self):
        while True:
            self.__print_menu()
            self.__ui_show_sorting_parameters()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.__ui_set_sorting_parameters()
            elif choice == "2":
                self.__ui_show_sorted_structures()
            elif choice == "3":
                break
            else:
                print(Fore.RED + "This choice was not found in the menu, please try again." + Style.RESET_ALL)
    def __ui_show_sorting_parameters(self):
        print(Fore.BLUE + "\n" + self.__structure_service.show_sorting_parameters() + "\n" + Style.RESET_ALL)
    def __ui_set_sorting_parameters(self):
        try:
            key = input("Enter the name of the structure parameter that you want to use for the sorting:")
            reverse = input("Enter True if you want to sort the structures in reverse order, or False if you want to sort the structures in normal order: ")
            self.__structure_service.set_sorting_parameters(key,reverse)
            print(Fore.BLUE + "The sorting parameters have been set successfully." + Style.RESET_ALL)
        except ValidationException as err:
            print(Fore.RED + str(err) + Style.RESET_ALL)
    def __ui_show_sorted_structures(self):
        self.__structure_service.sort_by_parameter()
        print("Here is the sorted list of the structures:")
        print(self.__structure_service.show_all_structures())