from model.repository import Repository
from model.entity.driver_licence import DriverLicence


class DriverLicenceService:
    def __init__(self):
        self.driver_licence_repo = Repository(DriverLicence)


    def save(self,driver_licence_info):
        return self.driver_licence_repo.save(driver_licence_info)


    def edit(self,driver_licence_info):
        return self.driver_licence_repo.edit(driver_licence_info)


    def delete(self,id):
        return self.driver_licence_repo.delete(id)


    def find_by_id(self,id):
        return self.driver_licence_repo.find_by_id(id)


    def find_by_serial(self,serial):
        return self.driver_licence_repo.find_by(DriverLicence).filter(DriverLicence.serial.like(serial+"%"))


    def find_all(self):
        return self.driver_licence_repo.find_all()
