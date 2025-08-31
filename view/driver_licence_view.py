from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as msg

from controller.driver_licence_controller import  *
from view.component.label_with_text_DL import *
from model.entity.driver_licence import *


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
            self.show_data_on_table(driver_licence_list)


    def show_data_on_table(self, driver_licence_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if driver_licence_list:
            for driver_licence in driver_licence_list:
                self.table.insert("", END , values=(driver_licence.to_tuple()))


    def select_driver_licence_information(self,event):
        selected_driver_licence = self.table.item(self.table.focus()) ["values"]
        if selected_driver_licence:
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
            self.show_data_on_table(driver_licence_list)


    def serial_search(self,event):
        status , driver_licence_list = self.driver_licence_controller.find_by_serial(self.serial_search.get())
        if status:
            self.show_data_on_table(driver_licence_list)


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
        LabelWithTextDriverLicence(self.window,"ID",self.id,10,10,"disable")

        self.person_id = StringVar()
        LabelWithTextDriverLicence(self.window,"Person_ID",self.person_id,10,70)

        self.serial = StringVar()
        LabelWithTextDriverLicence(self.window,"Serial",self.serial,10,130)

        self.licence_type = StringVar()
        LabelWithTextDriverLicence(self.window,"Licence_Type",self.licence_type,10,190)

        self.city = StringVar()
        LabelWithTextDriverLicence(self.window,"City",self.city,10,250)

        self.registered_date = StringVar()
        LabelWithTextDriverLicence(self.window,"Registered_Date",self.registered_date,10,310)

        self.expired_date = StringVar()
        LabelWithTextDriverLicence(self.window,"Expired_Date",self.expired_date,10,370)

        #searchs
        self.id_search = IntVar()
        LabelWithTextDriverLicence(self.window,"ID Search", self.id_search,300,10).text.bind("<KeyRelease>", self.id_search)

        self.serial_search = StringVar()
        LabelWithTextDriverLicence(self.window,"Serial Search", self.serial_search,715,10).text.bind("<KeyRelease>", self.serial_search)

        #Buttons
        Button(self.window,text = "New Information",width = 27, command = self.reset_form).place(x=10,y=425)
        Button(self.window,text = "Save",width = 7, command = self.save_click).place(x=10,y=465)
        Button(self.window, text="Edit", width=7, command= self.edit_click).place(x=80, y=465)
        Button(self.window, text="Delete", width=7, command= self.delete_click).place(x=150, y=465)

        #table
        self.table = ttk.Treeview(self.window, columns = [1,2,3,4,5,6,7], show = "headings",height=20)
        self.table.heading(1, text = "ID",anchor = "center")
        self.table.heading(2, text = "Person ID",anchor = "center")
        self.table.heading(3, text = "Serial",anchor = "center")
        self.table.heading(4, text = "Licence Type",anchor = "center")
        self.table.heading(5, text = "City",anchor = "center")
        self.table.heading(6, text = "Registered Date",anchor = "center")
        self.table.heading(7, text = "Expired Date",anchor = "center")

        self.table.column(1, width = 70,anchor = "center")
        self.table.column(2, width = 100,anchor = "center")
        self.table.column(3, width = 70,anchor = "center")
        self.table.column(4, width = 100,anchor = "center")
        self.table.column(5, width = 70,anchor = "center")
        self.table.column(6, width = 100,anchor = "center")
        self.table.column(7, width = 100,anchor = "center")


        self.table.bind("<<TreeviewSelect>>",self.select_driver_licence_information)
        self.table.place(x=300, y=70)


        self.reset_form()
        self.window.mainloop()