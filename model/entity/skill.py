class Skill:
    def __init__(self,id, person_id, title, institute, duration, register_date, score):
        self.id = id
        self.person_id = person_id
        self.title = title
        self.institute = institute
        self.duration = duration
        self.register_date = register_date
        self.score = score

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id, self.person_id, self.title, self.institute, self.duration, self.register_date, self.score))

