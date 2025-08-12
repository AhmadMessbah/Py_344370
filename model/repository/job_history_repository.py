from model.repository.database_manager import transaction_manager




def save(person_id, organisation, job_title, start_date, end_date, description):
    return transaction_manager(
        "",
        [],
        commit=True
    )