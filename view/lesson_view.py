from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk

from controller.lessons_controller import LessonController
from model.entity.lesson import Lesson
from view.component.label_with_text import LabelWithText

class LessonView:
    def reset_form(self):
        self.id.set(0)
        self.person_id.set("")
        self.title.set("")
        self.teacher.set("")
        self.unit.set(0)
        self.code.set(0)
        status, lessons_list = self.lessons_controller.find_all()
        if status:
            self.show_data_on_table(lessons_list)

    def show_data_on_table(self, lessons_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if lessons_list:
            for lessons in lessons_list:
                self.table.insert("", END, values=lessons.to_tuple())

    def select_lessons(self, event):
        selected_lessons = self.table.item(self.table.focus())["values"]
        if selected_lessons:
            lessons = Lesson(*selected_lessons)
            self.id.set(lessons.id)
            self.title.set(lessons.title)
            self.teacher.set(lessons.teacher)
            self.unit.set(lessons.unit)
            self.code.set(lessons.code)
            self.person_id.set(lessons.person_id)

    def search(self, event):
        status, lessons_list = self.lessons_controller.find_by_title_and_teacher(self.search_title.get(),
                                                                             self.search_teacher.get())
        if status:
            self.show_data_on_table(lessons_list)

    def save_click(self):
        status, message = self.lessons_controller.save(self.title.get(), self.teacher.get(), self.unit.get())
        if status:
            msg.showinfo("Saved", f"{message} Saved")
            self.reset_form()
        else:
            msg.showerror("Error", message)

    def edit_click(self):
        status, message = self.lessons_controller.edit(self.id.get(), self.person_id.get(),self.unit.get(),self.title.get(), self.teacher.get(), self.code.get())
        if status:
            msg.showinfo("Edited", f"message Edited")
            self.reset_form()
        else:
            msg.showerror("Error", message)

    def delete_click(self):
        status, message = self.lessons_controller.delete(self.id.get())
        if status:
            msg.showinfo("Deleted", f"message Deleted")
            self.reset_form()
        else:
            msg.showerror("Error", message)

    def __init__(self):
        self.lessons_controller = LessonController()
        self.win = Tk()
        self.win.title("lesson Profile")
        self.win.geometry("600x315")

        self.id = IntVar()
        LabelWithText(self.win, "Id", self.id, 20, 20, "readonly")

        self.person_id = StringVar()
        LabelWithText(self.win, "person_id", self.person_id, 20, 60)

        self.code = StringVar()
        LabelWithText(self.win, "code", self.code, 20, 100)

        self.unit = IntVar()
        LabelWithText(self.win, "unit", self.unit, 20, 140)

        self.search_title = StringVar()
        LabelWithText(self.win, "title Search", self.search_title, 220, 20).text.bind("<KeyRelease>", self.search)

        self.search_teacher = StringVar()
        LabelWithText(self.win, "teacher Search", self.search_teacher, 410, 20).text.bind("<KeyRelease>", self.search)

        self.table = ttk.Treeview(self.win, columns=[1, 2, 3, 4], show="headings")
        self.table.heading(1, text="Id")
        self.table.heading(2, text="person id")
        self.table.heading(3, text="teacher")
        self.table.heading(4, text="unit")
        self.table.heading(5, text="code")
        self.table.heading(6, text="title")

        self.table.column(1, width=70)
        self.table.column(2, width=110)
        self.table.column(3, width=110)
        self.table.column(4, width=70)
        self.table.column(5, width=110)
        self.table.column(6, width=110)

        self.table.bind("<<TreeviewSelect>>", self.select_lessons)
        self.table.place(x=220, y=60)

        Button(self.win, text="New lesson", width=23, command=self.reset_form).place(x=20, y=220)
        Button(self.win, text="Save", width=6, command=self.save_click).place(x=20, y=260)
        Button(self.win, text="Edit", width=6, command=self.edit_click).place(x=80, y=260)
        Button(self.win, text="Delete", width=6, command=self.delete_click).place(x=140, y=260)

        self.reset_form()
        self.win.mainloop()
