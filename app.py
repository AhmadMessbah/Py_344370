print("App Started")

from model.repository.database_manager import create_database
create_database()
print("Database Created")

from view.medical_view import *



# Test
# import test.person_test
