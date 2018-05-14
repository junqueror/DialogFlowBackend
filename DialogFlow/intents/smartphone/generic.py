from flask_assistant import context_manager

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone

from DialogFlow.session import Session
from DialogFlow.message import Message


def getSmartphoneShowCard(smartphoneBrand, smartphoneName):
    # Get products from DB
    smartphone = DbController.instance().getOneByCompanyAndName(SmartPhone, smartphoneBrand, smartphoneName)
    # Create response message
    message = Message(['Aquí lo tienes'])
    message.addCard(smartphone)
    message.addSuggestions('Más detalles', 'Ver opiniones', 'Ver tiendas')
    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('product-selected').lifespan = 2
    context_manager.set('product-selected', 'productId', smartphone.id)
    return message.response
