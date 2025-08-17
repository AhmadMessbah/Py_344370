from model.repository.database_manager import transaction_manager
import sqlite3


def save(person_id,disease,medicine,doctor,visit_date,status):
    return transaction_manager(
        "insert into medicals (person_id,disease,medicine,doctor,visit_date,status) values (?,?,?,?,?,?)",
        [person_id,disease,medicine,doctor,visit_date,status],
        commit=True
    )

def edit(person_id,disease,medicine,doctor,visit_date,status):
    return transaction_manager(
        "update medicals set person_id=?,disease=?,medicine=?,doctor=?,visit_date=?,status=? where id=?",
        [person_id, disease, medicine, doctor, visit_date, status],
        commit=True
    )


def remove(id):
    return transaction_manager(
        "delete from medicals where id=?",[id]
    )


def find_all():
    return transaction_manager(
        "select * from medicals"
    )

def find_by_id(id):
    return transaction_manager(
        "select * from medicals where id = ? ",
        [id]
    )

def find_by_name_and_family(doctor):
    return transaction_manager(
        "select * from medicals where doctor like ?",
        [doctor]
    )