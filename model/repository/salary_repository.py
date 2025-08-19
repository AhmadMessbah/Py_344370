from linecache import updatecache

from model.repository.database_manager import transaction_manager


class SalaryRepository:
    def save(self, person_id, weekly_hours, pay_for_hours, end_date, employment_type):
        return transaction_manager(
            "insert into salaries(person_id, weekly_hours, pay_for_hours, end_date, employment_type) values (?,?,?,?,?)",
            [person_id, weekly_hours, pay_for_hours, end_date, employment_type],
            commit=True
        )

    def edit(self, id, person_id, weekly_hours, pay_for_hours, end_date, employment_type):
        return transaction_manager(
            "update salaries set weekly_hours = ? ,pay_for_hours=? where person_id = ?",
            [person_id, weekly_hours, pay_for_hours, end_date, employment_type, id]
        )

    def delete(self,id):
        return transaction_manager(
            "delete from salaries where id = ?",
            [id],
            commit=True
        )

    def find_all(self):
        return transaction_manager(
            "select * from salaries",
        )

    def find_by_id(self,person_id):
        return transaction_manager(
            "select person_id from salaries ",
        )

    def find_by_person_id(self,person_id):
        return transaction_manager(
            "select * from salaries where person_id = ?",
        )

    def find_by_employment_type(self,employment_type):
        return transaction_manager(
            "select * from salaries where employment_type = ?",
        )

