class Marriage:
    def __init__(self, id,person_id ,name, family,marriage_date,childes):
        self.id = id
        self.person_id = person_id
        self.name = name
        self.family = family
        self.marriage_date = marriage_date
        self.childes = childes

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.person_id, self.name, self.family, self.age, self.marriage_date, self.childes))