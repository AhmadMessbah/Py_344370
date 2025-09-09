from model.entity.base import Base
from model.entity.education import Education
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from model.repository.repository import connection_string, engine, Session, Repository

connection_string = "sqlite:///./model/repository/class_project.db"

if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string, echo=True)
session = sessionmaker(bind=engine)

base = Base()
base.metadata.create_all(bind=engine)


class EducationRepository:
    def save(self, education):
        session = Session()
        session.add(education)
        session.refresh(education)
        session.commit()
        return education

    def edit(self, education):
        session = Session()
        session.merge(education)
        session.refresh(education)
        session.commit()
        return education

    def delete(self, education):
        session = Session()
        session.delete(education)
        session.refresh(education)
        session.commit()
        return education

    def find_all(self):
        session = Session()
        education_list = session.query(Education).all()
        return education_list

    def find_by_id(self, id):
        session = Session()
        return session.get(Education, id)

    def find_by_person_id(self, person_id):
        session = Session()
        return session.get(Education, person_id)

education_repository = Repository(Education)