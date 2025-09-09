from sqlalchemy import Column,Integer,String
from model.entity.base import Base

class Medical(Base):

    id = Column(Integer,primary_key=True,autoincrement=True)
    person_id = Column(Integer,nullable=False)
    disease = Column(String(30),nullable=False)
    medicine = Column(String(30),nullable=False)
    doctor = Column(String(30),nullable=False)
    visit_date = Column(String(30),nullable=False)
    status = Column(String(30),nullable=False)


    # def __init__(self, id, person_id, disease, medicine, doctor, visit_date, status):
    #     self.id = id
    #     self.person_id = person_id
    #     self.disease = disease
    #     self.medicine = medicine
    #     self.doctor = doctor
    #     self.visit_date = visit_date
    #     self.status = status

    # def __repr__(self):
    #     return f"{self.__dict__}"
    #
    # def to_tuple(self):
    #     return tuple((self.id, self.person_id, self.disease, self.medicine, self.doctor, self.visit_date, self.status))

    def __init__(self,person_id, disease, medicine, doctor, visit_date, status):
        self.person_id = person_id
        self.disease = disease
        self.medicine = medicine
        self.doctor = doctor
        self.visit_date = visit_date
        self.status = status