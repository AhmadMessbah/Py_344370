from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from warnings import showwarning

from typing_extensions import ReadOnly

from model.repository.skill_repository import *

def reset_form():
    id.set(0)
    person_id.set("")
    title.set("")
    institute.set("")
    duration.set("")
    register_date.set("")
    score.set(0)

def show_data_on_table():
    pass
def save_click():
    pass

def edit_click():
    pass

def remove_click():
    pass


def table_select(event):
    pass


def close_window():
    if messagebox.askyesno("Exit", "Are you sure ?"):
        win.destroy()


def search_skill(event):
    pass

win = Tk()
win.title("Skill")
win.resizable(width=False, height=False)
win.geometry("850x400")


# id
id=IntVar()
Label(win,text="Id").place(x=20,y=20)
Entry(win, textvariable=id).place(x=100,y=20)

# person id
person_id=IntVar()
Label(win,text="Person id").place(x=20,y=60)
Entry(win, textvariable=person_id).place(x=100,y=60)

# title
title=StringVar()
Label(win,text="Title").place(x=20,y=100)
Entry(win, textvariable=title).place(x=100,y=100)

# institute
institute=StringVar()
Label(win,text="Institute").place(x=20,y=140)
Entry(win, textvariable=institute).place(x=100,y=140)

# duration
duration=StringVar()
Label(win,text="Duration").place(x=20,y=180)
Entry(win, textvariable=duration).place(x=100,y=180)

# register date
register_date=StringVar()
Label(win,text="Register date").place(x=20,y=220)
Entry(win, textvariable=register_date).place(x=100,y=220)

# score
score=IntVar()
Label(win,text="Score").place(x=20,y=260)
Entry(win, textvariable=score).place(x=100,y=260)


# Buttons (Save-Edit-Remove)
Button(win, text="Clear", command=reset_form, width=29).place(x=20,y=300)
Button(win, text="Save", command=save_click, width=7).place(x=20,y=340)
Button(win, text="Edit", command=edit_click, width=7).place(x=95,y=340)
Button(win, text="Remove", command=remove_click, width=7).place(x=170,y=340)

# Search id
id_search = IntVar()
Label(win,text="Search Id").place(x=250,y=20)
id_search_txt = Entry(win, textvariable=id_search)
id_search_txt.bind("<KeyRelease>", )
id_search_txt.place(x=325,y=20)

# Search title and institute
title_institute_search = StringVar()
Label(win,text="Search title and institute").place(x=550,y=20)
title_institute_search = Entry(win, textvariable=title_institute_search)
title_institute_search.bind("<KeyRelease>", )
title_institute_search.place(x=710,y=20)



table = ttk.Treeview(win, height=12,columns=(1,2,3,4,5,6,7),show="headings")
table.column(1, width=70)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=80)
table.column(5, width=80)
table.column(6, width=80)
table.column(7, width=80)

table.heading(1, text="Id ")
table.heading(2, text="Person id")
table.heading(3, text="Title")
table.heading(4, text="Institute")
table.heading(5, text="Duration")
table.heading(6, text="Register date")
table.heading(7, text="Score")


table.bind("<<TreeviewSelect>>", )

table.place(x=250, y = 60)


win.protocol("WM_DELETE_WINDOW",  close_window)

reset_form()

win.mainloop()