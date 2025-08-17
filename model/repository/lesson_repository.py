from model.repository.database_manager import transaction_manager


def save(code,class_number,teacher,units,title):
    return transaction_manager(
        "insert into lessons(code,class_number,teacher,units,title) values(?,?,?,?,?)",
        [code,class_number,teacher,units,title],
        commit=True

    )

def edit(code,class_number,teacher,units,title):
    return transaction_manager(
        "",
        [code,class_number,teacher,units,title],
        commit=True
    )
def remove(code,class_number,teacher,units,title):
    return transaction_manager(
        "",
        [code]
        ,
        commit=True
    )