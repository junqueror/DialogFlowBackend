from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, ForeignKey
from ..dbController import DbController
from Application.settings import Settings


# Class to define the instances of relational tables
class RelTables:
    RangesScreens = Table('ranges_screens', DbController.instance().db.metadata,
                          Column('rangeID', Integer,
                                 ForeignKey(Settings.instance().DATABASE_SCHEMA + '.ranges.id',
                                            ondelete='CASCADE')),
                          Column('screenID', Integer,
                                 ForeignKey(Settings.instance().DATABASE_SCHEMA + '.screens.id',
                                            ondelete='CASCADE')),
                          schema=Settings.instance().DATABASE_SCHEMA)
