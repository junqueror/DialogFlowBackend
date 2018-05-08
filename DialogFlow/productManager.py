class ProductManager():
    productLists = {}

    @staticmethod
    def _getProductList(sessionId):
        if not sessionId in ProductManager.productLists.keys():
            ProductManager.productLists[sessionId] = []
        return ProductManager.productLists[sessionId]

    def _setProductList(sessionId, productIds):
        ProductManager.productLists[sessionId] = []
        for id in productIds:
            ProductManager.productLists[sessionId].append(id)
        return ProductManager.productLists[sessionId]

    @staticmethod
    def addProoduct(sessionId, productId):
        productList = ProductManager._getProductList(sessionId)
        productList.append(productId)

    @staticmethod
    def removeProoduct(sessionId, productId):
        productList = ProductManager._getProductList(sessionId)
        productList.remove(productId)

    @staticmethod
    def updateProoductList(sessionId, productIds):
        return ProductManager._setProductList(sessionId, productIds)
