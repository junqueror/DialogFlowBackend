from flask_assistant import context_manager

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone
from DialogFlow.agent import Agent
from DialogFlow.session import Session
from DialogFlow.message import Message


@Agent.intentException
def getSmartphoneShowEcommerces(request):
    # Get context parameters
    productId = int(context_manager.get_param('product-selected', 'productId'))
    # Get links
    smartphone = DbController().getOne(SmartPhone, productId)
    # Create response message
    message = Message(Agent().getAgentSays(request))
    message.addCarrousel(smartphone.affiliateLinks)
    # Set contexts
    context_manager.add('smartphone')
    context_manager.add('product-selected')
    context_manager.add('product-ecommerces')
    return message.response


@Agent.intentException
def showEcommerceSelected(request, eCommerceName):
    # Get context parameters
    productId = int(context_manager.get_param('product-selected', 'productId'))

    # Get from DB
    smartphone = DbController().getOne(SmartPhone, productId)
    affiliateLink = next((link for link in smartphone.affiliateLinks if link.ecommerce.name == eCommerceName), None)

    # Create response message
    message = Message(Agent().getAgentSays(request))
    message.addCard(affiliateLink)

    # Suggestions
    message.addSuggestions('Opiniones', 'Valoraciones', 'Historial de precios')

    # Set contexts
    context_manager.add('smartphone')
    context_manager.add('product-selected')
    context_manager.add('ecommerce-selected')
    context_manager.set('ecommerce-selected', 'affiliateLinkId', affiliateLink.id)
    return message.response
