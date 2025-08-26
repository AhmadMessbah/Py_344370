class Payment:
    def __init__(self,id, person_id, title, amount, pay_date, payment_type, description):
        self.id = id
        self.person_id = person_id
        self.title = title
        self.amount = amount
        self.pay_date = pay_date
        self.payment_type = payment_type
        self.description = description

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id, self.person_id, self.title, self.amount, self.pay_date, self.payment_type, self.description))