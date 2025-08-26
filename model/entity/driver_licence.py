class DriverLicence:
    def __init__(self,id,person_id, serial, license_type,city,register_date,expire_date):
        self.id = id
        self.person_id = person_id
        self.serial = serial
        self.license_type = license_type
        self.city = city
        self.register_date = register_date
        self.expire_date = expire_date

    def __repr__(self):
        return f"{self.__dict__}"


    def to_tuple(self):
        return tuple((self, self.id, self.person_id, self.serial, self.license_type, self.city, self.register_date, self.expire_date))


