from model.repository.database_manager import *

class DriverLicenceRepository:
    def save(self,driver_licence):
        return transaction_manager(
        "insert into driver_licences(person_id, serial, licence_type, city, registered_date, expired_date) values (?,?,?,?,?,?)",
        [driver_licence.person_id,driver_licence.serial,driver_licence.licence_type,driver_licence.city,driver_licence.registered_date,driver_licence.expired_date],
         commit = True
    )

    def edit(self,driver_licence):
         return transaction_manager(
         "update driver_licences set person_id=?,serial=?,licence_type=?,city=?,registered_date=?,expired_date=?  where id=?",
         [driver_licence.person_id,driver_licence.serial,driver_licence.licence_type,driver_licence.city,driver_licence.registered_date,driver_licence.expired_date,driver_licence.id],
          commit = True
    )

    def remove(self,id):
         return transaction_manager("delete from driver_licences where id=?",
                                    [id],
                                    commit = True)

    def find_all(self):
        return transaction_manager("select * from driver_licences")

    def find_by_id(self,id):
        return transaction_manager("select * from driver_licences where id=?",[id])

    def find_by_serial(self,serial):
        return transaction_manager("select * from driver_licences where serial=?",[serial])

