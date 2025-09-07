import re
from datetime import datetime

class Skill:
    def __init__(self,id, person_id, title, institute, duration, register_date, score):
        self.id = id
        self.person_id = person_id
        self.title = title
        self.institute = institute
        self.duration = duration
        self.register_date = register_date
        self.score = score

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        self._person_id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if re.match(r"^[a-zA-Z\s]{3,30}$", value):
            self._title = value
        else:
            raise ValueError("The title is not valid.")

    @property
    def institute(self):
        return self._institute

    @institute.setter
    def institute(self, value):
        if re.match(r"^[a-zA-Z\s]{3,30}$", value):
            self._institute = value
        else:
            raise ValueError("The institution is not valid.")

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        value = value.replace("/", "-").strip()
        date = datetime.strptime(value, "%Y-%m-%d").date()
        if date > datetime.now().date():
            raise ValueError("The register date is not valid.")
        else:
            self._register_date = date

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if 12 <= value <= 20:
            self._score = value
        else:
            raise ValueError("Score must be between 12 and 20.")

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id, self.person_id, self.title, self.institute, self.duration, self.register_date, self.score))

