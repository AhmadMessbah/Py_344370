from linecache import updatecache

from model.repository.database_manager import transaction_manager


def save(person_id, weekly_hours, pay_for_hours, end_date, employment_type):
    return transaction_manager(
        "insert into salaries(person_id, weekly_hours, pay_for_hours, end_date, employment_type) values (?,?,?,?,?)",
        [person_id, weekly_hours, pay_for_hours, end_date, employment_type],
        commit=True
    )


def edited():
    return transaction_manager(
        "update salaries set weekly_hours = ? ,pay_for_hours=? where person_id = ?",
    )


def delete():
    return transaction_manager(
        "delete from salaries where id = ?",
    )


def find_all():
    return transaction_manager(
        "select * from salaries",
    )


def find_by_id():
    return transaction_manager(
        "select person_id from salaries ",
    )
