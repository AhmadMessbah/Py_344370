from datetime import date ,time, datetime, timedelta


def date_validator(str_date):
    try:
        str_date = str_date.replace("/","-").strip()
        return datetime.strptime(str_date, "%Y-%m-%d").date()
    except:
        raise ValueError


#if date_validator(registered_date):
    #print("Registered date added")

#if date_validator(expired_date):
    #print("Expired date added")

