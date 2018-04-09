from sqlalchemy import Column, Integer, String, ForeignKey, func, select, cast
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.dialects.postgresql import ENUM
from DataBase.dbController import DbController
from Application.settings import Settings
from DataBase.DataModels.affiliateLink import AffiliateLink
from DialogFlow.card import Card


# Data model class to represent the smarphones database table
class SmartPhone(DbController.instance().db.Model):
    __tablename__ = 'smartphones'
    __table_args__ = Settings.instance().DATABASE_TABLE_ARGS

    # Table fields
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    company = Column(String, nullable=False)
    range = Column(String, ENUM('Baja', 'Media', 'Alta', 'Premium',
                                name='range',
                                schema=Settings.instance().DATABASE_SCHEMA,
                                create_type=True),
                   nullable=False)
    size = Column(String)
    weight = Column(String)
    screenSize = Column(String)
    screenType = Column(String)
    screenRes = Column(String)
    processor = Column(String)
    RAM = Column(String)
    memory = Column(String)
    battery = Column(String)
    backCameraRes = Column(String)
    frontCameraRes = Column(String)
    OS = Column(String)
    extras = Column(String)
    officialURL = Column(String)
    image = Column(String)

    # Relationships

    # Children
    affiliateLinks = relationship("AffiliateLink", uselist=True, lazy=True, passive_deletes=True)

    # Properties
    avgPrice = column_property(
        cast(func.coalesce(select([func.avg(AffiliateLink.price)]).where(AffiliateLink.smartphoneId == id)
                           .correlate_except(AffiliateLink).as_scalar(), 0), Integer))

    # Methods

    @staticmethod
    def getMainField():
        return SmartPhone.name

    def getResponseCard(self):
        return Card(title=self.name, link=self.officialURL, linkTitle='Web oficial',
                    text="Precio medio: s{0}".format(self.avgPrice))

    def __repr__(self):
        return '<SmartPhone: {0}>'.format(self.id)
