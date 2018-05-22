class Session():
    sessions = {}

    @staticmethod
    def getSession(request):
        sessionId = request['sessionId']
        if not sessionId in Session.sessions.keys():
            Session.sessions[sessionId] = Session()
        return Session.sessions[sessionId]

    def __init__(self):
        self.products = []
        self.productSelected = None
        self.query = None

    def addProducts(self, products):
        for product in products:
            self.products.append(product)

    def removeProducts(self, products):
        for product in products:
            self.products.remove(product)

    def updateProductList(self, products):
        self.products = []
        for product in products:
            self.products.append(product)
        return self.products

    def newFilter(self, function, *kwargs):
        self.products, self.query = function(query=None, *kwargs)
        return self.products

    def appendFilter(self, function, *kwargs):
        if not self.query:
            return self.newFilter(function, *kwargs)
        else:
            self.products, self.query = function(query=self.query, *kwargs)
        return self.products
