from model.repository.lesson_repository import *

def save_lesson(code,class_number,teacher,units,title):
    if code is None:
        return save(code,class_number,teacher,units,title)
    else:
        raise Exception('error')