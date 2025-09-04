from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as msg

from controller.driver_licence_controller import  *
from view.component.label_with_text import *
from model.entity.driver_licence import *
from view.component.table import *


class DriverLicenceView:
    def reset_form(self):
        self.id.set(0)
        self.person_id.set("")
        self.serial.set("")
        self.licence_type.set("")
        self.city.set("")
        self.registered_date.set("")
        self.expired_date.set("")
        status, driver_licence_list = self.driver_licence_controller.find_all()
        if status:
            self.table.refresh_table(driver_licence_list)



    def select_driver_licence_information(self,selected_driver_licence):
            driver_licence = DriverLicence(*selected_driver_licence)
            self.id.set(driver_licence.id)
            self.person_id.set(driver_licence.person_id)
            self.serial.set(driver_licence.serial)
            self.licence_type.set(driver_licence.licence_type)
            self.city.set(driver_licence.city)
            self.registered_date.set(driver_licence.registered_date)
            self.expired_date.set(driver_licence.expired_date)


    def id_search(self,event):
        status , driver_licence_list = self.driver_licence_controller.find_by_id(self.id_search.get())
        if status:
            self.table.refresh_table(driver_licence_list)


    def serial_search(self,event):
        status , driver_licence_list = self.driver_licence_controller.find_by_serial(self.serial_search.get())
        if status:
            self.table.refresh_table(driver_licence_list)


    def save_click(self):
        status ,message = self.driver_licence_controller.save(self.person_id.get(), self.serial.get(), self.licence_type.get(), self.city.get(), self.registered_date.get(), self.expired_date.get())
        if status:
            msg.showinfo("SAVED", f"{message} Saved")
            self.reset_form()
        else:
            msg.showerror("ERROR", message)


    def edit_click(self):
        status, message = self.driver_licence_controller.edit(self.id.get(), self.person_id.get(), self.serial.get(), self.licence_type.get(), self.city.get(), self.registered_date.get(), self.expired_date.get())

        if status:
            msg.showinfo("EDITED", f"{message} Edited")
            self.reset_form()
        else:
            msg.showerror("ERROR", message)


    def delete_click(self):
        status, message = self.driver_licence_controller.delete(self.id.get())
        if status:
            msg.showinfo("DELETED", f"{message} Deleted")
            self.reset_form()
        else:
            msg.showerror("ERROR", message)


    def __init__(self):
        self.driver_licence_controller = DriverLicenceController()
        self.window = Tk()
        self.window.title("Driver Licence")
        self.window.geometry("920x500")

        #LabelwithEntry
        self.id = IntVar()
        LabelWithText(self.window,"id",self.id,10,10, 20, "disable")

        self.person_id = StringVar()
        LabelWithText(self.window,"Person_id",self.person_id,10,70)

        self.serial = StringVar()
        LabelWithText(self.window,"Serial",self.serial,10,130)

        self.licence_type = StringVar()
        LabelWithText(self.window,"Licence_Type",self.licence_type,10,190)

        self.city = StringVar()
        LabelWithText(self.window,"City",self.city,10,250)

        self.registered_date = StringVar()
        LabelWithText(self.window,"Registered_Date",self.registered_date,10,310)

        self.expired_date = StringVar()
        LabelWithText(self.window,"Expired_Date",self.expired_date,10,370)

        #searchs
        self.id_search = IntVar()
        LabelWithText(self.window,"id Search", self.id_search,300,10).text.bind("<KeyRelease>", self.id_search)

        self.serial_search = StringVar()
        LabelWithText(self.window,"Serial Search", self.serial_search,715,10).text.bind("<KeyRelease>", self.serial_search)

        #Buttons
        Button(self.window,text = "New Information",width = 27, command = self.reset_form).place(x=10,y=425)
        Button(self.window,text = "Save",width = 7, command = self.save_click).place(x=10,y=465)
        Button(self.window, text="Edit", width=7, command= self.edit_click).place(x=80, y=465)
        Button(self.window, text="Delete", width=7, command= self.delete_click).place(x=150, y=465)

        #table
        self.table = Table(
        self.window,
       ["id", "Person id", "Serial", "Licence Type","City", "Registered Date", "Expired Date"],
        [70, 100, 70, 100, 70, 100, 100],
        300, 70,
        self.select_driver_licence_information
        )


        self.reset_form()
        self.window.mainloop()