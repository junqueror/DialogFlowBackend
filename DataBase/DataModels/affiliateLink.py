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
    shippingTime = Column(String, nullable=False, default="2 días")
    shippingPrice = Column(String, nullable=False, default="4.99€")

    # Relationships
    smartphoneId = Column(Integer, ForeignKey(Settings().DATABASE_SCHEMA + '.smartphones.id', ondelete='CASCADE'), nullable=False)
    ecommerceId = Column(Integer, ForeignKey(Settings().DATABASE_SCHEMA + '.ecommerce.id', ondelete='CASCADE'), nullable=False)

    # Children
    smartphone = relationship("SmartPhone", back_populates="affiliateLinks", lazy=True)
    ecommerce = relationship("Ecommerce", lazy=True)

    # Methods

    @property
    def title(self):
        return "Precio: {0}€".format(self.price)

    @property
    def subtitle(self):
        return "Precio: {0}€".format(self.price)

    @property
    def text(self):
        return "Valoración general de la tienda: {0}\nDescripción: {1}".format(self.ecommerce.rate,self.description)

    @property
    def description(self):
        return "Tiempo de envío: {0}\nCostes de envío: {1}".format(self.shippingTime, self.shippingPrice)

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
        return 'Comprar: {0}€'.format(self.price)

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
