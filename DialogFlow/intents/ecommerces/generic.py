from flask_assistant import context_manager

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone

from DialogFlow.session import Session
from DialogFlow.message import Message


def getSmartphoneShowEcommerces():
    # Get context parameters
    productId = int(context_manager.get_param('product-selected', 'productId'))
    # Get links
    smartphone = DbController.instance().getOne(SmartPhone, productId)
    # Create response message
    message = Message(['Estas son las mejores tiendas', 'Puedes comprarlo aqui'])
    message.addCarrousel(smartphone.affiliateLinks)
    # Set contexts
    context_manager.add('smartphone')
    context_manager.add('smartphone.selected.ecommerces')
    return message.response