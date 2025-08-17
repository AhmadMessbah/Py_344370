from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from model.repository.education_repository import *
from view.job_history_view import person_id


#id, person_id, university, grade, average, start_date, end_date
def reset_form():
    default_id.set(0)
    person_id.set(0)
    university.set("")
    average.set(0)
    start_date.set("")
    end_date.set("")
    show_data_on_table(find_all())

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
def select ():
    pass


window = Tk()
window.title("Class Info")
window.geometry("700x370")
window.resizable(False, False)

#id
default_id=IntVar()
Label(window, text="Id").grid(row=0, column=0)
Entry(window, textvariable=default_id).grid(row=1, column=0)

#person_id
person_id=IntVar()
Label(window, text="Person Id").grid(row=0, column=1)
Entry(window, textvariable=person_id).grid(row=1, column=1)

#university
university=StringVar()
Label(window, text="University").grid(row=0, column=2)
Entry(window, textvariable=university).grid(row=1, column=2)

#grade
grade=IntVar()
Label(window, text="Grade").grid(row=0, column=3)
Entry(window, textvariable=grade).grid(row=1, column=3)


#average
average=IntVar()
Label(window, text="Average").grid(row=0, column=3)
Entry(window, textvariable=average).grid(row=1, column=3)


# start_date
start_date=StringVar()
Label(window, text="Start Date").grid(row=0, column=3)
Entry(window, textvariable=start_date).grid(row=1, column=3)


# end_date
end_date=StringVar()
Label(window, text="End Date").grid(row=0, column=3)
Entry(window, textvariable=end_date).grid(row=1, column=3)


#buttons


#table



reset_form()
window.mainloop()