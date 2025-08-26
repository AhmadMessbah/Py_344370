from tkinter.ttk import *
from tkinter import ttk, Tk, StringVar, IntVar, Label, messagebox

from appier import message
from streamlit import status

from controller.medical_controller import MedicalController
from model.entity.medical import Medical
from view.component.label_with_text import LabelWithText
class MedicalView:
# 6
    def reset_form(self):
        self.id.set(0)
        self.person_id.set(0)
        self.disease.set("")
        self.medicine.set("")
        self. doctor.set("")
        self. visit_date.set("")
        self.status.set("")
        status,medical_list=self.medical_controller.find_all()


    def show_data_on_table(self,medical_list):
         for medical in self.table.get_children():
             self.table.delete(medical)

    def save_click(self):
        status,message=self.medical_controller.save(self.person_id.get(),self.disease.get(),self.medicine.get(),self.doctor.get(),self.visit_date.get(),self.status.get())
        if status:
            messagebox.showinfo("Saved",f"{message} Saved")
        else:
            messagebox.showerror("Error",message)


    def edit_click(self):
        status,message = self.medical_controller.edit(self.person_id.get(),self.disease.get(),self.medicine.get(),self.doctor.get(),self.visit_date.get(),self.status.get())
        if status:
            messagebox.showinfo("Edited", f"{message} Edited")
        else:
            messagebox.showerror("Error", message)



    def remove_click(self):
        pass


    # 7
    def table_select(event):
        pass

    def __init__(self):


# 0
    win = Tk()
    # geometry-title
    win.title("Medical")
    win.resizable(width=False, height=False)
    win.geometry("800x360")

    # 1
    # # id
    id = IntVar()
    Label(win, text="id").place(x=20, y=20)
    # Entry(win, textvariable=id).place(x=100,y=20)
    Entry(win, textvariable=id).place(x=100, y=20)

    # person_id
    person_id = IntVar()
    Label(win, text="person_id").place(x=20, y=60)
    Entry(win, textvariable=person_id).place(x=100, y=60)
    # Entry(win, textvariable=person_id).place(x=100,y=60)

    # disease
    disease = StringVar()
    Label(win, text="disease").place(x=20, y=100)
    Entry(win, textvariable=disease).place(x=100, y=100)

    #  medicine
    medicine = StringVar()
    Label(win, text="medicine ").place(x=20, y=140)
    Entry(win, textvariable=medicine).place(x=100, y=140)

    # doctor
    doctor = StringVar()
    Label(win, text="doctor").place(x=20, y=180)
    Entry(win, textvariable=doctor).place(x=100, y=180)

    # visit_date
    visit_date = StringVar()
    Label(win, text="visit_date").place(x=20, y=220)
    Entry(win, textvariable=visit_date).place(x=100, y=220)

    # status
    status = StringVar()
    # Label(win,text="status").place(x=20,y=260)
    Label(win, text="status").place(x=20, y=255)
    Entry(win, textvariable=status).place(x=100, y=255)

    # 2
    # Buttons (Save-Edit-Remove)
    # Button(win, text="Clear", command=reset_form, width=29).place(x=20,y=250)
    Button(win, text="Save", command=save_click, width=7).place(x=20, y=300)
    Button(win, text="Edit", command=edit_click, width=7).place(x=95, y=300)
    Button(win, text="Remove", command=remove_click, width=7).place(x=170, y=300)

    # 3
    # search_doctor
    search_doctor = StringVar()
    Label(win, text="Search Doctor").place(x=470, y=20)
    search_doctor_txt = Entry(win, textvariable=search_doctor)
    search_doctor_txt.bind("<KeyRelease>", search_doctor)
    search_doctor_txt.place(x=325, y=20)

    # 4
    # Table
    table = ttk.Treeview(win, height=12, columns=(1, 2, 3, 4, 5, 6, 7), show="headings")
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

    table.place(x=250, y=60)

    # win.protocol("WM_DELETE_WINDOW", close_window)


    reset_form()

    win.mainloop()







