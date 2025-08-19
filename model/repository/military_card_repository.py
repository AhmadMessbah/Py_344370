from model.repository.database_manager import transaction_manager


class MilitaryCardRepository:
    def save(self, military_card):
        return transaction_manager(
            "insert into military_cards (person_id, card_serial,licence_type,city,organisation,duration) values (?,?,?,?,?,?)",
            [military_card.person_id, military_card.card_serial,military_card.licence_type, military_card.city,military_card.organisation,military_card.duration],
            commit=True
        )

    def edit(self, military_card):
        return transaction_manager(
            "update military_cards set person_id=?, card_serial=?, licence_type=?, city=?, organisation=?, duration=? where id=?",
            [military_card.person_id, military_card.card_serial,military_card.licence_type, military_card.city,military_card.organisation,military_card.duration,military_card.id],

            commit=True
        )

    def delete(self, id):
        return transaction_manager(
            "delete from military_cards where id=?", [id],
            commit=True
        )

    def find_all(self):
        return transaction_manager(
            "select * from military_cards",
        )

    def find_by_id(self, id):
        return transaction_manager(
            "select * from military_card where id=?",
        )

    def find_by_card_serial(self,card_serial):
        return transaction_manager(
            "select * from military_card where card_serial=?",
            [card_serial],
        )