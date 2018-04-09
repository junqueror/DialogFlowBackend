from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Application.settings import Settings
from DataBase.dbController import DbController
from DataBase.RelModels.relTables import RelTables


# Data model class to represent the screens database table
class Screen(DbController.instance().db.Model):
    __tablename__ = 'screens'
    __table_args__ = Settings.instance().DATABASE_TABLE_ARGS

    # Table fields
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    minSize = Column(String)
    maxSize = Column(String)

    # Relationships

    # Children
    ranges = relationship('Range', secondary=RelTables.RangesScreens, passive_deletes=True, lazy=True)

    # Properties

    # Methods

    @staticmethod
    def getMainField():
        return Screen.name

    def __repr__(self):
        return '<Screen: {0}>'.format(self.id)
