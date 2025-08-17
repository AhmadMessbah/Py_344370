from tkinter.ttk import Entry, Button
from _tkinter import *
from tkinter import ttk, Tk, StringVar, IntVar, Label
from model.repository.medical_repository import *
from model.tools.validation import *
from view.skill_view import close_window





# 5
def reset_form():
    id.set(0)
    person_id.set(0)
    disease.set("")
    medicine.set("")
    doctor.set("")
    # visit_date("")
    status.set("")

# 6
def save_click():
    pass
    # if title_validator(title.get()) and title_validator(teacher.get()) and class_number_validator(class_number.get()) and 0<unit.get()<=24:
    #     save(title.get(),teacher.get(),class_number.get(),unit.get())
    #     messagebox.showinfo("Save", f"Successfully saved!")
    #     reset_form()
    #     show_data_on_table(find_all())
    # else:
    #     messagebox.showerror("Error", "Please enter a valid title/teacher/class number/unit")

def edit_click():
    pass
    # if title_validator(title.get()) and title_validator(teacher.get()) and class_number_validator(class_number.get()) and 0<unit.get()<=24:
    #     edit(code.get(),title.get(), teacher.get(), class_number.get(), unit.get())
    #     messagebox.showinfo("Edit", f"Successfully edited!")
    #     reset_form()
    #     show_data_on_table(find_all())
    # else:
    #     messagebox.showerror("Error", "Please enter a valid code/title/teacher/class number/unit")


def remove_click():
    pass
    # remove(code.get())
    # messagebox.showinfo("Remove", f"Successfully removed!")
    # reset_form()
    # show_data_on_table(find_all())

# 7
def table_select(event):
    pass
    # table_row=table.focus()
    # selected=table.item(table_row)["values"]
    # if selected:
    #     code.set(selected[0])
    #     title.set(selected[1])
    #     teacher.set(selected[2])
    #     class_number.set(selected[3])
    #     unit.set(selected[4])



# 0
win = Tk()
# geometry-title
win.title("Medical")
win.resizable(width=False, height=False)
win.geometry("800x360")


# 1
# # id
id=IntVar()
Label(win,text="id").place(x=20,y=20)
# Entry(win, textvariable=id).place(x=100,y=20)
Entry(win, textvariable=id).place(x=100,y=20)

# person_id
person_id=IntVar()
Label(win,text="person_id").place(x=20,y=60)
Entry(win, textvariable=person_id).place(x=100,y=60)
# Entry(win, textvariable=person_id).place(x=100,y=60)

# disease
disease=StringVar()
Label(win,text="disease").place(x=20,y=100)
Entry(win, textvariable=disease).place(x=100,y=100)


#  medicine
medicine=StringVar()
Label(win,text="medicine ").place(x=20,y=140)
Entry(win, textvariable=medicine).place(x=100,y=140)

# doctor
doctor=StringVar()
Label(win,text="doctor").place(x=20,y=180)
Entry(win, textvariable=doctor).place(x=100,y=180)


# visit_date
visit_date=StringVar()
Label(win,text="visit_date").place(x=20,y=220)
Entry(win, textvariable=visit_date).place(x=100,y=220)


# status
status=StringVar()
# Label(win,text="status").place(x=20,y=260)
Label(win,text="status").place(x=20,y=255)
Entry(win, textvariable=status).place(x=100,y=255)



# 2
# Buttons (Save-Edit-Remove)
# Button(win, text="Clear", command=reset_form, width=29).place(x=20,y=250)
Button(win, text="Save", command=save_click, width=7).place(x=20,y=300)
Button(win, text="Edit", command=edit_click, width=7).place(x=95,y=300)
Button(win, text="Remove", command=remove_click, width=7).place(x=170,y=300)



# 3
# search_doctor
search_doctor = StringVar()
Label(win,text="Search Doctor").place(x=470,y=20)
search_doctor_txt = Entry(win, textvariable=search_doctor)
search_doctor_txt.bind("<KeyRelease>", search_doctor)
search_doctor_txt.place(x=325,y=20)


# 4
# Table
table = ttk.Treeview(win, height=12,columns=(1,2,3,4,5,6,7),show="headings")
table.column(1, width=70)
table.column(2, width=70)
table.column(3, width=70)
table.column(4, width=70)
table.column(5, width=70)
table.column(6, width=70)
table.column(7, width=70)

table.heading(1, text="ID")
table.heading(2, text="Person_Id")
table.heading(3, text="Disease")
table.heading(4, text="Medicine")
table.heading(5, text="Doctor")
table.heading(6, text="Visit_Date")
table.heading(7, text="Status")

# TreeviewSelect
# bind--> table_select
table.bind("<<TreeviewSelect>>", table_select)

table.place(x=250, y = 60)


# win.protocol("WM_DELETE_WINDOW", close_window)


reset_form()

win.mainloop()



