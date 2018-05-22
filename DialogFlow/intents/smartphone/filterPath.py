
from flask_assistant import context_manager

from DataBase.dbController import DbController
from DataBase.DataModels import *
from DialogFlow.agent import Agent
from DialogFlow.session import Session
from DialogFlow.message import Message


@Agent.intentException
def getCategoryAskRange(request, productCategory):
    if productCategory == 'Smartphone':
        ranges = DbController().getAll(Range)
        # Create response message
        message = Message(Agent().getAgentSays(request))
        message.response = message.response.build_carousel()
        for range in ranges:
            message.response.add_item(title=range.name, key=range.name, description=range.description)
    else:
        # Create response message
        message = Message(['Lo siento, pero ahora mismo solo puedo ayudarte con la categoría de SmartPhones.'])

    # Set contexts and lifespans
    context_manager.add(productCategory)

    return message.response


@Agent.intentException
def getRangeAskScreen(smartphoneRange):
    # Get from DB
    range = DbController().getOneByName(Range, smartphoneRange)
    # Create response message
    message = Message([
        'Vamos a empezar por las dimensiones del SmartPhone, que dependen principalmente del tamaño de pantalla.',
        'Las dimensiones del SmartPhone determinan su tamaño. ¿Qué tamaño de pantalla estás buscando?'])
    message.response.build_carousel()
    for screen in range.screens:
        message.response.add_item(title=screen.name, key=screen.name, description=screen.description)
    # Set contexts and lifespans
    context_manager.add('smartphone')

    return message.response
