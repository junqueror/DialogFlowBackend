from flask_assistant import context_manager, event

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone
from DialogFlow.agent import Agent
from DialogFlow.session import Session
from DialogFlow.message import Message


@Agent.intentException
def generic(request, quantity):
    # Get session object
    session = Session.getSession(request)

    # Get user request text
    searchs = request['result']['resolvedQuery'].split(' ')

    # Get products from DB
    products = []
    # [products.append(product) for search in searchs for product in
    # session.appendFilter(DbController().getAllFilterBy(SmartPhone, search)[1], SmartPhone) if product not in products]


    for search in searchs:
        results, query = DbController().getAllFilterBy(SmartPhone, search)
        if len(results) > 0: # searh is a valid property for Smartphones
            products = session.appendFilter(DbController().getAllFilterBy, SmartPhone, search)

    # Create response message
    message = Message(Agent().getAgentSays(request))
    message.addListOrCarrousel('Aquí los tienes'.format(len(session.products)), session.products)
    # Set contexts and lifespans
    context_manager.add('smartphone')
