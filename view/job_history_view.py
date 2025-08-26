from tkinter import *
from tkinter import messagebox, Tk
from tkinter import ttk

from scripts.regsetup import description


#id, person_id, organisation, job_title, start_date, end_date, description

def reset_form():
    pass


def save_click():
    pass


def delete_click():
    pass


def search_person():
    pass


def show_data():
    pass


def select():
    pass


window = Tk()
window.title("Job History")
window.geometry("900x500")
window.resizable(False, False)


#id
system_id = IntVar()
Label(window, text="ID").place(x=20, y=30)
Entry(window, textvariable=system_id).place(x=100, y=30)

#person_id
person_id = StringVar()
Label(window, text="Person ID").place(x=20, y=75)
Entry(window, textvariable=person_id).place(x=100, y=75)

#organisation
organisation = StringVar()
Label(window, text="Organisation").place(x=20, y=120)
Entry(window, textvariable=organisation).place(x=100, y=120)

#job title
job_title = StringVar()
Label(window, text="Job Title").place(x=20, y=165)
Entry(window, textvariable=job_title).place(x=100, y=165)

#start date
start_date = StringVar()
Label(window, text="Start Date").place(x=20, y=210)
Entry(window, textvariable=start_date).place(x=100, y=210)

#end date
end_date = StringVar()
Label(window, text="End Date").place(x=20, y=255)
Entry(window, textvariable=end_date).place(x=100, y=255)


#description
description_ = StringVar()
Label(window, text="Description").place(x=20, y=300)
Entry(window, textvariable=description_).place(x=100, y=300)

#buttons
Button(window, text="Save", width=7).place(x=20, y=380)
Button(window, text="Edit", width=7).place(x=91, y=380)
Button(window, text="Delete", width=7).place(x=166, y=380)
Button(window, text="Clear", width=28).place(x=20, y=420)

#search by job title
search_job_title = StringVar()
Label(window, text="Search Job Title").place(x=330, y=30)
Entry(window, textvariable=search_job_title).place(x=430, y=30)

#search by organisation
search_organisation = StringVar()
Label(window, text="Search Organisation").place(x=580, y=30)
Entry(window, textvariable=search_organisation).place(x=700, y=30)


#table
table = ttk.Treeview(window, height = 15, columns = ("id", "person_id","organisation", "job_title", "start_date", "end_date", "description"), show="headings")


table.column("id", width=60)
table.column("person_id", width=65)
table.column("organisation", width=77)
table.column("job_title", width=65)
table.column("start_date", width=65)
table.column("end_date", width=65)
table.column("description", width=90)


table.heading("id", text="ID")
table.heading("person_id", text="Person ID")
table.heading("organisation", text="Organisation")
table.heading("job_title", text="Job Title")
table.heading("start_date", text="Start Date")
table.heading("end_date", text="End Date")
table.heading("description", text="Description")

table.place(x=330, y=120)







window.mainloop()