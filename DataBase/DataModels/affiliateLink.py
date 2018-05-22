from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from DataBase.dbController import DbController
from Application.settings import Settings


# Data model class to represent the ecommerce database table
class AffiliateLink(DbController().db.Model):
    __tablename__ = 'affiliateLinks'
    __table_args__ = Settings().DATABASE_TABLE_ARGS

    # Table fields
    id = Column(Integer, primary_key=True, autoincrement=True)
    linkUrl = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    # Relationships
    smartphoneId = Column(Integer, ForeignKey(Settings().DATABASE_SCHEMA + '.smartphones.id', ondelete='CASCADE'), nullable=False)
    ecommerceId = Column(Integer, ForeignKey(Settings().DATABASE_SCHEMA + '.ecommerce.id', ondelete='CASCADE'), nullable=False)

    # Children
    smartphone = relationship("SmartPhone", back_populates="affiliateLinks", lazy=True)
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
        return AffiliateLink.linkUrl

    def __repr__(self):
        return '<AffiliateLink: {0}>'.format(self.id)
