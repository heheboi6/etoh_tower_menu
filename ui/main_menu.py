from tkinter.font import Font

from service.structure_service import StructureService
from tkinter import *
from tkinter import ttk

from ui.show_tower_menu import ShowTowerMenu


class MainMenu:
    def __init__(self, structure_service : StructureService):
        self.__structure_service = structure_service
        self.__root = Tk()
        self.__root.title("Main menu")
        self.__root.resizable(True, True)
        self.__root.geometry("370x100")
        self.__root.protocol("WM_DELETE_WINDOW", self.__root.destroy)
        self.__canvas = Canvas(self.__root)
        self.__frame = ttk.Frame(self.__root)
        self.__frame.grid(columnspan=3,rowspan=3)
    def __build_menu(self):
        big_font = Font(family="Times New Roman", size=20)
        small_font = Font(family="Times New Roman", size=12)
        ttk.Label(self.__frame, text="Choose an option from the menu:",font=big_font).grid(column=0, row=0)
        ttk.Button(self.__frame,text = "Show all towers",width=60,command=self.open_show_tower_menu).grid(column=0, row=1)
    def open_show_tower_menu(self):
        new_menu = ShowTowerMenu(self.__structure_service)
        new_menu.run_show_tower_menu()
    def run(self):
        self.__build_menu()
        self.__root.mainloop()