from tkinter import Label, Entry


class LabelWithText:
    def __init__(self, windows, text, variable, x, y):
        self.label = Label(windows, text=text)
        self.label.place(x=x, y=y)
        self.text = Entry(windows, textvariable=variable,width=15)
        self.text.place(x=x + 80, y=y)
