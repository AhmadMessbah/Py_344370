from model.entity.driver_licence import DriverLicence
from model.repository.database_manager import *

class DriverLicencesRepository:
    def save(self,driver_licence):
       return transaction_manager(
      "insert into driver_licences(person_id, serial, license_type, city, register_date, expire_date) values (?,?,?,?,?,?)",
      [driver_licence.person_id,driver_licence.serial, driver_licence.license_type, driver_licence.city, driver_licence.register_date, driver_licence.expire_date],
      commit=True
      )

    def edit(self,driver_licence):
       return transaction_manager(
        "update driver_licences set id=?,person_id=?, serial=?, license_type=?, city=?, register_date=?, expire_date=? where id=?",
        [driver_licence.id,driver_licence.person_id,driver_licence.serial, driver_licence.license_type, driver_licence.city, driver_licence.register_date, driver_licence.expire_date],
        commit=True
       )

    def delete(self,id):
        return transaction_manager(
         "delete from driver_licences where id=?",
         [id],
         commit=True
        )

    def find_by_id(self,id):
        licence_info = transaction_manager(
         "select * from driver_licences where id=?",
         [id]
        )
        licence_info =DriverLicence(*licence_info)
        return licence_info


    def find_by_serial(self,serial):
        licence_info = transaction_manager(
         "select * from driver_licences where serial like?",
         [serial+"%"]
        )
        licence_info = DriverLicence(*licence_info)
        return licence_info


    def find_all(self):
        licence_info_list = transaction_manager(
        "select * from driver_licences",
        )
        licence_info_list = list(map(lambda licence_info: DriverLicence(*licence_info), licence_info_list))