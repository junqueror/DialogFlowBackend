from DialogFlow.session import Session


class SessionManager():
    sessions = {}

    @staticmethod
    def getProductList(sessionId):
        if not sessionId in SessionManager.sessions.keys():
            SessionManager.sessions[sessionId] = Session()
        return SessionManager.sessions[sessionId]

    def _setProductList(sessionId, productIds):
        SessionManager.sessions[sessionId] = []
        for id in productIds:
            SessionManager.sessions[sessionId].products.append(id)
        return SessionManager.sessions[sessionId]

    @staticmethod
    def addProducts(sessionId, productIds):
        for productId in productIds:
            productList = SessionManager.getProductList(sessionId)
            productList.productIds.append(productId)

    @staticmethod
    def removeProducts(sessionId, productIds):
        for productId in productIds:
            productList = SessionManager.getProductList(sessionId)
            productList.productIds.remove(productId)

    @staticmethod
    def updateProductList(sessionId, productIds):
        return SessionManager._setProductList(sessionId, productIds)
