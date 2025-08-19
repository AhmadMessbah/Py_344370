from model.repository.military_card_repository import MilitaryCardRepository


class MilitaryCardService:
    def __init__(self):
        self.repo = MilitaryCardRepository()

    def save(self, military_card):
        return self.repo.save(military_card)

    def edit(self, military_card):
        return self.repo.edit(military_card)

    def delete(self, id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, id):
        return self.repo.find_by_id(id)

    def find_by_card_serial(self,card_serial):
        return self.repo.find_by_card_serial(card_serial)