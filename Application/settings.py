import os
from Utils.singleton import Singleton


# Class to define constant settings
class Settings(metaclass=Singleton):

    # Build a new instance of Settings
    def __init__(self):

        # Flask
        self.flask_debug = True
        self.flask_host = '0.0.0.0'
        self.flask_port = int(os.getenv('PORT', 5000))

        # Local DataBase
        self.database_host = "localhost"
        self.database_port = 5432
        self.database_user = "junquera"
        self.database_password = "pablo3934"
        self.database_name = "dialogflow"
        self.database_schema = "public"

        # Heroku DataBase
        self.heroku_database_host = 'ec2-79-125-12-27.eu-west-1.compute.amazonaws.com'
        self.heroku_database_port = 5432
        self.heroku_database_user = "oqnmljapoeesnr"
        self.heroku_database_password = "acdcc3cba4925a8d0b73a2e52f77c895151224f622c262b6f90cb812f7a96f1f"
        self.heroku_database_name = "d7obcs4tg1rc0l"
        self.heroku_database_schema = "public"

        self.database_rebuilt = True
        self.database_test_data = True

        # DialogFlow
        self.dialogflow_dev_token = 'c87709891561448daca17fda76f1e491'
        self.dialogflow_client_token = 'ceaf6b97fe074b359dabdc6e8fcc0428 '

        # Frontend
        self.frontend_mainColor = "#FF614B"

        # Charts
        self.charts_fileName = "tempChart.png"
        self.charts_filePath = os.path.join(os.pardir, "Graphics", self.charts_fileName)
        self.charts_endpoint = "{0}:{1}/api/dialogflow/chart".format(os.getenv('HOST', 'http://localhost'), int(os.getenv('PORT', 5000)))

    # Class to load the configuration for flask from settings
    class FlaskBaseConfig:
        DEBUG = None
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SECRET_KEY = None
        SQLALCHEMY_DATABASE_URI = None
        LDAP_USE_TLS = False

        # DialogFlow
        DEV_ACCES_TOKEN = 'c87709891561448daca17fda76f1e491'
        ASSIST_ACTIONS_ON_GOOGLE = True

        def __init__(self):
            Settings().FlaskBaseConfig.DEBUG = Settings().FLASK_DEBUG
            Settings().FlaskBaseConfig.SQLALCHEMY_TRACK_MODIFICATIONS = False
            Settings().FlaskBaseConfig.SQLALCHEMY_DATABASE_URI = Settings().DATABASE_URI

    @property
    def FLASK_DEBUG(self):
        return self.flask_debug

    @property
    def FLASK_HOST(self):
        return self.flask_host

    @property
    def FLASK_PORT(self):
        return self.flask_port

    # Database properties
    
    @property
    def DATABASE_TEST_DATA(self):
        return self.database_test_data
        
    @property
    def DATABASE_URI(self):
        if 'HEROKU_ENV' in os.environ:
            return "postgresql://{0}:{1}@{2}:{3!s}/{4}".format(self.heroku_database_user, self.heroku_database_password, self.heroku_database_host,
                                                          self.heroku_database_port, self.heroku_database_name)
        else:
            return "postgresql://{0}:{1}@{2}:{3!s}/{4}".format(self.database_user, self.database_password, self.database_host,
                                                          self.database_port, self.database_name)

    @property
    def DATABASE_SCHEMA(self):
        return self.database_schema

    @property
    def DATABASE_TABLE_ARGS(self):
        return {"schema": self.database_schema}

    @property
    def DATABASE_REBUILT(self):
        return self.database_rebuilt

    @property
    def DATABASE_TEST_DATA(self):
        return self.database_test_data

    @property
    def DIALOGFLOW_DEV_TOKEN(self):
        return self.dialogflow_dev_token

    @property
    def DIALOGFLOW_CLIENT_TOKEN(self):
        return self.dialogflow_client_token
