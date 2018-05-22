from Application.settings import Settings
from Application.flaskWrapper import FlaskWrapper
from DataBase.dbController import DbController
from DialogFlow.agent import Agent

# Class to instantiate the application
class App:

    # Initialize the instance of App
    def __init__(self):
        # Create a Flask instance with app and API
        self.flask = FlaskWrapper(Settings().FlaskBaseConfig())

    def run(self, flaskHost, flaskPort):

        # DataBase
        DbController().initApp(self.flask.App)  # Initialize DB on the application

        if Settings().DATABASE_REBUILT:
            DbController().createTables(self.flask.App)
        if Settings().DATABASE_TEST_DATA:
            DbController().createTestData(self.flask.App)  # Add test data into de DataBase

        # Flask
        self.flask.App.run(flaskHost, port=flaskPort, debug=Settings().FLASK_DEBUG, use_reloader=False)

