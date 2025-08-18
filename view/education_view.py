from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from controller import education_controller


# id, person_id, university, grade, average, start_date, end_date
def reset_form():
    default_id.set(0)
    person_id.set("")
    university.set("")
    average.set(0)
    start_date.set("")
    end_date.set("")
    show_data_on_table(education_controller.find_all())


def save_click():
    pass


def edit_click():
    pass


def delete_click():
    pass


def search_person():
    pass


def show_data_on_table(table):
    pass


def select():
    pass


window = Tk()
window.title("Class Info")
window.geometry("855x450")
window.resizable(False, False)

# id
default_id = IntVar()
Label(window, text="Id").place(x=20, y=30)
Entry(window, textvariable=default_id, state="readonly").place(x=86, y=30)

# person_id
person_id = StringVar()
Label(window, text="Person Id").place(x=20, y=70)
Entry(window, textvariable=person_id).place(x=86, y=70)

# university
university = StringVar()
Label(window, text="University").place(x=20, y=110)
Entry(window, textvariable=university).place(x=86, y=110)

# grade
grade = StringVar()
Label(window, text="Grade").place(x=20, y=150)
Entry(window, textvariable=grade).place(x=86, y=150)

# average
average = IntVar()
Label(window, text="Average").place(x=20, y=190)
Entry(window, textvariable=average).place(x=86, y=190)

# start_date
start_date = StringVar()
Label(window, text="Start Date").place(x=20, y=230)
Entry(window, textvariable=start_date).place(x=86, y=230)

# end_date
end_date = StringVar()
Label(window, text="End Date").place(x=20, y=270)
Entry(window, textvariable=end_date).place(x=86, y=270)

# buttons
Button(window, text="Save", command=save_click, width=7).place(x=20, y=330)
Button(window, text="Edit", command=edit_click, width=7).place(x=87, y=330)
Button(window, text="Delete", command=delete_click, width=7).place(x=152, y=330)
Button(window, text="Clear", command=search_person, width=26).place(x=20, y=370)

# search by name
search_name = StringVar()
Label(window, text="Search Name").place(x=250, y=20)
Entry(window, textvariable=search_name).place(x=340, y=20)

# search by grade
search_grade = StringVar()
Label(window, text="Search Grade").place(x=610, y=20)
Entry(window, textvariable=search_grade).place(x=700, y=20)

# table
table = ttk.Treeview(window, height=15,columns=("id", "person_id", "university", "grade", "average", "start_date", "end_date"),show="headings")

table.column("id", width=82)
table.column("person_id", width=82)
table.column("university", width=82)
table.column("grade", width=82)
table.column("average", width=82)
table.column("start_date", width=82)
table.column("end_date", width=82)

table.heading("id", text="Id")
table.heading("person_id", text="Person id")
table.heading("university", text="University")
table.heading("grade", text="Grade")
table.heading("average", text="Average")
table.heading("start_date", text="Start Date")
table.heading("end_date", text="End Date")

# table.bind("<<TreeviewSelect>>", select)
table.place(x=252, y=70)

reset_form()
window.mainloop()
