from controller.lessons_controller import save



print("lessons view (gui)")
code=int(input("enter code: "))
teacher=input("enter teacher: ")
unit=int(input("enter unit: "))
class_number=int(input("enter class number: "))
title=input("enter title: ")
person_id=input("enter person id: ")
save(code, teacher, unit, class_number, title, person_id)