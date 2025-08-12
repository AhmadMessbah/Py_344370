from controller.person_controller import save

print("Person View (gui)")

name = input("Enter Name : ")
family = input("Enter Family : ")
age = input("Enter Age : ")
save(name, family, age)