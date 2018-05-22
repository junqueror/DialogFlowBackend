from flask_assistant import context_manager, event

from DataBase.dbController import DbController
from DataBase.DataModels.smartPhone import SmartPhone
from DialogFlow.agent import Agent
from DialogFlow.session import Session
from DialogFlow.message import Message


@Agent.intentException
def bestBattery(request, quantity):
    # Get session object
    session = Session.getSession(request)
    # Get products from DB
    products = session.appendFilter(DbController().getBestBattery, SmartPhone, quantity)
    # Create response message
    message = Message(['Listo! Estos son los móviles con batería de larga duración',
                       'Aquí los tienes',
                       'Estos son los que tienen batería de más capacidad'])
    message.addListOrCarrousel('Los {0} smartphones con más batería'.format(len(products)), products)
    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('bestBattery').lifespan = 2

    return message.response


@Agent.intentException
def cheapest(request, quantity):
    # Get session object
    session = Session.getSession(request)
    # Get products from DB
    products = session.appendFilter(DbController().getCheapests, SmartPhone, quantity)
    # Create response message
    message = Message(['Estos son los smartphones más baratos',
                       'Aquí tienes los móviles con el precio más bajo'])
    message.addListOrCarrousel('Los {0} smartphones más baratos'.format(len(products)), products)
    # Set contexts and lifespans
    context_manager.add('smartphone')
    context_manager.add('cheapest')

    return message.response


@Agent.intentException
def mostPowerful(request, quantity):
    # Get session object
    session = Session.getSession(request)
    # Get products from DB
    products = session.appendFilter(DbController().getMostPowerful, SmartPhone, quantity)
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
