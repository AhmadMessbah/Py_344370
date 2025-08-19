class Education:
    def __init__(self, id, person_id, university, grade, average, start_date, end_date):
        self.id = id
        self.person_id = person_id
        self.university = university
        self.grade = grade
        self.average = average
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return (self.id, self.person_id, self.university, self.grade, self.average, self.start_date, self.end_date)