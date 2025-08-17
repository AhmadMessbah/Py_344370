from model.repository.database_manager import transaction_manager



def save(person_id,title,institute,duration,register_date,score):
    return transaction_manager(
        "insert into skills (person_id,title,institute,duration,register_date,score) values (?,?,?,?,?,?)",
        [person_id,title,institute,duration,register_date,score],
        commit=True
    )

def edit(id,person_id, title, institute,duration,register_date,score):
    return transaction_manager(
        "update skills set person_id=?,title=?,institute=?,duration=?,register_date=?,score=? where id=?",
        [person_id, title, institute,duration,register_date,score,id],
         commit=True
     )

def remove(id):
    return transaction_manager(
        "delete from skills where id=?",
        [id],
        commit=True
    )

def find_all():
    skills = transaction_manager("select * from skills")
    return skills

def find_by_id(id):
    skill=transaction_manager("select * from skills where id=?",
                           [id])
    return skill

def find_by_title_and_institute(title,institute):
    title_institute=transaction_manager("select * from skills where title like ? and institute like ?",
                                        [title+"%", institute + "%"])
    return title_institute