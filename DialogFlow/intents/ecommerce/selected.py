import random
from flask_assistant import context_manager

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone
from DataBase.DataModels.affiliateLink import AffiliateLink
from DialogFlow.agent import Agent
from DialogFlow.message import Message
from Application.settings import Settings


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


@Agent.intentException
def showPriceTrack(request):
    # Get context parameters
    productId = int(context_manager.get_param('product-selected', 'productId'))
    affiliateLinkId = int(context_manager.get_param('product-selected', 'affiliateLinkId'))

    # Get from DB
    smartphone = DbController().getOne(SmartPhone, productId)
    affiliateLink = DbController().getOne(AffiliateLink, productId)

    # Create response message
    messages = [message.format(icon1="📉", icon2="💸") for message in Agent().getAgentSays(request)] # Set icons
    message = Message([message.split('.')[0] for message in messages])
    message.response.card(title="{0}{1} - {2}".format(smartphone.company, smartphone.name, affiliateLink.ecommerce.name),
                          text=random.choice([message.split('.')[1] for message in messages]),
                          img_url=Settings().PRICE_TRACKER_ENDPOINT,
                          link=affiliateLink.link,
                          linkTitle=affiliateLink.linkTitle)

    # Set contexts
    context_manager.add('smartphone')
    context_manager.add('product-selected')
    context_manager.add('ecommerce-selected')
    context_manager.set('ecommerce-selected', 'affiliateLinkId', affiliateLink.id)
    context_manager.add('priceTracker')
    return message.response