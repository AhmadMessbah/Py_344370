print("App Started")

from model.repository.database_manager import create_database
create_database()
print("Database Created")

# Test
import test.person_test

from model.repository.driver_licence_repository import *
save(1,"a1","b2","tehran",1,1,)

