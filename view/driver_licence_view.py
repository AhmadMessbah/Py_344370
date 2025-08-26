from tkinter import *
from tkinter.ttk import *
import messagebox as msg
from view.component.label_with_text import LabelWithText
from controller.driver_licences_controller import *

class DriverLicenceView:
    def save_clicked(self):
        self.driver_licences_controller = DriverLicencesController
        status,message = self.driver_licences_controller.save(self.person_id.get(),self.serial.get(),self.city.get(),self.register_date.get(),self.expire_date.get())
        if status:
           msg.showinfo( "Saved",f"{message}saved")
        else:
           msg.showerror("Not Saved",f"{message}Not Saved")

    def edit_clicked(self):
        self.driver_licences_controller = DriverLicencesController()
        status, message = self.driver_licences_controller.edit(self.id.get(), self.person_id.get(), self.serial.get(), self.city.get(), self.register_date.get(),self.expire_date.get())
        if status:
            msg.showinfo("Edited", f"{message}edited")
        else:
            msg.showerror("Not edited", f"{message}Not edited")

    def delete_clicked(self):
        self.driver_licences_controller = DriverLicencesController
        status, message = self.driver_licences_controller.delete(self.id.get())
        if status:
            msg.showinfo("Deleted", f"{message}deleted")
        else:
            msg.showerror("Not deleted", f"{message}Not deleted")

    def reset_form(self):
        pass

    def select_person(self):
        pass

    def search(self,event):
        pass


    def __init__(self):
        self.driver_licences_controller = DriverLicencesController
        self.window = Tk()
        self.window.title("Driver Licence")
        self.window.geometry("700x500")

        self.id = IntVar()
        LabelWithText(self.window,"id",self.id,10,50)

        self.person_id = StringVar()
        LabelWithText(self.window,"person_id",self.person_id,10,100)

        self.serial = StringVar()
        LabelWithText(self.window,"serial",self.serial,10,150)

        self.license_type = StringVar()
        LabelWithText(self.window,"license_type",self.license_type,10,200)

        self.city = StringVar()
        LabelWithText(self.window,"city",self.city,10,250)

        self.register_date = StringVar()
        LabelWithText(self.window,"register_date",self.register_date,10,300)

        self.expire_date = StringVar()
        LabelWithText(self.window,"expire_date",self.expire_date,10,350)

        self.id_search = IntVar()
        LabelWithText(self.window,"id_search",self.id_search,10,100).text.bind("<KeyRelease>",self.search)

        Button(self.window,text="New Person",width=8,command=self.save_clicked).place(x=10,y=450)
        Button(self.window,text="Save",width=8,command=self.save_clicked).place(x=60,y=450)
        Button(self.window,text="Edit",width=8,command=self.edit_clicked).place(x=110,y=450)
        Button(self.window,text="Delete",width=8,command=self.delete_clicked).place(x=160,y=450)

        self.table = ttk.Treeview(self.window,columns=[1,2,3,4,5,6,7],show="headings")
        self.table.heading("1",text="ID",anchor="center")
        self.table.heading("2",text="Person ID",anchor="center")
        self.table.heading("2",text="Person ID",anchor="center")
        self.table.heading("3",text="Serial",anchor="center")
        self.table.heading("4",text="License Type",anchor="center")
        self.table.heading("5",text="City",anchor="center")
        self.table.heading("6",text="Register Date",anchor="center")
        self.table.heading("7",text="Expiration Date",anchor="center")

        self.table.column("1",width=120)
        self.table.column("2",width=120)
        self.table.column("3",width=120)
        self.table.column("4",width=120)
        self.table.column("5",width=120)
        self.table.column("6",width=120)
        self.table.column("7",width=120)

        self.table.bind("<<TreeviewSelect>>",self.select_person)
        self.table.place(x=50,y=100)




        self.window.mainloop()

