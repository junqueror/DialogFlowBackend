from DataBase.DataModels import Article


# Class to insert test data in the database
class DbData:

    @staticmethod
    def createTables(db, app):
        with app.app_context():
            db.drop_all()
            db.create_all()

    @staticmethod
    def addtData(db, app):
        with app.app_context():
            # Articles

            article1 = Article(title="First article",
                               text="This is the first article",
                               author="Pablo")
            article2 = Article(title="Second article",
                               text="This is the second article",
                               author="Andrés")
            article3 = Article(title="Test article",
                               text="A demo article",
                               author="Pablo")

            # Add to Database
            db.session.add(article1)
            db.session.add(article2)
            db.session.add(article3)
            db.session.commit()
