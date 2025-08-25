print("App Started")

from model.repository.database_manager import create_database
create_database()
print("Database Created")

import test.person_test


print("Salam")