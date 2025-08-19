from model.repository.job_history_repository import JobRepository




def save(person_id, organisation, job_title, start_date, end_date, description):
    job_history_repository.save(person_id, organisation, job_title, start_date, end_date, description)

def edit(id, person_id, organisation, job_title, start_date, end_date, description):
    job_history_repository.edit(id, organisation, job_title, start_date, end_date, description)

def delete(id):
    job_history_repository.delete(id)

def find_all():
    job_history_repository.find_all()

def find_by_id(id):
    job_history_repository.find_by_id(id)

def find_by_job_title(job_title):
    job_history_repository.find_by_job_title(job_title)