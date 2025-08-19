from tkinter import *
import tkinter.messagebox as msg
from controller.person_controller import PersonController
from view.component.label_with_text import LabelWithText

class PersonView:
    def save_click(self):
        status, message = self.person_controller.save(self.name.get() ,self.family.get(), self.age.get())
        if status:
            msg.showinfo("Saved", message)
        else:
            msg.showerror("Error", message)

    def __init__(self):
        self.person_controller = PersonController()
        self.win= Tk()
        self.win.title("Person Profile")
        self.win.geometry("300x300")

        self.id = IntVar()
        LabelWithText(self.win, "Id", self.id, 20,20)

        self.name = StringVar()
        LabelWithText(self.win, "Name", self.name, 20,60)

        self.family= StringVar()
        LabelWithText(self.win, "Family", self.family, 20,100)

        self.age = IntVar()
        LabelWithText(self.win, "Age", self.age, 20,140)


        Button(self.win, text="Save", width=8,command=self.save_click).place(x=20,y=250)
        self.win.mainloop()




