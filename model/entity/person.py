class Person:
    def __init__(self, id, name, family, age):
        self.id = id
        self.name = name
        self.family = family
        self.age = age

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id, self.name, self.family, self.age))



