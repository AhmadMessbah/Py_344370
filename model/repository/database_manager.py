import sqlite3


def transaction_manager(sql_command, parameter_list=None, commit=False):
    connection = sqlite3.connect('./model/repository/class_project.db')
    cursor = connection.cursor()
    if parameter_list:
        cursor.execute(sql_command, parameter_list)
    else:
        cursor.execute(sql_command)
    if commit:
        connection.commit()
        result_list = parameter_list
    else:
        result_list = cursor.fetchall()
    cursor.close()
    connection.close()
    return result_list


def create_database():
    connection = sqlite3.connect('./model/repository/class_project.db')
    cursor = connection.cursor()

    # Person table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            family TEXT,
            age INTEGER
        )
        """
    )

    # DRIVER LICENSE table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS driver_licences(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             person_id REFERENCES PERSONS,
             serial TEXT,
             licence_type TEXT,
             city TEXT,
             registered_date TEXT,
             expired_date TEXT
        )
        """
    )
    # MILITARY CARD TABLE
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS military_cards(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        person_id REFERENCES PERSONS,
        card_serial TEXT,
        licence_type TEXT,
        city TEXT,
        organisation TEXT,
        duration TEXT
        )
        """
    )

    # Education table
    cursor.execute(
        """
        create table if not exists educations (
        id integer PRIMARY KEY AUTOINCREMENT,
        person_id REFERENCES PERSONS ,
        university text not null,
        grade text not null,
        average integer,
        start_date text not null,
        end_date   text not null 
        )
        """
    )

    # Salary table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS salaries
        (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id        REFERENCES PERSONS ,
            weekly_hours     INTEGER,
            pay_for_hours    INTEGER,
            end_date         INTEGER,
            employment_type text
        )
        """
    )

    # job history table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id TEXT NOT NULL,
            organisation TEXT NOT NULL,
            job_title TEXT NOT NULL,
            start_date integer,
            end_date integer,
            description TEXT
        )
        """
    )

    # marriage table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS marriages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id references persons,
            name TEXT,
            family TEXT,
            marriage_date INTEGER,
            is_alive TEXT,
            childs TEXT
        )   
        """
    )

    # child_table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS childs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        person_id INTEGER,
        name TEXT,
        family TEXT,
        birth_date TEXT,
        is_alive INTEGER ,
        stauts INTEGER 
        )
        """

    )

    cursor.execute(
        # medical
        """
        create table if not exists medicals (
        id integer PRIMARY KEY AUTOINCREMENT,
        person_id integer ,
        disease text not null,
        medicine text not null,
        doctor text,
        visit_date integer not null,
        status  text not null 
        )
        """
    )

    cursor.close()
    connection.close()
