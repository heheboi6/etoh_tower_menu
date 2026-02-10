from colorama import Fore, Style

from domain.validator import ValidationException
from service.roulette_service import RouletteService

class RouletteMenu:
    def __init__(self, roulette_service : RouletteService):
        self.__roulette_service = roulette_service
        self.__roulette_active = False
    @staticmethod
    def __read_option():
        while True:
            file_option = input("Do you want to load a roulette from a file, or create a new one? (file/new):").strip().lower()
            if file_option == "file":
                return file_option
            elif file_option == "new":
                return file_option
            else:
                print(Fore.RED + "You did not enter a valid option, please try again." + Style.RESET_ALL)
    def __mini_random_menu(self):
        while True:
            structure_choice = input("Do you want to beat this structure, or skip it? (beat/skip)").strip().lower()
            if structure_choice == "beat":
                eliminated = self.__roulette_service.beat_current_structure()
                if eliminated:
                    print(Fore.BLUE + "This tower has been eliminated from the roulette, good job." + Style.RESET_ALL)
                return
            elif structure_choice == "skip":
                return
            else:
                print(Fore.RED + "You did not enter a valid option, please try again." + Style.RESET_ALL)
    @staticmethod
    def __read_yes_no(message : str):
        while True:
            exit_option = input(message).strip().lower()
            if exit_option == "y":
                return True
            elif exit_option == "n":
                return False
            else:
                print(Fore.RED + "You did not enter a valid option, please try again." + Style.RESET_ALL)
    def __read_tower_rush_option(self):
        while True:
            tower_rush_option = input("Enter the number of the option that you want:").strip().lower()
            if tower_rush_option == "1":
                self.__roulette_service.set_tower_rush_mode("none")
                return
            elif tower_rush_option == "2":
                self.__roulette_service.set_tower_rush_mode("from start")
                return
            elif tower_rush_option == "3":
                self.__roulette_service.set_tower_rush_mode("progressive")
                return
            else:
                print(Fore.RED + "You did not enter a valid option, please try again." + Style.RESET_ALL)
    @staticmethod
    def __print_menu():
        print("Choose an option from the menu:")
        print("1. Create a new roulette, or load an existing roulette;")
        print("2. Show everything in the roulette;")
        print("3. Save the roulette to a file;")
        print("4. Generate a random tower according to the created roulette;")
        print("5. Go back to the main menu;")
    @staticmethod
    def __print_tower_rush_options():
        print("Before continuing, you need to choose in which way do you want to include tower rushes:\n")
        print("1. Do not include tower rushes in the roulette in any way.")
        print("2. Include every tower rush in the roulette from the very start.")
        print("3. Add tower rushes to the roulette only when you beat every tower in an area once, and increase the limit to 2 when you beat every tower twice, to 3 when you beat every tower 3 times, and so on.")
    def run(self):
        while True:
            self.__print_menu()
            choice = input("Choose an option from the menu:")
            if choice == "1":
                self.__ui_create_roulette()
            elif choice == "2" and self.__roulette_active:
                self.__ui_show_roulette()
            elif choice == "3" and self.__roulette_active:
                self.__ui_save_roulette()
            elif choice == "4" and self.__roulette_active:
                self.__ui_generate_random_structure()
            elif choice == "5":
                break
            else:
                if choice in ["2","3","4"] and not self.__roulette_active:
                    print(Fore.BLUE + "This option is valid, but you can't access it until you created the roulette." + Style.RESET_ALL)
                else:
                    print(Fore.RED + "This option was not found in the menu, please try again." + Style.RESET_ALL)
    def __ui_create_roulette(self):
        file_option = self.__read_option()
        try:
            if file_option == "file":
                file_name = input("Please enter the name of the file that contains the roulette:")
                self.__roulette_service.create_roulette(file_name=file_name)
                print(Fore.BLUE + "The roulette has been loaded successfully, and the other options in the menu are now open." + Style.RESET_ALL)
                self.__roulette_active = True
            else:
                beat_limit = int(input("Please enter how many times do you want to beat a tower before it is eliminated from the roulette:"))
                self.__roulette_service.create_roulette(beat_limit=beat_limit)
                self.__print_tower_rush_options()
                self.__read_tower_rush_option()
                if self.__roulette_service.get_tower_rush_mode() != "none":
                    response = self.__read_yes_no("Do you want to include Pit of Misery Tower Rush in this roulette?(y/n)")
                    self.__roulette_service.set_include_pomtr(response)
                print(Fore.BLUE + "The roulette has been created successfully, and the other options in the menu are now open." + Style.RESET_ALL)
                self.__roulette_active = True
        except ValidationException as error:
            print(Fore.RED + str(error) + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "You did not enter a valid number, please try again." + Style.RESET_ALL)
    def __ui_save_roulette(self):
        try:
            file_name = input("Please enter the name of the file in which you want to save the roulette:")
            self.__roulette_service.save_roulette(file_name)
            print(Fore.BLUE + "The roulette has been saved successfully in the desired folder, though it will not appear until you exit the application." + Style.RESET_ALL)
        except ValidationException as error:
            print(Fore.RED + str(error) + Style.RESET_ALL)
    def __ui_show_roulette(self):
        print(self.__roulette_service.show_roulette())
    def __ui_generate_random_structure(self):
        total_structures = self.__roulette_service.get_roulette_total()
        if total_structures[0] >= total_structures[1]:
            print(Fore.RED + "You already beat every tower in this roulette, you cannot generate new towers anymore." + Style.RESET_ALL)
            return
        print(Fore.GREEN + "The roulette will auto-save your beaten towers and your last tower if it is saved in a file, so don't worry about saving in that case." + Style.RESET_ALL)
        last_structure = self.__roulette_service.get_last_structure()
        if last_structure is not None:
            print("The last structure that the roulette gave you before leaving was:\n" + Fore.BLUE + str(last_structure) + "\n" + Style.RESET_ALL)
            self.__mini_random_menu()
        while True:
            random_structure_str = self.__roulette_service.generate_random_structure()
            print("The structure that the roulette gave you is:\n" + Fore.BLUE + random_structure_str + "\n" + Style.RESET_ALL)
            self.__mini_random_menu()
            total_structures = self.__roulette_service.get_roulette_total()
            if total_structures[0] >= total_structures[1]:
                print(Fore.BLUE + "You have beaten every tower that the roulette gave you, congratulations!" + Style.RESET_ALL)
                return
            exit_option = self.__read_yes_no("Do you want to exit the roulette? (y/n):")
            if exit_option:
                return
