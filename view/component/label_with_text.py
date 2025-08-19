from tkinter import Label, Entry


class LabelWithText:
    def __init__(self, windows, text, variable, x, y):
        Label(windows, text=text).place(x=x, y=y)
        Entry(windows, textvariable=variable).place(x=x + 80, y=y)
