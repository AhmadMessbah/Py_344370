from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk

from controller.skill_controller import SkillController
from model.entity.skill import Skill
from view.component.label_with_text import LabelWithText
from view.component.table import Table


class SkillView:
    def reset_form(self):
        self.id.set(0)
        self.person_id.set("")
        self.title.set("")
        self.institute.set("")
        self.duration.set("")
        self.register_date.set("")
        self.score.set(0)
        status, skill_list= self.skill_controller.find_all()
        if status:
            self.table.refresh_table(skill_list)

    def select_skill(self, selected_skill):
        skill = Skill(*selected_skill)

        self.id.set(skill.id)
        self.person_id.set(skill.person_id)
        self.title.set(skill.title)
        self.institute.set(skill.institute)
        self.duration.set(skill.duration)
        self.register_date.set(skill.register_date)
        self.score.set(skill.score)

    def search(self, event):
        status, skill_list = self.skill_controller.find_by_title_and_institute(self.search_title.get(), self.search_institute.get())

        if status:
            self.table.refresh_table(skill_list)

    def save_click(self):
        status, message = self.skill_controller.save(self.person_id.get(), self.title.get(), self.institute.get(),self.duration.get(),self.register_date.get(),self.score.get())
        if status:
            msg.showinfo("Saved", f"{message} Saved")
            self.reset_form()
        else:
            msg.showerror("Error", message)

    def edit_click(self):
        status, message = self.skill_controller.edit(self.id.get(),self.person_id.get(), self.title.get(), self.institute.get(),self.duration.get(),self.register_date.get(),self.score.get())
        if status:
            msg.showinfo("Edited", f"message Edited")
            self.reset_form()
        else:
            msg.showerror("Error", message)

    def delete_click(self):
        status, message = self.skill_controller.delete(self.id.get())
        if status:
            msg.showinfo("Deleted", f"message Deleted")
            self.reset_form()
        else:
            msg.showerror("Error", message)

    # def close_window(self):
    #     if msg.askyesno("Exit", "Are you sure ?"):
    #         self.win.destroy()

    def __init__(self):
        self.skill_controller = SkillController()
        self.win = Tk()
        self.win.title("Skill")
        self.win.resizable(width=False, height=False)
        self.win.geometry("880x400")

        # id
        self.id = IntVar()
        LabelWithText(self.win, "Id", self.id, 20, 20, "readonly")

        # person id
        self.person_id = StringVar()
        LabelWithText(self.win, "Person id", self.person_id, 20, 60)

        # title
        self.title = StringVar()
        LabelWithText(self.win, "Title", self.title, 20, 100)

        # institute
        self.institute = StringVar()
        LabelWithText(self.win, "Institute", self.institute, 20, 140)

        # duration
        self.duration = StringVar()
        LabelWithText(self.win, "Duration", self.duration, 20, 180)

        # register date
        self.register_date = StringVar()
        LabelWithText(self.win, "Register date", self.register_date, 20, 220)

        # score
        self.score = IntVar()
        LabelWithText(self.win, "Score", self.score, 20, 260)

        # search title
        self.search_title = StringVar()
        LabelWithText(self.win, "Search Title", self.search_title, 250, 20).text.bind("<KeyRelease>",self.search)

        # search institute
        self.search_institute = StringVar()
        LabelWithText(self.win, "Search Institute", self.search_institute, 550, 20).text.bind("<KeyRelease>",self.search)

        #table
        self.table = Table(
            self.win,
            ["Id", "Person Id", "Title", "Institute", "Duration", "Register Date", "Score"],
            [70, 100, 100, 80, 80, 100, 80],
            250, 60,
            self.select_skill
        )

        # Buttons (Clear-Save-Edit-Remove)
        Button(self.win, text="New Skill", command=self.reset_form,width=28).place(x=20,y=300)
        Button(self.win, text="Save", command=self.save_click, width=7).place(x=20,y=340)
        Button(self.win, text="Edit", command=self.edit_click, width=7).place(x=95,y=340)
        Button(self.win, text="Remove", command=self.delete_click, width=7).place(x=170,y=340)

        self.reset_form()

        self.win.mainloop()

        # self.win.protocol("WM_DELETE_WINDOW",  self.close_window)