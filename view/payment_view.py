from tkinter import *
import tkinter.messagebox as msg

from controller.payment_controller import PaymentController
from model.entity.payment import Payment
from view.component.label_with_text import LabelWithText
from view.component.table import Table

class PaymentView:
    def reset_form(self):
        self.id.set(0)
        self.person_id.set(0)
        self.title.set("")
        self.amount.set(0)
        self.pay_date.set("")
        self.payment_type.set("")
        self.description.set("")
        status, payment_list = self.payment_controller.find_all()
        if status:
            self.table.refresh_table(payment_list)



    def select_payment(self, event):
        payment = Payment(*selected_payment[1:])
        payment.id=selected_payment[0]
        self.id.set(payment.id)
        self.person_id.set(payment.person_id)
        self.title.set(payment.title)
        self.amount.set(payment.amount)
        self.pay_date.set(payment.pay_date)
        self.payment_type.set(payment.payment_type)
        self.description.set(payment.description)


    def search_by_payment_type(self, event):
        status,payment_list=self.payment_controller.find_by_payment_type(self.search_payment_type.get())
        if status:
            self.table.refresh_table(payment_list)

    def search_id(self, event):
        status, payment_list = self.payment_controller.find_by_id(self.search_by_id.get())
        if status:
            self.table.refresh_table(payment_list)

    def save_click(self):
        status, message = self.payment_controller.save(self.person_id.get(), self.title.get(),
                                                       self.amount.get(), self.pay_date.get(), self.payment_type.get(),
                                                       self.description.get())
        if status:
            msg.showinfo("Saved", f"{message} Saved")
            self.reset_form()
        else:
            msg.showerror("Error", message)

    def edit_click(self):
        status, message = self.payment_controller.edit(self.id.get(), self.person_id.get(), self.title.get(),
                                                       self.amount.get(), self.pay_date.get(), self.payment_type.get(),
                                                       self.description.get())
        if status:
            msg.showinfo("Edited", f"{message} Edited")
            self.reset_form()
        else:
            msg.showerror("Error", message)

    def delete_click(self):
        status, message = self.payment_controller.delete(self.id.get())
        if status:
            msg.showinfo("Deleted", f" Deleted ")
            self.reset_form()
        else:
            msg.showerror("Error", message)

    def __init__(self):
        self.payment_controller = PaymentController()
        self.win = Tk()
        self.win.title("Payment Profile")
        self.win.geometry("940x440")

        self.id = IntVar()
        LabelWithText(self.win, "Id", self.id, 40, 20, state="readonly")

        self.person_id = IntVar()
        LabelWithText(self.win, "Person Id", self.person_id, 40, 60)

        self.title = StringVar()
        LabelWithText(self.win, "Title", self.title, 40, 100)

        self.amount = IntVar()
        LabelWithText(self.win, "Amount", self.amount, 40, 140)

        self.pay_date = StringVar()
        LabelWithText(self.win, "Pay Date", self.pay_date, 40, 180)

        self.payment_type = StringVar()
        LabelWithText(self.win, "Payment Type", self.payment_type, 40, 220)

        self.description = StringVar()
        LabelWithText(self.win, "Description", self.description, 40, 260)

        self.search_by_id = IntVar()
        LabelWithText(self.win, "Search ID", self.search_by_id, 250, 20).text.bind("<KeyRelease>", self.search_id)

        self.search_payment_type = StringVar()
        LabelWithText(self.win, "Search Type", self.search_payment_type, 500, 20).text.bind("<KeyRelease>", self.search_by_payment_type)

        self.table=Table(
            self.win,
            ["Id","Person Id","Title","Amount","Pay Date","Payment Type","Description"],
            [70,70,110,70,70,110,110],
            250,60,
            self.select_payment
        )


        Button(self.win, text="New Payment", width=23, command=self.reset_form).place(x=40, y=300)
        Button(self.win, text="Save", width=6, command=self.save_click).place(x=40, y=340)
        Button(self.win, text="Edit", width=6, command=self.edit_click).place(x=100, y=340)
        Button(self.win, text="Delete", width=6, command=self.delete_click).place(x=160, y=340)

        self.reset_form()

        self.win.mainloop()
