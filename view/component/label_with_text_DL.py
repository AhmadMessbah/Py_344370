from view.component.label_with_text import *
class LabelWithTextDriverLicence:
    def __init__(self, windows, text, variable, x, y, state="normal"):
        self.label = Label(windows, text=text)
        self.label.place(x=x, y=y)
        self.text = Entry(windows, textvariable=variable, width=15, state=state)
        self.text.place(x=x + 100, y=y)
