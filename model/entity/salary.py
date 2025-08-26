class Salary:
    def __init__(self, id, person_id, weekly_hour, pay_for_hours, end_date, employment_type):
        self.id = id
        self.person_id = person_id
        self.weekly_hour = weekly_hour
        self.pay_for_hours = pay_for_hours
        self.end_date = end_date
        self.employment_type = employment_type

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(self.__dict__.values())
