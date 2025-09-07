from controller.person_controller import PersonController


person_controller = PersonController()


# print(person_controller.save("ali", "alipour", 20))
# print(person_controller.save("ali", "alipour", 20))
# print(person_controller.save("ali", "alipour", 20))
# print(person_controller.edit(3, "hhhhhh", "alipour", 15))
# from view.person_view import PersonView

# person_controller.delete(1)
#
# ui =PersonView()


# print(person_controller.find_by_family("a"))


print(person_controller.find_all())