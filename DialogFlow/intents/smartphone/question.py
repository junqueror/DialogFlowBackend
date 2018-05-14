from flask_assistant import context_manager

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone

from DialogFlow.session import Session
from DialogFlow.message import Message


def bestBattery(assistant, quantity):
    # Get session object
    session = Session.getSession(assistant.request['sessionId'])
    # Get products from DB
    products = session.appendFilter(DbController.instance().getBestBattery, SmartPhone, quantity)
    # Create response message
    message = Message(['Listo! Estos son los móviles con batería de larga duración',
                       'Aquí los tienes',
                       'Estos son los que tienen batería de más capacidad'])
    message.addListOrCarrousel(products)
    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('bestBattery').lifespan = 2

    return message.response


def cheapest(assistant, quantity):
    # Get session object
    session = Session.getSession(assistant.request['sessionId'])
    # Get products from DB
    products = session.appendFilter(DbController.instance().getCheapests, SmartPhone, quantity)
    # Create response message
    message = Message(['Estos son los smartphones más baratos',
                       'Aquí tienes los móviles con el precio más bajo'])
    message.addListOrCarrousel('Los {0} smartphones más baratos'.format(len(products)), products)
    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('cheapest')

    return message.response


def mostPowerful(assistant, quantity):
    # Get session object
    session = Session.getSession(assistant.request['sessionId'])
    # Get products from DB
    products = session.appendFilter(DbController.instance().getMostPowerful, SmartPhone, quantity)
    # Create response message
    message = Message(['Listo! Estos son',
                       'Aquí los tienes',
                       'Los smartphones más potentes son los que tienen más cantidad de memoria RAM, y son los '
                       'siguientes'])
    message.addListOrCarrousel('Los {0} smartphones más potentes'.format(len(products)), products)
    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('mostPowerful').lifespan = 2
    return message.response
