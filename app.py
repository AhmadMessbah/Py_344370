print("App Started")

from model.repository.database_manager import create_database
create_database()
print("Database Created")


# Test
# import test.person_test
import test.salary_test