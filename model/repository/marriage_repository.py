from model.entity.marriage_repository import Marriage
from model.repository.database_manager import transaction_manager

class MarriageRepository:
    def save(self, marriage):
        return transaction_manager(
            "insert into marriages (person_id,name,family,marriage_date,childes) values (?, ?,?,?,?)",
            [marriage.person_id,marriage.name,marriage.family,marriage.childes],
            commit=True

        )

    def edit(self, marrriage):
        return transaction_manager(
            "update marriages set person_id=?,name=?, family=?, age=?,marriage_date=?,childes=? where id=?",
            [marriage.name, marriage.family, marriage.age, marriage.id],
            commit=True
        )

    def delete(self, id):
        return transaction_manager(
            "delete from marriages where id=?",
            [id],
            commit=True
        )

    def find_all(self):
        marriage_list= transaction_manager(
            "select * from marriages",
        )
        marriage_list= list(map(lambda marriage: marriage(*marriage), marriage_list))
        return marriage_list

    def find_by_id(self, id):
        marriage = transaction_manager(
            "select * from marriages where id=?",
        )
        marriage =  Person(*marriage)
        return marriage

    def find_by_name_and_family(self, name, family):
        marriage_list = transaction_manager(
            "select * from marriages where name like ? and family like ?",
            [name+"%", family+"%"],
        )
        marriage_list = list(map(lambda marriage: marriage(*marriage), marriage_list))
        return marriage_list















































