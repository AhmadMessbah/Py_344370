from model.repository.database_manager import transaction_manager



class ChildRepository:
    def save(self,child):
        return transaction_manager(
            "insert into childes (id, person_id, name, family, birth_date, is_alive, status) values (?,?,?,?,?,?,?)",
            [child.id, child.person_id, child.name, child.family, child.birth_date, child.is_alive, child.status],
            commit=True
        )

    def edit(seld, child):
        return transaction_manager(
            "update childes set person_id=?,name=?,family=?,birth_date=?,is_alive=?,status=? where id=?",
            [child.person_id, child.name, child.family, child.birth_date, child.is_alive, child.status, child.id],
            commit=True
        )

    def delete (self,child):
        return transaction_manager(
            "delete from childes where id=?",
            [child.person_id, child.name, child.family, child.birth_date, child.is_alive, child.status],
            commit=True
        )

    def find_all(self):
        return transaction_manager(
            "select * from childes"
        )

    def find_by_id(self, id):
        child_list = transaction_manager(
            "select * from childes")
        return child_list

    def find_by_person_id(self, person_id):
        return transaction_manager(
            "select * from childes where id = ? ",
            [id]
        )

    def find_by_name_and_family(self, name, family):
        return transaction_manager(
            "select * from childes where name = ? ",
            [name+"%",family+"%"]
        )
