from model.entity.person import Person
from model.tools.logging import Logger

Logger.info("App Started")

import test.person_test


from view.person_view import PersonView
ui = PersonView()
