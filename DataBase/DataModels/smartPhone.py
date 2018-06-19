from sqlalchemy import Column, Integer, String, ForeignKey, func, select, cast
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.dialects.postgresql import ENUM
from DataBase.dbController import DbController
from Application.settings import Settings
from DataBase.DataModels.affiliateLink import AffiliateLink


# Data model class to represent the smarphones database table
class SmartPhone(DbController().db.Model):
    __tablename__ = 'smartphones'
    __table_args__ = Settings().DATABASE_TABLE_ARGS

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

    ratePerformance = Column(Integer)
    rateBattery = Column(Integer)
    rateCamera = Column(Integer)
    rateScreen = Column(Integer)
    rateSoftware = Column(Integer)

    # Relationships
    rangeId = Column(Integer, ForeignKey(Settings().DATABASE_SCHEMA + '.ranges.id', ondelete='CASCADE'),
                     nullable=False)

    # Children
    affiliateLinks = relationship("AffiliateLink", back_populates="smartphone", uselist=True, lazy=True,
                                  passive_deletes=True)

    # Properties

    rate = column_property((rateBattery + rateCamera + ratePerformance + rateScreen + rateSoftware) / 5)
    # cast(func.coalesce(select([func.avg(rateBattery, rateCamera, ratePerformance, rateScreen, rateSoftware)]).as_scalar(), 0), Integer))
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
        return "OS: {0}\n RAM: {1}\nProcesador: {2}\nCámaras: {3}/{4}\nBatería: {5}".format(self.OS,
                                                    self.RAM,
                                                    self.processor,
                                                    self.frontCameraRes,
                                                    self.backCameraRes,
                                                    self.battery)

    @property
    def description(self):
        return "OS: {0}\n RAM: {1}\nProcesador: {2}\nPantalla: {3}{4}{5}\nCámaras: {6}-{7}\nBatería: {8}\n Otros: {9}".format(self.OS,
                                                                     self.RAM,
                                                                     self.processor,
                                                                     self.screenSize,
                                                                     self.screenRes,
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

    @property
    def rates(self):
        return [self.ratePerformance, self.rateCamera, self.rateBattery, self.rateScreen, self.rateSoftware]

    @staticmethod
    def getMainField():
        return SmartPhone.name

    def __repr__(self):
        return '<SmartPhone: {0} {1}>'.format(self.company, self.name)
