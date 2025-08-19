from model.entity.person import Person
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
        person_list= transaction_manager(
            "select * from persons",
        )
        person_list= list(map(lambda person: Person(*person), person_list))
        return person_list

    def find_by_id(self, id):
        person = transaction_manager(
            "select * from persons where id=?",
        )
        person =  Person(*person)
        return person

    def find_by_name_and_family(self, name, family):
        person_list = transaction_manager(
            "select * from persons where name like ? and family like ?",
            [name+"%", family+"%"],
        )
        person_list = list(map(lambda person: Person(*person), person_list))
        return person_list
