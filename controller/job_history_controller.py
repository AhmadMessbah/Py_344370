import re


from model.entity.job_history import JobHistory
from model.service.job_history_service import JobHistoryService

class JobHistoryController:
    def __init__(self):
        self.service = JobHistoryService()

    def save(self,person_id, organisation, job_title, start_date, end_date, description):
        job_history = JobHistory(None, person_id, organisation,
        job_title, start_date,
        end_date, description)
        return True ,self.service.save(job_history)

    def edit(self,id, person_id, organisation, job_title, start_date, end_date, description):
        job_history = JobHistory(None, person_id, organisation,
        job_title, start_date,
        end_date, description)
        return True, self.service.save(job_history)

    def delete(self,id):
        return True, self.service.delete(id)

    def find_all(self):
        return True, self.service.find_all()

    def find_by_id(self,id):
        return True, self.service.find_by_id(id)

    def find_by_job_title(self,job_title):
        return True, self.service.find_by_job_title(job_title)