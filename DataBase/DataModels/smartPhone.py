from sqlalchemy import Column, Integer, String, ForeignKey, func, select, cast
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.dialects.postgresql import ENUM
from DataBase.dbController import DbController
from Application.settings import Settings
from DataBase.DataModels.affiliateLink import AffiliateLink


# Data model class to represent the smarphones database table
class SmartPhone(DbController.instance().db.Model):
    __tablename__ = 'smartphones'
    __table_args__ = Settings.instance().DATABASE_TABLE_ARGS

    # Table fields
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    company = Column(String, nullable=False)
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
    rangeId = Column(Integer, ForeignKey(Settings.instance().DATABASE_SCHEMA + '.ranges.id', ondelete='CASCADE'),
                     nullable=False)

    # Children
    affiliateLinks = relationship("AffiliateLink", uselist=True, lazy=True, passive_deletes=True)

    # Properties
    avgPrice = column_property(
        cast(func.coalesce(select([func.avg(AffiliateLink.price)]).where(AffiliateLink.smartphoneId == id)
                           .correlate_except(AffiliateLink).as_scalar(), 0), Integer))

    # Methods

    @property
    def title(self):
        return "{0} {1}".format(self.company, self.name)

    @property
    def subtitle(self):
        return "Precio medio: s{0}".format(self.avgPrice)

    @property
    def text(self):
        return "{0}, \nRAM: {1}, {2}, {3}/{4}".format(self.OS,
                                                      self.RAM,
                                                      self.processor,
                                                      self.frontCameraRes,
                                                      self.backCameraRes)

    @property
    def description(self):
        return "{0}, {1}, {2}, {3} {4} {5}, {6}/{7}, {8}, {9} ".format(self.OS,
                                                                       self.RAM,
                                                                       self.processor,
                                                                       self.screenSize,
                                                                       self.screenSize,
                                                                       self.screenType,
                                                                       self.frontCameraRes,
                                                                       self.backCameraRes,
                                                                       self.battery,
                                                                       self.extras)

    @property
    def imgUrl(self):
        return self.image

    @property
    def imgAlt(self):
        return self.image

    @property
    def link(self):
        return self.officialURL

    @property
    def linkTitle(self):
        return 'Web oficial',

    @property
    def key(self):
        return self.name,

    @property
    def synonyms(self):
        return []


def getMainField():
    return SmartPhone.name

def __repr__(self):
    return '<SmartPhone: {0} {1}>'.format(self.company, self.name)
