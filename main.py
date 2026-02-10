from repo.structure_file_repo import StructureFileRepo
from service.roulette_service import RouletteService
from service.structure_service import StructureService
from ui.main_menu import MainMenu

structure_repo = StructureFileRepo("structures.txt")
structure_service = StructureService(structure_repo)
roulette_service = RouletteService(structure_repo)
menu = MainMenu(structure_service, roulette_service)
menu.run()