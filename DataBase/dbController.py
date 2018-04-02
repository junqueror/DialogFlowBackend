from DataBase.dbWrapper import DbWrapper
from Utils.singleton import Singleton


# Singleton class to make requests to de database
@Singleton
class DbController(DbWrapper):

    # Builds a new instance of DB if it is necessary
    def __init__(self):
        DbWrapper.__init__(self)

    def commitDB(self):
        self._db.session.commit()

    def getOne(self, model, ID):
        article = self._db.session.query(model).filter_by(id=ID).one()
        return article

    def getAll(self, model):
        articles = self._db.session.query(model).all()
        return articles, len(articles)

    def delete(self, model, ID):
        result = self._db.session.query(model).filter_by(id=ID).delete(synchronize_session='fetch')
        self.commitDB()
        return True if result == 1 else False

    def add(self, object):
        self._db.session.add(object)
        self.commitDB()
        return True