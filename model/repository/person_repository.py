from model.repository.database_manager import transaction_manager


class PersonRepository:
    def save(self, person):
        return transaction_manager(
            "insert into persons (name, family, age) values (?,?,?)",
            [person.name, person.family, person.age],
            commit=True
        )

    def edit(self, person):
        return transaction_manager(
            "update persons set name=?, family=?, age=? where id=?",
            [person.name, person.family, person.age, person.id],
            commit=True
        )

    def delete(self, id):
        return transaction_manager(
            "delete from persons where id=?",
            [id],
            commit=True
        )

    def find_all(self):
        return transaction_manager(
            "select * from persons",
        )

    def find_by_id(self, id):
        return transaction_manager(
            "select * from persons where id=?",
        )

    def find_by_name_and_family(self, name, family):
        return transaction_manager(
            "select * from persons where name like ? and family like ?",
            [name+"%", family+"%"],
        )
