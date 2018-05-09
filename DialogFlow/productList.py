from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone

class ProductList():
    ids = []

    def getBasicCards(self):
        smartphoneCards = []
        for id in self.ids:
            smartphone = DbController.instance().getOne(SmartPhone, id)
            smartphoneCards.append(smartphone.getBasicCard())
        return smartphoneCards

    def getCompleteCards(self):
        smartphoneCards = []
        for id in self.ids:
            smartphone = DbController.instance().getOne(SmartPhone, id)
            smartphoneCards.append(smartphone.getCompleteCard())
        return smartphoneCards

