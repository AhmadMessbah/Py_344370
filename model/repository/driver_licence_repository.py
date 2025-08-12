from model.repository.database_manager import *

def save(person_id,serial,licence_type ,city,registered_date,expired_date):
    return transaction_manager(
        "insert into driver_licences(person_id, serial, licence_type, city, registered_date, expired_date) values (?,?,?,?,?,?)",
        [person_id,serial,licence_type,city,registered_date,expired_date],
         commit = True
    )

def edit(id,person_id,serial,licence_type,city,registered_date,expired_date):
    return transaction_manager(""
                        "update driver_licences set id=?,person_id=?,serial=?,licence_type=?,city=?,registered_date=?,expired_date=?  where id=?",
                       [person_id,serial,licence_type,city,registered_date,expired_date, id],
         commit = True
   )

def remove(id):
    return transaction_manager("delete from driver_licences where id=?",[id],commit = True)



def find_all():
    license_list = transaction_manager("select * from driver_licences")
    return license_list

def find_by_id(id):
    person_id = transaction_manager("select * from driver_licences where id=?",[id])
    return person_id

def find_by_serial(serial):
    license_serial= transaction_manager("select * from driver_licences where serial=?",[serial])
    return license_serial

