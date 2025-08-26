from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *


window = Tk()
window.geometry("730x390")
window.title("Military Card")
window.configure(bg="lightblue")

#id
id_panel = Label(window, text="ID",bg="lightblue")
id_panel.place(x=10 , y=10)
ID=IntVar()
id_panel_EN=Entry(window, textvariable=ID,state="disabled",bg="lightpink")
id_panel_EN.place(x=92 , y=10)

#person_id
person_id_panel = Label(window, text="Person_ID",bg="lightblue")
person_id_panel.place(x=10 , y=50)
Person_ID=StringVar()
person_id_panel_EN= Entry(window, textvariable=Person_ID,bg="lightpink")
person_id_panel_EN.place(x=92 , y=50)

#card_serial
card_serial_panel = Label(window, text="card_Serial",bg="lightblue")
card_serial_panel.place(x=10 , y=90)
card_serial=StringVar()
card_serial_panel_EN= Entry(window, textvariable=card_serial,bg="lightpink")
card_serial_panel_EN.place(x=92 , y=90)

#licence_type
license_type_panel = Label(window, text="License_Type",bg="lightblue")
license_type_panel.place(x=10 , y=130)
license_type=StringVar()
license_type_panel_EN= Entry(window, textvariable=license_type,bg="lightpink")
license_type_panel_EN.place(x=92 , y=130)


#city
city_panel = Label(window, text="City",bg="lightblue")
city_panel.place(x=10 , y=170)
city=StringVar()
city_panel_EN= Entry(window, textvariable=city,bg="lightpink")
city_panel_EN.place(x=92 , y=170)

#organisation
organisation_panel = Label(window, text="Organisation",bg="lightblue")
organisation_panel.place(x=10 , y=210)
organisation=StringVar()
organisation_panel_EN= Entry(window, textvariable=organisation,bg="lightpink")
organisation_panel_EN.place(x=92 , y=210)

# duration
duration_panel = Label(window, text="Expire_Date",bg="lightblue")
duration_panel.place(x=10 , y=250)
duration=StringVar()
duration_panel_EN= Entry(window, textvariable=duration,bg="lightpink")
duration_panel_EN.place(x=92 , y=250)

#find by id
id_founder_panel = Label(window, text="ID Founder :",bg="lightblue")
id_founder_panel.place(x=250 , y=10)
id_founder=StringVar()
id_founder_panel_EN= Entry(window, textvariable=id_founder,bg="lightpink")
id_founder_panel_EN.place(x=325 , y=10)

#find by card_serial
card_serial_founder_panel = Label(window, text="Card_serial Founder :",bg="lightblue")
card_serial_founder_panel.place(x=468, y=10)
card_serial_found=StringVar()
card_serial_founder_panel_EN= Entry(window, textvariable=card_serial_found,bg="lightpink")
card_serial_founder_panel_EN.place(x=590, y=10)


#buttons
save_btn=Button(window, text="Save",bg="lightgreen",fg="black",width=8)
save_btn.place(x=10 , y=350)
edit_btn=Button(window, text="Edit",bg="lightgreen",fg="black",width=8)
edit_btn.place(x=80 , y=350)
remove_btn=Button(window, text="Remove",bg="lightgreen",fg="black",width=8)
remove_btn.place(x=150 , y=350)
clear_btn=Button(window, text="Clear",bg="lightgreen",fg="black",width=28)
clear_btn.place(x=10 , y=290)

#find by all
fnd_btn=Button(window, text="Find all",bg="lightgreen",fg="black",width=28)
fnd_btn.place(x=10 , y=320)

#table
table=ttk.Treeview(window,height=15,columns=(1,2,3,4,5,6),show="headings")
table.heading(1, text="ID")
table.heading(2, text="card_Serial")
table.heading(3, text="License Type")
table.heading(4, text="City")
table.heading(5, text="Organisation")
table.heading(6, text="Duration")

table.column(1,width=70, anchor="center")
table.column(2,width=70, anchor="center")
table.column(3,width=85, anchor="center")
table.column(4,width=70, anchor="center")
table.column(5,width=85, anchor="center")
table.column(6,width=85, anchor="center")


table.place(x=250,y=50)
window.mainloop()