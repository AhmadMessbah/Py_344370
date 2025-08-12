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

    cursor.close()
    connection.close()
