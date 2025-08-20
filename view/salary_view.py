from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk

from controller.salary_controller import SalaryController
from model.entity.salary import Salary
from view.component.label_with_text import LabelWithText

class SalaryView:
    def reset_form(self):
        self.id.set(0)
        self.person_id.set(0)
        self.pay_for_hours.set(0)
        self.weekly_hours.set(0)
        self.end_date.set("")
        self.employment_type.set("")
        status, salary_list = self.salary_controller.find_all()
        if status:
            self.show_data_on_table(salary_list)

    def show_data_on_table(self, salary_list):
        for item in self.tabel.get_children():
            self.tabel.delete(item)
        if salary_list:
            for salary in salary_list:
                self.tabel.insert("",END,values=salary.to_tuple())

    def select_salary(self, event):
        selected_id = self.tabel.item(self.tabel.focus(), "values")
        if selected_id:
            salary=Salary(*selected_id)
            self.id.set(salary.id)
            self.person_id.set(salary.person_id)
            self.pay_for_hours.set(salary.pay_for_hours)
            self.weekly_hours.set(salary.weekly_hour)
            self.end_date.set(salary.end_date)
            self.employment_type.set(salary.employment_type)

    def search(self,event):
        status, salary_list = self.salary_controller.find_by_id (self.search_id.get()) and self.salary_controller.find_by_person_id(self.search_person_id.get())
        if status:
            self.show_data_on_table(salary_list)

    def save_click(self):
        status, message = self.salary_controller.save(self.id.get(), self.person_id.get(), self.weekly_hours.get(),
                                                      self.pay_for_hours.get(), self.end_date.get(),self.employment_type.get())
        if status:
            msg.showinfo("saved", message)
            self.reset_form()
        else:
            msg.showerror("error", message)

    def edit_click(self):
        status, message = self.salary_controller.edit(self.id.get(), self.person_id.get(), self.weekly_hours.get(),
                                                      self.pay_for_hours.get(), self.end_date.get(),self.employment_type.get())
        if status:
            msg.showinfo("edited", message)
            self.reset_form()
        else:
            msg.showerror("error", message)

    def delete_click(self):
        status, message = self.salary_controller.delete(self.id.get())
        if status:
            msg.showinfo("deleted", message)
            self.reset_form()
        else:
            msg.showerror("error", message)

    def __init__(self):
        self.salary_controller = SalaryController()
        self.win = Tk()
        self.win.title("salary")
        self.win.geometry("680x360")

        self.id=IntVar()
        LabelWithText(self.win,"ID",self.id,20,20)

        self.person_id = IntVar()
        LabelWithText(self.win, "person id",self.person_id,20,60)

        self.weekly_hours = IntVar()
        LabelWithText(self.win, "weekly hours",self.weekly_hours,20,100)

        self.pay_for_hours = IntVar()
        LabelWithText(self.win, "pay for hours",self.pay_for_hours,20,140)

        self.end_date = StringVar()
        LabelWithText(self.win, "end date",self.end_date,20,180)

        self.employment_type = StringVar()
        LabelWithText(self.win, "employment type",self.employment_type,20,220)

        self.search_person_id = IntVar()
        LabelWithText(self.win, "search person id",self.search_person_id,220,20)

        self.search_id = IntVar()
        LabelWithText(self.win, "search person id",self.search_id,410,60)



        Button(self.win, text="save", width=7, command=self.save_click).place(x=20, y=300)
        Button(self.win, text="edit", width=7, command=self.edit_click).place(x=90, y=300)
        Button(self.win, text="remove", width=7, command=self.delete_click).place(x=160, y=300)
        # tabel
        self.tabel = ttk.Treeview(self.win, height=12, columns=(1, 2, 3, 4, 5), show="headings")
        self.tabel.column(1, width=60)
        self.tabel.column(2, width=90)
        self.tabel.column(3, width=90)
        self.tabel.column(4, width=70)
        self.tabel.column(5, width=90)

        # tabel taitel
        self.tabel.heading(1, text="person id")
        self.tabel.heading(2, text="weekly hours")
        self.tabel.heading(3, text="pay for hours")
        self.tabel.heading(4, text="end date")
        self.tabel.heading(5, text="employment_type")

        self.tabel.bind("<<TreeviewSelect>>", self.select_salary)
        self.tabel.place(x=250, y=60)

        self.reset_form()
        self.win.mainloop()









# def reset_form():
#
#     person_id.set()
#     weekly_hours.set()
#     pay_for_hours.set()
#     end_date.set()
#     employment_type.set()
#
#     show_date_on_table(find_all())
#
#
# def select_product(event):
#     tabel_raw = tabel.focus()
#     selected = tabel.item(tabel_raw)['values']
#     print(tabel_raw, selected)
#     person_id.set(selected[0])
#     weekly_hours.set(selected[1])
#     pay_for_hours.set(selected[2])
#     end_date.set(selected[3])
#     employment_type.set(selected[4])
#
#
# def show_date_on_table(product_list):
#     for item in tabel.get_children():
#         tabel.delete(item)
#
#     for product in product_list:
#         tabel.insert("", END, values=product)
#
#
# product_list = []
#
#
# def save_check():
#     save(person_id.get(), weekly_hours.get(), pay_for_hours.get(), end_date.get(), employment_type.get())
#     messagebox.showinfo("Saved", f"Saved successfully!")
#     reset_form()
#     show_date_on_table(find_all())
#
#
# def edit_check():
#     edit(id.get(), person_id.get(), weekly_hours.get(), pay_for_hours.get(), end_date.get(), employment_type.get())
#     messagebox.showinfo("edit", f"edite successfully!")
#     reset_form()
#     show_date_on_table(find_all())
#
#
# def remove_check():
#     delete(id.get)
#     messagebox.showinfo("delete", f"delete successfully!")
#     reset_form()
#     show_date_on_table(find_all())
#
