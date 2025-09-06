from time import strptime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from controller.education_controller import EducationController
from model.entity.education import Education
from view.component.label_with_text import LabelWithText
from persiantools.jdatetime import JalaliDate
from datetime import datetime

# id, person_id, university, grade, average, start_date, end_date



class EducationView:
    def reset_form(self):
        self.id.set(0)
        self.person_id.set("")
        self.university.set("")
        self.grade.set("")
        self.average.set(0)
        self.start_date.set("")
        self.end_date.set("")
        status, education_list = self.education_controller.find_all()
        if status:
            self.table.refresh_table(education_list)

    def select_education(self,selected_person):
        education=Education(*selected_person)
        self.id.set(education.id)
        self.person_id.set(education.person_id)
        self.university.set(education.university)
        self.grade.set(education.grade)
        self.average.set(education.average)
        self.start_date.set(education.start_date)
        self.end_date.set(education.end_date)

        start_date_str = self.start_date.get()
        start_date_jalali = JalaliDate.strptime(start_date_str, "%Y-%m-%d")

        end_date_str = self.end_date.get()
        end_date_jalali = JalaliDate.strptime(end_date_str, "%Y-%m-%d")


    def search_person_id(self, event):
        status, education_list = self.education_controller.find_by_person_id(self.search_person_id_var.get())
        if status:
            self.table.refresh_table(education_list)

    def search_id(self, event):
        status, education_list = self.education_controller.find_by_id(self.search_id_var.get())
        if status:
            self.table.refresh_table(education_list)

    def save_click(self):
        status,message=self.education_controller.save(self.person_id.get(),
        self.university.get(),self.grade.get(),self.average.get(),self.start_date.get(),self.end_date.get())
        if status:
            messagebox.showinfo("Saved",f"{message} Saved")
            self.reset_form()
        else:
            messagebox.showerror("Error",message)

    def edit_click(self):
        status, message = self.education_controller.edit(self.id.get(),self.person_id.get(),
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
        self.window.title("Education Info")
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

        self.average = DoubleVar()
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

        self.table = Table(
            self.window,
            ["ID","Person ID","University","Grade","Average","Start Date","End Date"],
            [70,110,110,70,70,70,70],
            240,70,
            self.select_education
        )
        self.reset_form()
        self.window.mainloop()

class Table:
    def __init__(self, master, headers, widths, x, y, select_function):
        self.master = master
        self.x = x
        self.y = y
        self.headers = headers
        self.widths = widths
        self.select_function = select_function
        self.columns = list(range(len(headers)))

        self.table = ttk.Treeview(self.master, columns=self.columns, show="headings")
        for col in self.columns:
            self.table.column(col, width=self.widths[col])
            self.table.heading(col, text=self.headers[col])

        self.table.bind("<ButtonRelease>", self.select_table)
        self.table.bind("<KeyRelease>", self.select_table)
        self.table.place(x=x, y=y)

    def refresh_table(self, data_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if data_list:
            for data in data_list:
                self.table.insert("", END, values=tuple(data.__dict__.values()))

    def select_table(self, event):
        data = self.table.item(self.table.focus())["values"]
        self.select_function(data)






