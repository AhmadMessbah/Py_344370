from tkinter import *
from controller.child_controller import *
from model.entity.childs import Child


from openpyxl.workbook import child
from streamlit import status


class Childs_View:
    def save_click(self ):
        self.id.set(0)
        self.person_id("")
        self.name("")
        self.family("")
        self.birth_date("")
        self.status("")
        status , child_list= self.child_controller.find_all
        if status:
            self.show_data_on_table(child_list)

    def show_data_on_table(self, child_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if child_list:
            for person in child_list:
                self.table.insert("", END, values=child.to_tuple())

    def select_child(self, event):
        selected_child = self.table.item(self.table.focus())["values"]
        if selected_child:
            person = child(*selected_child)
            self.id.set(child.id)
            self.person_id.set(child.person_id)
            self.name.set(child.name)
            self.family.set(child.family)
            self.birth_date.set(child.birth_date)
            self.status.set(child.status)

    def search(self, event):
        status, child_list = self.child_controller.find_by_name_and_family(self.search_name.get(), self.search_family.get())

        if status:
            self.show_data_on_table(child_list)


    def  save_click
        pass

    def edit_click(self):
        pass

    def delete_click(self):
        pass

    def __init__(self):
        self.child_controller = ChildController()
        self.win =Tk
        self.win.title=("child profile")
        self.win.geometry("880x400")






