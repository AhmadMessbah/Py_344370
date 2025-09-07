from model.entity.person import Person
from model.tools.logging import Logger

Logger.info("App Started")

# import test.person_test
# from view.person_view import PersonView
# ui = PersonView()



person1 = Person("A", "B", 10)
person2 = Person("A", "B", 10)
person3 = Person("A", "B", 10)


person_list = [person1, person2, person3]
print(person_list)

