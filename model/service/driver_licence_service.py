from model.repository.driver_licence_repository import *

class DriverLicenceService:
    def __init__(self):
        self.driver_licence_repo = DriverLicenceRepository()


    def save(self,driver_licence):
        return self.driver_licence_repo.save(driver_licence)


    def edit(self,driver_licence):
        #driver_licence = self.driver_licence_repo.find_by_id(driver_licence)
        #if driver_licence :
            return self.driver_licence_repo.edit(driver_licence)
        #else :
            #raise ValueError ("id not found to edit !")


    def delete(self,id):
        #driver_licence = self.driver_licence_repo.find_by_id(id)
        #if driver_licence :
            return self.driver_licence_repo.delete(id)
        #else :
            #raise ValueError ("id not found to delete !")


    def find_by_id(self,id):
        return self.driver_licence_repo.find_by_id(id)


    def find_by_serial(self,serial):
        return self.driver_licence_repo.find_by_serial(serial)


    def find_all(self):
        return self.driver_licence_repo.find_all()
