from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *


window = Tk()
window.geometry("730x390")
window.title("Driver Licences")
window.configure(bg="lightblue")

#id
id_panel = Label(window, text="ID",bg="lightblue")
id_panel.place(x=10 , y=10)
ID=IntVar()
id_panel_EN=Entry(window, textvariable=ID,state="disabled",bg="lightyellow")
id_panel_EN.place(x=92 , y=10)

#person_id
person_id_panel = Label(window, text="Person_ID",bg="lightblue")
person_id_panel.place(x=10 , y=50)
Person_ID=StringVar()
person_id_panel_EN= Entry(window, textvariable=Person_ID,bg="lightyellow")
person_id_panel_EN.place(x=92 , y=50)

#serial
serial_panel = Label(window, text="Serial",bg="lightblue")
serial_panel.place(x=10 , y=90)
serial=StringVar()
serial_panel_EN= Entry(window, textvariable=serial,bg="lightyellow")
serial_panel_EN.place(x=92 , y=90)

#licence_type
license_type_panel = Label(window, text="License_Type",bg="lightblue")
license_type_panel.place(x=10 , y=130)
license_type=StringVar()
license_type_panel_EN= Entry(window, textvariable=license_type,bg="lightyellow")
license_type_panel_EN.place(x=92 , y=130)


#city
city_panel = Label(window, text="City",bg="lightblue")
city_panel.place(x=10 , y=170)
city=StringVar()
city_panel_EN= Entry(window, textvariable=city,bg="lightyellow")
city_panel_EN.place(x=92 , y=170)

#register_date
register_date_panel = Label(window, text="Register_Date",bg="lightblue")
register_date_panel.place(x=10 , y=210)
register_date=StringVar()
register_date_panel_EN= Entry(window, textvariable=register_date,bg="lightyellow")
register_date_panel_EN.place(x=92 , y=210)

# expire_date
expire_date_panel = Label(window, text="Expire_Date",bg="lightblue")
expire_date_panel.place(x=10 , y=250)
expire_date=StringVar()
expire_date_panel_EN= Entry(window, textvariable=expire_date,bg="lightyellow")
expire_date_panel_EN.place(x=92 , y=250)

#find by id
id_founder_panel = Label(window, text="ID Founder",bg="lightblue")
id_founder_panel.place(x=250 , y=10)
id_founder=StringVar()
id_founder_panel_EN= Entry(window, textvariable=id_founder,bg="lightyellow")
id_founder_panel_EN.place(x=320 , y=10)

#find by serial
serial_founder_panel = Label(window, text="Serial Founder",bg="lightblue")
serial_founder_panel.place(x=505, y=10)
serial_found=StringVar()
serial_founder_panel_EN= Entry(window, textvariable=serial_found,bg="lightyellow")
serial_founder_panel_EN.place(x=590, y=10)


#buttons
save_btn=Button(window, text="Save",bg="brown",fg="white",width=8)
save_btn.place(x=10 , y=350)
edit_btn=Button(window, text="Edit",bg="brown",fg="white",width=8)
edit_btn.place(x=80 , y=350)
remove_btn=Button(window, text="Remove",bg="brown",fg="white",width=8)
remove_btn.place(x=150 , y=350)
clear_btn=Button(window, text="Clear",bg="brown",fg="white",width=28)
clear_btn.place(x=10 , y=290)

#find by all
fnd_btn=Button(window, text="Find all",bg="brown",fg="white",width=28)
fnd_btn.place(x=10 , y=320)

#table
table=ttk.Treeview(window,height=15,columns=(1,2,3,4,5,6),show="headings")
table.heading(1, text="ID")
table.heading(2, text="Serial")
table.heading(3, text="License Type")
table.heading(4, text="City")
table.heading(5, text="Register Date")
table.heading(6, text="Expire Date")

table.column(1,width=70, anchor="center")
table.column(2,width=70, anchor="center")
table.column(3,width=85, anchor="center")
table.column(4,width=70, anchor="center")
table.column(5,width=85, anchor="center")
table.column(6,width=85, anchor="center")


table.place(x=250,y=50)
window.mainloop()