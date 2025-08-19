class Medical:
    def __init__(self, id, person_id, disease, medicine, doctor, visit_date, status):
        self.id = id
        self.person_id = person_id
        self.disease = disease
        self.medicine = medicine
        self.doctor = doctor
        self.visit_date = visit_date
        self.status = status

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id, self.person_id, self.disease, self.medicine, self.doctor, self.visit_date, self.status))
