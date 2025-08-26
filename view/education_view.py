from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from controller.education_controller import EducationController
from model.entity.education import Education
from view.component.label_with_text import LabelWithText

# id, person_id, university, grade, average, start_date, end_date



class EducationView:
    def reset_form(self):
        self.id.set(0)
        self.person_id.set(0)
        self.university.set("")
        self.grade.set("")
        self.average.set(0)
        self.start_date.set("")
        self.end_date.set("")
        status, education_list = self.education_controller.find_all()
        if status:
            self.show_data_on_table(education_list)

    def show_data_on_table(self, education_list):
        for education in self.table.get_children():
            self.table.delete(education)

        if education_list:
            for education in education_list:
                self.table.insert("", END, values=education.to_tuple())

    def select_education(self, event):
        selected_education = self.table.item(self.table.focus())["values"]
        if selected_education:
            education = Education(*selected_education)
            self.id.set(education.id)
            self.person_id.set(education.person_id)
            self.university.set(education.university)
            self.average.set(education.average)
            self.grade.set(education.grade)
            self.start_date.set(education.start_date)
            self.end_date.set(education.end_date)

    def search_person_id(self, event):
        status, education_list = self.education_controller.find_by_person_id(self.search_person_id_var.get())
        if status:
            self.show_data_on_table(education_list)

    def search_id(self, event):
        status, education_list = self.education_controller.find_by_id(self.search_id_var.get())
        if status:
            self.show_data_on_table(education_list)

    def save_click(self):
        status,message=self.education_controller.save(self.person_id.get(),
        self.university.get(),self.grade.get(),self.average.get(),self.start_date.get(),self.end_date.get())
        if status:
            messagebox.showinfo("Saved",f"{message} Saved")
        else:
            messagebox.showerror("Error",message)

    def edit_click(self):
        status, message = self.education_controller.save(self.person_id.get(),
                 self.university.get(), self.grade.get(), self.average.get(),
                 self.start_date.get(), self.end_date.get())
        if status:
            messagebox.showinfo("Edited", f"{message} Edited")
            self.reset_form()
        else:
            messagebox.showerror("Error", message)

    def delete_click(self):
        status, message = self.education_controller.delete(self.id.get())
        if status:
            messagebox.showinfo("Deleted", f"{message} Deleted")
            self.reset_form()
        else:
            messagebox.showerror("Error", message)



    def __init__(self):
        self.education_controller = EducationController()
        self.window = Tk()
        self.window.title("Class Info")
        self.window.geometry("855x450")
        self.window.resizable(False, False)

        self.id = IntVar()
        LabelWithText(self.window,"Id",self.id,20,30)

        self.person_id = StringVar()
        LabelWithText(self.window,"Person ID",self.person_id,20,70)

        self.university = StringVar()
        LabelWithText(self.window,"University",self.university,20,110)

        self.grade = StringVar()
        LabelWithText(self.window,"Grade",self.grade,20,150)

        self.average = IntVar()
        LabelWithText(self.window,"Average",self.average,20,190)

        self.start_date = StringVar()
        LabelWithText(self.window,"Start Date",self.start_date,20,230)

        self.end_date = StringVar()
        LabelWithText(self.window,"End Date",self.end_date,20,270)

        Button(self.window, text="Save", width=7,command=self.save_click).place(x=20, y=330)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=87, y=330)
        Button(self.window, text="Delete",  width=7,command=self.delete_click).place(x=152, y=330)
        Button(self.window, text="Clear", width=26,command=self.reset_form).place(x=20, y=370)


        self.search_id_var = StringVar()
        LabelWithText(self.window,"Search ID",self.search_id_var,250,20).text.bind("<KeyRelease>", self.search_id)

        self.search_person_id_var = StringVar()
        LabelWithText(self.window,"Search Person ID",self.search_person_id_var,600,20).text.bind("<KeyRelease>", self.search_person_id)

        self.table = ttk.Treeview(self.window, columns=[1, 2, 3, 4,5,6,7], show="headings",height=15)
        self.table.heading(1, text="Id")
        self.table.heading(2, text="Person Id")
        self.table.heading(3, text="University")
        self.table.heading(4, text="Grade")
        self.table.heading(5, text="Average")
        self.table.heading(6, text="Start Date")
        self.table.heading(7, text="End Date")

        self.table.column(1, width=70)
        self.table.column(2, width=110)
        self.table.column(3, width=110)
        self.table.column(4, width=70)
        self.table.column(5, width=70)
        self.table.column(6, width=70)
        self.table.column(7, width=70)

        self.table.bind("<<TreeviewSelect>>", self.select_education)
        self.table.place(x=240, y=70)

        self.window.mainloop()



