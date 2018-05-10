from sqlalchemy import Column, Integer, String, ForeignKey, func, select, cast
from sqlalchemy.orm import relationship, column_property
from sqlalchemy.dialects.postgresql import ENUM
from DataBase.dbController import DbController
from Application.settings import Settings
from DataBase.DataModels.affiliateLink import AffiliateLink
from DialogFlow.responseModel import ResponseModel
from DialogFlow.card import Card



# Data model class to represent the smarphones database table
class SmartPhone(DbController.instance().db.Model, ResponseModel):
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

    def getBasicCard(self):
        return Card(title=self.title,
                    link=self.link,
                    linkTitle=self.linkTitle,
                    text=self.sortText,
                    )

    def getCompleteCard(self):
        return Card(title=self.title,
                    subtitle=self.subtitle,
                    link=self.link,
                    linkTitle=self.linkTitle,
                    img_url=self.imgUrl,
                    img_alt=self.imgAlt,
                    text=self.longText)

    @property
    def title(self):
        return self.title
    def __init__(self):
        super(SmartPhone).__init__(title="{0} {1}".format(self.company, self.name),
                                   subtitle="Precio medio: s{0}".format(self.avgPrice),
                                   sortText="{0}, {1}, {2}, {3}/{4}".format(self.OS,
                                                                            self.RAM,
                                                                            self.processor,
                                                                            self.frontCameraRes,
                                                                            self.backCameraRes),
                                   longText="{0}, {1}, {2}, {3} {4} {5}, {6}/{7}, {8}, {9} ".format(self.OS,
                                                                                                    self.RAM,
                                                                                                    self.processor,
                                                                                                    self.screenSize,
                                                                                                    self.screenSize,
                                                                                                    self.screenType,
                                                                                                    self.frontCameraRes,
                                                                                                    self.backCameraRes,
                                                                                                    self.battery,
                                                                                                    self.extras),
                                   imgUrl=self.image,
                                   imgAlt=self.image,
                                   link=self.officialURL,
                                   linkTitle='Web oficial',
                                   text="Precio medio: s{0}".format(self.avgPrice))

    @staticmethod
    def getMainField():
        return SmartPhone.name

    def __repr__(self):
        return '<SmartPhone: {0}>'.format(self.id)
