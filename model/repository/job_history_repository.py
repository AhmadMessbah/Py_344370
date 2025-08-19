from model.repository.database_manager import transaction_manager


class JobRepository:

    def save(self, job_history):
        return transaction_manager(
            "insert into jobs(person_id, organisation, job_title, start_date, end_date, description) "
            "values(?,?,?,?,?,?)",
            [job_history.person_id, job_history.organisation, job_history.job_title,
             job_history.start_date, job_history.end_date, job_history.description],
            commit=True
        )

    def edit(self, job_history):
        return transaction_manager(
            "update jobs set person_id=?, organisation=?, job_title=?, start_date=?, end_date=?, description=? where id=?",
            [job_history.person_id, job_history.organisation, job_history.job_title,
             job_history.start_date, job_history.end_date,
             job_history.description, job_history.id ],
            commit=True
        )

    def delete(self,id):
        return transaction_manager(
            "delete from jobs where id=?",
            [id],
            commit=True
        )

    def find_all(self):
        return transaction_manager(
            "select * from jobs"
        )

    def find_by_id(self,id):
        id = transaction_manager(
            "select * from jobs where id=?",
            [id]
        )

    def find_by_job_title(self,job_title):
        job_title = transaction_manager(
            "select * from jobs where job_title like ?",
            [job_title])
