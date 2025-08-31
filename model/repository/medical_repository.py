from model.repository.database_manager import transaction_manager
import sqlite3
from model.entity.medical import Medical


class MedicalRepository:
    def save(self, medical):
        return transaction_manager(
            "insert into medicals (person_id,disease,medicine,doctor,visit_date,status) values (?,?,?,?,?,?)",
            [medical.person_id, medical.mdisease, medical.medicine, medical.doctor, medical.visit_date, medical.status],
            commit=True
        )

    def edit(self, medical):
        return transaction_manager(
            "update medicals set person_id=?,disease=?,medicine=?,doctor=?,visit_date=?,status=? where id=?",
            [medical.person_id, medical.disease, medical.medicine, medical.doctor, medical.visit_date, medical.status],
            commit=True
        )

    def remove(self, id):
        return transaction_manager(
            "delete from medicals where id=?", [id],
            commit=True
        )

    def find_all(self):
        medical_list = transaction_manager(
            "select * from medicals"
        )
        medical_list = list(map(lambda medical:Medical(*medical),medical_list))
        return medical_list

    def find_by_id(self, id):
        medical = transaction_manager(
            "select * from medicals where id = ? ",
            [id])
        medical = Medical(*medical)
        return medical


    def find_by_person_id(person_id):
        medical_list = transaction_manager(
            "select * from medicals where person_id like ?",
            [person_id] )
        medidal_list = list(map(lambda medical:Medical(*medical),medical_list))
        return medical_list
