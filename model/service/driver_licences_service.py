from model.repository.driver_licences_repository import *

class DriverLicencesService:
    def __init__(self):
        self.repo = DriverLicencesRepository()


    def save(self, driver_licence):
          return self.repo.save(driver_licence)


    def edit(self, driver_licence):
        licence_info = self.repo.find_by_id(id)
        if licence_info:
            return self.repo.edit(driver_licence)
        else:
            raise ValueError("licence information for this id not found")


    def delete(self,id):
        licence_info = self.repo.find_by_id(id)
        if licence_info:
            return self.repo.delete(id)
        else:
            raise ValueError("licence information for this id not found")


    def find_by_id(self,id):
        return self.repo.find_by_id(id)


    def find_by_serial(self,serial):
        return self.repo.find_by_serial(serial)


    def find_all(self):
        return self.repo.find_all()
