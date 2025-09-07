from model.tools.logging import Logger

Logger.info("App Started")

from model.repository.database_manager import create_database
create_database()
Logger.info("Database Created")



import test.person_test
# from view.person_view import PersonView
# ui = PersonView()



