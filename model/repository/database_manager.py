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
            person_id REFERENCES persons,
            organisation TEXT NOT NULL,
            job_title TEXT NOT NULL,
            start_date TEXT,
            end_date TEXT,
            description TEXT
        )
        """
    )

    # marriage table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS marriages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id REFERENCES persons,
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
        CREATE TABLE IF NOT EXISTS childes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        person_id REFERENCES persons,
        name TEXT,
        family TEXT,
        birth_date TEXT,
        is_alive INTEGER ,
        status INTEGER 
        )
        """

    )

    # medical table
    cursor.execute(
        """
        create table if not exists medicals (
        id integer PRIMARY KEY AUTOINCREMENT,
        person_id REFERENCES persons,
        disease text not null,
        medicine text not null,
        doctor text,
        visit_date integer not null,
        status  text not null 
        )
        """
    )

    # Skill table
    cursor.execute(
        """
        create table if not exists skills
        (
            id integer PRIMARY KEY AUTOINCREMENT,
            person_id REFERENCES persons,
            title text not null,
            institute text not null,
            duration text not null,
            register_date text not null,
            score integer not null
        )
        """
    )


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS lessons (
        id integer PRIMARY KEY AUTOINCREMENT,
        person_id REFERENCES persons,
        title TEXT NOT NULL,
        code INTEGER NOT NULL,
        teacher TEXT NOT NULL,
        units INTEGER NOT NULL,
        class_number INTEGER NOT NULL
        )
        """
    )

    cursor.close()
    connection.close()
