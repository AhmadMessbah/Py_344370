from sqlalchemy import Column, Integer, String
from model.entity.base import Base
import re
from datetime import datetime

class Education(Base):
    __tablename__ = "educations"

    id = Column(Integer, primary_key=True,autoincrement=True)
    person_id = Column(String(10), nullable=False,unique=True)
    university = Column(String(20), nullable=False)
    grade = Column(String(20), nullable=False)
    average = Column(Integer)
    start_day= Column(String(10), nullable=False)
    end_day = Column(String(10), nullable=False)


    def __init__(self, person_id: str, university: str, grade: str, average: int, start_date: str,
                 end_date: str):
        self.person_id = person_id
        self.university = university
        self.grade = grade
        self.average = average
        self.start_date = start_date
        self.end_date = end_date

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
    def university(self):
        return self._university

    @university.setter
    def university(self, value):
        if re.match(r"^[a-zA-Z\s]{3,30}$", value):
            self._university = value
        else:
            raise ValueError("University must be a valid string.")

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value

    @property
    def average(self):
        return self._average

    @average.setter
    def average(self, value):
        if 0 <= value <= 20:
            self._average = value
        else:
            raise ValueError("average must be between 0 and 20.")

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = datetime.strptime(value, "%Y-%m-%d")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        end = datetime.strptime(value, "%Y-%m-%d")
        if end >= self.start_date:
            self._end_date = end
            value.replace("/", "-").strip()
        else:
            raise ValueError("End date must be after start date")


    def __str__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.id, self.person_id, self.university, self.grade, self.average, self.start_date, self.end_date))
