from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk

from controller.person_controller import PersonController
from model.entity.person import Person
from view.component.label_with_text import LabelWithText


class PersonView:
    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.age.set(0)
        status, person_list = self.person_controller.find_all()
        if status:
            self.show_data_on_table(person_list)

    def show_data_on_table(self, person_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if person_list:
            for person in person_list:
                self.table.insert("", END, values=person.to_tuple())

    def select_person(self, event):
        selected_person = self.table.item(self.table.focus())["values"]
        if selected_person:
            person = Person(*selected_person)
            self.id.set(person.id)
            self.name.set(person.name)
            self.family.set(person.family)
            self.age.set(person.age)

    def search(self, event):
        status, person_list = self.person_controller.find_by_name_and_family(self.search_name.get(),
                                                                             self.search_family.get())
        if status:
            self.show_data_on_table(person_list)

    def save_click(self):
        status, message = self.person_controller.save(self.name.get(), self.family.get(), self.age.get())
        if status:
            msg.showinfo("Saved", f"{message} Saved")
            self.reset_form()
        else:
            msg.showerror("Error", message)

    def edit_click(self):
        status, message = self.person_controller.edit(self.id.get(), self.name.get(), self.family.get(), self.age.get())
        if status:
            msg.showinfo("Edited", f"message Edited")
            self.reset_form()
        else:
            msg.showerror("Error", message)

    def delete_click(self):
        status, message = self.person_controller.delete(self.id.get())
        if status:
            msg.showinfo("Deleted", f"message Deleted")
            self.reset_form()
        else:
            msg.showerror("Error", message)

    def __init__(self):
        self.person_controller = PersonController()
        self.win = Tk()
        self.win.title("Person Profile")
        self.win.geometry("600x315")

        self.id = IntVar()
        LabelWithText(self.win, "Id", self.id, 20, 20, "readonly")

        self.name = StringVar()
        LabelWithText(self.win, "Name", self.name, 20, 60)

        self.family = StringVar()
        LabelWithText(self.win, "Family", self.family, 20, 100)

        self.age = IntVar()
        LabelWithText(self.win, "Age", self.age, 20, 140)

        self.search_name = StringVar()
        LabelWithText(self.win, "Name Search", self.search_name, 220, 20).text.bind("<KeyRelease>", self.search)

        self.search_family = StringVar()
        LabelWithText(self.win, "Family Search", self.search_family, 410, 20).text.bind("<KeyRelease>", self.search)

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4], show="headings")
        self.table.heading(1, text="Id")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Family")
        self.table.heading(4, text="Age")

        self.table.column(1, width=70)
        self.table.column(2, width=110)
        self.table.column(3, width=110)
        self.table.column(4, width=70)

        self.table.bind("<<TreeviewSelect>>", self.select_person)
        self.table.place(x=220, y=60)

        Button(self.win, text="New Person", width=23, command=self.reset_form).place(x=20, y=220)
        Button(self.win, text="Save", width=6, command=self.save_click).place(x=20, y=260)
        Button(self.win, text="Edit", width=6, command=self.edit_click).place(x=80, y=260)
        Button(self.win, text="Delete", width=6, command=self.delete_click).place(x=140, y=260)

        self.reset_form()
        self.win.mainloop()
