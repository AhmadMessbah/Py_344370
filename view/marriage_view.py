from controller.marriage_controller import save
print("marriage view (gui)")


person_id = input("Enter person_id : ")
id = input("Enter id : ")
name = input("Enter name : ")
family = input("Enter family : ")
marriage_date= input("Enter marriage_date: ")
is_alive = input("Enter is_alive : ")
childes = input("Enter childes : ")
save(id,name,family,marriage_date,is_alive,childes)
