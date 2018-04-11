from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from DataBase.dbController import DbController
from Application.settings import Settings


# Data model class to represent the ecommerces database table
class AffiliateLink(DbController.instance().db.Model):
    __tablename__ = 'affiliateLinks'
    __table_args__ = Settings.instance().DATABASE_TABLE_ARGS

    # Table fields
    id = Column(Integer, primary_key=True, autoincrement=True)
    link = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    # Relationships
    smartphoneId = Column(Integer, ForeignKey(Settings.instance().DATABASE_SCHEMA + '.smartphones.id', ondelete='CASCADE'), nullable=False)
    ecommerceId = Column(Integer, ForeignKey(Settings.instance().DATABASE_SCHEMA + '.ecommerces.id', ondelete='CASCADE'), nullable=False)

    # Children
    smartphone = relationship("SmartPhone", lazy=True)
    ecommerce = relationship("SmartPhone", lazy=True)

    # Methods

    @staticmethod
    def getMainField():
        return AffiliateLink.link

    def __repr__(self):
        return '<AffiliateLink: {0}>'.format(self.id)
