import re


from model.entity.job_history import JobHistory
from model.service.job_history_service import JobHistoryService

class JobHistoryController:
    def __init__(self):
        self.service = JobHistoryService()

    def save(self,person_id, organisation, job_title, start_date, end_date, description):
        try:
            job_history = JobHistory(None, person_id, organisation,
            job_title, start_date,
            end_date, description)
            return True ,self.service.save(job_history)
        except Exception as e:
            return False, f"Error!!! {e}"

    def edit(self,id, person_id, organisation, job_title, start_date, end_date, description):
        try:
            job_history = JobHistory(None, person_id, organisation,
            job_title, start_date,
            end_date, description)
            return True, self.service.save(job_history)
        except Exception as e:
            return False, f"Error!!! {e}"

    def delete(self,id):
        try:
            return True, self.service.delete(id)
        except Exception as e:
            return False, f"Error!!! {e}"

    def find_all(self):
        try:
            return True, self.service.find_all()
        except Exception as e:
            return False, f"Error!!! {e}"

    def find_by_id(self,id):
        try:
            return True, self.service.find_by_id(id)
        except Exception as e:
            return False, f"Error!!! {e}"

    def find_by_job_title(self,job_title):
        try:
            return True, self.service.find_by_job_title(job_title)
        except Exception as e:
            return False, f"Error!!! {e}"