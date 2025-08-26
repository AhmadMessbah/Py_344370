class JobHistory:
    def __init__(self, id, person_id, organisation, job_title, start_date, end_date, description):
        self.id = id
        self.person_id = person_id
        self.organisation = organisation
        self.job_title = job_title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description


    def __repr__(self):
        return f"{self.__dict__}"


    def to_tuple(self):
        return (self.id, self.person_id,
        self.organisation,self.job_title,
        self.start_date, self.end_date,
        self.description
        )


