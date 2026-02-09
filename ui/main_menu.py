from colorama import Fore, Style

from service.structure_service import StructureService
from ui.show_tower_menu import ShowTowerMenu


class MainMenu:
    def __init__(self, structure_service: StructureService):
        self.__structure_service = structure_service
    @staticmethod
    def __print_main_menu():
        print("Choose an option from the main menu:")
        print("1. Open the menu which shows all of the towers;")
        print("2. Open the roulette menu;")
        print("3. Exit the application;")
    def run(self):
        while True:
            self.__print_main_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.__ui_open_show_tower_menu()
            elif choice == "3":
                break
            else:
                print(Fore.RED + "This choice was not found in the menu, please try again." + Style.RESET_ALL)
    def __ui_open_show_tower_menu(self):
        s_t_m = ShowTowerMenu(self.__structure_service)
        s_t_m.run()