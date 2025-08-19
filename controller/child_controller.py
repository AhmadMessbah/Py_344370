import re

from model.entity.childs import Child
from model.service.childs_service import ChildService

class ChildController:
    def __init__(self):
        self.service = ChildService()

    def save(self,person_id, name, family, birth_date, is_alive, status):
        try:
            if re.match(r"^[0-9] {4}$", birth_date):
               childs = Child(None, id, person_id, name, family, birth_date, is_alive, status)
               return self.service.save(childs)
            else:
                raise ValueError("تاریخ تولد قابل قبول نیست")
        except Exception as e:
            return False, f"Error : {e}"

    def edite(self,id, person_id, name, family, birth_date, is_alive, status):
        try:
            if re.match(r"^[0-9] {4}$", birth_date):
               childs = Child(id, person_id, name, family, birth_date, is_alive, status)
               return self.service.edit(childs)
            else:
                raise ValueError("تاریخ تولد قابل قبول نیست")
        except Exception as e:
            return False, f"Error : {e}"

    def delete(self,id):
        try:
            return True, "info :user deleted successfuly"
        except Exception as e:
            return False, f"Error : {e}"

    def find_all():
        try:
            return childs_service.find_all()
        except Exception as e:
            return False, f"Error : {e}"

    def find_by_id(id):
        try:
            child = childs_service.find_by_id(id)
            if not child:
                raise ValueError("کاربر مورد نظر یافت نشد")
            return True, child
        except Exception as e:
            return False, f"Error : {e}"

    def find_by_person_id(person_id):
        try:
            return True, childs_service.find_by_person_id(person_id)
        except Exception as e:
            return False, f"Error : {e}"

    def find_by_name_and_family(name, family):
        try:
            return True, childs_service.find_by_name_and_family(name, family)
        except Exception as e:
            return False, f"Error : {e}"