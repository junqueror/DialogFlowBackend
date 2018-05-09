from DialogFlow.productList import ProductList

class ProductManager():
    productLists = {}

    @staticmethod
    def getProductList(sessionId):
        if not sessionId in ProductManager.productLists.keys():
            ProductManager.productLists[sessionId] = ProductList()
        return ProductManager.productLists[sessionId]

    def _setProductList(sessionId, productIds):
        ProductManager.productLists[sessionId] = []
        for id in productIds:
            ProductManager.productLists[sessionId].productIds.append(id)
        return ProductManager.productLists[sessionId]

    @staticmethod
    def addProducts(sessionId, productIds):
        for productId in productIds:
            productList = ProductManager.getProductList(sessionId)
            productList.productIds.append(productId)

    @staticmethod
    def removeProducts(sessionId, productIds):
        for productId in productIds:
            productList = ProductManager.getProductList(sessionId)
            productList.productIds.remove(productId)

    @staticmethod
    def updateProductList(sessionId, productIds):
        return ProductManager._setProductList(sessionId, productIds)
