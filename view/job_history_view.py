from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk

from controller.job_history_controller import JobHistoryController
from model.entity.job_history import JobHistory
from view.component.label_with_text import LabelWithText

#id, person_id, organisation, job_title, start_date, end_date, description

class JobHistoryView:


    def reset_form(self):
        self.id.set(0)
        self.person_id.set("")
        self.organisation.set("")
        self.job_title.set("")
        self.start_date.set("")
        self.end_date.set("")
        self.description.set("")
        status, job_history_list = self.job_history_controller.find_all()
        if status:
            self.show_data(job_history_list)



    def save_click(self):
        status, message = self.job_history_controller.save(
            self.id.get(),
            self.person_id.get(),
            self.organisation.get(),
            self.job_title.get(),
            self.start_date.get(),
            self.end_date.get(),
            self.description.get()
        )
        if status:
            msg.showinfo("saved",f"{message} Saved")
        else:
            msg.showerror("Error", message)



    def edit_click(self):
        status, message = self.job_history_controller.save(
            self.id.get(),
            self.person_id.get(),
            self.organisation.get(),
            self.job_title.get(),
            self.start_date.get(),
            self.end_date.get(),
            self.description.get()
        )
        if status:
            msg.showinfo("Edited", f"message Edited")
            self.reset_form()
        else:
            msg.showerror("Error", message)


    def delete_click(self):
        status, message = self.job_history_controller.delete(self.id.get())
        if status:
            msg.showinfo("deleted",f"message Deleted")
        else:
            msg.showerror("Error", message)



    def search_person(self, event):
        status, job_history_list = self.job_history_controller.find_by_job_title(self.search_job_title.get())
        if status:
            self.show_data(job_history_list)


    def show_data(self, job_history_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if job_history_list:
            for person in job_history_list:
                self.table.insert("", END, values=person.to_tuple())


    def select(self, event):
        selected_person = self.table.item(self.table.focus())["values"]
        if selected_person:
            job_history = JobHistory(*selected_person)
            self.id.set(job_history.id)
            self.person_id.set(job_history.person_id)
            self.organisation.set(job_history.organisation)
            self.job_title.set(job_history.job_title)
            self.start_date.set(job_history.start_date)
            self.end_date.set(job_history.end_date)
            self.description.set(job_history.description)




    def __init__(self):
        self.job_history_controller = JobHistoryController()
        self.window = Tk()
        self.window.title("Job History")
        self.window.geometry("900x500")


        #id
        self.id = IntVar()
        LabelWithText(self.window, "Id", self.id, 20, 30, "readonly")

        #person_id
        self.person_id = IntVar()
        LabelWithText(self.window, "Person Id", self.person_id, 20, 75)

        #organisation
        self.organisation = IntVar()
        LabelWithText(self.window, "Organisation", self.organisation, 20, 120)

        #job title
        self.job_title = IntVar()
        LabelWithText(self.window, "Job Title", self.job_title, 20, 165)

        #start date
        self.start_date = IntVar()
        LabelWithText(self.window, "Start Date", self.start_date, 20, 210)

        #end date
        self.end_date = IntVar()
        LabelWithText(self.window, "End Date", self.end_date, 20, 255)


        #description
        self.description = StringVar()
        LabelWithText(self.window, "Description", self.description, 20, 300)

        #buttons
        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=380)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=91, y=380)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=166, y=380)
        Button(self.window, text="Clear", width=28, command=self.reset_form).place(x=20, y=420)

        #search by job title
        self.search_job_title = StringVar()
        LabelWithText(self.window, "Search Job Title", self.search_job_title, 330, 30).text.bind("<keyRelease>", self.search_person)



        #table
        self.table = ttk.Treeview(self.window, height = 15, columns = ("id", "person_id","organisation", "job_title", "start_date", "end_date", "description"), show="headings")


        self.table.column("id", width=60)
        self.table.column("person_id", width=65)
        self.table.column("organisation", width=77)
        self.table.column("job_title", width=65)
        self.table.column("start_date", width=65)
        self.table.column("end_date", width=65)
        self.table.column("description", width=90)


        self.table.heading("id", text="ID")
        self.table.heading("person_id", text="Person ID")
        self.table.heading("organisation", text="Organisation")
        self.table.heading("job_title", text="Job Title")
        self.table.heading("start_date", text="Start Date")
        self.table.heading("end_date", text="End Date")
        self.table.heading("description", text="Description")

        self.table.bind("<<TreeviewSelect>>", self.select)

        self.table.place(x=330, y=120)

        self.reset_form()
        self.window.mainloop()