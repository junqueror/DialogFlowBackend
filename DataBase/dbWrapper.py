from flask_sqlalchemy import SQLAlchemy


# Singleton class to make requests to de database
class DbWrapper():

    # Builds a new instance of DbWrapper
    def __init__(self):
        self._db = SQLAlchemy()

    @property
    def db(self):
        return self._db

    def initApp(self, app):
        self._db.init_app(app)

    def createTables(self, app):
        from DataBase.dbData import DbData
        DbData.createTables(self._db, app)

    def createTestData(self, app):
        from DataBase.dbData import DbData
        DbData.addtData(self._db, app)
