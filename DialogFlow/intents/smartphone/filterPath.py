from flask_assistant import context_manager

from DataBase.dbController import DbController
from DataBase.DataModels import *

from DialogFlow.session import Session
from DialogFlow.message import Message


def getCategoryAskRange(productCategory):
    if productCategory == 'Smartphone':
        ranges = DbController.instance().getAll(Range)
        # Create response message
        message = Message(['¿Qué categoría de móvil estás buscando?',
                           '¿Qué rango de SmartPhones te interesa?',
                           'Elije una de las siguientes gamas para poder empezar',
                           'Lo primero es elegir la gama de SmartPhones que buscamos. '
                           'Ten encuenta que de esta decisión depende bastante el precio, '
                           'por lo que te recomiendo que elijas de acuerdo a tus necesidades reales. '
                           'No queremos gastar dinero en algo que no necesitamos!'])
        message.response.build_carousel()
        for range in ranges:
            message.response.add_item(title=range.name, key=range.name, description=range.description)
    else:
        # Create response message
        message = Message(['Lo siento, pero ahora mismo solo puedo ayudarte con la categoría de SmartPhones.'])

    # Set contexts and lifespans
    context_manager.add(productCategory)

    return message.response


def getRangeAskScreen(smartphoneRange):
    # Get from DB
    range = DbController.instance().getOneByName(Range, smartphoneRange)
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
