from model.repository import  skill_repository

def save(person_id,title,institute,duration,register_date,score):
    if score<=12:
        raise ValueError("نمره زیر 12 مناسب ثبت نام نیست")

    if score>20:
        raise ValueError("نمره بالای 20 مناسب ثبت نام نیست")

    return skill_repository.save(person_id,title,institute,duration,register_date,score)

def edit(id,person_id, title, institute,duration,register_date,score):
    skill=skill_repository.find_by_id(id)
    if skill:
        if score<=12:
            raise ValueError("نمره زیر 12 مناسب ثبت نام نیست")

        if score > 20:
            raise ValueError("نمره بالای 20 مناسب ثبت نام نیست")

        return skill_repository.edit(id,person_id,title,institute,duration,register_date,score)
    else:
        raise ValueError("فردی با چنین کدی پیدا نشد !!!")

def remove(id):
    skill = skill_repository.find_by_id(id)
    if skill:
        return skill_repository.remove(id)
    else:
        raise ValueError("فردی با چنین کدی پیدا نشد !!!")

def find_all():
    return skill_repository.find_all()

def find_by_id(id):
    return skill_repository.find_by_id(id)

def find_by_title_and_institute(title,institute):
    return skill_repository.find_by_title_and_institute(title,institute)