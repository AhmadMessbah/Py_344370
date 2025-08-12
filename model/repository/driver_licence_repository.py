from model.repository.database_manager import *

def save(person_id,serial,licence_type ,city,registered_date,expired_date):
    transaction_manager(
        "insert into driver_licence(person_id,serial,licence_type ,city,registered_date,expired_date) values (?,?,?,?,?,?)",
        [person_id,serial,licence_type,city,registered_date,expired_date],
         commit = True
    )

def edit(id,person_id,serial,licence_type,city,registered_date,expired_date):
    transaction_manager(""
                        "update driver_licence set id=?,person_id=?,serial=?,licence_type=?,city=?,registered_date=?,expired_date=?  ",
                       [id,person_id,serial,licence_type,city,registered_date,expired_date],
         commit = True
   )

def remove(id):
    transaction_manager("delete from driver_licence where id=?",[id],commit = True)





