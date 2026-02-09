import tkinter
from tkinter import Tk, Canvas, ttk, StringVar, IntVar

from service.structure_service import StructureService

class ShowTowerMenu:
    __OPTIONS = ["name","area"]
    def __init__(self, structure_service : StructureService):
        self.__structure_service = structure_service
        self.__root = Tk()
        self.__root.title("Show towers")
        self.__root.resizable(True, True)
        self.__root.geometry("1200x800")
        self.__root.protocol("WM_DELETE_WINDOW", self.__root.destroy)
        self.__initialize_table_frame()
        self.__interactive_frame = tkinter.Frame(self.__root)
        self.__interactive_frame.grid()
        self.__value_inside = StringVar(self.__root)
        self.__value_inside.set("name")
        self.__check_value = IntVar(self.__root)
        self.__check_value.set(False)
    def __initialize_table_frame(self):
        self.__frame = tkinter.Frame(self.__root)
        self.__frame.grid()
        self.__canvas = Canvas(self.__frame)
    def run_show_tower_menu(self):
        self.__build_menu()
        self.__root.mainloop()
    def __build_menu(self):
        ttk.Button(self.__interactive_frame, text="Show all towers:",command=self.__ui_show_all_structures).grid(column=0, row=0)
        ttk.OptionMenu(self.__interactive_frame,self.__value_inside,self.__value_inside.get(),*self.__OPTIONS).grid(column=1, row=0)
        ttk.Checkbutton(self.__interactive_frame,variable=self.__check_value,text="Reverse order",offvalue=False,onvalue=True).grid(column=2, row=0)
    def __ui_show_all_structures(self):
        self.__frame.destroy()
        self.__initialize_table_frame()
        self.__structure_service.sort_by_parameter(key=self.__value_inside.get(),reverse=self.__check_value.get())
        result = self.__structure_service.show_all_structures()
        row = -1
        for structure in result:
            row += 1
            area = structure.get_area()
            name = structure.get_name()
            ttk.Label(self.__frame, text=area).grid(column=0, row=row)
            ttk.Label(self.__frame, text=name).grid(column=1, row=row)
        self.__frame.update()
        size_tuple = self.__frame.grid_bbox(0,0,1,row)
        row += 1
        max_x = size_tuple[2]
        inc_y = size_tuple[3] // row
        self.__canvas.config(width=max_x, height=size_tuple[3])
        self.__canvas.grid(column=0, row=0, columnspan=2, rowspan=row)
        current_y = 2.0
        self.__canvas.create_line(0, 1, max_x, 1, fill="black")
        #for index in range(len(result)):
            #current_y += inc_y
            #self.__canvas.create_line(0, current_y, max_x, current_y, fill="black")
        self.__frame.update()

