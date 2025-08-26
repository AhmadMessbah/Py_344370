from tkinter import *

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
            self.id.set(person.id)
            self.name.set(person.name)
            self.family.set(person.family)
            self.age.set(person.age)




