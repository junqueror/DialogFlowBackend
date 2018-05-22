from flask_assistant import context_manager

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone
from DialogFlow.agent import Agent
from DialogFlow.session import Session
from DialogFlow.message import Message


@Agent.intentException
def getSmartphoneShowEcommerces():
    # Get context parameters
    productId = int(context_manager.get_param('product-selected', 'productId'))
    # Get links
    smartphone = DbController().getOne(SmartPhone, productId)
    # Create response message
    message = Message(['Estas son las mejores tiendas', 'Puedes comprarlo aqui'])
    message.addCarrousel(smartphone.affiliateLinks)
    # Set contexts
    context_manager.add('smartphone')
    context_manager.add('smartphone.selected.ecommerce')
    return message.response