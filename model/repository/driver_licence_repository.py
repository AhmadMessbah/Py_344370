from model.entity.driver_licence import DriverLicence
from model.repository.database_manager import  *

class DriverLicenceRepository:
    def save(self,driver_licence):
        return transaction_manager(
            " insert into driver_licences (person_id, serial, licence_type, city, registered_date, expired_date) values (?,?,?,?,?,?)",
            [driver_licence.person_id, driver_licence.serial, driver_licence.licence_type, driver_licence.city,driver_licence.registered_date, driver_licence.expired_date],
            commit = True
        )


    def edit(self,driver_licence):
        return transaction_manager(
            " update driver_licences set person_id = ? , serial = ? , licence_type = ? , city = ? , registered_date = ? , expired_date = ? where id = ?",
            [driver_licence.person_id, driver_licence.serial, driver_licence.licence_type, driver_licence.city,driver_licence.registered_date, driver_licence.expired_date, driver_licence.id],
            commit = True
        )


    def delete(self,id):
        return transaction_manager(
            " delete from driver_licences where id = ?",
            [id],
            commit = True
        )


    def find_by_id(self,id):
        driver_licence = transaction_manager(
            " select * from driver_licences where id = ?",
            [id]
        )
        if driver_licence:
            driver_licence = DriverLicence(*driver_licence[0])
            return driver_licence
        else:
            raise ValueError("id not found")


    def find_by_serial(self,serial):
        driver_licence = transaction_manager(
            " select * from driver_licences where serial like ?",
            [serial + "%"]
        )
        if driver_licence:
            driver_licence = DriverLicence(*driver_licence[0])
            return driver_licence
        else:
            raise ValueError("serial not found")


    def find_all(self):
        driver_licence_list = transaction_manager(
            " select * from driver_licences "
        )
        if driver_licence_list:
            driver_licence_list = list(map(lambda driver_licence : DriverLicence(*driver_licence), driver_licence_list))
            return driver_licence_list
        else:
            raise ValueError("driver licence list out of range")
