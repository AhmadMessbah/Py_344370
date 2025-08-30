class DriverLicence:
    def __init__(self, id, person_id, serial, licence_type, city, registered_date, expired_date):
        self.id = id
        self.person_id = person_id
        self.serial = serial
        self.licence_type = licence_type
        self.city = city
        self.registered_date = registered_date
        self.expired_date = expired_date


    def __repr__(self):
        return f"{self.__dict__}"


    def to_tuple(self):
        return tuple((self.id, self.person_id, self.serial, self.licence_type, self.city, self.registered_date, self.expired_date))
