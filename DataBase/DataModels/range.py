from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Application.settings import Settings
from DataBase.dbController import DbController
from DataBase.RelModels.relTables import RelTables


# Data model class to represent the ranges database table
class Range(DbController().db.Model):
    __tablename__ = 'ranges'
    __table_args__ = Settings().DATABASE_TABLE_ARGS

    # Table fields
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    # Relationships

    # Children
    screens = relationship('Screen', secondary=RelTables.RangesScreens, passive_deletes=True, lazy=True)

    # Properties

    # Methods

    @staticmethod
    def getMainField():
        return Range.name

    def __repr__(self):
        return '<Range: {0}>'.format(self.id)
