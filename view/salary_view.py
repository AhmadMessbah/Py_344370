from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk, messagebox
from model.repository.salary_repository import *


def reset_form():
    person_id.set()
    weekly_hours.set()
    pay_for_hours.set()
    end_date.set()
    employment_type.set()

    show_date_on_table(find_all())


def select_product(event):
    tabel_raw = tabel.focus()
    selected = tabel.item(tabel_raw)['values']
    print(tabel_raw, selected)
    person_id.set(selected[0])
    weekly_hours.set(selected[1])
    pay_for_hours.set(selected[2])
    end_date.set(selected[3])
    employment_type.set(selected[4])

def show_date_on_table(product_list):
    for item in tabel.get_children():
        tabel.delete(item)

    for product in product_list:
        tabel.insert("", END, values=product)

product_list = []


def save_check():
    save(person_id.get(),weekly_hours.get(),pay_for_hours.get(),end_date.get(),employment_type.get())
    messagebox.showinfo("Saved", f"Saved successfully!")
    reset_form()
    show_date_on_table(find_all())


def edit_check():
    edit(id.get(),person_id.get(), weekly_hours.get(), pay_for_hours.get(), end_date.get(), employment_type.get())
    messagebox.showinfo("edit", f"edite successfully!")
    reset_form()
    show_date_on_table(find_all())


def remove_check():
    delete(id.get)
    messagebox.showinfo("delete", f"delete successfully!")
    reset_form()
    show_date_on_table(find_all())


window = Tk()
# از روی کلاس سیم کارت کپی پیست کردین بله
window.geometry("680x360")
window.title("salary")
window.resizable(False, False)

# person id
Label(window, text="person id").place(x=20, y=20)
person_id = IntVar()
Entry(window, textvariable=person_id).place(x=95, y=20)

# weekly_hours
Label(window, text="weekly hours").place(x=20, y=60)
weekly_hours = IntVar()
Entry(window, textvariable=weekly_hours).place(x=95, y=60)

# pay_for_hours
Label(window, text="pay for hours").place(x=20, y=100)
pay_for_hours = IntVar()
Entry(window, textvariable=pay_for_hours).place(x=95, y=100)

# end date
Label(window, text="end date").place(x=20, y=140)
end_date = StringVar()
Entry(window, textvariable=end_date).place(x=95, y=140)

# employment_type
Label(window, text="employment_type").place(x=20, y=180)
employment_type = StringVar()
Entry(window, textvariable=employment_type).place(x=95, y=180)



Button(window, text="save", width=7, command=save_check).place(x=20, y=300)
Button(window, text="edit", width=7, command=save_check).place(x=90, y=300)
Button(window, text="remove", width=7, command=save_check).place(x=160, y=300)
# tabel
tabel = ttk.Treeview(window, height=12, columns=(1, 2, 3, 4, 5), show="headings")
tabel.column(1, width=60)
tabel.column(2, width=90)
tabel.column(3, width=90)
tabel.column(4, width=70)
tabel.column(5, width=90)

# tabel taitel
tabel.heading(1, text="person id")
tabel.heading(2, text="weekly hours")
tabel.heading(3, text="pay for hours")
tabel.heading(4, text="end date")
tabel.heading(5, text="employment_type")


tabel.bind("<<TreeviewSelect>>", select_product)

tabel.place(x=250, y=60)
window.mainloop()
