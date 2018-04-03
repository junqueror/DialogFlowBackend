import os
from Utils.singleton import Singleton

@Singleton
# Class to define constant settings
class Settings:

    # Build a new instance of Settings
    def __init__(self):

        # Flask
        self.flask_debug = True
        self.flask_host = '0.0.0.0'
        self.flask_port = int(os.getenv('PORT', 5000))

       # DataBase
        self.database_host = 'ec2-79-125-12-27.eu-west-1.compute.amazonaws.com'
        self.database_port = 5432
        self.database_user = "oqnmljapoeesnr"
        self.database_password = "acdcc3cba4925a8d0b73a2e52f77c895151224f622c262b6f90cb812f7a96f1f"
        self.database_name = "d7obcs4tg1rc0l"
        self.database_schema = "public"

        self.database_rebuilt = True
        self.database_test_data = True

    # Class to load the configuration for flask from settings
    class FlaskBaseConfig:
        DEBUG = None
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SECRET_KEY = None
        SQLALCHEMY_DATABASE_URI = None
        LDAP_USE_TLS = False

        # DialogFlow
        DEV_ACCES_TOKEN = 'c87709891561448daca17fda76f1e491'

        def __init__(self):
            Settings.instance().FlaskBaseConfig.DEBUG = Settings.instance().FLASK_DEBUG
            Settings.instance().FlaskBaseConfig.SQLALCHEMY_TRACK_MODIFICATIONS = False
            Settings.instance().FlaskBaseConfig.SQLALCHEMY_DATABASE_URI = Settings.instance().DATABASE_URI

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
