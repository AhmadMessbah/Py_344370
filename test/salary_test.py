#from model.repository.salary_repository import *


from model.service.salary_service import *
#test is ok
# save(100,100,10,"2025-11-31", "Yearly")

#test is ok
#delete(5)

#
#test is not ok
#edit(100,2,4,"1996-09-12","salary")


#test is ok
#print(find_all())

#test is ok
#print(find_by_id())

#test is ok
#print(find_by_person_id())

#test is ok
#print(find_by_employment_type()


# ui test
from view.salary_view import SalaryView

ui = SalaryView()