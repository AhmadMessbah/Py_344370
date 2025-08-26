from model.repository.job_history_repository import JobRepository

class JobHistoryService:
    def __init__(self):
        self.repo = JobRepository()

    def save(self, job_history):
        return self.repo.save(job_history)

    def edit(self, job_history):
        return self.repo.edit(job_history)

    def delete(self, id):
        return self.repo.delete(id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, id):
        return self.repo.find_by_id(id)

    def find_by_job_title(self, job_title):
        return self.repo.find_by_job_title(job_title)