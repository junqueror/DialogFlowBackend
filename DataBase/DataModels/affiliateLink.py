from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from DataBase.dbController import DbController
from Application.settings import Settings
from DialogFlow.product import Product


# Data model class to represent the ecommerces database table
class AffiliateLink(DbController.instance().db.Model):
    __tablename__ = 'affiliateLinks'
    __table_args__ = Settings.instance().DATABASE_TABLE_ARGS

    # Table fields
    id = Column(Integer, primary_key=True, autoincrement=True)
    linkUrl = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    # Relationships
    smartphoneId = Column(Integer, ForeignKey(Settings.instance().DATABASE_SCHEMA + '.smartphones.id', ondelete='CASCADE'), nullable=False)
    ecommerceId = Column(Integer, ForeignKey(Settings.instance().DATABASE_SCHEMA + '.ecommerces.id', ondelete='CASCADE'), nullable=False)

    # Children
    smartphone = relationship("SmartPhone", lazy=True)
    ecommerce = relationship("Ecommerce", lazy=True)

    # Methods

    @property
    def title(self):
        return self.ecommerce.name

    @property
    def subtitle(self):
        return "Precio: s{0}".format(self.price)

    @property
    def text(self):
        return "Valoración: {0}".format(self.ecommerce.rate)

    @property
    def description(self):
        return self.ecommerce.description

    @property
    def imgUrl(self):
        return self.ecommerce.image

    @property
    def imgAlt(self):
        return self.ecommerce.image

    @property
    def link(self):
        return self.linkUrl

    @property
    def linkTitle(self):
        return 'Comprar',

    @property
    def key(self):
        return self.ecommerce.name,

    @property
    def synonyms(self):
        return []

    @staticmethod
    def getMainField():
        return AffiliateLink.link

    def __repr__(self):
        return '<AffiliateLink: {0}>'.format(self.id)
