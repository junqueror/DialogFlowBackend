from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from DataBase.dbController import DbController
from Application.settings import Settings


# Data model class to represent the ecommerces database table
class Ecommerce(DbController.instance().db.Model):
    __tablename__ = 'ecommerces'
    __table_args__ = Settings.instance().DATABASE_TABLE_ARGS

    # Table fields
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    URL = Column(String, nullable=False)
    image = Column(String, nullable=False)
    description = Column(String)

    # Relationships

    # Children
    affiliateLinks = relationship("AffiliateLink", uselist=True, lazy=True, passive_deletes=True)

    # Methods

    @staticmethod
    def getMainField():
        return Ecommerce.name

    def __repr__(self):
        return '<Ecommerce: {0}>'.format(self.id)
