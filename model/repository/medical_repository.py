from model.repository.database_manager import transaction_manager
import sqlite3


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
            "delete from medicals where id=?", [id]
        )

    def find_all(self):
        return transaction_manager(
            "select * from medicals"
        )

    def find_by_id(self, id):
        return transaction_manager(
            "select * from medicals where id = ? ",
            [id]
        )

    def find_by_name_and_family(doctor):
        return transaction_manager(
            "select * from medicals where doctor like ?",
            [doctor]
        )
