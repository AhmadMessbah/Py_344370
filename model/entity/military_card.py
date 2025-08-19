class MilitaryCard:
    def __init__(self, id, person_id, card_serial, licence_type, city, organisation, duration):
        self.id = id
        self.person_id = person_id
        self.card_serial = card_serial
        self.licence_type = licence_type
        self.city = city
        self.organisation = organisation
        self.duration = duration


    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id, self.person_id, self.card_serial, self.licence_type, self.city, self.organisation, self.duration))