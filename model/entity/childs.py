class Child:
    def __init__(self,id, person_id, name, family, birth_date, is_alive, status):
        self.id = id
        self.person_id = person_id
        self.name = name
        self.family = family
        self.birth_date = birth_date
        self.is_alive = is_alive
        self.status = status


    def __str__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id, self.person_id, self.name, self.family, self.birth_date, self.is_alive, self.status))