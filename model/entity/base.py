from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    def __repr__(self):
        return str({c.name: getattr(self, c.name) for c in self.__table__.columns})

    def to_tuple(self):
        return tuple(self.__dict__.values())