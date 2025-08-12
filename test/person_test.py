from model.repository.person_repository import save_to_db
from model.service.person_service import save_person
from controller.person_controller import save

# print(save_to_db("ali", "alipour", 50))
# print(save_person("ali", "alipour", 35))
print(save("ali", "alipour", 26))