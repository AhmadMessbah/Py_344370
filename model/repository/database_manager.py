import sqlite3


def transaction_manager(sql_command, parameter_list, commit=False):
    connection = sqlite3.connect('./model/repository/class_project.db')
    cursor = connection.cursor()
    cursor.execute(sql_command, parameter_list)
    if commit:
        connection.commit()
    cursor.close()
    connection.close()


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
        CREATE TABLE IF NOT EXISTS driver_licence(
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

    # Education table
    cursor.execute(
        """
        create table if not exists education (
        id integer PRIMARY KEY AUTOINCREMENT,
        person_id references PERSONS ,
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
        CREATE TABLE IF NOT EXISTS salary
        (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id        INTEGER,
            weekly_hours     INTEGER,
            pay_for_hours    INTEGER,
            end_date         INTEGER,
            employment_type text
        )
        """
    )

    cursor.close()
    connection.close()
