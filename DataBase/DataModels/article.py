from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from DataBase.dbController import DbController
from Application.settings import Settings


# Data model class to represent the article database table
class Article(DbController.instance().db.Model):
    __tablename__ = 'article'
    __table_args__ = Settings.instance().DATABASE_TABLE_ARGS

    # Table fields
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    author = Column(String, nullable=False)

    # Relationships

    @staticmethod
    def getMainField():
        return Article.title

    def __repr__(self):
        return '<Article: {0}>'.format(self.id)
